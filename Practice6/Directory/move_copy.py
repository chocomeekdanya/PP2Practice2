

import shutil
import os

# Create destination directory
os.makedirs("destination", exist_ok=True)

# Copy file
shutil.copy("sample.txt", "destination/sample.txt")

# Move file
shutil.move("sample_backup.txt", "destination/sample_backup.txt")

print("Files copied and moved successfully.")
