
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from typing import Optional, Any

class DatamodelConfig(BaseModel):
    type_mapping: dict[str,str] = {
            "int": int,
            "str": str,
            "float": float,
            "bool": bool,
            "bytes": bytes,
        }
    base_fields: dict[str, Any] = {
            "run_id":(Optional[int], Field(default=None, primary_key=True, nullable=False)),
            "set_name":(str, Field()),
            "rep": (int, Field())
        }
    
    class Config:
        arbitrary_types_allowed = True
    

BASE_CONFIG:DatamodelConfig = DatamodelConfig()


class Base1(SQLModel):
    type_mapping: dict[str,str] = {
            "int": int,
            "str": str,
            "float": float,
            "bool": bool,
            "bytes": bytes,
        }
    base_fields: dict[str, Any] = {
            "run_id":(Optional[int], Field(default=None, primary_key=True, nullable=False)),
            "set_name":(str, Field()),
            "rep": (int, Field())
        }