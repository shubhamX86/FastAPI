# Model validator functions are used to validate and transform data before it is assigned to model fields. 
# They can be defined using the `@model_validator` decorator, which allows you to specify the validation logic for a particular field or the entire model.



from pydantic import BaseModel,EmailStr,AnyUrl, field_validator, model_validator
from typing import List,Dict,Optional,Annotated

from sqlalchemy import values

from sqlalchemy import values


class Patient(BaseModel):
    name:str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allegries: List[str]
    contact_details: Dict[str, str]
    
    
    
    @model_validator(mode='after')  
    def validate_emegrgency_contact(cls, model):
        """
        Custom model validator to ensure that the emergency contact is provided if the patient is married.
        This method will be called automatically by Pydantic after all fields have been validated.
        It checks if the patient is married and raises a ValueError if the emergency contact is not provided.
        """
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact must be provided for patients over 60 years old')
        return model
   

   
   
   
   
def insert_patient(patient: Patient):
        """
        Function to insert a new patient into the database.
        This function takes a Patient object as input, validates it using Pydantic, and then inserts it into the database.
        """
        
        print(f"inserting pateint: {patient.name} ")
        print(f"email: {patient.email} ")
        print(f"age: {patient.age} ")
        print(f"weight: {patient.weight} ")
        print(f"married: {patient.married} ")
        print(f"allegries: {patient.allegries} ")
        print(f"contact_details: {patient.contact_details} ")
        print("Patient inserted successfully into the database.")
        
        
patient_info={"name": "John Doe", "email": "xyz@hdfc.com", "age": 40, "weight": 70.5, "married": True, "allegries": ['pollen', 'dust'], "contact_details": {"phone": "123-456-7890", "email": "john.doe@example.com", "emergency_contact": "987-654-3210"}}

patient1= Patient(**patient_info)
insert_patient(patient1)