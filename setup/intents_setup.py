# Imports the Google Cloud client library
import os
import dialogflow_v2beta1 as dialogflow
import management.intent_management as intent_mng

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "pythontest-59c9c"


intent = {
    "display_name": "test",
    "webhook_state": True,
    "training_phrases": [{"parts": [{"text": "school", "entity_type": "@school"}], "type": "EXAMPLE"}],
    "parameters": [{"display_name": "school", "entity_type_display_name": "@medical_profession", "value": "$school"}]
}
client = dialogflow.IntentsClient()
parent = client.project_agent_path('pythontest-59c9c')

client.create_intent(parent, intent)



# session_client = dialogflow.SessionsClient()
#
# # INTENTS SETUP
# training_phrases = ["mi serve una visita dal podologo", "mi serve una visita dal Podologo", "cerca un podologo",
#                    "cerca un Podologo", "prenota un podologo"]
#
# intent_mng.create_intent(projectID, "book_visit", training_phrases, "cioss")








