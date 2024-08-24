from optiface.datamodel.sql_model_util import SQLModelUtil
from optiface.datamodel.sql_feature import TableConfigCreate

def main():
    file:str = "optiface/experiments/features.json"
    db_name = "database"
    new_table = TableConfigCreate(file=file).run()
    smu = SQLModelUtil(db_name=db_name)


if __name__ == "__main__":
    main()
