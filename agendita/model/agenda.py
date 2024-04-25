class Agenda:
    def __init__(self, name, users, events, date, duration, description=None, tags=None, location=None):
        self.name=name 
        self.users=users
        self.events=events
        self.date=date
        self.duration=duration
        self.description=description
        self.tags=tags
        self.location=location
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def get_events(self):
        return self.events

    def set_events(self, events):
        self.events = events

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def __str__(self):
        return f"Agenda: {self.name}, users: {[str(usuari) for usuari in self.users]}, events: {[str(esdeveniment) for esdeveniment in self.events]}"


  