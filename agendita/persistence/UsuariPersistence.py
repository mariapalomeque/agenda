from .UsuariPersistenceInterface import UsuariPersistenceInterface

class UsuariPersistence(UsuariPersistenceInterface):
    def save(self, user_id, user):
        user_dict = {
            "_id": user_id,
            "name": user.get_name(),
            "surname": user.get_surname(),
            "gmail": user.get_gmail(),
            "password": user.get_password(),
            "residence": user.get_residence()
        }
        
        print("Usuario guardado exitosamente:", user_dict)
    
    def find(self, user_id):
    
        user_data = self.collection.find_one({"_id": user_id})
        return user_data

    def update(self, user_id, user):
        
        query = {"_id": user_id}
        new_values = {
            "$set": {
                "name": user.get_name(),
                "surname": user.get_surname(),
                "gmail": user.get_gmail(),
                "password": user.get_password(),
                "residence": user.get_residence()
            }
        }
        self.collection.update_one(query, new_values)

    def delete(self, user_id):
        self.collection.delete_one({"_id": user_id})
