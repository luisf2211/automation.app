from flask import Flask, jsonify, request
import http.client
import json
from rivescript import RiveScript

app=Flask(__name__)
bot=RiveScript();
token="EAANAKuhPhaIBOxba6ZCcMZCNS9IVlgf5yKgFQmwPHHTQnc10ycyqD5HlZBRfM0UQ3CGolZAZCeKBcEeiJB9purOazQukgjKH60IRMh7eN7wFXks3PCuyTeCxgndwSjEdrsqabnK2rKYZBV5TTPZBI7Cjo4kxZAmxotT8pS9aHAvGu5GYmPh2SDS1FheY2ctobRRKf8iMr4gAnBo23AIZD"

def send_message(mensajeRespuesta):
    if not mensajeRespuesta:
        return jsonify({'error': 'No JSON received'}), 400
    
    url = "graph.facebook.com"  
    
    conn=http.client.HTTPSConnection(url, None)
    
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"  
    }

    data=json.dumps({
        "messaging_product": "whatsapp",
        "to": "18295082211",
        "type": "text", 
        "text": {
            "body": mensajeRespuesta
        }
    })

    try:
        conn.request('POST', '/v20.0/420616191126433/messages', body=data, headers=headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        print(response.read().decode())
        conn.close()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    
    if request.method == "GET":
        if request.args.get('hub.verify_token') == "HolaNovato":
            return request.args.get('hub.challenge')
        else:
          return "Error de autentificacion."
    
    data=request.get_json()
    if data is not None:
        telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
        bot.load_file('automation_whatsapp/brain.rive')
        bot.sort_replies()
        botMsg = bot.reply('localuser', mensaje)
        send_message(botMsg)
    return jsonify({"status": "success"}, 200)

if __name__ == "__main__":
  #app.run(debug=True, host='0.0.0.0', port=5001)
  app.run(debug=True)