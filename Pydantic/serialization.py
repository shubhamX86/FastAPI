# Nested Models : it means that one model can contain another model as a field.
# This allows for more complex data structures and better organization of related data.
# Nested models are useful when you have a model that contains other models as part of its structure.


from xml.etree.ElementInclude import include

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
  
  
  
temp=patient1.model_dump() # This will convert the Patient object into a dictionary, including the nested Address model.
print("\n")
temp=patient1.model_dump(include={'address'}) # This will convert the Patient object into a JSON string, including the nested Address model.
temp=patient1.model_dump(exclude={'address': {'street'}}) # This will convert the Patient object into a JSON string, excluding the street field of the nested Address model.
print(temp)
print(type(temp))