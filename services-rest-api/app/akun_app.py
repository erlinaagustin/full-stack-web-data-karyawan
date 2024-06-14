import datastore
from sqlalchemy.ext.asyncio import AsyncSession
from schema import daftarAkun, loginAkun

async def registrasiAkun(data:daftarAkun, db:AsyncSession):
    async with db as session:
        try:
            res, err = await datastore.registerAkun(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
            
        except Exception as e:
            return None, e

async def login(data: loginAkun, db: AsyncSession):
    async with db as session:
        try:
            if data.username == "" or data.password == "":
                raise Exception(f"username and password must be provided")
            
            res, err = await datastore.loginAccount(data.username, data.password, session)
            if err is not None or res["username"] != data.username:
                raise Exception("username and password not be valid")
            
            await session.commit()

            return res, None
        except Exception as e:
            return None, e