from schema import dataKaryawan, updateData, deleteData, getDatabyID
from model import Karyawan
from sqlalchemy import select,  update, delete
import datetime

    
async def tambahKaryawan(data:dataKaryawan, session):
    try:
        paramsInsert = Karyawan(
            nama = data.nama,
            jabatan = data.jabatan,
            department = data.department
            )

        session.add(paramsInsert)
        return data, None
    
    except Exception as e:
        return None, e
    
async def updateKaryawan(data:updateData, session):
    try:
        query = update(Karyawan).where(Karyawan.id == data.id).values(
            nama = data.nama, 
            jabatan = data.jabatan, 
            department = data.department)
        
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e
    
async def deleteKaryawan(data:deleteData, session):
    try:
        query = delete(Karyawan).where(Karyawan.id == data.id)
        
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e
    
async def lihatDataKaryawan(session):
    try:
        query = select(Karyawan)
        result = await session.execute(query)
        karyawan = result.scalars().all()

        return karyawan, None
    except Exception as e:
        return None, e

    
async def lihatDataKaryawanbyID(data: getDatabyID, session):
    try:
        query = select(Karyawan).where(Karyawan.id == data.id)
        result = await session.execute(query)
        karyawan = result.scalars().first()

        return karyawan, None
    except Exception as e:
        return None, e
      


