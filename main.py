import menu_choices
import save_load_dict

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    veg_list = save_load_dict.unpickle_it()

    choice = 0

    while choice != QUIT:
        choice = menu_choices.get_menu_choice()

        if choice == LOOK_UP:
            menu_choices.look_up(veg_list)

        elif choice == ADD:
            menu_choices.add(veg_list)

        elif choice == CHANGE:
            menu_choices.change(veg_list)

        elif choice == DELETE:
            menu_choices.delete(veg_list)


    save_load_dict.pickle_it(veg_list)

main()





