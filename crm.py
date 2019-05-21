from contact import Contact

class CRM:

  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)
  
  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')
  
  
  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit()
  # Finish off the rest for 3 through 6
  # To be clear, the methods add_new_contact and modify_existing_contact
  # don't do anything yet
  
  
  def add_new_contact(self):
    # get all the required info from our user:
    print('Enter First Name: ')
    first_name = input()

    print('Enter Last Name: ')
    last_name = input()

    print('Enter Email Address: ')
    email = input()

    print('Enter a Note: ')
    note = input()

    Contact.create(first_name, last_name, email, note)
  
  @classmethod
  def modify_existing_contact(cls):
    print('Enter ID: ')
    id = input()
    contact = Contact.find(id)
    print(contact)
    print('please enter an attribute to change')
    n_attribute = input()
    print('please enter a new value')
    n_value = input()
    contact.update(n_attribute, n_value)
    return contact.update
    
    

  def delete_contact(self):
    print('Please enter ID of contact to delete: ')
    id = input()
    contact = Contact.find(int(id))
    contact.delete()
  
  
  def display_all_contacts(self):
    Contact.all()
  
  def search_by_attribute(self):
    print('Which attribute would you like to search by?: ')
    attribute = input()
    print('Which value would you like to search by?: ')
    value = input()
    show_contact = Contact.find_by(attribute, value)
    print(show_contact)
    

a_crm_app = CRM()
a_crm_app.main_menu()

