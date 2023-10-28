import re

command = input()
total_money = 0
bought_furniture = []
pattern = r">>([A-za-z]+)<<(\d+\.?\d+)!(\d+)"

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)

    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
