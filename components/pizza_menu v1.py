#component numero 5 v1

pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie',
               'Vegan', 'Chicken Deluxe', 'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']

pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

number_pizzas = 12

#print("How many Dream pizzas would you like to order today?")
#num_pizza = int(input)

for count in range (number_pizzas):
    print(count,pizza_names[count],pizza_prices[count])
