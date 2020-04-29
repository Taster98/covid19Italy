# coding=utf-8
import string
import datetime
import urllib3
import numpy as np
import urllib, json
import time
import telepot
from telepot.loop import MessageLoop
import cfg.config

def handle(msg):
    url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json"
    res = urllib.urlopen(url)
    data = json.loads(res.read())

    if(msg["text"] == "/help"):
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id,"Benvenuto su Covid19ITBot!\n\nQuesto bot serve per ottenere le ultime news riguardanti il covid-19 in Italia.\n\nPer usarlo, seleziona uno dei comandi:\n\n'/generale' -> mostra la situazione del covid generale in tutta italia")
    elif(msg["text"] == "/generale"):
        #data ultimo aggiornamento
        aggiornamento = data[0]["data"]
        upd = str(aggiornamento)[:10]
        upd = time.strptime(upd,"%Y-%m-%d")
        dataFin = str(upd.tm_mday) + "-"+str(upd.tm_mon) + "-" + str(upd.tm_year)
        #totale dei positivi
        totale_positivi = data[0]["totale_positivi"]
        #totale nuovi positivi
        nuovi_positivi = data[0]["nuovi_positivi"]
        #deceduti
        deceduti = data[0]["deceduti"]
        #variazione positivi tra ieri e oggi
        variazione_totale_positivi = data[0]["variazione_totale_positivi"]
        #dimessi guariti
        dimessi_guariti = data[0]["dimessi_guariti"]
        #tamponi effettuati
        tamponi = data[0]["tamponi"]
        #totale ospedalizzati
        ospedalizzati = data[0]["totale_ospedalizzati"]
        messaggio = "COVID-19 SITUAZIONE DEL "+dataFin+"\n\nI casi in totale sono: "+totale_positivi+"\nI nuovi casi di oggi sono: "+nuovi_positivi+"\nLa differenza tra ieri e oggi di nuovi casi è: "+variazione_totale_positivi+"\nI morti totali sono: "+deceduti+"\nI dimessi guariti totali sono: "+dimessi_guariti+"\nIl totale di ospedalizzati è: "+ospedalizzati+"\nIl totale di tamponi effettuati è: "+tamponi+"\nPer ulteriori informazioni, visita: http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus \n\nSE HAI SINTOMI SIMIL-INFLUENZALI RESTA A CASA, E CHIAMA IL 1500."


bot = telepot.Bot(cfg.config.getToken())

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)


