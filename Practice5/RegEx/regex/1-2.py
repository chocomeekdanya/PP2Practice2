import re

pattern = r"ab*"

strings = ["a", "ab", "abb", "ac", "b"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s) #1task
  ---
import re

pattern = r"ab{2,3}"

strings = ["ab", "abb", "abbb", "abbbb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s) #task2
