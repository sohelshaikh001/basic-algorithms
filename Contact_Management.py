
# Contact Manager Application Using List and Tuple


contacts_details = []

def add_info_contact(): 
    name = input("Enter full Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    for contact in contacts_details:
        if contact[0].lower() == name.lower():
            print("Contact with this name already exists!")
            return
    
    contacts_details.append((name, phone, email))
    print("Details added successfully!")

def view_info_contacts():
    if not contacts_details:
        print("No contacts found.")
        return
    
    print("\nContacts List:")
    for contact in contacts_details:
        print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

def search_info_contact():
    name = input("Enter Name to Search: ")
    
    for contact in contacts_details:
        if contact[0].lower() == name.lower():
            print(f"Found: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            return
    print("Contact not found!")

def update_info_contact():
    name = input("Enter Name to Update: ")
    
    for index, contact in enumerate(contacts_details):
        if contact[0].lower() == name.lower():
            new_phone = input("Enter New Phone Number: ")
            contacts_details[index] = (contact[0], new_phone, contact[2])
            print("Phone number updated successfully!")
            return
    print("Contact not found!")

def delete_info_contact():
    name = input("Enter Name to Delete: ")
    
    for contact in contacts_details:
        if contact[0].lower() == name.lower():
            contacts_details.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def main():
    while True:
        print("\nWelcome to Contact Manager")
        print("A. Add")
        print("B. View")
        print("C. Search")
        print("D. Update")
        print("E. Delete")
        print("F. Exit")
        choice = input("Enter the keyword: ")
        
        if choice == 'A':
            add_info_contact()
        elif choice == 'B':
            view_info_contacts()
        elif choice == 'C':
            search_info_contact()
        elif choice == 'D':
            update_info_contact()
        elif choice == 'E':
            delete_info_contact()
        elif choice == 'F':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid keyword! Please try again.")

main()
