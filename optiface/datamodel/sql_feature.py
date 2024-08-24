import json
from typing import Dict, Any, List
from pydantic import create_model, BaseModel, ConfigDict
from sqlmodel import Field, SQLModel
from optiface.datamodel.config import BASE_CONFIG, DatamodelConfig

class TableConfigCreate:
    def __init__(self, file:str, config:DatamodelConfig = BASE_CONFIG):
        self.file: str = file
        self.type_mapping:Dict[str] = config.type_mapping
        self.base_fields: Dict[str, Any] = config.base_fields
        self.fields: Dict[str, Any] = {}


    def read_json(self):
        with open(self.file, 'r') as f:
            self.config:Dict[str, str] = json.load(f)


    def extract_features(self):
        self.table_name:str = self.config.get("table").get("name")
        columns: List[str] = self.config.get("table").get("features")

        for column in columns:
            field_name = column.get("name")
        
            field_type = self.type_mapping.get(column.get("type"), str)
            self.fields[field_name] = (field_type, Field())


    def create_dynamic_model(self):
        self.base_fields.update(self.fields) 

        create_model(
            self.table_name,
            __base__=SQLModel,
            __cls_kwargs__={"table": True},
            model_config=ConfigDict(arbitrary_types_allowed=True),
            **self.base_fields,
        )
    

    def run(self):
        self.read_json()
        self.extract_features()

        return self.create_dynamic_model()
    

