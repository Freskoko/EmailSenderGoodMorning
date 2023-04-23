from smtplib import SMTP
from ssl import create_default_context
# from dotenv import load_dotenv
import os
from datetime import date
from email.mime.text import MIMEText

from bike_ava import get_bike_info
from calendar_events import get_clean_events
from weather_getter import get_weather
from githubgetter import githubgetterpopular

#TODO add more api
#TODO make it so it does it each morning

def send_mail():

    calendar_events = get_clean_events()
    weather = get_weather()
    today = str(date.today())

    event_html = ""
    for event in calendar_events:
        event_html += f'<li>{event["start_time"][-9:-3]} to {event["end_time"][-9:-3]} | {event["title"]}</li>'


    # load_dotenv()

    port = 587  
    # smtp_server = "smtp-mail.outlook.com"
    smtp_server = "smtp.office365.com"
    sender_email = "goodmorningbot12345@outlook.com"  
    receiver_email = "frishcoco@gmail.com"  
    password = os.environ["email_pass"]

    html_content = f"""\

    <h1>Goodmorning Henrik! {today}</h1>

    <div>

        <p> Bikes at Greighallen this morning: <b> {get_bike_info()} </b>   </p> 

    </div>

    <div>
        <p>
    Todays temperature is looking like 
     </p> 

    <ul>
     <li> {weather[0][0]} C at {weather[0][1][-5:]} am </p> 
     <li> {weather[7][0]} C at {weather[7][1][-5:]} pm </p> 
     <li> {weather[12][0]} C at {weather[12][1][-5:]} pm </p> 
     <li> {weather[-2][0]} C at {weather[-2][1][-5:]} pm </p> 
    </ul>
       
    </div>

    <div>
        <p>Todays calendar events are:</p>
        <ul>{event_html}</ul>
    </div>

    <div>
        <p>
        On github today this repo is trending:
            <div>
                    <b> {githubgetterpopular()} </b> 
            </div>
        </p> 
    </div>

    <div>
        <p>
        Have a nice day :-)
        </p> 
    </div>

    """

    message = MIMEText(html_content, "html")
    message["Subject"] = f"Hey, Goodmorning Henrik {today}"

    context = create_default_context()
    with SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return message.as_string()

def main():
    send_mail()
    return "Mail sent successfully", 200

print(main())
