# AI Code Generator

This project is an AI-powered code generation tool that utilizes the `ollama` and `llama_index` libraries to read code files, generate code snippets based on user prompts, and provide descriptions of the generated code. The tool is designed to assist developers by automating code generation tasks.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)


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

4. Install the required packages:
```bash
pip install -r requirements.txt
```

5. Set up environment variables: Create a .env file in the root directory of the project and add any necessary environment variables.

# Usage

1. Place you PDF documents and code files in the `data` directory
2. Run the main Scripts:
```bash
python main.py
```

3. Follow the prompts in the terminal to enter your queries. Type q to quit the program.


# Directory Structure

/project-root
│
├── /data                # Directory containing PDF and code files
│   ├── your_file.pdf    # Example PDF file for processing
│   └── test.py          # Test script for the application
│
├── /output              # Directory where generated code files will be saved
│
├── /prompts.py          # Contains prompt templates for code generation
│
├── /code_reader.py      # Contains the code reader functionality
│
├── main.py              # Main script to run the application
│
├── requirements.txt      # List of required Python packages
│
├── .env                 # Environment variables (create this file)
│
└── .venv                # Virtual environment directory (created during setup)

# Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
