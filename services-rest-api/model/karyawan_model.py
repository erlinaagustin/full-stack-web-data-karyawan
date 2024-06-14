from sqlalchemy import(
  Column, String, Integer, Date, ForeignKey
)
from sqlalchemy.orm import relationship

from utils import Base

class Karyawan(Base):
    __tablename__ = "karyawans"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    jabatan = Column(String)
    department = Column(String)
      
