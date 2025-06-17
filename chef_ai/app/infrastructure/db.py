"""Database utilities."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from chef_ai.app.domain.models import Base


class Database:
    """Database abstraction layer."""

    def __init__(self, url: str) -> None:
        self.engine = create_engine(url, future=True)
        self.SessionLocal = sessionmaker(
            self.engine, expire_on_commit=False, future=True
        )

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return self.SessionLocal()
