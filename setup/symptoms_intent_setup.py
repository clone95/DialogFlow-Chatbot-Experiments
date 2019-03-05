import random as rand
import os
import dialogflow_v2 as dialogflow
import itertools as iters

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/jack/Desktop/work/CLOUDIFAI/mycare-patients-6d3e767f97e4.json"
projectID = "mycare-patients"

client = dialogflow.IntentsClient()
parent = client.project_agent_path(projectID)

body_parts = []
phrase = {}
phrases = []
professions = []

# professions
with open("data/medical_profession_entries.csv") as file:
    for el in file.readlines():
        professions.append(el[:-1])

# body parts list
with open("data/body_parts.csv") as file:
    for line in file:
        if len(line.split(",")) == 1:
            body_parts.append(line[:-1])
        else:
            body_parts.append(line.split(",")[0])

main_verb = [" ho ", " provo ", " sento ", "percepisco"]
complement = [" male ", " dolore "]
position = " vicino ", " sopra ", " sotto ", "  dentro "
preposition = [" alle ", " a ", " ai ", " al ", " agli "]

professions_intro = [" mi serve un ", " cerca un ", " cercami un ", " trova un ", " trovami un ", " ho bisogno di un "]

for verb, comp, pos, prep, medic_i in iters.product(main_verb, complement, position, preposition, professions_intro):
    phrase = {
        "parts": [

            {"text": verb},

            {"text": comp},

            {"text": pos},

            {"text": prep},

            {"text": str(body_parts[rand.randint(0, len(body_parts)-1)]),
             "entity_type": "@body_parts", "alias": "body_parts"},

            {"text": medic_i},

            {"text": professions[rand.randint(0, len(professions)-1)],
             "entity_type": "@medical_profession", "alias": "medic"}

            ]}

    phrases.append(phrase)

for el in phrases:
    print(el)

print(body_parts)

intent = {

    "display_name": "symptom_intent",

    "webhook_state": True,

    "training_phrases": phrases,

    "output_contexts": [{"name": "projects/{}/agent/sessions/setup_session/contexts/symptom_intent".format(projectID),
                         "lifespan_count": 5}],

    "parameters": [

                   {"display_name": "medic", "entity_type_display_name": "@medical_profession",
                    "value": "$medic.original", "mandatory": True},
                   {"display_name": "body_parts", "entity_type_display_name": "@body_parts",
                    "value": "$body_part.original", "mandatory": True},
                   ]
        }

response = client.create_intent(parent, intent)
