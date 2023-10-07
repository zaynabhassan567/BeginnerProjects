import csv


def main():
    print("Welcome to the Online Registration System")

    while True:
        choice = input("Enter '1' to register, '2' to view registrations, or 'q' to quit: ")

        if choice == '1':
            register()
        elif choice == '2':
            view_registrations()
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    with open('registrations.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    print("Registration successful!")


def view_registrations():
    try:
        with open('registrations.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, email, phone = row
                print(f"Name: {name}, Email: {email}, Phone: {phone}")
    except FileNotFoundError:
        print("No registrations found.")


if __name__ == '__main__':
    main()
