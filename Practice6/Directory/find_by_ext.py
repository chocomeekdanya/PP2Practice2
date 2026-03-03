

import os

extension = ".txt"

for file in os.listdir("."):
    if file.endswith(extension):
        print(file)
