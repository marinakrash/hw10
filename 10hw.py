from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, Record.name, Record.phone):
        self.data[Record.name]=Record.phone

class Record:
    name=Field._name
    phone=Field.all_phone_num

    def add_phone(self, _phone):
        self.phone.append(_phone)

    def delete_phone(self, _phone):
        self.phone.remove(_phone)

    def update_phone(self, _phone):
        self.phone.clear()
        self.phone.append(_phone)

class Field:
    def __init__(self, Name.new_name):
        self._name_ = Name.new_name

    all_phone_num = []

class Name(Field):
    new_name=''

class Phone(Field):
    def __init__(self, phone_num):
        self.phone_num = phone_num
