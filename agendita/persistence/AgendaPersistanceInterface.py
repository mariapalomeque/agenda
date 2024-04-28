from abc import ABC, abstractmethod

class AgendaPersistenceInterface(ABC):
    @abstractmethod
    def save(self, agenda_id, event):
        pass

    @abstractmethod
    def find(self, agenda_id, event_id):
        pass

    @abstractmethod
    def update(self, agenda_id, event_id, event):
        pass

    @abstractmethod
    def delete(self, agenda_id, event_id):
        pass