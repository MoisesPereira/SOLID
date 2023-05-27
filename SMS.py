import Abstract.Notification as Notification


class SMS(Notification.Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send SMS "{message}" to {self.phone}')