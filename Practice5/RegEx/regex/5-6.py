import re

pattern = r"a.*b"

strings = ["ab", "acb", "a123b", "aX", "baab"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s) #5
---
import re

text = "Hello, world. Python is fun"

result = re.sub(r"[ ,\.]", ":", text)

print(result) #6
