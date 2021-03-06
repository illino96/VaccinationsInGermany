# Import packages
import telepot
from telepot.loop import MessageLoop
import datetime
from datetime import datetime, timedelta
import requests
import pandas as pd

# Bot token received from @BotFather
TOKEN = YOUR_BOT_TOKEN

def collectvaccine():
    url_of_file = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx;jsessionid=3ACA01138E44048EB9ADD7A063EC79CE.internet122?__blob=publicationFile"

    response = requests.get(url_of_file)

    print(response)

    file = open("test.xlsx","wb")
    file.write(response.content)
    file.close()
    
    df = pd.read_excel("test.xlsx", sheet_name=1)
    NDS = df.iloc[8]
    BRD = df.iloc[16]
    SH = df.iloc[14]

    ges_kum = int(BRD[1])
    ges_dif = int(BRD[2])

    nds_kum = int(NDS[1])
    nds_dif = int(NDS[2])

    sh_kum = int(SH[1])
    sh_dif = int(SH[2])
    
    final_string = "*BRD gesamt:* {}\n*BRD∆:* {}\n*NDS gesamt:* {}\n*NDS∆:* {}\n*SH gesamt:* {}\n*SH∆:* {}".format(ges_kum,ges_dif,nds_kum,nds_dif,sh_kum,sh_dif)
    return final_string
            
#Main function to identify incoming traffic
def handle(msg):
        content_type, chat_type, chat_id, = telepot.glance(msg)
        if content_type == "text":
            print(content_type, chat_type, chat_id,msg["text"])
            # Checks user input
            if msg["text"] in ["/getVaccinations"]:
                bot.sendMessage(chat_id, collectvaccine(),parse_mode="markdown")
                
#creates the object bot and starts messageloop -> handle
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
    date_time = datetime.now()
    date_time = str(date_time)
    if date_time[11:13] == "09" and date_time[14:16] == "30" and date_time[17] == "0":
        bot.sendMessage(YOUR_CHAT_ID, collectvaccine(),parse_mode="markdown")               
                            
