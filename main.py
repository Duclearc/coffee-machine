import resources

supplies = resources.supplies


def show_supplies(profit):
    """Returns string with list of current supplies"""
    supplies_list = f'Money: ${profit}\n'
    measurement = 'ml'
    for supply in supplies:
        if supply == 'coffee':
            measurement = 'mg'
        supplies_list += f'{supply.title()}: {supplies[supply]}{measurement}\n'
    return supplies_list


def desired_coffee(coffee):
    """Returns the desired coffee info from the Menu"""
    for coffee_option in resources.MENU:
        if coffee_option == coffee:
            return resources.MENU[coffee_option]


def check_supplies(coffee_info):
    """Returns True if current supplies are sufficient for the requested coffee"""
    proceed = True
    for ingredient in coffee_info['ingredients']:
        if supplies[ingredient] < coffee_info['ingredients'][ingredient]:
            proceed = False
    return proceed


def make_purchase(coffee, price):
    print(f'One {coffee.title()} costs ${price}')
    quarters = 0.25 * int(input('How many Quarters would you like to insert? -> '))
    dimes = 0.10 * int(input('How many Dimes would you like to insert? -> '))
    nickels = 0.05 * int(input('How many Nickels would you like to insert? -> '))
    pennies = 0.01 * int(input('How many Pennies would you like to insert? -> '))

    total = round(quarters + dimes + nickels + pennies, 2)
    print(total)
    if price > total:
        print(f'⚠️ Insufficient amount.'
              f'The selected coffee costs ${price}, and only ${total} was inserted. '
              f'Collect your coins bellow and try again')
        return False
    elif total > price:
        change = round(total - price, 2)
        change_message = f' Please take your change of ${change}.'
    else:
        change_message = ''
    print(f'☕️ Here\'s your {coffee}.{change_message}')
    return True


def adjust_supplies(coffee):
    for ingredient in coffee:
        supplies[ingredient] -= coffee[ingredient]


def request_new_coffee():
    """Starts the coffee machine. Asks for your request and calls following action appropriately"""
    machine_power = True
    profit = 0
    while machine_power:
        request = input('\nWhat would you like? (espresso/latte/cappuccino)\n-> ').lower()

        if request == 'report':
            print(show_supplies(profit))

        elif request == 'off':
            print('MACHINE OFF')
            machine_power = False

        elif request == 'espresso' or request == 'latte' or request == 'cappuccino':
            coffee_info = desired_coffee(request)
            if check_supplies(coffee_info):
                if make_purchase(request, coffee_info['cost']):
                    profit += float(coffee_info['cost'])
                adjust_supplies(coffee_info['ingredients'])

            else:
                print('Not enough ingredients. Please ask management for refill or order another type of coffee.')

        else:
            print('invalid request')


request_new_coffee()
