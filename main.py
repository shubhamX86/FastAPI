# making a fastapi application for doctor to manage his patients details.

#to run the app use the command: uvicorn main:app --reload

from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field,computed_field
from typing import Annotated,Literal, Optional
import json

app = FastAPI()

#===============================================================================================
# Creating a Pydantic model for patient data. This model will be used to validate the data before it is stored in the database.
class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description="The ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="The name of the patient", example="John Doe")]
    city: Annotated[str, Field(..., description="The city of the patient", example="New York")]
    age: Annotated[int, Field(...,gt=0, lt=100, description="The age of the patient", example=30)]
    gender: Annotated[Literal["Male", "Female", "others", "male", "female"], Field(..., description="The gender of the patient", example="Male")]
    
    height: Annotated[float, Field(..., gt=0,description="The height of the patient in meters", example=175.5)]
    weight: Annotated[float, Field(..., gt=0,description="The weight of the patient in kilograms", example=70.5)]
    
    
    # computed field to calculate the BMI of the patient based on their height and weight. The BMI is calculated using the formula: BMI = weight (kg) / (height (m) * height (m)).
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    # computed field to determine the health verdict of the patient based on their BMI. The verdict is determined using the following criteria:
    # Underweight: BMI < 18.5 
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
#===================================================================================================================================================================================================================
# pydantic model for patient update data. This model will be used to validate the data before it is updated in the database. The fields in this model are optional, so that the doctor can update only the fields that he wants to update.

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="The name of the patient", example="John Doe")]
    city: Annotated[Optional[str], Field(default=None, description="The city of the patient", example="New York")]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=100, description="The age of the patient", example=30)]
    gender: Annotated[Optional[Literal["Male", "Female", "others", "male", "female"]], Field(default=None, description="The gender of the patient", example="Male")]
    height: Annotated[Optional[float], Field(default=None, gt=0, description="The height of the patient in meters", example=175.5)]
    weight: Annotated[Optional[float], Field(default=None, gt=0, description="The weight of the patient in kilograms", example=70.5)]
#===============================================================================================================================================================================================
# Utility functions to load and save data from/to the database. In this case, the database is a JSON file named "patients.json". The load_patients function reads the data from the JSON file and returns it as a list of dictionaries. The save_data function writes the data to the JSON file.

#creating a helper function to load the data from the database. here the our data base is a json file named "patients.json". we will load the data from this file and return it as a list of dictionaries.

def load_patients():
    with open("patients.json", "r") as f:
        data=json.load(f)
    return data

#saving the data to the database. here the our data base is a json file named "patients.json". we will save the data to this file.
def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)

#=============================================================================================================


#=====================================================================================================================
#Endpoints for the FastAPI application. These endpoints will be used to perform CRUD operations on the patient data. The endpoints are defined using the FastAPI decorators and the Pydantic model is used to validate the data before it is stored in the database.
#===============================================================================================================================

@app.get("/")
def hello():
    return {"message": "Patient Management System"}


@app.get("/about")
def about():
    return {"message": "A fully functional patient management system built with FastAPI."}

@app.get('/view')
def view():
    return load_patients()


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str=Path(..., description="The ID of the patient to view", example="P001")):
    
    #load all the patients from the database and find the patient with the given id. if found return the patient details else return a message saying patient not found.
    
    data= load_patients()
    
    #iterate through the list of patients and find the patient with the given id. if found return the patient details else return a message saying patient not found.
    
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    
    

@app.get('/sort')   
def sort_patient(sort_by: str=Query(..., description="sort the patients on the basic of height,weight or bmi", example="bmi"),order: str=Query("asc", description="sort the patients in ascending or descending order")):
    
    
    valid_fileds=["height","weight","bmi"]
    if sort_by not in valid_fileds:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fileds)}")
    
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Valid orders are: asc, desc")
    
    data= load_patients()
    
    sort_order= True if order=="asc" else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data



@app.post('/create')
def create_patient(patient: Patient):
    
    #load the data from the database and check if the patient with the given id already exists in the database. if yes return a message saying patient already exists else add the patient to the database and return a message saying patient created successfully.
    data = load_patients()
    
    # check if the patient with the given id already exists in the database. if yes return a message saying patient already exists else add the patient to the database and return a message saying patient created successfully.
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    #new patient is added to the database and the data is saved to the json file.
    
    data[patient.id] = patient.model_dump(exclude=['id']) 
    
    # convert the patient object to a dictionary and add it to the data dictionary.
    
    # save the data to the database.
    save_data(data)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})


@app.put('/update/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    #load the data from the database and check if the patient with the given id exists in the database. if yes update the patient details else return a message saying patient not found.
    data = load_patients()
    
    # check if the patient with the given id exists in the database. if yes update the patient details else return a message saying patient not found.
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    
    existing_patient_info=data[patient_id]  # get the existing patient details from the database.
    
    #update the patient details with the new data provided in the request body.
    updated_patient_info = patient_update.model_dump(exclude_unset=True)  # Get only the fields that were provided in the request body
        
    merged_patient_info = {**existing_patient_info, **updated_patient_info}  # Merge the existing patient info with the updated info
    merged_patient_info.pop('bmi', None)                                    # Remove the BMI field from the merged info, as it will be recalculated based on the updated height and weight
    merged_patient_info.pop('verdict', None)                                 # Remove the verdict field from the merged info, as it will be recalculated based on the updated BMI
    merged_patient_info['id'] = patient_id    # Add the patient ID back to the merged info, as it is required for creating a new Patient object
                     
     
     
    patient_pydantic_obj = Patient(**merged_patient_info)  # Create a new Patient object with the updated info

#->pydantic ojbj-> dict
    updated_patient_record = patient_pydantic_obj.model_dump(exclude=['id'])  # Convert the updated Patient object back to a dictionary, excluding the ID
    
    #add this dic to data
    
    data[patient_id] = updated_patient_record  # Update the patient info in the data dictionary
    # save the updated data to the database.
    save_data(data)
    
    # return the updated patient so the recalculated bmi and verdict are visible immediately.
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient": data[patient_id]})




@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    #load the data from the database and check if the patient with the given id exists in the database. if yes delete the patient details else return a message saying patient not found.
    data = load_patients()
    
    # check if the patient with the given id exists in the database. if yes delete the patient details else return a message saying patient not found.
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    #delete the patient details from the database.
    del data[patient_id]
    
    # save the updated data to the database.
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})