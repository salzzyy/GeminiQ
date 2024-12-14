import os
from pathlib import Path
import logging

# Define list of files
list_of_files = [
    "QAWithPDF/_init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experimemts/experiment.ipynb",
    "logger.py",
    "exception.py",
    "StreamplitApp.py",
    "setup.py",
]

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Iterate through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Correct function is os.makedirs
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Creating the file
        logging.info(f"Creating file; {filepath}")
    else:
        logging.info(f"File {filepath} already exists.")
