import dialogflow_backend.helper as help

doctors = [

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

                "titles": ["base_medic", "hearth_surgeon"],

                "planned_visits": [

                    {
                        "patient_name": "Giulio Cesare",
                        "date": "17/02/2019",
                        "reason": "normal check",
                        "starting_hour": 15,
                        "duration_in_minutes": 40
                    },

                    {
                        "patient_name": "Alessandro Magno",
                        "date": "19/02/2019",
                        "reason": "abnormal hearth pace",
                        "starting_hour": 18,
                        "duration_in_minutes": 20
                    }

                                ]
            }
        ]


def main():
    db = help.connect_to_database()
    collection = db.get_collection("doctors")
    for doctor in doctors:
        collection.save(doctor)








if __name__ == "__main__":
    main()