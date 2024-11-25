import random
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


load_dotenv()


# Email credentials from .env file
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")


# Check if credentials are loaded
if not SENDER_EMAIL or not SENDER_PASSWORD:
    raise Exception("Email credentials are missing. Please check your .env file.")


#List of People
participants = [
    {"name": "Daksh", "email": "daksh.jr107@gmail.com"},
    {"name": "Aaron", "email": "changa2119@gmail.com"},
    {"name": "Aiden", "email": "aidengraham2013@gmail.com"},
    {"name": "Avery", "email": "avery.bettesworth643@gmail.com"},
    {"name": "Carter", "email": "carterkrause10@gmail.com"},
]


#Assign Secret Santas at random
names = [i["name"] for i in participants]
random.shuffle(names)
assignments = {names[j]: names[(j + 1) % len(names)] for j in range(len(names))}


#Send emails using SMTP
def send_email(to_email, subject, body):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = SENDER_EMAIL
            msg["To"] = to_email
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")


for participant in participants:
    giver = participant["name"]
    getter = assignments[giver]


    subject = "Hear Ye, Brave Souls! A Gift Giving Quest Awaits Thee"
    body = f"""
    Hear ye, hear ye, noble soul of great renown!

    Thou art most honorably summoned to partake in the legendary and ancient rites of Secret Santa, in this glorious Year of Our Lord 2024!
    By the decree of destiny herself, thou hast been anointed to bear the title of Secret Giver to {getter}, a sacred charge shrouded in secrecy. Keep this charge guarded as a knight would his sacred oath, with the vigilance of a knight defending the realm, for thy identity must remain shrouded in the veils of secrecy. Guard thy identity, for to reveal thyself would invite great dishonor!

    Upon the morrow, when the golden sun doth ascend to cast its radiant blessing upon our fellowship, shall the sacred exchange of tokens commence. Let it be known, for thy gift must be valued at nigh unto thirty doubloons. Let not thy gift be burdened with wrappings; bring it as it is, plain and true.

    Stand steadfast, O noble bearer of this charge. May thy heart brim with mirth, and may thy chosen token bring great joy to its destined keeper. Go forth, with wisdom and valor, to fulfill thy glorious task!
    """

    send_email(participant["email"], subject, body)




print("All assignments sent successfully!")