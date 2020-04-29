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
    content_type, chat_type, chat_id = telepot.glance(msg)
    if(msg["text"] == "/help"):
        bot.sendMessage(chat_id,"Benvenuto su Covid19ITBot!\n\nQuesto bot serve per ottenere le ultime news riguardanti il covid-19 in Italia.\n\nPer usarlo, seleziona uno dei comandi:\n\n'/generale' -> mostra la situazione del covid generale in tutta italia\n'/covid' -> mostra dettagli sul covid")
    elif(msg["text"] == "/generale"):
        #data ultimo aggiornamento
        aggiornamento = data[0]["data"]
        upd = str(aggiornamento)[:10]
        upd = time.strptime(upd,"%Y-%m-%d")
        dataFin = str(upd.tm_mday) + "-"+str(upd.tm_mon) + "-" + str(upd.tm_year)
        #totale dei positivi
        totale_positivi = str(data[0]["totale_positivi"])
        #totale nuovi positivi
        nuovi_positivi = str(data[0]["nuovi_positivi"])
        #deceduti
        deceduti = str(data[0]["deceduti"])
        #variazione positivi tra ieri e oggi
        variazione_totale_positivi = str(data[0]["variazione_totale_positivi"])
        #dimessi guariti
        dimessi_guariti = str(data[0]["dimessi_guariti"])
        #tamponi effettuati
        tamponi = str(data[0]["tamponi"])
        #totale ospedalizzati
        ospedalizzati = str(data[0]["totale_ospedalizzati"])
        messaggio = "COVID-19 SITUAZIONE DEL "+dataFin+"\n\nI casi in totale sono: "+totale_positivi+"\nI nuovi casi di oggi sono: "+nuovi_positivi+"\nLa differenza tra ieri e oggi di nuovi casi è: "+variazione_totale_positivi+"\nI morti totali sono: "+deceduti+"\nI dimessi guariti totali sono: "+dimessi_guariti+"\nIl totale di ospedalizzati è: "+ospedalizzati+"\nIl totale di tamponi effettuati è: "+tamponi+"\nPer ulteriori informazioni, visita: http://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus \n\nSE HAI SINTOMI SIMIL-INFLUENZALI RESTA A CASA, E CHIAMA IL 1500.\n\n\n#restaacasa\n\n\n"
        bot.sendMessage(chat_id,messaggio)
    elif(msg["text"] == "/covid"):
        messaggio = "Le persone che hanno contratto il virus potrebbero manifestare i sintomi dopo 1-14 giorni. I sintomi più comuni della malattia da coronavirus (COVID-19) sono febbre, stanchezza e tosse secca. La maggior parte delle persone (circa l'80%) guarisce dalla malattia senza aver bisogno di cure particolari.\nPiù raramente, la malattia può essere grave e portare persino al decesso. Gli anziani e le persone con altre patologie (ad esempio asma, diabete o cardiopatia) potrebbero essere più vulnerabili e quindi ammalarsi gravemente.\n\nSintomi riscontrabili:\n-tosse\n-febbre\n-stanchezza\n-difficoltà respiratorie (casi gravi).\n\nPer maggiori informazioni, visita il sito: http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioFaqNuovoCoronavirus.jsp?id=228&lingua=italiano \n\n\n#restaacasa\n\n"
        bot.sendMessage(chat_id,messaggio)
    elif(msg["text"] == "/start"):
        bot.sendMessage(chat_id,"Benvenuto su Covid19ITBot!")
    elif(msg["text"] == "/regione"):
        keyboard = ReplyKeyboardMarkup(keyboard=[['Add', 'List'], ['Settings', 'Web']])
        bot.sendMessage(chat_id, 'Some text ...', reply_markup=keyboard)

        


bot = telepot.Bot(cfg.config.getToken())

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)


