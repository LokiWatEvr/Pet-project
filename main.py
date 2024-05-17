
contacts = []

def add_contact():

    key = input("Введите ключ контакта: ")
    name = input("Введите имя контакта: ")
    email = input("Введите адрес электронной почты контакта: ")
    phone = input("Введите номер телефона контакта: ")
    birthday = input("Введите день рождения контакта (формат ГГГГ-ММ-ДД): ")
    note = input("Введите заметку о контакте: ")

    
    new_contact = {"key": key, "name": name, "email": email, "phone": phone, "birthday": birthday, "note": note}


    contacts.append(new_contact)


def search_contact():

    key_to_search = input("Введите ключ контакта, который нужно найти: ")

  
    for contact in contacts:
        if contact["key"] == key_to_search:
            return contact

  
    return None


def list_contacts():

    for contact in contacts:
        print_contact(contact)


def print_contact(contact):
    print("Ключ:", contact["key"])
    print("Имя:", contact["name"])
    print("Почта:", contact["email"])
    print("Номер телефона:", contact["phone"])
    print("День рождения:", contact["birthday"])
    print("Заметка:", contact["note"])


def show_menu():
    print("nМеню:")
    print("1. Добавить контакт")
    print("2. Редактировать контакт")
    print("3. Удалить контакт")
    print("4. Поиск контакта")
    print("5. Вывести список контактов")
    print("6. Выход")

def delete_contact():
    print('hi')
def edit_contact():
    print('hi')

while True:
    
    show_menu()


    choice = input("Введите номер пункта меню: ")

   
    if choice == "1":
        add_contact()
    elif choice == "2":
        edit_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        list_contacts()
    elif choice == "6":
        break
    else:
        print("Неверный выбор.")