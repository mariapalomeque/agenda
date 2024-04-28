class Usuari:
    def __init__(self, name, gmail, password, surname=None, residence=None):
        self._name = name
        self._surname = surname
        self._gmail = gmail
        self._password = password
        self._residence = residence

    # Getters
    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_gmail(self):
        return self._gmail

    def get_password(self):
        return self._password

    def get_residence(self):
        return self._residence

    # Setters
    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_gmail(self, gmail):
        self._gmail = gmail

    def set_password(self, password):
        self._password = password

    def set_residence(self, residence):
        self._residence = residence