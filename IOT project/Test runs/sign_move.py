import os
import shutil
from pathlib import Path

# Define base paths using pathlib (works on all OS)
base_dir = Path(__file__).resolve().parent  # Get the script's directory
src = base_dir / "archive_3" / "asl_dataset"
dest = base_dir / "archive_3" / "Allsign"

# Ensure the destination folder exists
dest.mkdir(parents=True, exist_ok=True)

# Iterate over all files and move them
for folder in src.iterdir():
    if folder.is_dir():  # Ensure it's a directory
        for pic in folder.iterdir():
            if pic.is_file():  # Ensure it's a file
                shutil.move(str(pic), str(dest))

print("Done")
