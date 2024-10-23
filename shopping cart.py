foods =[]
prices = []
total = 0

while True:
    food =input("Enter a food you want to buy  (q to quite): ")
    if food.lower() == "q":
       break
    else:
        price= float(input(f"enter the amount of a {food}: $"))
        foods.append(food)
        prices.append(price)

print ("----- YOUR CART ---------")

for food in foods:
        print(food ,end = " ")
for price in prices:
        total += price
print (f"your total amount is {total}")