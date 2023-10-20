# TypeEvalPy: A Micro-benchmarking Framework for Python Type Inference Tools

<p align="center">
<img src="TypeEvalPy.jpg" width="60%" align="center">
</p>


## 📌 **Key Features**:
- 📜 Contains **154 code snippets** to test and benchmark.
- 🏷 Offers **845 type annotations** across a diverse set of Python functionalities.
- 📂 Organized into **18 distinct categories** targeting various Python features.
- 🚢 Seamlessly manages the execution of **containerized tools**.
- 🔄 Efficiently transforms inferred types into a **standardized format**.
- 📊 Produces **meaningful metrics** for in-depth assessment and comparison.

---

## 🏆 TypeEvalPy Leaderboard

Below is a comparison showcasing exact matches across different tools, coupled with `top_n` predictions for our ML-based tools.

| 🛠️ Tool | Top-n | Function Return Type | Function Parameter Type | Local Variable Type | Total |
|----|----|----|----|----|----|
| **[HeaderGen](https://github.com/ashwinprasadme/headergen)** | 1 | 186 | 56 | 321 | 563 |
| **[Jedi](https://github.com/davidhalter/jedi)** | 1 | 122 | 0 | 293 | 415 |
| **[Pyright](https://github.com/microsoft/pyright)** | 1 | 100 | 8 | 297 | 405 |
| **[HiTyper](https://github.com/JohnnyPeng18/HiTyper)** | 1<br>3<br>5 | 163<br>173<br>175 | 27<br>37<br>37 | 179<br>225<br>229 | 369<br>435<br>441 |
| **[HiTyper (static)](https://github.com/JohnnyPeng18/HiTyper)** | 1 | 141 | 7 | 102 | 250 |
| **[Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)** | 1 | 155 | 32 | 6 | 193 |
| **[Type4Py](https://github.com/saltudelft/type4py)** | 1<br>3<br>5 | 39<br>103<br>109 | 19<br>31<br>31 | 99<br>167<br>174 | 157<br>301<br>314 |

---

## 📥 Installation

1. **Install Dependencies and Set Up Virtual Environment**

   Run the following commands to set up your virtual environment and activate the virtual environment.

   ```bash
   python3 -m venv .env
   ```

   ```bash
   source .env/bin/activate
   ```

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage: Running the Analysis

1. **Navigate to the `src` Directory**

   ```bash
   cd src
   ```

2. **Execute the Analyzer**

   Run the following command to start the benchmarking process on all tools:

   ```bash
   python main_runner.py
   ```

   or

   Run analysis on specific tools

   ```
   python main_runner.py --runners headergen hityperdl
   ```

   Available options: headergen, pyright, scalpel, jedi, hityper, type4py, hityperdl

   The results will be generated in the `.results` folder within the root directory of the repository. Each results folder will have a timestamp, allowing you to easily track and compare different runs.

---

### 🤝 Contributing

Thank you for your interest in contributing! To add support for a new tool, please utilize the Docker templates provided in our repository. After implementing and testing your tool, please submit a pull request (PR) with a descriptive message. Our maintainers will review your submission, and merge them.

---

### ⭐️ Show Your Support

Give a ⭐️ if this project helped you!
