from pydantic import BaseModel,EmailStr,AnyUrl, field_validator
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name:str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allegries: List[str]
   
    
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        """
        Custom validator for the email field.
        This method will be called automatically by Pydantic when validating the email field.
        It checks if the email domain is 'example.com' and raises a ValueError if it is not.
        """
        vaild_domains = ['hdfc.com',  'icici.com']
        domain_name= value.split('@')[-1]
        
        if domain_name not in vaild_domains:
            raise ValueError(f'Email domain must be one of the following: {", ".join(vaild_domains)}')
        return value
        
        
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        """
        Custom validator for the name field.
        This method will be called automatically by Pydantic when validating the name field.
        It transforms the name to uppercase before storing it in the database.
        """
        return value.upper()
    
    
    @field_validator('age')
    @classmethod
    def validate_age(cls, value):
        """
        Custom validator for the age field.
        This method will be called automatically by Pydantic when validating the age field.
        It checks if the age is a positive integer and raises a ValueError if it is not.
        """
        if value < 1 or value > 49:
            raise ValueError('Age must be between 1 and 49')
        return value
    
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
        print("Patient inserted successfully into the database.")
        
        
patient_info={"name": "John Doe", "email": "xyz@hdfc.com", "age": 40, "weight": 70.5, "married": True, "allegries": ['pollen', 'dust']}

patient1= Patient(**patient_info)
insert_patient(patient1)