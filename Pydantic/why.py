from pydantic import BaseModel

#pydantic model for patient data
# what is pydantic model? pydantic is a data validation and settings management library for python. it uses python type annotations to validate the data.
# it is used to define the structure of the data and validate the data before it is stored in the database. it is also used to define the structure of the data that is returned from the database.

class Patient(BaseModel):
    name: str
    age: int
  #  medical_history: list[str]
  
  
def insert_patient(patient: Patient):
    """
    Function to insert a new patient into the database.
    This function takes a Patient object as input, validates it using Pydantic, and then inserts it into the database.
    """
    print(f"Inserting patient: {patient.name}, Age: {patient.age}")
  
  
  
"""Creating the object of the pydantic model. 
 this object will be used to validate the data before it is stored in the database."""
 
patient_info={"name": "John ", "age": 30}
patient1 = Patient(**patient_info)  # This will create a Patient object with the provided data, and pydantic will validate it. 
#(**kwargs is used to unpack the dictionary into keyword arguments for the Patient constructor.)

# calling the insert_patient function to insert the patient into the database.

insert_patient(patient1)  # This will call the insert_patient function with the validated Patient object.