# Creating the pydantic model for patient data

from operator import lt
from turtle import title

from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50,title="Name",description="Patient's name")]   #  annotated is used for metadata .  name is a required field for 50 characters. if the name is more than 50 characters then pydantic will raise an error.
    age: int = Field(gt=0,lt=50)  # age should be a positive integer between 0 and 50
    weight: Annotated[float, Field(gt=0,strict=True)]   # weight should be a positive float , strict=True means that the value should be a float and not an integer. if the value is an integer then pydantic will raise an error.
    linkdin_url: Optional[AnyUrl] = None  #optional field for linkdin url. if the patient has a linkdin profile then it will be stored here else it will be None.
    bmi: float
    married: bool= False   #default value for married field is False. if the patient is married then it will be True else it will be False.
    allegries: Annotated[Optional[List[str]], Field(default=None, title="Allergies", description="List of patient's allergies")] = None
    contact_details: Dict[str, str]
    blood_group: Annotated[str, Field(title="Blood Group", description="Patient's blood group")]  #blood group should be one of the following A+, A-, B+, B-, AB+, AB-, O+, O-. if the blood group is not one of these then pydantic will raise an error.

    #optional fields can be added using Optional type hint --> this is useful when we want to make some fields optional in the model. for example if we want to make the allegries field optional we can do it like this: optional[allegries: List[str]] = None. this means that the allegries field can be either a list of strings or None. if it is None then it means that the patient has no allegries.
    
def insert_patient(patient: Patient):
    """
    Function to insert a new patient into the database.
    This function takes a Patient object as input, validates it using Pydantic, and then inserts it into the database.
    """
    
    print(f"inserting pateint: {patient.name} ")
    print(f"age: {patient.age} ")
    print(f"weight: {patient.weight} ")
    print(f"bmi: {patient.bmi} ")
    print(f"married: {patient.married} ")
    print(f"allegries: {patient.allegries} ")
    print(f"contact_details: {patient.contact_details} ")
    print(f"blood_group: {patient.blood_group} ")
    print("Patient inserted successfully into the database.")
    
    
    
    
    
Patient_info={"name": "John Doe", "age": 30, "weight": 70.5, "bmi": 22.5, "married": True, "allegries": ['pollen', 'dust'], "contact_details": {"phone": "123-456-7890", "email": ("john.doe@example.com")}, "blood_group": "O+", "linkdin_url": "https://www.linkedin.com/in/johndoe/"}
Patient1 = Patient(**Patient_info)  # This will create a Patient object with the provided data, and pydantic will validate it.
insert_patient(Patient1)


""" For the data validation pydatinc
use the inbuild validation method for example for tostore the email address in the contact_details field we can use the EmailStr type hint from pydantic. 
this will validate the email address and raise an error if the email address is not valid. for example if we want to store the email address in the contact_details field 
we can do it like this: contact_details: Dict[str, EmailStr]. this means that the contact_details field is a dictionary with string keys and EmailStr values.
if the value of the email key is not a valid email address then pydantic will raise an error.




# Constraints in pydantic model
pydantic also provides a way to add constraints to the fields in the model.
for example if we want to add a constraint to the age field that it should be greater than 0 then we can do it like this: age: conint(gt=0). this means that the age field is an integer and it should be greater than 0.
if the value of the age field is less than or equal to 0 then pydantic will raise an error.


"""