# goit-pycore-hw-08

Беремо завдання https://github.com/Kate2603/goit-pycore-hw-07/tree/main/task_2

Технiчний опис завдання

☝ В цьому домашньому завданні ви повинні додати функціонал збереження адресної книги на диск та відновлення з диска.


Для цього — ви маєте вибрати pickle протокол серіалізації/десеріалізації даних та реалізувати методи, які дозволять зберегти всі дані у файл і завантажити їх із файлу.



Головна мета, щоб застосунок не втрачав дані після виходу із застосунку та при запуску відновлював їх з файлу. Повинна зберігатися адресна книга з якою ми працювали на попередньому сеансі.



Реалізуйте функціонал для збереження стану AddressBook у файл при закритті програми і відновлення стану при її запуску.



Приклади коду, які стануть в нагоді:

Серіалізація з pickle

import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено



Інтеграція збереження та завантаження в основний цикл

def main():
    book = load_data()

    # Основний цикл програми

    save_data(book)  # Викликати перед виходом з програми



Ці приклади допоможуть вам у реалізації домашнього завдання.


Критерії оцінювання:

Реалізовано протокол серіалізації/десеріалізації даних за допомогою pickle
Всі дані повинні зберігатися при виході з програми
При новому сеансі Адресна книга повинна бути у застосунку, яка була при попередньому запуску.


-----------------------------------------
1. hello: Отримати вітання від бота.

2. close або exit: Закрити програму.

3. Add Contacts:
Command: add John 1234567890 
Command: add John 5555555555 
Command: add-birthday John 05.12.1985
Command: add Jane 9876543210 
Command: add-birthday Jane 12.05.1990 

Command: add Janet 9875987210 
Command: add-birthday Janet 02.11.2001 

Command: add Simon 3535353535 
Command: add-birthday Simon 06.03.1997 

Command: add Mila 9519519519 
Command: add-birthday Mila 08.09.1983 

6. View  all Contacts:
Command: all 
Expected Output: 
Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985 
Contact name: Jane, phones: 9876543210, birthday: 12.05.1990 

7. Show Birthday:
Command: show-birthday John 
Expected Output: John: 05.12.1985 

8. Upcoming Birthdays:
Command: birthdays 
Expected Output: 
John: 1985-12-05 Jane: 1990-05-12 

9. Invalid Command:
Command: invalid-command 
Expected Output: Invalid command.

---------------------------------------------
# Так працює мій консольний додаток


# Initial Address Book:
# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Contact name: Janet, phones: 9875987210, birthday: 02.11.2001
# Enter a command: hello
# How can I help you?
# Enter a command: add Simon 3535353535
# Contact added.   
# Enter a command: add-birthday Simon 06.03.1997
# Birthday added.  
# Enter a command: all
# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Contact name: Janet, phones: 9875987210, birthday: 02.11.2001
# Contact name: Simon, phones: 3535353535, birthday: 06.03.1997
# Enter a command: close
# Good bye!

# Address Book After Deserialization:
# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Contact name: Janet, phones: 9875987210, birthday: 02.11.2001
# Contact name: Simon, phones: 3535353535, birthday: 06.03.1997

# Initial Address Book:
# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Contact name: Janet, phones: 9875987210, birthday: 02.11.2001
# Contact name: Simon, phones: 3535353535, birthday: 06.03.1997
# Enter a command: hello
# How can I help you?
# Enter a command: add Mila 9519519519
# Contact added.   
# Enter a command: add-birthday Mila 08.09.1983
# Birthday added.  
# Enter a command: all
# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Contact name: Janet, phones: 9875987210, birthday: 02.11.2001
# Contact name: Simon, phones: 3535353535, birthday: 06.03.1997
# Contact name: Mila, phones: 9519519519, birthday: 08.09.1983
# Enter a command: close
# Good bye!

# Address Book After Deserialization:
# Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
# Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
# Contact name: Janet, phones: 9875987210, birthday: 02.11.2001
# Contact name: Simon, phones: 3535353535, birthday: 06.03.1997
# Contact name: Mila, phones: 9519519519, birthday: 08.09.1983

# Serialization and deserialization successful! Data matches.