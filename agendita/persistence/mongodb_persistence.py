from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBPersistence:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
    
    def save(self, agenda_id, event):
        event_dict = {
            "date": event.date,
            "duration": event.duration,
            "title": event.title,
            "description": event.description,
            "tags": event.tags,
            "location": event.location
        }
       
        result = self.collection.update_one(
            {"_id": ObjectId(agenda_id)},
            {"$push": {"events": event_dict}}
        )
        return result.inserted_id
    
    def find(self, agenda_id, event_id):
        agenda = self.collection.find_one({"_id": ObjectId(agenda_id)})
        if agenda:
            for event in agenda.get("events", []):
                if str(event.get("_id")) == event_id:
                    return event
        return None
    
    def update(self, agenda_id, event_id, event):
        event_dict = {
            "date": event.date,
            "duration": event.duration,
            "title": event.title,
            "description": event.description,
            "tags": event.tags,
            "location": event.location
        }
        result = self.collection.update_one(
            {"_id": ObjectId(agenda_id), "events._id": ObjectId(event_id)},
            {"$set": {"events.$": event_dict}}
        )
        return result.modified_count
    
    def delete(self, agenda_id, event_id):
        
        result = self.collection.update_one(
            {"_id": ObjectId(agenda_id)},
            {"$pull": {"events": {"_id": ObjectId(event_id)}}}
        )
        return result.deleted_count
