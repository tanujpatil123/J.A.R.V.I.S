import pywhatkit
from datetime import datetime



def whatsapp(no, message):
    # Get the current time
    now = datetime.now()

    # Extract hour and minute
    time_hr = int(now.strftime("%H"))
    time_min = (int(now.strftime("%M")))+(1)
    pywhatkit.sendwhatmsg(no, message, time_hr, time_min)
    



