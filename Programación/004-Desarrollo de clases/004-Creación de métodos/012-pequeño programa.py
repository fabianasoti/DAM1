class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
        
    # Estos son los setters y los getters
    def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self, nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email
        
# CRUD - Create, Read, Update, Delete
# CRUD SQL - Insert, Select, Update, Delete
        
