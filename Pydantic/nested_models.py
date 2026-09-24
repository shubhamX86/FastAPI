# Nested Models : it means that one model can contain another model as a field.
# This allows for more complex data structures and better organization of related data.
# Nested models are useful when you have a model that contains other models as part of its structure.


from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    street: str
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name:str
    gender: str
    age: int
    address: Address  # Nested model: Address is a field in the Patient model
    
    


address_info = {"street": "123 Main St", "city": "New York", "state": "NY", "pin": "10001"}
patient_info = {"name": "John Doe", "gender": "male", "age": 30, "address": address_info}  


address1= Address(**address_info)  # This will create an Address object with the provided data, and pydantic will validate it.
patient1= Patient(**patient_info)  # This will create a Patient object with the provided
  
  
  
print(patient1)
print(patient1.name)
print(patient1.address.pin)
print(patient1.address.city)




# Advantage of nested models are :

# 1) 