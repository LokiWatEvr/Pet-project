contacts = []
key = 1

def add_contact():
    global key
    name = input("Введите имя: ")
    email = input("Введите адрес электронной почты: ")
    phone = input("Введите номер телефона: ")
    new_contact = {"key": key, "name": name, "email": email, "phone": phone}
    contacts.append(new_contact)
    print("Контакт успешно добавлен. Ключ контакта:", key)
    key += 1

def edit_contact():
    contact_key = int(input("Введите ключ контакта для редактирования: "))
    for contact in contacts:
        if contact["key"] == contact_key:
            print("Контакт найден.")
            print("Выберите данные для редактирования:")
            print("1. Имя")
            print("2. Адрес электронной почты")
            print("3. Номер телефона")
            choice = input("Введите соответствующую цифру: ")
            if choice == "1":
                new_name = input("Введите новое имя: ")
                contact["name"] = new_name
            elif choice == "2":
                new_email = input("Введите новый адрес электронной почты: ")
                contact["email"] = new_email
            elif choice == "3":
                new_phone = input("Введите новый номер телефона: ")
                contact["phone"] = new_phone
            print("Контакт успешно отредактирован.")
            return
    print("Контакт не найден.")

def delete_contact():
    contact_key = int(input("Введите ключ контакта для удаления: "))
    for contact in contacts:
        if contact["key"] == contact_key:
            contacts.remove(contact)
            print("Контакт успешно удален.")
            return
    print("Контакт не найден.")

def search_contact():
    contact_key = int(input("Введите ключ контакта для поиска: "))
    for contact in contacts:
        if contact["key"] == contact_key:
            print(f"Имя: {contact['name']}, Электронная почта: {contact['email']}, Телефон: {contact['phone']}")
            return
    print("Контакт не найден.")

def display_contacts():
    if len(contacts) == 0:
        print("Список контактов пуст.")
    else:
        print("Список контактов:")
        for contact in contacts:
            print(f"Ключ: {contact['key']}, Имя: {contact['name']}, Электронная почта: {contact['email']}, Телефон: {contact['phone']}")

# Меню действий
while True:
    print("\nМеню:")
    print("1. Добавить контакт")
    print("2. Отредактировать контакт")
    print("3. Удалить контакт")
    print("4. Найти контакт")
    print("5. Отобразить все контакты")
    print("6. Выйти")

    choice = input("Выберите действие (введите соответствующую цифру): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        edit_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите действие из меню.")
    