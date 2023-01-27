import view
import model

def start():
    choice=''
    while choice !=8:
        choice=view.main_menu()
        print(choice)
        match choice:
            case 1:
                model.open_file()

            case 2:
                model.save_file()

            case 3:
                view.show_contacts(model.get_phonebook())

            case 4:
                new_contact=list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                find = view.find_contact()
                model.delete_contact(find)

            case 6:
                find=view.change_contact()
                model.change_contact(find)

            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                pass

            case _:
                view.input_error()
