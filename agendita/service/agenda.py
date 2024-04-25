class Agenda:
    def __init__(self, nom, usuaris, esdeveniments, data, duracio, descripcio=None, tags=None, ubicacio=None):
        self.nom=nom 
        self.usuaris=usuaris
        self.esdeveniments=esdeveniments
        self.data=data
        self.duracio=duracio
        self.descripcio=descripcio
        self.tags=tags
        self.ubicacio=ubicacio
    
    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_usuaris(self):
        return self.usuaris

    def set_usuaris(self, usuaris):
        self.usuaris = usuaris

    def get_esdeveniments(self):
        return self.esdeveniments

    def set_esdeveniments(self, esdeveniments):
        self.esdeveniments = esdeveniments

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_duracio(self):
        return self.duracio

    def set_duracio(self, duracio):
        self.duracio = duracio

    def get_descripcio(self):
        return self.descripcio

    def set_descripcio(self, descripcio):
        self.descripcio = descripcio

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def get_ubicacio(self):
        return self.ubicacio

    def set_ubicacio(self, ubicacio):
        self.ubicacio = ubicacio

    def __str__(self):
        return f"Agenda: {self.nom}, Usuaris: {[str(usuari) for usuari in self.usuaris]}, Esdeveniments: {[str(esdeveniment) for esdeveniment in self.esdeveniments]}"


    def add_event(self, agenda_id, event):
        return self.persistence.save(agenda_id, event)
    
    def get_event(self, agenda_id, event_id):
        return self.persistence.find(agenda_id, event_id)
    
    def update_event(self, agenda_id, event_id, event):
        return self.persistence.update(agenda_id, event_id, event)
    
    def delete_event(self, agenda_id, event_id):
        return self.persistence.delete(agenda_id, event_id)
