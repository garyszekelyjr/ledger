from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Transaction(Base):
    __tablename__ = 'transaction'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column()
