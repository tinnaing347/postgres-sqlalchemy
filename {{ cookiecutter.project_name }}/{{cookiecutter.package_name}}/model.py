from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import relationship

Base = declarative_base()

class SampleTable(Base):
    __tablename__ = 'sample_table'