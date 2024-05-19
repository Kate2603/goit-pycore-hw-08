import pickle
from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday already exists for this contact.")

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = self.birthday.value if self.birthday else "No birthday"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phones == other.phones and self.birthday == other.birthday
        return False


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                if (birthday_date - today).days <= 7:
                    upcoming_birthdays.append((record.name.value, birthday_date.strftime("%d.%m.%Y")))
        return upcoming_birthdays


def parse_input(user_input):
    return user_input.split()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)
    return wrapper


@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    message = ""
    if record:
        record.add_birthday(birthday)
        message = "Birthday added."
    else:
        message = f"Contact {name} not found."
    return message


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return f"{record.name.value}: {record.birthday.value}"
    else:
        return f"No birthday found for {name}."


@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"{name}: {birthday}" for name, birthday in upcoming_birthdays])
    else:
        return "No upcoming birthdays found."


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    # Load the serialized data from the file at the start of the application
    book = load_data()  # Initialize the address book with existing data
    print("Initial Address Book:")
    for name, record in book.data.items():
        print(record)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)  # Save the address book data before exiting
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            name, phone, *_ = args
            record = book.find(name)
            message = "Contact updated."
            if record is None:
                record = Record(name)
                book.add_record(record)
                message = "Contact added."
            if phone:
                record.add_phone(phone)
            print(message)

        elif command == "change":
            name, old_phone, new_phone = args
            record = book.find(name)
            if record:
                record.edit_phone(old_phone, new_phone)
                print("Phone number updated.")
            else:
                print(f"Contact {name} not found.")

        elif command == "phone":
            name, *_ = args
            record = book.find(name)
            if record:
                phones = "; ".join(p.value for p in record.phones)
                print(f"Phones for {name}: {phones}")
            else:
                print(f"Contact {name} not found.")

        elif command == "all":
            for name, record in book.data.items():
                print(record)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

    # Serialize the address book data to a file before exiting
    save_data(book)

    # Load the serialized data back into a new address book (for demonstration)
    new_book = load_data()

    # Print the new state of the address book after deserialization
    print("\nAddress Book After Deserialization:")
    for name, record in new_book.data.items():
        print(record)

    # Compare the data in the original and new address books
    if book.data == new_book.data:
        print("\nSerialization and deserialization successful! Data matches.")
    else:
        print("\nSerialization and deserialization failed! Data mismatch.")


if __name__ == "__main__":
    main()

