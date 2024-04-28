from abc import ABC, abstractmethod
from pymongo import MongoClient

class UsuariPersistenceInterface(ABC):
    
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
    
    @abstractmethod
    def save(self, user_id, user):
        pass
    
    @abstractmethod
    def find(self, user_id):
        pass
    
    @abstractmethod
    def update(self, user_id, user):
        pass
    
    @abstractmethod
    def delete(self, user_id):
        pass
