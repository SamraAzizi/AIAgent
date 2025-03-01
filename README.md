# AI Code Generator

This project is an AI-powered code generation tool that utilizes the `ollama` and `llama_index` libraries to read code files, generate code snippets based on user prompts, and provide descriptions of the generated code. The tool is designed to assist developers by automating code generation tasks.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Load and parse documents from a specified directory.
- Generate code snippets based on user input.
- Read the contents of code files.
- Save generated code to output files.
- Retry mechanism for error handling.

## Requirements

- Python 3.7 or higher
- Virtual environment (recommended)
- Required Python packages listed in `requirements.txt`

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>


2. Create a Virtual environment: 
```bash
python -m venv ai
```

3. Activate The virtual environment:
- On Windows
```bash
ai\Scripts\activate
```

- On macOS/Linux
```bash
source ai/bin/activate
```
