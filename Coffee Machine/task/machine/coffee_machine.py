# Write your code here
class Coffee:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        self.counter = 0
        self.water_amount = 0
        self.milk_amount = 0
        self.beans_amount = 0
        self.cups_amount = 1
        self.money_amount = 0

    def fill_machine(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def calc_availability(self):
        min_counter = min(self.water // self.water_amount, self.milk // self.milk_amount, self.beans // self.beans_amount)
        if min_counter < self.counter:
            print(f'No, I can make only {min_counter} cups of coffee')
        elif min_counter == self.counter:
            print(f'Yes, I can make that amount of coffee')
        else:
            print(f'Yes, I can male that amount of coffee (and even {min_counter - my_coffee.counter} more than that')

    def check_resources(self, coffee_check):
        if coffee_check == '1':
            if self.water - espresso.water_amount < 0:
                print('Sorry, not enough water!')
                return False
            elif self.milk - espresso.milk_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.beans - espresso.beans_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.cups - espresso.cups_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.money - espresso.money_amount < 0:
                print('Sorry, not enough milk!')
                return False
        elif coffee_check == '2':
            if self.water - latte.water_amount < 0:
                print('Sorry, not enough water!')
                return False
            elif self.milk - latte.milk_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.beans - latte.beans_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.cups - latte.cups_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.money - latte.money_amount < 0:
                print('Sorry, not enough milk!')
                return False
        elif coffee_check == '3':
            if self.water - cappuccino.water_amount < 0:
                print('Sorry, not enough water!')
                return False
            elif self.milk - cappuccino.milk_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.beans - cappuccino.beans_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.cups - cappuccino.cups_amount < 0:
                print('Sorry, not enough milk!')
                return False
            elif self.money - cappuccino.money_amount < 0:
                print('Sorry, not enough milk!')
                return False
        return True

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee_check = str(input())
        if coffee_check == 'back':
            return True
        if not my_coffee.check_resources(coffee_check):
            return False

        print('I have enough resources, making you a coffee!')
        if coffee_check == '1':
            my_coffee.water -= espresso.water_amount
            my_coffee.beans -= espresso.beans_amount
            my_coffee.cups -= espresso.cups_amount
            my_coffee.money += espresso.money_amount
        elif coffee_check == '2':
            my_coffee.water -= latte.water_amount
            my_coffee.milk -= latte.milk_amount
            my_coffee.beans -= latte.beans_amount
            my_coffee.cups -= latte.cups_amount
            my_coffee.money += latte.money_amount
        elif coffee_check == '3':
            my_coffee.water -= cappuccino.water_amount
            my_coffee.milk -= cappuccino.milk_amount
            my_coffee.beans -= cappuccino.beans_amount
            my_coffee.cups -= cappuccino.cups_amount
            my_coffee.money += cappuccino.money_amount

    def status(self):
        print('\nThe coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')


espresso = Coffee()
espresso.water_amount = 250
espresso.beans_amount = 16
espresso.money_amount = 4

latte = Coffee()
latte.water_amount = 350
latte.milk_amount = 75
latte.beans_amount = 20
latte.money_amount = 7

cappuccino = Coffee()
cappuccino.water_amount = 200
cappuccino.milk_amount = 100
cappuccino.beans_amount = 12
cappuccino.money_amount = 6

my_coffee = Coffee()

option = ''
while option != 'exit':
    option = input('\nWrite action (buy, fill, take, remaining, exit):')
    if option == 'buy':
        my_coffee.buy()
    elif option == 'fill':
        my_coffee.fill_machine()
    elif option == 'take':  # take
        print(f'I gave you $ {my_coffee.money}')
        my_coffee.money -= my_coffee.money
    elif option == 'remaining':
        my_coffee.status()


"""
class Coffee_machine:

    def __init__(self):

        self.state = "choosing an action"
        self.amount_of_water = 400
        self.amount_of_milk = 540
        self.amount_of_coffee = 120
        self.no_of_cups = 9
        self.amount_of_money = 550


    def status(self):
            print(f'''\nThe coffee machine has:
{self.amount_of_water} of water
{self.amount_of_milk} of milk
{self.amount_of_coffee} of coffee beans
{self.no_of_cups} of disposable cups
${self.amount_of_money} of money\n''')

    def take(self):
            print(f"I give you ${self.amount_of_money}\n")
            self.amount_of_money = 0

    def buy(self, user_choice):

        if user_choice in ["1", "2", "3"]:
            ingredients = self.coffee(user_choice)
            self.check_and_make(ingredients)
        else:
            pass

    def coffee(self, typee):
        #water, coffee, milk, money, cup
        if typee == "1":
            return [250, 16, 0, 4, 1] #espresso
        if typee == "2":
            return [350, 20, 75, 7, 1] #latte
        if typee == "3":
            return [200, 12, 100, 6, 1] #cappucino


    def check_and_make(self, list_of_ingredients):

        if self.amount_of_water - list_of_ingredients[0] < 0:
            print("Sorry, not enough water!")
        elif self.amount_of_coffee - list_of_ingredients[1] < 0:
            print("Sorry, not enough coffee!")
        elif self.amount_of_milk - list_of_ingredients[2] < 0:
            print("Sorry, not enough milk!")
        elif self.no_of_cups - list_of_ingredients[4] < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.amount_of_water -= list_of_ingredients[0]
            self.amount_of_coffee -= list_of_ingredients[1]
            self.amount_of_milk -= list_of_ingredients[2]
            self.amount_of_money += list_of_ingredients[3]
            self.no_of_cups -= list_of_ingredients[4]

    def fill(self, user_input, ingredient):
        return ingredient + int(user_input)


    def take_action(self, user_input):
        if self.state == "choosing an action":
            if user_input == "buy":
                self.state = "choosing type of coffee"
            elif user_input == "remaining":
                self.status()
            elif user_input == "fill":
                self.state = "filling water"
            elif user_input == "take":
                self.take()
                self.state = "choosing an action"
            elif user_input == "exit":
                self.state = "switching off"
        elif self.state == "choosing type of coffee":
            self.buy(user_input)
            self.state = "choosing an action"
        elif self.state == "filling water":
            self.amount_of_water = self.fill(user_input, self.amount_of_water)
            self.state = "filling milk"
        elif self.state == "filling milk":
            self.amount_of_milk = self.fill(user_input, self.amount_of_milk)
            self.state = "filling coffee"
        elif self.state == "filling coffee":
            self.amount_of_coffee = self.fill(user_input, self.amount_of_coffee)
            self.state = "filling cups"
        elif self.state == "filling cups":
            self.no_of_cups = self.fill(user_input, self.no_of_cups)
            self.state = "choosing an action"
        else:
            pass

new_machine = Coffee_machine()
new_machine.state

while True:

    if new_machine.state == "choosing an action":
        new_machine.take_action(input("Write action (buy, fill, take, remaining, exit):\n"))
    elif new_machine.state == "choosing type of coffee":
        new_machine.take_action(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
    elif new_machine.state == "filling water":
        new_machine.take_action(input("Write how many ml of water do you want to add:\n"))
    elif new_machine.state == "filling milk":
        new_machine.take_action(input("Write how many ml of milk do you want to add:\n"))
    elif new_machine.state == "filling coffee":
        new_machine.take_action(input("Write how many grams of coffee beans do you want to add:\n"))
    elif new_machine.state == "filling cups":
        new_machine.take_action(input("Write how many disposable cups of coffee do you want to add:\n"))
    else:
        break
"""
