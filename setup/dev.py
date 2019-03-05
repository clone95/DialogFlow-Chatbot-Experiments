# Imports the Google Cloud client library
import os
import dialogflow
import management.entity_type_management as entity_types_mng
import management.entity_management as entity_mng


# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "pythontest-59c9c"

session_client = dialogflow.SessionsClient()

entity_types_mng.list_entity_types(projectID)
