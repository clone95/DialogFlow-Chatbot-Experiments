# Imports the Google Cloud client library
import os
import dialogflow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\CLOUDIFAI\Google\pythontest-f8d5e75dddcd.json"


session_client = dialogflow.SessionsClient()

def list_entity_types(project_id):
    import dialogflow_v2 as dialogflow
    entity_types_client = dialogflow.EntityTypesClient()

    parent = entity_types_client.project_agent_path(project_id)

    entity_types = entity_types_client.list_entity_types(parent)

    for entity_type in entity_types:
        print('Entity type name: {}'.format(entity_type.name))
        print('Entity type display name: {}'.format(entity_type.display_name))
        print('Number of entities: {}\n'.format(len(entity_type.entities)))

list_entity_types("pythontest-59c9c")