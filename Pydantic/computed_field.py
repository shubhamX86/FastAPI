# Computed Field is a Pydantic feature that allows you to define computed fields in your models. These fields are not stored in the database but are derived from other fields in the model.
# You can use computed validators to perform calculations, transformations, or any other logic needed to derive the value of a field based on other fields.  

# deriving the BMI (Body Mass Index) of a patient based on their weight and height. The BMI is calculated using the formula: BMI = weight (kg) / (height (m) * height (m)).


from pydantic import BaseModel, EmailStr, computed_field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allegries: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    
    
       
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
        print(f"bmi: {patient.bmi} ")
        print("Patient inserted successfully into the database.")
        
        
patient_info={"name": "John Doe", "email": "xyz@hdfc.com", "age": 40, "weight": 70.5, "height": 1.75, "married": True, "allegries": ['pollen', 'dust'], "contact_details": {"phone": "123-456-7890", "email": "john.doe@example.com", "emergency_contact": "987-654-3210"}}

patient1= Patient(**patient_info)
insert_patient(patient1)