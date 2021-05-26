##This is a basic coffee machine app with basic coffe machine functions!
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def user_choice():
    choice = input('What kind of coffee would you like?\nespresso, latte, or cappuccino?\n').lower()
    if choice == 'espresso':
        format_float = "{:.2f}".format(menu[choice]['cost'])  
        print(f'That will be ${format_float}')
        return 'espresso'
    if choice == 'latte':
        format_float = "{:.2f}".format(menu[choice]['cost'])  
        print(f'That will be ${format_float}')
        return 'latte'
    if choice == 'cappuccino':
        format_float = "{:.2f}".format(menu[choice]['cost'])  
        print(f'That will be ${format_float}')
        return 'cappuccino'



def resource_report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g')


def check_coins(user_choice):
    item_cost_int = menu[user_choice]['cost']
    item_cost = "{:.2f}".format(menu[user_choice]['cost']) 
    user_quarters = int(input('How many quarters?\n')) * .25
    user_dimes = int(input('How many dimes?\n')) * .10
    user_nickles = int(input('How many nickles?\n')) * .05
    total_paid = round(user_quarters + user_dimes + user_nickles, 2)
    change = round(item_cost_int - total_paid, 2) * -1

    if total_paid > item_cost_int:
        yes_no = input(f'Are you sure you want to purchase this item for: ${item_cost}?\n').lower()
        if yes_no == 'yes':
            print(f'Please collect your change of {change}. Thanks you for your purchase!')
            return True
        if yes_no == 'no':
            print(f'Please take your refund of: {total_paid}')
            return False
    
    if total_paid < item_cost_int:
        print(f'Please insert the minimum amount of coins')
        check_coins(user_choice)

        


def available_resources(user_choice):
    available_water = resources['water']
    available_coffee = resources['coffee']
    available_milk = resources['milk']
    required_milk = 0
    required_water = menu[user_choice]['ingredients']['water']
    required_coffee = menu[user_choice]['ingredients']['coffee']

    if user_choice != 'espresso':
        required_milk = menu[user_choice]['ingredients']['milk']

    if available_water >= required_water and available_milk >= required_milk and available_coffee >= required_coffee:
        resources['water'] = available_water - required_water
        resources['milk'] = available_milk - required_milk
        resources['coffee'] = available_coffee - required_coffee
        return True

    if available_water < required_water or available_milk < required_milk or available_coffee < required_coffee:
        return False 
    

def coffee_machine_MAIN():
    make_me = user_choice()
    ingredients = available_resources(make_me)
    
    if ingredients == True:
        is_paid = check_coins(make_me)

    if ingredients == False:
        resource_report()
        print('Check resource levels!')
        return

    additional_cups = input('Would you like to make any additional cup? Y/N?').lower()
    if additional_cups == 'y':
        coffee_machine_MAIN()
    if additional_cups == 'n':
        print('Have a great day!')
        return

coffee_machine_MAIN()