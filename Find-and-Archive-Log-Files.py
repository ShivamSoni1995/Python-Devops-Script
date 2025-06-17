import glob
import tarfile

log_files = glob.glob("/var/log/*.log")
with tarfile.open("logs_backup.tar.gz", "w:gz") as tar:
    for file in log_files:
        tar.add(file)
        print(f"Archived: {file}")

