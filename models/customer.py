from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List


class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(250), nullable=False)
    email: Mapped[str] = mapped_column(db.String(250), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(16), nullable=False)
    username: Mapped[str] = mapped_column(db.String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(250), nullable=False)
    role_id: Mapped[int] = mapped_column(db.Integer, nullable=False, default=2) # 1 for admin and # 2 for user
    
    orders: Mapped[List["Order"]] = db.relationship(back_populates="customer")
    
  
    
    
   


    
    
    
