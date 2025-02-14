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
        print(f"✅ Contact '{name}' added successfully!")

    def search_contact(self, name):
        results = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if results:
            print("\n🔎 Search results:")
            for contact in results:
                print(contact)
        else:
            print(f"❌ No contact found with the name '{name}'")

    def display_all_contacts(self):
        if self.contacts:
            print("\n📒 All contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("📭 No contacts in the phone book.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"🗑️ Contact '{name}' deleted successfully!")
                return
        print(f"❌ No contact found with the name '{name}'")

    def edit_contact(self, name, new_phone, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                contact.address = new_address
                print(f"✏️ Contact '{name}' updated successfully!")
                return
        print(f"❌ No contact found with the name '{name}'")


phone_book = PhoneBook()

while True:
    print("\n📞 Phone Book Menu:")
    print("1️⃣ Add a contact")
    print("2️⃣ Search a contact by name")
    print("3️⃣ Display all contacts")
    print("4️⃣ Delete a contact")
    print("5️⃣ Edit a contact")
    print("6️⃣ Exit")

    choice = input("Enter your choice (1-6): ")

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
        delete_name = input("Enter the name of the contact to delete: ")
        phone_book.delete_contact(delete_name)

    elif choice == '5':
        edit_name = input("Enter the name of the contact to edit: ")
        new_phone = input("Enter new phone number: ")
        new_address = input("Enter new address: ")
        phone_book.edit_contact(edit_name, new_phone, new_address)

    elif choice == '6':
        print("👋 Exiting phone book. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
