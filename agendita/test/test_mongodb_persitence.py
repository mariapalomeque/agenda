import unittest
from persistence.mongodb_persistence import MongoDBPersistence
from model.event import Event

class TestMongoDBPersistence(unittest.TestCase):
    def setUp(self):
        self.connection_string = "mongodb://2023felipegonzalez:nAYGx9zr8p4wJGqs@clustermongo.d8e2ioa.mongodb.net/agenda_db"
        self.database_name = "agenda_db"
        self.collection_name = "events"
        self.persistence = MongoDBPersistence(self.connection_string, self.database_name, self.collection_name)
    
    def tearDown(self):
        self.persistence.collection.delete_many({})  # Elimina todos los documentos de la colección después de cada prueba

    def test_save(self):
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.persistence.save(new_event)
        self.assertIsNotNone(event_id)

    def test_find(self):
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.persistence.save(new_event)

        retrieved_event = self.persistence.find(event_id)
        self.assertIsNotNone(retrieved_event)
    
    def test_update(self):
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.persistence.save(new_event)

        updated_data = {
            "description": "New description"
        }
        result = self.persistence.update(event_id, updated_data)
        self.assertEqual(result, 1)

    def test_delete(self):
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.persistence.save(new_event)

        result = self.persistence.delete(event_id)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
