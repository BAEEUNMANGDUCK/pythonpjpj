import os

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
TOKEN = os.environ.get("TOKEN")
client = Client(ACCOUNT_SID, TOKEN)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, ticket_info, sheet_data):
        self.ticket_info = ticket_info
        self.sheet_data = sheet_data
        # print(self.ticket_info)
        # print(self.sheet_data)

    def send_message(self):
        try:
            if self.ticket_info[0] < self.sheet_data["lowestPrice"]:
                message = client.messages \
                    .create(
                    body=f"Low price alert! Only €{self.ticket_info[0]} from {self.ticket_info[1]}-{self.ticket_info[2]} to {self.ticket_info[3]}-{self.ticket_info[4]}, from {self.ticket_info[5]} to {self.ticket_info[6]}",
                    from_=os.environ.get('from_'),
                    to=os.environ.get('to')
                )
        except TypeError:
            pass
