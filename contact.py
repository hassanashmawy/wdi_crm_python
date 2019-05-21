class Contact:

  contacts = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    """This method should initialize the contact's attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id
    Contact.next_id += 1

  def __repr__(self):
    return '{} {} {} {}'.format(self.first_name, self.last_name,self.email, self.note)

  @classmethod
  def create(cls,first_name, last_name, email, note):
    new_contact = Contact(first_name, last_name, email, note)
    """This method should call the initializer,
    store the newly created contact, and then return it
    """
    cls.contacts.append(new_contact)

    return new_contact

    
    

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    for contact in cls.contacts:
      print(contact)

  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """
    for contact in cls.contacts:
      if int(id) == contact.id:
          return contact
    

  def update(self, attribute, value):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
    
    setattr(self, attribute, value)
    return self

  @classmethod
  def find_by(cls, attribute, value):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
    for contact in cls.contacts:
      if getattr(contact, attribute) == value:
        return contact
      # if attribute == 'first_name':
      #   if value == contact.first_name:
      #     return contact
      # elif attribute == 'last_name':
      #     if value == contact.last_name:
      #      return contact
      # elif attribute == 'email':
      #     if value == contact.email:
      #       return contact
      # elif attribute == 'note':
      #     if value == contact.note:
      #       return contact
      # elif attribute == 'id': 
      #     if value == contact.id:
      #       return contact


  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""
    del cls.contacts[0 : len(cls.contacts)]


  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return '{} {}'.format(self.first_name, self.last_name)


  def delete(self):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
    Contact.contacts.remove(self)

  # Feel free to add other methods here, if you need them.

# contact = Contact('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')


contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')

# print(len(Contact.contacts))
# # print(contact1.id)
# # print(contact2.id)
# Contact.all()
# Contact.find(2)
# print()
# print(Contact.find_by('email','bettymakes@bitmakerlabs.com'))
# print(contact1.full_name())
# Contact.delete_all()
# # print(Contact.contacts)
# # print(contact1.delete())
# print(contact1.update('first_name', 'John'))
# print(Contact.contacts)