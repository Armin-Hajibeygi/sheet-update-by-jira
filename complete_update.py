import subprocess
import logging

# Set up logging
logging.basicConfig(filename="logs.log", level=logging.DEBUG)

# Create a formatter that includes a timestamp
formatter = logging.Formatter("%(asctime)s: %(message)s")

# Set the formatter for the root logger
logging.getLogger().handlers[0].setFormatter(formatter)

# Log some messages
logging.info("This is an info message")

subprocess.run(["python3", "update_report.py"], check=True)
subprocess.run(["python3", "del_metrics.py"], check=True)
