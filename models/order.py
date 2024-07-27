from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import Column, Integer, Date, ForeignKey, Table
from typing import List
from models.order_product import order_product

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[datetime] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey("customers.id"))
    customer: Mapped["Customer"] = db.relationship(back_populates="orders")
    products: Mapped[List["Product"]] = db.relationship(secondary=order_product)


    