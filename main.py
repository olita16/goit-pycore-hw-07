import datetime
from address_book import AddressBook, Record, Birthday

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            return "Invalid input. Please check the format and try again."
    return wrapper

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    
    record.add_birthday(birthday)
    return f"Birthday for {name} added."

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    
    birthday = record.birthday
    if not birthday:
        return f"Birthday for {name} is not set."
    
    return f"{name}'s birthday is on {birthday.value.strftime('%d.%m.%Y')}."

@input_error
def birthdays(args, book):
    return "\n".join(book.get_upcoming_birthdays())

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    
    record.edit_phone(old_phone, new_phone)
    return f"Phone number for {name} updated."

@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact {name} not found."
    
    return f"{name}'s phones: {'; '.join(p.value for p in record.phones)}"

@input_error
def show_all_contacts(book):
    if not book.data:
        return "No contacts available."
    return "\n".join(str(record) for record in book.data.values())

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
