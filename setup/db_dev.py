import app.helper as hlp

db = hlp.connect_to_database()
collection = db.get_collection("doctors")
a = collection.find({"first_name": "Annibale"})

a = collection.find({'name': {"first_name": "Annibale"}})

#a = collection.find({"ciao": "ciao"})

a = collection.find({'name.first_name': "Annibale"})

for el in a:
    print(el)
