import json


with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':10} {'MTU':5}")
print("-" * 80)


interfaces = data["imdata"]

for item in interfaces:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:50} {descr:20} {speed:10} {mtu:5}")
