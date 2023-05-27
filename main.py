# Main for call other class SOLID Principles.

import BankAccount as BKAccount
import Sensor as Sensor
import Email as Email
import SMS as SMS
import Contact as Contact
import NotificationManager as NotificationManager


# Single Responsibily
account_number = 123456
balance = 100
bank_account = BKAccount.BankAccount(account_number, balance)
bank_account.withdraw_money(90)
# Single Responsibily
# Single Responsibily


# Open/Close Principles
def detect_temperature():
    print("Detecting objects using temperature sensor... ")


def detect_proximity():
    print("Detecting objects using proximity sensor....")


def detect_camera():
    print("Detecting objects using camera sensor... ")


temperature_sensor = Sensor.Sensor(detect_temperature())
proximity_sensor = Sensor.Sensor(detect_proximity())
camera_sensor = Sensor.Sensor(detect_camera())
# Open/Close Principles
# Open/Close Principles


# Liskov Substitution Principle
print("\n")
contact = Contact.Contact('Moises Monster', 'moises@xxx.com', '(55)11-96542-7788')

sms_notification = SMS.SMS(contact.phone)
email_notification = Email.Email(contact.email)

notification_manager = NotificationManager.NotificationManager(sms_notification)
notification_manager.send('SMS Moises')
#
notification_manager.notification = email_notification
notification_manager.send('EMAIL Moises')
# Liskov Substitution Principle
# Liskov Substitution Principle