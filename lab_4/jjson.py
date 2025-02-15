import json
with open("sample-data.json", "r") as file:
    data = json.load(file)

interfaces = data["imdata"]

print(f"{'DN':<60} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("=" * 100)

for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<60} {description:<20} {speed:<10} {mtu:<10}")
