from schema import daftarAkun, loginAkun
from model import Akun
from sqlalchemy import select,  update,  and_
from fastapi.encoders import jsonable_encoder

    
async def registerAkun(data:daftarAkun, session):
    try:
        paramsInsert = Akun(
            nama = data.nama,
            username = data.username,
            password = data.password
            )

        session.add(paramsInsert)
        return data, None
    
    except Exception as e:
        return None, e

async def loginAccount(username:str, password:str, session):
    try:
        query = select(Akun).filter(and_(Akun.username == username, Akun.password == password))
        data = await session.execute(query)
        proxy = data.scalars().first()
        
        if proxy not in (None, []):
            return jsonable_encoder(proxy), None
        else:
            raise Exception("data not found")
    except Exception as e:
        return None, e

