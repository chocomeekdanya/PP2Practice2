import re

text = "HelloWorldTest"

result = re.sub(r"(?<!^)(?=[A-Z])", " ", text)

print(result) #9
---
import re

def camel_to_snake(text):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()

print(camel_to_snake("helloWorldTest")) #10
