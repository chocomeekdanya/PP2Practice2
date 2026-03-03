
import os

filename = "sample_copy.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} deleted successfully.")
else:
    print("File does not exist.")
