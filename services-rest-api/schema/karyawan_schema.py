from pydantic import BaseModel

class dataKaryawan(BaseModel):
    nama:str
    jabatan:str
    department:str

class updateData(BaseModel):
    id: int
    nama: str
    jabatan: str
    department: str

class deleteData(BaseModel):
    id: int

class getDatabyID(BaseModel):
    id:int