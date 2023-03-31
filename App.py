import os
import openai

from Flask import Flask, request
from twilio.twiml.messaging_response import messaging_response


openai.api_key =os.getenv("OPENAI_API_KEY")
allowed_phone_number=os.getenv("ALLOWED_PHONE_NUMBER")

app =Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    inbound_text_message = request.values.get('Body', None)

    phone_number =request.values.get('From', None)


    if allowed_phone_number == phone_number:
        chatgpt_response =openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "sytem", "content": "You are a helpful assistant that sends responses as short SMS messages."},
                        {"role": "user", "content": inbound_text_message}
            ]
        )

        chatgpt_message = chatgpt_response['choices'][0]['message']['content']
    message_response =MessagingResponse()
    message_response.message("Hello!")


    return str(message_response)


    if__name__ ==("__main__") 
    app.run(debug=True)