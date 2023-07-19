import os
from typing import *

import torch
import asyncio

from typet5.model import ModelWrapper
from typet5.train import PreprocessArgs
from typet5.utils import *
from typet5.function_decoding import (
    RolloutCtx,
    PreprocessArgs,
    DecodingOrders,
    AccuracyMetric,
)
from typet5.static_analysis import PythonProject, reorder_signature_map
from pathlib import Path


def benchmark_root() -> Path:
    return Path("/tmp/micro-benchmark")


def get_subfolders(root_path, max_levels=2):
    subfolders = []
    root_path_str = str(root_path)
    for root, dirs, files in os.walk(root_path_str):
        current_level = root.count(os.sep) - root_path_str.count(os.sep) + 1
        if current_level == 1:
            continue
        if current_level > max_levels:
            continue
        for dir_name in dirs:
            subfolder_path = Path(root) / dir_name
            subfolder_rel_path = subfolder_path.relative_to(root_path)
            subfolders.append(str(subfolder_rel_path))
    return subfolders


print(benchmark_root())
os.chdir(benchmark_root())

# download or load the model
wrapper = ModelWrapper.load_from_hub("MrVPlusOne/TypeT5-v7")
device = torch.device(f"cuda" if torch.cuda.is_available() else "cpu")
wrapper.to(device)
print("model loaded")

# set up the rollout parameters
rctx = RolloutCtx(model=wrapper)
pre_args = PreprocessArgs()
# Double-traversal decoding order, where the model can make corrections # to its previous predictions in the second pass
decode_order = DecodingOrders.DoubleTraversal()


def write_predictions_to_file(project_root, sig_map):
    for path, sig in sig_map.items():
        parts = str(path).split("/")
        folder_path = project_root
        for part in parts[:-1]:
            part = part.replace(".", "/")
            folder_path /= f"{part}.txt"
        with open(folder_path, "a") as file:
            file.write(f"{parts[1]}:{str(sig)}\n")


async def main():
    subfolders = get_subfolders(benchmark_root())
    for subfolder in subfolders:
        print(f"Parsing project: {subfolder}")
        project = PythonProject.parse_from_root(benchmark_root() / subfolder)
        eval_r = await rctx.evaluate_on_projects([project], pre_args, decode_order)

        output_dir = benchmark_root() / subfolder
        sig_map = reorder_signature_map(
            eval_r.predictions[0].predicted_sigmap, eval_r.label_maps[0]
        )
        write_predictions_to_file(output_dir, sig_map)
        print(f"Predictions written to: {output_dir}")


asyncio.run(main())
