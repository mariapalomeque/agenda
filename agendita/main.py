from model.event import Event
from persistence.mongodb_persistence import MongoDBPersistence
from service.agenda import Agenda

def main():
    connection_string = "2023felipegonzalez:nAYGx9zr8p4wJGqs@clustermongo.d8e2ioa.mongodb.net/agenda_db"
    database_name = "agenda_db"
    collection_name = "events"

    persistence = MongoDBPersistence(connection_string, database_name, collection_name)

    agenda = Agenda(persistence)

    new_event = Event(
        date="2024-04-20",
        duration="2 hours",
        title="Meeting",
        description="Discuss project updates",
        tags=["meeting", "project"],
        location="Office"
    )

    agenda.add_event(new_event)
    print("Evento agregado exitosamente.")

if __name__ == "__main__":
    main()