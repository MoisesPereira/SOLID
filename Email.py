import Abstract.Notification as Notification


class Email(Notification.Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send Email "{message}" to {self.email}')