

with open("sample.txt", "a") as file:
    file.write("Appending a new line.\n")
    file.write("Another appended line.\n")

print("New lines appended.\n")

# Verify content
with open("sample.txt", "r") as file:
    print(file.read())
