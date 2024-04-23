class Agenda:
    def __init__(self, persistence):
        self.persistence = persistence
    
    def add_event(self, agenda_id, event):
        return self.persistence.save(agenda_id, event)
    
    def get_event(self, agenda_id, event_id):
        return self.persistence.find(agenda_id, event_id)
    
    def update_event(self, agenda_id, event_id, event):
        return self.persistence.update(agenda_id, event_id, event)
    
    def delete_event(self, agenda_id, event_id):
        return self.persistence.delete(agenda_id, event_id)
