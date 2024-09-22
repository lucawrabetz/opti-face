
from sqlmodel import SQLModel, create_engine, Session


class SQLModelUtil:
    def __init__(self, db_name:str = "database"):
        self.db_dir:str = "db"
        self.db_name:str = db_name
        self.db_url:str = f"sqlite:///{self.db_dir}/{self.db_name}.db"
        self._make_engine()
        self._register_tables()

    def _make_engine(self):
        self.engine = create_engine(self.db_url, echo=True)

    def _register_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        return Session(self.engine)
    
    def insert_records(self):
        pass

    def read(self):
       pass