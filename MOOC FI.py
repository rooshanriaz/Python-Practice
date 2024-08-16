"""number = int(input(print("Please type in a number;")))
if number == 1984:
    print("Orwell")
else:
    print(f"{number}")"""

ask_name = input(print("Please tell me your name"))
ask_quantity = int(input(print("How many portions of soup?")))

price = 5.90

if ask_name != 'jerry':
    price = price * ask_quantity
    print(price)
elif ask_name == 'jerry':
    print('Next please!')