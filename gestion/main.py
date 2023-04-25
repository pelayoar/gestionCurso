from login import Login

class Main:
    def __init__(self):
        self.login = Login()

    def run(self):
        self.login.run()

if __name__ == "__main__":
    main = Main()
    main.run()
