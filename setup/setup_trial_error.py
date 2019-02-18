import os
import dialogflow
import management.intent_management as intent_mng

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "pythontest-59c9c"

session_client = dialogflow.SessionsClient()

intent_mng.list_intents(projectID)
