from collections import UserDict


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as mess:
            print(f"Error. {str(mess)}")
            return

    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    @input_error
    def __init__(self, value):
        if not value:
            raise ValueError("Name can't be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        if len(value) != 10 or not value.isdigit():  # 10 digits check
            raise ValueError("Phone must consist of 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @input_error
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    @input_error
    def remove_phone(self, phone):
        if phone in map(str, self.phones):
            self.phones = [p for p in self.phones if p.value != phone]
        else:
            raise KeyError(f"Phone {phone} not found")

    @input_error
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise KeyError(f"Phone {old_phone} not found")

    @input_error
    def find_phone(self, phone):
        if phone in map(str, self.phones):
            return phone
        else:
            raise KeyError(f"Phone {phone} not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    @input_error
    def find(self, name):
        for record in self.data.keys():
            if record == name:
                return self.data[record]
        raise KeyError("Name not found")

    @input_error
    def delete(self, name):
        if name in self.data.keys():
            del self.data[name]
            return
        raise KeyError("Name not found")
