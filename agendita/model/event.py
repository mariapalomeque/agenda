class Event:
    def __init__(self, date, duration, title, description=None, tags=None, location=None):
        self._date = date
        self._duration = duration
        self._title = title
        self._description = description
        self._tags = tags
        self._location = location
    
    @property
    def date(self):
        return self._date
    
    @property
    def duration(self):
        return self._duration
    
    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def location(self):
        return self._location
    
    @date.setter
    def date(self, date):
        self._date = date
    
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    
    @title.setter
    def title(self, title):
        self._title = title
    
    @description.setter
    def description(self, description):
        self._description = description
    
    @tags.setter
    def tags(self, tags):
        self._tags = tags
    
    @location.setter
    def location(self, location):
        self._location = location
