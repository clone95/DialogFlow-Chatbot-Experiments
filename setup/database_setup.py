import app.helper as hlp
import datetime

data = [
            {
                "name": {
                     "first_name": "Annibale",
                     "second_name": "Barca",
                     "clinic_name": "Ambulatorio di Cardiochirurgia - Annibale Barca"
                        },

                "address": {
                    "street": "Via dei Pioppi",
                    "number": "63",
                    "city": "Ferrara",
                    "region": "Emilia Romagna",
                    "postal_code": "44034"
                        },

                "titles": ["podologo", "chirurgo"],

                "planned_visits": [

                    {
                        "patient_name": "Giulio Cesare",
                        "date": datetime.datetime(2019, 5, 13, 15, 00),
                        "reason": "normal check",
                        "duration_in_minutes": 40
                    },

                    {
                        "patient_name": "Alessandro Magno",
                        "date": datetime.datetime(2019, 5, 23, 15, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },

                    {
                        "patient_name": "Marco Andreati",
                        "date": datetime.datetime(2019, 5, 22, 18, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },

                    {
                        "patient_name": "Luca Corli",
                        "date": datetime.datetime(2019, 5, 26, 18, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },

                    {
                        "patient_name": "Carlo Santoro",
                        "date": datetime.datetime(2019, 5, 16, 18, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },

                    {
                        "patient_name": "Beppe Grillo",
                        "date": datetime.datetime(2019, 5, 18, 18, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },

                    {
                        "patient_name": "Matteo Salvini",
                        "date": datetime.datetime(2019, 5, 21, 18, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },

                    {
                        "patient_name": "Giuseppe Conte",
                        "date": datetime.datetime(2019, 5, 20, 18, 00),
                        "reason": "abnormal hearth pace",
                        "duration_in_minutes": 20
                    },
                                ]
            }
        ]

db = hlp.connect_to_database()
db.create_collection("doctors")
collection = db.get_collection("doctors")
for el in data:
    collection.insert_one(el)

