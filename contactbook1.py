from builtins import print, input
contacts={}
def add_contact():
    name=input("Enter Name:")
    phone=input("Enter Phone Number:")
    email=input("Enter Email:")
    address=input("Enter Address:")
    contacts[name]={
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("NO contacts found")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone:{info['Phone']}")
            print(f"Email:{info['Email']}")
            print(f"Address:{info['Address']}")

def search_contact(query):
      results = []
      for name, info in contacts.items():
          if query.lower() in name.lower() or query in info['Phone']:
              results.append((name,info))
      if results:
          print(f"Search results for '{query}':")
          for name,info in results:
              print(f"Name: {name}")
              print(f"Phone:{info['Phone']}")
              print(f"Email:{info['Email']}")
              print(f"Address:{info['Address']}")
      else:
          print("No matching contacts found")
def update_contact():
      name=input("Enter the name of the contact to update")
      if name in contacts:
          print(f"Updating contact:{name}")
          add_contact()
          print(f"Contact '{name}' not found")
def delete_contact():
      name=input("Enter the name of the contact to delete")
      if name in contacts:
          del contacts[name]
          print(f"Contact {name} deleted successfully!")
      else:
          print(f"Contact '{name}' not found")
while True:
      print("\nContact Book")
      print("1. Add Contact")
      print("2. View Contacts")
      print("3. Search Contact")
      print("4. Update Contact")
      print("5. Delete Contact")
      print("6. Exit")

      choice=input("Enter your choice(1-6):")
      if choice=='1':
          add_contact()
      elif choice=='2':
          view_contacts()
      elif choice=='3':
          query=input("Enter name or phone number to search:")
          search_contact(query)
      elif choice=='4':
          update_contact()
      elif choice=='5':
          delete_contact()
      elif choice=='6':
          break
      else:
          print("Invalid choice Please try again")



