class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"


def input_error(error_message=""):
    def error_decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error_detail:
                error_detail = str(error_detail) or "no details"
                error_descr = f"Error. {error_message} Details: {error_detail}"
                return colors.RED + error_descr + colors.END

        return inner

    return error_decorator


@input_error("Can`t parse the input")
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error("Can't add contact. Give me name and phone please.")
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error("Can't change contact. Give me name and phone please.")
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        raise ValueError("Name not found")


@input_error("Can`t show phone.")
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise ValueError("Name not found")


@input_error()
def show_all(contacts):
    all_list = ""
    for name, phone in contacts.items():
        all_list += f"{name}: {phone}\n"
    return all_list.removesuffix("\n")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
