# Bugfix: Updated the AFK Bot to handle edge cases properly.

import time

class AFKBot:
    def __init__(self):
        self.afk = False
        self.user_status = "Online"

    def set_afk(self):
        self.afk = True
        self.user_status = "AFK"

    def return_from_afk(self):
        if self.afk:
            self.afk = False
            self.user_status = "Online"

    def check_inactivity(self):
        # Check for user inactivity
        pass

    def notify(self):
        if self.afk:
            print("User is AFK")
        else:
            print("User is active")

# Main program flow
if __name__ == '__main__':
    bot = AFKBot()
    bot.set_afk()
    bot.notify()