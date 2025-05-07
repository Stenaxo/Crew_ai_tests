#!/usr/bin/env python
import sys
import warnings
from pathlib import Path
from crew import Papa

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
SCRIPT_DIR = Path(__file__).parent
jpg_path = str(SCRIPT_DIR/"test.jpg")

def run():
    """
    Run the crew.
    """
    inputs = {
        "jpg_path" : jpg_path
        }
    try:
        Papa().crew().kickoff(inputs = inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()