import re

def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print(snake_to_camel("hello_world_test")) #7
--
import re

text = "HelloWorldTest"

result = re.split(r"(?=[A-Z])", text)

print(result) #8
