import json

# open JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':10} {'MTU':5}")
print("-" * 80)

# navigate through JSON structure
interfaces = data["imdata"]

for item in interfaces:
    att

