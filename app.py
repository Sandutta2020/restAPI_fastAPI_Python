from fastapi import FastAPI,HTTPException
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import uvicorn
class Employee(BaseModel):
    eid: str
    ename:str
    sal:int
app = FastAPI()

df =pd.read_csv('employee.csv')

@app.get('/')
def employee_list():
    return df.to_dict('split')
@app.get('/employee_filtered')
def user_list(minsal: Optional[int] = None, maxsal: Optional[int] = None):

    if minsal and maxsal:
        df_new =df[(df['sal'] >= minsal) &  (df['sal'] <= maxsal)]
        return df_new.to_dict('split')
    else:
        return {'employee': "Invalid Query"}

@app.post('/employees')
def user_add(employee: Employee):
    global df
    print(pd.DataFrame({"eid":employee.eid,"ename":employee.ename,"sal":employee.sal}, index=[len(df)]))
    df=pd.concat([df,pd.DataFrame({"eid":employee.eid,"ename":employee.ename,"sal":employee.sal}, index=[len(df)])]).reset_index()
    return df.to_dict('split')

def employee_existence_check(eid):
    try:
        if eid in df['eid'].values:
            return True
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail='Employee Not Found')

@app.put('/employees/{eid}')
def user_update(employee: Employee, eid: str):
    employee_existence_check(eid)
    print(employee)
    df.loc[df['eid']==eid,'ename']=employee.ename
    df.loc[df['eid']==eid,'sal']=employee.sal
    return df.to_dict('split')

@app.delete('/employees/{eid}')
def user_delete(eid: str):
    employee_existence_check(eid)
    df.drop(df[(df['eid']==eid)].index ,inplace=True)
    return df.to_dict('split')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
