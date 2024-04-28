# agendita/persistence/AgendaPersistence.py
class AgendaPersistence:
    def save(self, agenda_id, event):
         agenda_data = self.collection.find_one({"_id": agenda_id})
         if agenda_data:
             events = agenda_data.get("events", [])
             events.append(event)
             self.collection.update_one({"_id": agenda_id}, {"$set": {"events": events}})
             pass

    def find(self, agenda_id, event_id):
         agenda_data = self.collection.find_one({"_id": agenda_id})
         if agenda_data:
             events = agenda_data.get("events", [])
             for event in events:
                 if event.get("_id") == event_id:
                     return event
         return None
    pass

    def update(self, agenda_id, event_id, event):
         agenda_data = self.collection.find_one({"_id": agenda_id})
         if agenda_data:
             events = agenda_data.get("events", [])
             for i, e in enumerate(events):
                 if e.get("_id") == event_id:
                     events[i] = event
                     self.collection.update_one({"_id": agenda_id}, {"$set": {"events": events}})
                     pass

    def delete(self, agenda_id, event_id):
        
         agenda_data = self.collection.find_one({"_id": agenda_id})
         if agenda_data:
             events = agenda_data.get("events", [])
             events = [e for e in events if e.get("_id") != event_id]
             self.collection.update_one({"_id": agenda_id}, {"$set": {"events": events}})
    pass
