import app.helper as hlp
import datetime

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
                        "date": datetime.datetime(2019, 5, 29, 15, 00),
                        "reason": "normal check",
                        "starting_hour": 15,
                        "duration_in_minutes": 40
                    },

                    {
                        "patient_name": "Alessandro Magno",
                        "date": datetime.datetime(2019, 5, 29, 18, 00),
                        "reason": "abnormal hearth pace",
                        "starting_hour": 18,
                        "duration_in_minutes": 20
                    }

                                ]
            }
        ]


