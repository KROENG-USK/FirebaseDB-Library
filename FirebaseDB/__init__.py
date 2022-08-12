"""
Ini Program Library FirebaseDB
Pengembang : 
1. Basyair
2. Allail

This Program Firebase Main
!!! WARNING : DILARANG KERAS MENGUBAH ISI FILE INI / PLASGIARISME !!!
"""

import json
import firebase_admin as FDB
from firebase_admin import credentials
from firebase_admin import db

class db_ref:
    # buat inisialisasi object class db_ref
    def __init__(self, https_firebase="", cred_firebase="", reference=""):
        try:
            # buka file alamat database
            with open(https_firebase) as file:
                databaseURL = json.load(file)["https"];

            # buka file sertifikat database
            cred = credentials.Certificate(cred_firebase);
            FDB.initialize_app(cred, {
                'databaseURL': databaseURL
            })

            # ambil reference root firebase
            if reference == "" or reference == None:
                print("Informasi -> Silahkan isi nama reference database");
                return exit();
            
            self.ref = db.reference(reference);

        except:
            print("Error def __init__ library firebase bermasalah!!!");

    def database(self):
        return self.ref