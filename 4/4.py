def parse_input(user_input):
    if not user_input.strip():  
        return "", []  
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "There is no contact with this name."
        except IndexError:
            return "Give me name."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "This name already in contacts"
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]  
    return f"{name}: {contacts[name]}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
l

if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "":
            print("You didn't enter any command. Please try again.")
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
