
from llama_index.core.tools import FunctionTool
import os

def code_reader_func(file_name):
    path = os.path.join("data", file_name)

    try:
        with open (path, "r") as f:
            content = f.read()
