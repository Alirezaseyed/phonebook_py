class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Address: {self.address}"


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, address):
        contact = Contact(name, phone, address)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def search_contact(self, name):
        results = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if results:
            print("Search results:")
            for contact in results:
                print(contact)
        else:
            print(f"No contact found with the name '{name}'")

    def display_all_contacts(self):
        if self.contacts:
            print("All contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts in the phone book.")


# Example usage
phone_book = PhoneBook()

while True:
    print("\nPhone Book Menu:")
    print("1. Add a contact")
    print("2. Search a contact by name")
    print("3. Display all contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        phone_book.add_contact(name, phone, address)

    elif choice == '2':
        search_name = input("Enter the name to search: ")
        phone_book.search_contact(search_name)

    elif choice == '3':
        phone_book.display_all_contacts()

    elif choice == '4':
        print("Exiting phone book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
