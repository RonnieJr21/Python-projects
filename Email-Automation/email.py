import threading
import random


banner = """
___________________________________________________________________________________________________
|      (`\ .-') /`   ('-.                                  _   .-')       ('-.  ,---.             |
|       `.( OO ),' _(  OO)                                ( '.( OO )_   _(  OO) |   |             |
|    ,--./  .--.  (,------.,--.       .-----.  .-'),-----. ,--.   ,--.)(,------.|   |             |
|    |      |  |   |  .---'|  |.-')  '  .--./ ( OO'  .-.  '|   `.'   |  |  .---'|   |     __      | 
|    |  |   |  |,  |  |    |  | OO ) |  |('-. /   |  | |  ||         |  |  |    |   |    |  |     |
|    |  |.'.|  |_)(|  '--. |  |`-' |/_) |OO  )\_) |  |\|  ||  |'.'|  | (|  '--. |  .'    |__|     |
|    |         |   |  .--'(|  '---.'||  |`-'|   \ |  | |  ||  |   |  |  |  .--' `--'              |
|    |   ,'.   |   |  `---.|      |(_'  '--'\    `'  '-'  '|  |   |  |  |  `---..--.      ___     |        
|    '--'   '--'   `------'`------'   `-----'      `-----' `--'   `--'  `------''--'      \  \    |
|                                                                                          \  \   |
|    Author: RJHJ                                                                          /__/   |
|_________________________________________________________________________________________________| 
"""

print(banner)

class User:
    
    def __init__(self, name) -> None:
        self.name = name
        print(f"User [{name}] has been created")

    def write_my_report(self, file_name, file_content):
        try:
            with open(f"python/{file_name}", "x") as file:
                if file.writable: file.write(str(file_content))
        except:
            print("Something went wrong making this file")

    def create_email(self) -> dict:
        print("email sent")

    def edit_email(self, num, Email) -> dict:
        if num == 1:
            print("You can change the recipient here.")
            Email["To"] = input("New Recipient: ")
        elif num == 2:
            print("You can change the subject here.")
            Email["Subject"] = input("New Subject: ")
        elif num == 3:
            print("You can change the content here.")
            Email["Content"] = input("New Content: ")
        elif num == 4:
            print("You can change the attachment here.")
            Email["Attachment"] = input("New Attachment's location: ")
        else:
            print("There was an error editing your email.")
        
        print(f"Does this look correct?\n To: {Email['To']} \n Subject: {Email['Subject']} \n Content: {Email['Content']} \n Attachments: {Email['Attachment']}\n 1.)Yea that looks right \n 2.) No")
        looks_good = int(input("Number: "))
       
        if looks_good == 1:
            return Email
        elif looks_good == 2:
           print(f"What would you like to change? \n1.) {Email['To']} \n2.) {Email['Subject']} \n3.) {Email['Content']} \n4.) {Email['Attachment']}")
           edit_email_choice = int(input("Number: "))
           self.edit_email(edit_email_choice, Email)
        else:
            print("Somthing went wrong.\nedit_email: else statement--")
        
    def send_email(self, *new_created_email):
        Email = {
            "To" : "recepient",
            "Subject": "subject",
            "Content" : "content",
            "Attachment": "attachment"
        }
        list_of_emails = [Email, new_created_email]
        
         
        print("Do you need to send an email with new information? \n 1.) Yes I do \n 2.) No use old one\n 3.) send it")
        email_choice = int(input("Number: "))
        for email in list_of_emails:
            print(email)
        try:
            if email_choice == 1:
                Email = self.create_email()
            elif email_choice == 2:
                print(f"Did you need to change any of your previous information? \n1.) {Email['To']} \n2.) {Email['Subject']} \n3.) {Email['Content']} \n4.) {Email['Attachment']}")
                edit_email_choice = int(input("Number: "))
                newEmail = self.edit_email(edit_email_choice, Email)
                list_of_emails.append(newEmail)
                print(newEmail, "It is here!")
                new_created_email = newEmail
                self.send_email(new_created_email)

            elif email_choice == 3:
                print("Email sent!")
        except:
            print("something went wrong")

user1 =  User("ronnie")
user1.send_email()






        

