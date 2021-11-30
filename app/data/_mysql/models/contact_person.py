from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.data._mysql.models import Base


class ContactPerson(Base):
    __tablename__ = "contact_persons"

    contact_person_id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    supplier = relationship("Supplier", back_populates="contact_persons")
    manufacturer = relationship("ManuFacturer", back_populates="contact_persons")

    # supplier = relationship("Supplier", backref="contact_person", uselist=False)
    # manufacturer = relationship("ManuFacturer", backref="contact_person", uselist=False)
