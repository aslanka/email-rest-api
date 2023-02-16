from flask import Flask
from smtplib import SMTP
app = Flask(__name__)

@app.route('/', methods=['POST'])
def sendEmail():
  smtp_port = SMTP("smtp.gmail.com", 587)

  
  smtp_port.ehlo()


  smtp_port.starttls()

  
  smtp_port.login("ayushlanka106@gmail.com" , "")


  subject = "Tutoring Considation Appointment"
  body = "Thank you for making an appointment. You should be receiving a call soon from one of our tutor consultents!"
  final_message = f"Subject: {subject} \n \n {body}"


  address_list = ["dsi.indomnius@gmail.com"]
  smtp_port.sendmail("ayushlanka106@gmail.com", "dsi.indominus@gmail.com", final_message)
  return "email sent"
  smtp_port.quit()


if __name__ == "__main__":
  app.run()
