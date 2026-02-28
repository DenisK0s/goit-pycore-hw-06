from collections import UserDict

class Field:
    def __init__(self, value):
        self._validate(value)
        self.value = value
    
    def _validate(self, value):
        pass

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    REQUIRED_LENGTH = 10
    
    def _validate(self, phone):
        if len(phone) != Phone.REQUIRED_LENGTH:
            raise ValueError(f"The phone number must be {Phone.REQUIRED_LENGTH} digits long!")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, new_phone: str):
        try:
            is_phone_exists = self._is_phone_exists(new_phone)
            if is_phone_exists:
                print(f"The phone number {new_phone} already exists!")
                return

            phone = Phone(new_phone)
            self.phones.append(phone)
            print(f"The phone number {phone} has been successfully added!")
        except ValueError as e:
            print(f"ValueError: {e}") 
          
    def remove_phone(self, phone_to_remove: str):
        phone = self.find_phone(phone_to_remove)
        if phone:
            self.phones.remove(phone)  
            print(f"The phone number {phone} has been successfully removed!")
         
    def edit_phone(self, old_phone: str, new_phone: str):
        phone = self.find_phone(old_phone)
        if phone:
            old_phone_index = self.phones.index(phone)
            self.phones[old_phone_index] = Phone(new_phone)
         
    def find_phone(self, phone: str) -> Phone | None:
        if not len(self.phones) > 0:
            print("The phone list is empty.")
        elif not self._is_phone_exists(phone):
            print("Phone number {phone} not found.")
        else:
            result = list(filter(lambda p: p.value == phone, self.phones))
            return result[0]
        
    def _is_phone_exists(self, phone):
        return any(p.value == phone for p in self.phones)
                 
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
       def add_record(self, new_record: Record):
        new_record_key = new_record.name.value

        if new_record_key in self.data:
            print(f"Record with name {new_record_key} already exists!")
            return
        
        self.data[new_record_key] = new_record
        print("Record was successfully added!")
       
       def delete(self, record_name: str):
            record = self.find(record_name)
            if record:
                 del self.data[record_name]
                 print("Record was successfully deleted!")

       def find(self, record_name: str) -> Record:
            record = self.data.get(record_name)
            return record or print("Record not found!")