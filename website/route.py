from flask import Flask, request
import os
app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")
  return phone_number

  if text == '':
    response  = "CON welcome to medicode \n"
    response += "1. Register"
    
  elif text == '1':
    response = "CON Please enter your details:\n"
    response += "1. Enter your name\n"
    name = input("")  
    response += name
    response += "\n2. Enter your ID\n"
    id_number = input("")  
    response += id_number

  else:
      return

  return response
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))
