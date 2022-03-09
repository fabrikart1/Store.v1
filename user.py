class User:
    id = 0
    def __init__(self, id, name, email, phone):
        User.id += 1
        self.name = name
        self.email = email
        self.phone = phone

class Administrator:
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone)

    def catalog_edit(self):  # редактирование каталога
        pass

    def price_edit(self):  # редактирование прайс-листа
       pass


class Catalog:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Item:

    def __init__(self, id):
