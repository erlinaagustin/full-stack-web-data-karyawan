import datastore
from sqlalchemy.ext.asyncio import AsyncSession
from schema import dataKaryawan, updateData, deleteData, getDatabyID



async def tambahDataKaryawan(data:dataKaryawan, db:AsyncSession):
    async with db as session:
        try:
            res, err = await datastore.tambahKaryawan(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
            
        except Exception as e:
            return None, e
        
async def lihatKaryawan(db:AsyncSession):
    async with db as session:
        try:
            res, err = await datastore.lihatDataKaryawan(session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        

async def lihatKaryawanID(data:getDatabyID, db:AsyncSession):
    async with db as session:
        try:
            res, err = await datastore.lihatDataKaryawanbyID(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e        

async def updateDataKaryawan(data:updateData, db:AsyncSession):
    async with db as session:
        try:
            if data.id=="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.updateKaryawan(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        
async def deleteDataKaryawan(data:deleteData, db:AsyncSession):
    async with db as session:
        try:
            if data.id=="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.deleteKaryawan(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e