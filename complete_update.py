import subprocess

subprocess.run(["python3", "update_report.py"], check=True)
subprocess.run(["python3", "del_metrics.py"], check=True)
