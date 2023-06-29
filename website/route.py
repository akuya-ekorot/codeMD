from flask import Flask, request
import os

app = Flask(__name__)

response = ""

@app.route('/ussd', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    print(text)

    if text == '':
        response = "CON welcome to medicode \n"
        response += "1. Register"
    elif text == '1':
        response = "CON Please enter your name\n"
    elif text == 'name':
        name = request.values.get("text", "")
        response = "CON Please enter your ID\n"
    elif text == 'id':
        id_number = request.values.get("text", "")
        response = "CON Registration successful!\n"
        response += "Name: {}\n".format(name)
        response += "ID: {}\n".format(id_number)

    else:
        return

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))

