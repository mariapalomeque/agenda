import unittest
from model.event import Event
from persistence.mongodb_persistence import MongoDBPersistence
from agendita.service.agenda_service import Agenda

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.connection_string = "mongodb://2023felipegonzalez:nAYGx9zr8p4wJGqs@clustermongo.d8e2ioa.mongodb.net/agenda_db"
        self.database_name = "agenda_db"
        self.collection_name = "agendas"  # Cambiar el nombre de la colección a "agendas" para reflejar la nueva estructura
        self.persistence = MongoDBPersistence(self.connection_string, self.database_name, self.collection_name)
        self.agenda = Agenda(self.persistence)
    
    def test_add_event(self):
        agenda_id = "60626d2a4e7e830b04c27136"  # ID de la agenda donde se agregarán los eventos
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.agenda.add_event(agenda_id, new_event)  # Se pasa el ID de la agenda
        self.assertIsNotNone(event_id)
    
    def test_get_event(self):
        agenda_id = "60626d2a4e7e830b04c27136"  # ID de la agenda donde se buscarán los eventos
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.agenda.add_event(agenda_id, new_event)

        retrieved_event = self.agenda.get_event(agenda_id, event_id)  # Se pasa el ID de la agenda
        self.assertIsNotNone(retrieved_event)
    
    def test_update_event(self):
        agenda_id = "60626d2a4e7e830b04c27136"  # ID de la agenda donde se actualizarán los eventos
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.agenda.add_event(agenda_id, new_event)

        updated_data = {
            "description": "New description"
        }
        self.assertTrue(self.agenda.update_event(agenda_id, event_id, updated_data))  # Se pasa el ID de la agenda
    
    def test_delete_event(self):
        agenda_id = "60626d2a4e7e830b04c27136"  # ID de la agenda donde se eliminarán los eventos
        event_data = {
            "date": "2024-04-20",
            "duration": "2 hours",
            "title": "Meeting",
            "description": "Discuss project updates",
            "tags": ["meeting", "project"],
            "location": "Office"
        }
        new_event = Event(**event_data)
        event_id = self.agenda.add_event(agenda_id, new_event)

        self.assertTrue(self.agenda.delete_event(agenda_id, event_id))  # Se pasa el ID de la agenda

if __name__ == '__main__':
    unittest.main()
