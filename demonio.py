from twython import Twython
import random
import os
import time

# Claves de la aplicacion Twitter

app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

def leertxtenlista():

 # Bucle infinito
 try:
  mensaje = ""

  # Abrimos el archivo
  archi=open('twit','r')
  lineas=archi.readlines()

  # Elegir un twit aleatorio
  t = random.randint(0,len(lineas)-1)
  mensaje = lineas[t]
  # Agrega el Tweet
  twitter.update_status(status=mensaje)
  archi.close()
  
 except:
  
  time.sleep(3)
  pass
 
leertxtenlista()
