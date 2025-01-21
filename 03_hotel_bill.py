from datetime import datetime

print(f"{'='*35}")
print(f"{'Hotel Nature':^35}")
print(f"{'='*35}")
a = datetime.now()
print("Time:", a.strftime("%Y-%m-%d %H:%M:%S %a"))
print(f"{'-'*35}")
print(f"{'Menu':^12}{'Quantity':>8}{'Price':^13}")
print(f"{'-'*35}")


all_dish = []
all_quantity = []
fixed_price = []
all_price = []

quan = int(input("How many items:"))
for i in range(0, quan):
    dish = input("Enter dish name")
    all_dish.append(dish)
    quantity = input("Enter quantity")
    all_quantity.append(quantity)
    price = input("Enter price")
    fixed_price.append(float(price))
    total = float(price) * int(quantity)
    all_price.append(float(total))

bill = 0


for i in range(len(all_dish)):
    print(f"{all_dish[i]:^12} {all_quantity[i]:^8} {fixed_price[i]:>6}")
    bill += all_price[i]

print(f"{'-'*35}")
print(f"  Total: {' ':>12} ₹{bill}")
print(f"{'='*35}")
