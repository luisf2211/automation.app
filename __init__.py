from flask import Flask, jsonify, request
#LIBRERIAS PARA ENVIAR MENSAJES VIA WHTSAPP
from heyoo import WhatsApp
app = Flask(__name__)

access_token = 'EAANAKuhPhaIBO6Y1O7jE6BPrQV6rpkG1gdLdJskIoZA4p5tvO6GDl2KPVjZARXrvpLXrL43UGzRudYYevW4diBucEze2GKZBcI05c1WUvI03DBd2HPZATVUzVUTBRR7y7ZASkiyxi9GwYWyV5ZAvLnoHLjQM4QUpa0HkdNDNt9cS9UZCrcdzb1s3scKkpEPuWL8KN7LV4cVVV5ydAuS';
facebook_id_number = '420616191126433';

#EJECUTAMOS ESTE CODIGO CUANDO SE INGRESE A LA RUTA ENVIAR
@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    #TOKEN DE ACCESO DE FACEBOOK
    token=access_token
    
    #IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono=facebook_id_number
    
    #TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia='527122264370'
    
    #MENSAJE A ENVIAR
    textoMensaje="Hola Mundo";
    
    #URL DE LA IMAGEN A ENVIAR
    #urlImagen='https://i.imgur.com/r5lhxgn.png'
    
    #INICIALIZAMOS ENVIO DE MENSAJES
    mensajeWa=WhatsApp(token,idNumeroTeléfono)
    
    #ENVIAMOS UN MENSAJE DE TEXTO
    mensajeWa.send_message(textoMensaje,telefonoEnvia)
    
    #ENVIAMOS UNA IMAGEN
    #mensajeWa.send_image(image=urlImagen,recipient_id=telefonoEnvia,)
    
    return "mensaje enviado exitosamente"

#INICIAMSO FLASK
if __name__ == "__main__":
  app.run(debug=True)