LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def get_menu_choice():
    print('\n\033[4m' + 'Vegetable List and its Price :' + '\033[0m')
    print('1. Look up a Vegetable')
    print('2. Add a new Vegetable')
    print('3. Edit a Vegetable')
    print('4. Delete a Vegetable')
    print('5. Quit\n')

    choice = int(input('Enter your choice : '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice : '))

    return choice

def look_up(veg_list):
    veg_name = input('Enter a vegetable name : ')

    if veg_name in veg_list:
        return veg_list[veg_name]
    else:
        print('The vegetable name not found.')


def add(veg_list):
    veg_name = input('Enter a vegetable name : ')
    price = int(input('Enter the price : '))

    if veg_name not in veg_list:
        veg_list[veg_name] = price
    else:
        print('Vegetable name already exist.')


def change(veg_list):
    veg_name = input('Enter a vegetable name : ')

    if veg_name in veg_list:
        price = int(input('Enter the new price :'))
        veg_list[veg_name] = price
    else:
        print('The vegetable name not found.')


def delete(veg_list):
    veg_name = input('Enter a vegetable name: ')

    if veg_name in veg_list:
        del veg_list[veg_name]
    else:
        print('Vegetable name not found')