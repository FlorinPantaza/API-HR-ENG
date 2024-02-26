from fastapi import FastAPI, HTTPException, status

from pydantic import BaseModel

from typing import Optional

app = FastAPI()

class Item(BaseModel):

    Name: str

    Job_title: str

    Competence: str

    Time_in_hours: int

class UpdateItem(BaseModel):

    Name: Optional[str] = None

    Job_title: Optional[str] = None

    Competence: Optional[str] = None

    Time_in_hours: Optional[int] = None

management = {
    
    1:{
        "Name":"Paul",
        
        "Job_title":"Manager",

        "Competence":"Manages_the_company",

        "Time_in_hours":"8"
    },

    2:{
        "Name":"Evelyn",

        "Job_title":"Project_manager",

        "Competence":"Manages_the_projects",

        "Time_in_hours":"8"
    },

    3:{
        "Name":"Steve",

        "Job_title":"Team_leader",

        "Competence":"Lead_the_IT_team_and_HR",

        "Time_in_hours":"8"
    },

    4:{
        "Name":"Jane",

        "Job_title":"Softwaredeveloper_first_level",

        "Competence":"Write_code",

        "Time_in_hours":"10"
    },

    5:{ 
        "Name":"Dan",

        "Job_title":"Softwaredeveloper_second_level",

        "Competence":"Control_Jane",

        "Time_in_hours":"10"

    }

}   


@app.get('/')

def My_Company():

    return {'Mesage':'Wellcome to my Company'}

@app.get('/contact')

def contact():

    return {'Mesage':'This is my contact Page'}    

@app.get('task/{item_id}')

def get_task(item_id: int):

    if item_id not in management:

        return HTTPException(status_code=404, detail="This ID was not found")

    return management[item_id]   

@app.post('/create_task/{item_id}')

def create_task(item_id: int, item: Item):

    if item_id in management:

        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This ID exist already")

    management[item_id] = {"Name":item.Name, "Job_titel":item.Job_titel, "Compentence":item.Competence, "Time_in_hours":item.Time_in_hours}
    
    return management[item_id]

@app.delete('/delete-task/')

def delete_task(item_id:int):

    if item_id not in management:

        return HTTPException(status_code=404, detail="This ID was not found")

    del management[item_id]

    return HTTPException(status_code=200) 

@app.put('update_management/{item_id}')

def update_management(item_id:int, item:UpdateItem):

    if item_id not in management:

        return HTTPException(status_code=404, detail="This ID was not found")

    if item.Name != None:

        management[item_id]["Name"] = item.Name

    if item.Job_title != None:
        
        management[item_id]["Job_title"] = item.Job_title

    if item.Competence != None:

        management[item_id]["Competence"] = item.Competence

    if item.Time_in_hours != None:

        management[item_id]["Time_in_hours"] = item.Time_in_hours

    return management[item_id]                  