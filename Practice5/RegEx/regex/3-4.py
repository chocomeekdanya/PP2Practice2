import re

text = "hello_world test_case Invalid_Case"

pattern = r"\b[a-z]+_[a-z]+\b"

print(re.findall(pattern, text)) #3
---
import re

text = "Hello world Test ABC"

pattern = r"\b[A-Z][a-z]+\b"

print(re.findall(pattern, text)) #4
