from FirebaseDB import db_ref
ref = db_ref("./path/https/alamat_db.json", "./path/to/serviceAccountKey.json", "testing")
db = ref.database()

db.child("Test").push("Hello") # push
db.child("Test").set("Hello") # set

# print
data = db.child("Test").get()
print(data)

# delete
db.child("Test").delete()

