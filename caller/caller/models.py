from sqlalchemy import Column, DateTime, Integer, Numeric, String

from caller.db import Base


class CallModel(Base):
    __tablename__ = "calls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_currency = Column(String(8))
    to_currency = Column(String(8))
    amount = Column(Integer)
    converted_value = Column(Numeric(10, 2))
    when = Column(DateTime, nullable=True)
