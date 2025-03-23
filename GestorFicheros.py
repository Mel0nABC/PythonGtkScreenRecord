from pathlib import Path
from datetime import datetime, date, time, timezone


def check_file_exist(newFileName):
    dir = Path(".").iterdir()
    for d in dir:
        if d.name == newFileName:
            # print("Si existe")
            return True


def get_file_name():
    return f"RECORD_FILE-{datetime.now()}.mp4"


def finish_record_rename_file():
    p = Path("output.mp4")
    p.rename(get_file_name())
