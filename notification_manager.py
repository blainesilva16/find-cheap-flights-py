import smtplib

my_email = "anablaine1234@gmail.com"
password = "zcriyugyosntpmdz"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,cheap_flights):
        try:
            for flight in cheap_flights:
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs="blainesilva16@gmail.com",
                        msg=f"Subject:We have a cheaper flight for {flight["city"]}!\n\n{flight["info"]}")
        except:
            print("No emails sent because there was no cheaper flight.")
