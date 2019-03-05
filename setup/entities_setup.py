# Imports the Google Cloud client library
import os
import dialogflow
import management.entity_type_management as entity_types_mng
import management.entity_management as entity_mng

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/jack/Desktop/work/CLOUDIFAI/mycare-patients-6d3e767f97e4.json"
projectID = "mycare-patients"
client = dialogflow.EntityTypesClient()
parent = client.project_agent_path(projectID)
session_client = dialogflow.SessionsClient()


days_entities = []

for day in range(1, 30):
    days_entities.append({"value": str(day),
                          "synonyms": [str(day)]})

client = dialogflow.EntityTypesClient()
parent = client.project_agent_path(projectID)

# day of the month
entity_id = entity_types_mng.create_entity_type(projectID, "day_of_the_month", 1)
parent_entity_type = parent + "/entityTypes/{}".format(entity_id.name[-36:])
client.batch_create_entities(parent_entity_type, days_entities)

# hour of the day
entity_id = entity_types_mng.create_entity_type(projectID, "hour_of_the_day", 1)
hour_entities = []
for hour in [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]:
    hour_entities.append({"value": str(hour),
                          "synonyms": [str(hour)]})

parent_entity_type = parent + "/entityTypes/{}".format(entity_id.name[-36:])
client.batch_create_entities(parent_entity_type, hour_entities)


# medical_profession entity_type creation
entity_id = entity_types_mng.create_entity_type(projectID, "medical_profession", 1)

medics_entities = []

with open("medical_profession_entries.csv", "r") as file:
    for entry in file:
        medics_entities.append({"value": entry,
                                "synonyms": [entry]})


parent_entity_type = parent + "/entityTypes/{}".format(entity_id.name[-36:])
client.batch_create_entities(parent_entity_type, medics_entities)
