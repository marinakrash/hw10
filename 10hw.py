from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

class Record:
    def __init__(self, 'name': Name, 'phone': Phone = None):
        self.name=name.name
        self.phone=phone.phone

    def add_phone(self, phone):
        self.phone.append(phone)

    def delete_phone(self, phone):
        self.phone.remove(phone)

    def update_phone(self, phone):
        self.phone.clear()
        self.phone.append(phone)

class Field:
    def __init__(self, name):
        self.name = name


class Name(Field):
    pass

class Phone(Field):
    def __init__(self, phone):
        self.phone=[]
        self.phone.append(phone)
