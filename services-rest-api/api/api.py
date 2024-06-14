from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import data_app
from app import akun_app
from utils import get_async_session, respOutCustom
from schema import daftarAkun, loginAkun, dataKaryawan, updateData, deleteData, getDatabyID

router = APIRouter()


@router.post("/register/")
async def registerAkunRouter(
    request:daftarAkun,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await akun_app.registrasiAkun(request, db)
    if err != None:
        return respOutCustom("02", f"registrasi akun gagal: {err}", None)
    
    return respOutCustom("00", "sukses", outResponse)

@router.post("/login/")
async def loginAkunRouter(
    request: loginAkun,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await akun_app.login(request, db)
    if err != None:
        return respOutCustom("02", f"login gagal: {err}", None)
    
    return respOutCustom("00", "sukses", outResponse)

@router.post("/tambah-data-karyawan/")
async def tambahKaryawanRouter(
    request:dataKaryawan,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await data_app.tambahDataKaryawan(request, db)
    if err != None:
        return respOutCustom("02", f"tambah data karyawan gagal: {err}", None)
    
    return respOutCustom("00", "sukses", outResponse)

@router.get("/lihat-data-karyawan/")
async def lihatKaryawanRouter(
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await data_app.lihatKaryawan(db)
    if err !=None:
        return respOutCustom("02", f"data gagal ditampilkan: {err}", None)
    return respOutCustom("00", "sukses", outResponse)

@router.get("/lihat-data-karyawan-by-id/")
async def lihatKaryawanIDRouter(
    id: int,
    db: AsyncSession = Depends(get_async_session)
):
    request = getDatabyID(id=id)
    outResponse, err = await data_app.lihatKaryawanID(request, db)
    if err is not None:
        return respOutCustom("02", f"data gagal ditampilkan: {err}", None)
    return respOutCustom("00", "sukses", outResponse)

@router.post("/update-data-karyawan/")
async def updateKaryawanRouter(
    request:updateData,
    db:AsyncSession = Depends(get_async_session)
):
    outResponse, err = await data_app.updateDataKaryawan(request, db)
    if err != None:
        return respOutCustom("02", f"update data gagal: {err}", None)
    
    return respOutCustom("00", "sukses", outResponse)

@router.delete("/delete-data-karyawan/")
async def deleteKaryawanRouter(
    request:deleteData,
    db:AsyncSession = Depends(get_async_session)
):
    outResponse, err = await data_app.deleteDataKaryawan(request, db)
    if err != None:
        return respOutCustom("02", f"hapus data gagal: {err}", None)
    
    return respOutCustom("00", "sukses", outResponse)


