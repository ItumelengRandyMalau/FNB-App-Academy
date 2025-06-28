#Create a shopping cart programme that will continuosly ask the user for a food and price of that product
#Have an exit clause if the user wishes to stop adding more to their cart
#At the end show the food items and the total cost to the user


foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy press q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: R"))
        foods.append(food)
        prices.append(price)
print("--- YOUR CART---")

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price

print("\n")
print(f"Your total is: R{total}")