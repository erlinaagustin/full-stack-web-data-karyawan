from pydantic import BaseModel

class daftarAkun(BaseModel):
    nama:str
    username:str
    password:str

class loginAkun(BaseModel):
    username:str
    password:str