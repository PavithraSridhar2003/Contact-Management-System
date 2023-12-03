""""Certainly! Below is a simple example of a contact management system in Python using a dictionary to store contacts. Note that this is a console-based implementation, and for a more user-friendly interface, you might want to explore graphical user interface (GUI) libraries like Tkinter."""

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'Phone': phone_number, 'Email': email, 'Address': address}

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"{name}: {details['Phone']}")

    def search_contact(self, search_term):
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['Phone']:
                print(f"{name}: {details['Phone']} {details['Email']} {details['Address']}")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['Phone'] = new_phone_number
            self.contacts[name]['Email'] = new_email
            self.contacts[name]['Address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

# Example usage:
contact_manager = ContactManager()
contact_manager.add_contact('John Doe', '123-456-7890', 'john@example.com', '123 Main St')
contact_manager.add_contact('Jane Smith', '987-654-3210', 'jane@example.com', '456 Oak St')

contact_manager.view_contacts()

contact_manager.search_contact('John')

contact_manager.update_contact('John Doe', '111-222-3333', 'john_new@example.com', '456 Pine St')

contact_manager.delete_contact('Jane Smith')

contact_manager.view_contacts()


#Feel free to adapt and extend this code based on your specific needs and use cases.