

from fastapi import FastAPI
from pydantic import BaseModel
import requests

import json
app=FastAPI()


db={}
import requests




class Employee(BaseModel):
    id:int 
    employee_name:str
    employee_age:int
    employee_salary:int
'''
Base = declarative_base()


class Employee(BaseModel):
    __tablename__ = 'employee'
    id = Column(Integer(), primary_key=True, nullable=False, unique=True)
    employee_name = Column(String(40), nullable=False)
    employee_age =Column(Integer())
    employee_salary = Column(Integer())'''
  

@app.get('/')
def index():
	return {'key' : 'value'}

@app.get('/employee')
def get_employee():
	
	r=requests.get(f'http://dummy.restapiexample.com/api/v1/employees')
	
	print(r.status_code)
	current = r.json().get('data')
	
	
	
	return current


@app.post('/employee')
def create_employee(employee:Employee):
	print(employee)
	id=employee.dict().get('id')
	#r = requests.post(f'http://dummy.restapiexample.com/api/v1/create' ,json=json.dumps(employee, default=json_util.default))
	#current = r.json().get('data')
	#print(current)
	#return current
	if db.get(id):

		return db
	db[id]=employee.dict()
	return db



@app.post('/allemployee')
def all_employee(employee:Employee):
	

	j=requests.get(f'http://dummy.restapiexample.com/api/v1/employees')
	print(j.status_code)
	currents = j.json().get('data')
	currents.append(create_employee(employee))
	


	return currents

if __name__ == '__main__':
	uvicorn.run(app, host="127.0.0.1", port=8000)