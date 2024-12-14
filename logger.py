import logging
import os
from datetime import datetime

# Correct the f-string for the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Fix the logging format string
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)
