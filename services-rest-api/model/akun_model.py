from sqlalchemy import(
  Column, String, Integer, Date, ForeignKey
)
from sqlalchemy.orm import relationship

from utils import Base

class Akun(Base):
    __tablename__ = "akuns"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    username = Column(String)
    password = Column(String)
      
