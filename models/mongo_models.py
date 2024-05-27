from config import livres_collection, adherents_collection, prets_collection, users_collection

def add_book(book):
    livres_collection.insert_one(book)

def add_adherent(adherent):
    adherents_collection.insert_one(adherent)

def add_pret(pret):
    prets_collection.insert_one(pret)

def add_user(user):
    users_collection.insert_one(user)

def authenticate_user(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    return user is not None

def get_all_books():
    return list(livres_collection.find())

def get_all_adherents():
    return list(adherents_collection.find())

def get_all_prets():
    return list(prets_collection.find())
