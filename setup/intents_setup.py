# Imports the Google Cloud client library
import os
import dialogflow
import management.intent_management as intent_mng

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "pythontest-59c9c"

session_client = dialogflow.SessionsClient()

# INTENTS SETUP
training_phrases = ["mi serve una visita dal podologo", "mi serve una visita dal Podologo", "cerca un podologo",
                   "cerca un Podologo", "prenota un podologo"]

intent_mng.create_intent(projectID, "book_visit", training_phrases, "")







