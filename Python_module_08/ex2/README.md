# Matrix Data Engineering - Accessing the Mainframe

"Know thyself." — The Oracle knows everything because she has access to the mainframe’s configuration. In this final mission (`ex02`), we master **Secure Configuration Management**.

---

##  Core Concepts

### 1. Environment Variables (.env)
In professional applications, we never "hardcode" sensitive information (like passwords or API keys) directly into the Python source code. Instead, we use **Environment Variables**.
- **The .env file:** A local text file that stores key-value pairs of configuration.
- **Why?** It allows the same code to behave differently in "Development" vs "Production" without changing a single line of Python.

### 2. Development vs. Production Modes
A Data Engineer works in different "Realities":
- **Development (`development`):** A safe sandbox. We use local databases, fake API keys, and set `LOG_LEVEL=DEBUG` to see every detail of what the code is doing.
- **Production (`production`):** The real world. We use secure, high-performance databases and set `LOG_LEVEL=INFO` to keep the logs clean and efficient.



### 3. Security & Rigor: The .gitignore
One of the most critical aspects of **Rigor** is protecting secrets.
- **The .env file:** Contains your actual secrets. **NEVER** upload this to GitHub.
- **The .env.example file:** A template that shows other developers which variables they need to set, but without providing the actual secret values.
- **The .gitignore:** A gatekeeper file that tells Git to ignore sensitive files like `.env` and heavy folders like `matrix_env/`.



---

##  Technical Implementation

### The `python-dotenv` Library
We use the `python-dotenv` module to bridge the gap between our `.env` file and the Python `os` module.
- `load_dotenv()`: Scans the directory for a `.env` file and loads its contents into the system's environment.
- `os.getenv('KEY')`: Retrieves the value. If the key is missing, we can provide a safe default value.

---

##  Mission: Exercise 02

The goal is to build `oracle.py`, a secure configuration system that reads from the mainframe.
## Usage

To run the Oracle system, follow these steps to ensure your environment is correctly configured:

### 1. Setup the Configuration Template
Copy the example environment file to create your active `.env` file. This prevents your actual secrets from being tracked by Git.
```bash
cp .env.example .env