# Imports the Google Cloud client library
import os
import dialogflow
import management.entity_type_management as entity_types_mng
import management.entity_management as entity_mng


# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "pythontest-59c9c"

session_client = dialogflow.SessionsClient()


# month day creation
entity_id = entity_types_mng.create_entity_type(projectID, "day_of_the_month", 1)
for day in range(1, 30):
    entity_mng.create_entity(projectID, entity_id.name[-36:], str(day), [str(day)])

# working hor of the day creation
entity_id = entity_types_mng.create_entity_type(projectID, "hour_of_the_day", 1)
for hour in [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]:
    entity_mng.create_entity(projectID, entity_id.name[-36:], str(hour), [str(hour)])

# ENTITIES_TYPE AND ENTITIES SETUP
# does not handle synonyms for simplicity
# medical_profession entity_type creation
entity_id = entity_types_mng.create_entity_type(projectID, "medical_profession", 1)
print(entity_id.name[-36:])
with open("medical_profession_entries.csv", "r") as file:
    for entry in file:
        # entity type ID, when created, starts on the 36 from last char in the response attribute .name
        entity_mng.create_entity(projectID, entity_id.name[-36:], entry, [entry])


