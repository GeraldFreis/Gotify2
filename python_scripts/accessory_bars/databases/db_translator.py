import pandas as pd

"""
Class to manage the translating of the databases to a list
-> constructor requires a string of the database name
"""
class Db_Translator():
    __slots__ = ("db_name", "db_connection")
    def __init__(self, given_db_name: str):
        self.db_name = given_db_name
        self.db_connection = pd.read_csv(given_db_name)
    
    # function to return a list of the content in the database
    def content_list(self)->list:
        return list(line for line in self.db_connection)
    
    # function that returns a set of the content in the database
    def content_set(self)->set:
        return set(line for line in self.db_connection)
    
    # requires data_list to be a dictionary
    def write_to_db(self, data_list: dict)->None:
        df = pd.DataFrame(data_list)
        df.to_csv(self.db_name) # possible pitfall as we might write over content
    