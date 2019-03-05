import random as rand
import os
import dialogflow_v2 as dialogflow
import itertools as iters

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/jack/Desktop/work/CLOUDIFAI/mycare-patients-6d3e767f97e4.json"
projectID = "mycare-patients"

client = dialogflow.IntentsClient()
parent = client.project_agent_path(projectID)
cities = []
professions = []
hours = []
days = []

cities_intro = [" a ", " presso ", " vicino a "]
professions_intro = [" mi serve un ", "cerca un ", " cercami un ", " trova un ", " trovami un ", " ho bisogno di un "]
hours_intro = [" alle ", " per le ", " alle ore "]
days_intro = [" il giorno ", " il "]

with open("data/cities.csv") as file:
    for el in file.readlines():
        cities.append(el[:-2])

with open("data/medical_profession_entries.csv") as file:
    for el in file.readlines():
        professions.append(el[:-1])

for el in range(8, 19, 1):
    hours.append(el)

days.append("domani")
days.append("la settimana prossima")
days.append("questa settimana")

hours.append("alla mattina")
hours.append("nella mattina")
hours.append("al pomeriggio")
hours.append("nel pomeriggio")

for el in range(1, 31, 1):
    days.append(el)

phrase = {}
phrases = []

for medic_i, city_i, day_i, hour_i in iters.product(professions_intro, cities_intro, days_intro, hours_intro):

    phrase = {
                "parts": [
                    # medic
                    {"text": medic_i},
                    {"text": professions[rand.randint(0, len(professions)-1)],
                     "entity_type": "@medical_profession", "alias": "medic"},
                    # city
                    {"text": city_i},
                    {"text": cities[rand.randint(0, len(cities)-1)],
                     "entity_type": "@sys.geo-city", "alias": "city"},
                    # day of the month
                    {"text": day_i},
                    {"text": str(days[rand.randint(0, len(days)-1)]),
                     "entity_type": "@day_of_the_month", "alias": "day"},
                    # hour of the day
                    {"text": hour_i},
                    {"text": str(hours[rand.randint(0, len(hours)-1)]),
                     "entity_type": "@hour_of_the_day", "alias": "hour"}]}

    phrases.append(phrase)

hours = []
for el in range(8, 19, 1):
    hours.append(el)

for el in range(0, 5):
    phrase = {
        "parts": [
            # medic
            {"text": medic_i},
            {"text": professions[rand.randint(0, len(professions) - 1)],
             "entity_type": "@medical_profession", "alias": "medic"},
            # city
            {"text": city_i},
            {"text": cities[rand.randint(0, len(cities) - 1)],
             "entity_type": "@sys.geo-city", "alias": "city"},
            # day of the month
            {"text": day_i},
            {"text": str(days[rand.randint(0, len(days) - 1)]),
             "entity_type": "@day_of_the_month", "alias": "day"},
            # hour of the day
            {"text": " tra le "},
            {"text": str(hours[rand.randint(0, len(hours) - 1)]),
             "entity_type": "@hour_of_the_day", "alias": "hour1"},
            {"text": " e le "},
            {"text": str(hours[rand.randint(0, len(hours) - 1)]),
             "entity_type": "@hour_of_the_day", "alias": "hour2"
             }]}

    phrases.append(phrase)

# call API to create intent
for el in phrases:
    print(el)

intent = {

    "display_name": "book_visit_v2",
    "webhook_state": True,

    "training_phrases": phrases,

    "output_contexts": [{"name": "projects/{}/agent/sessions/setup_session/contexts/book_visit_v2".format(projectID),
                         "lifespan_count": 5}],

    "parameters": [

                   {"display_name": "medic", "entity_type_display_name": "@medical_profession",
                    "value": "$medic.original", "mandatory": True},
                   {"display_name": "hour1", "entity_type_display_name": "@hour_of_the_day",
                    "value": "$hour.original", "mandatory": True},
                   {"display_name": "hour2", "entity_type_display_name": "@hour_of_the_day",
                    "value": "$hour.original", "mandatory": False},
                   {"display_name": "day", "entity_type_display_name": "@day_of_the_month",
                    "value": "$day.original", "mandatory": True},
                   {"display_name": "city", "entity_type_display_name": "@sys.geo-city",
                    "value": "$city.original", "mandatory": True}
                   ]
        }

response = client.create_intent(parent, intent)
