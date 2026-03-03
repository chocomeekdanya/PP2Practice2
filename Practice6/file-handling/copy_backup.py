

import shutil

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")

# Create backup
shutil.copy("sample.txt", "sample_backup.txt")

print("File copied and backup created.")
