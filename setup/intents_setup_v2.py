import random as rand
import os
import dialogflow_v2 as dialogflow
import management.intent_management as intent_mng
import itertools as iter

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "e56f1764-316e-4de6-b77b-eb7fd07c5afa"

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

with open("cities.csv") as file:
    for el in file.readlines():
        cities.append(el.split("\t")[1])

with open("medical_profession_entries.csv") as file:
    for el in file.readlines():
        professions.append(el[:-1])

for el in range(8, 19, 1):
    hours.append(el)

for el in range(1, 31, 1):
    days.append(el)

phrase = {}
phrases = []

for medic_i, city_i, day_i, hour_i in iter.product(professions_intro, cities_intro, days_intro, hours_intro):

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
                   {"display_name": "hour", "entity_type_display_name": "@hour_of_the_day",
                    "value": "$hour.original", "mandatory": True},
                   {"display_name": "day", "entity_type_display_name": "@day_of_the_month",
                    "value": "$day.original", "mandatory": True},
                   {"display_name": "city", "entity_type_display_name": "@sys.geo-city",
                    "value": "$city.original", "mandatory": True}
                   ]
        }

response = client.create_intent(parent, intent)
