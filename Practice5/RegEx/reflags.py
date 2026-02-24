import re

text = "Hello hello HELLO"

matches = re.findall("hello", text, re.IGNORECASE)
print(matches)
----------
import re

text = """cat
dog
cow"""

matches = re.findall("^c.*", text, re.MULTILINE)
print(matches)
----------
import re

text = "Hello\nWorld"

print(re.findall("Hello.*World", text))
# []

print(re.findall("Hello.*World", text, re.DOTALL))
# ['Hello\nWorld']
