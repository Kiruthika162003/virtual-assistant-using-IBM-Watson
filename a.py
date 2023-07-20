# Import required libraries
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Replace 'YOUR_API_KEY' and 'YOUR_ASSISTANT_ID' with your actual credentials
authenticator = IAMAuthenticator('YOUR_API_KEY')
assistant = AssistantV1(
    version='2021-06-14',  # Adjust version to the one you're using
    authenticator=authenticator
)
assistant_id = 'YOUR_ASSISTANT_ID'

# Function to send a message to the assistant
def send_message(input_text):
    response = assistant.message(
        assistant_id=assistant_id,
        input={
            'message_type': 'text',
            'text': input_text
        }
    ).get_result()
    return response

# Example usage
user_input = "What time slots are available on Monday?"
response = send_message(user_input)

# Process the response
if response['output']['generic']:
    for message in response['output']['generic']:
        if message['response_type'] == 'text':
            print("Assistant:", message['text'])
