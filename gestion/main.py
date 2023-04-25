from login import Login
from addCurso import AddCurso

class Main:
    def __init__(self):
        self.login = Login()



    def run(self):
        self.login.run()


if __name__ == "__main__":
    main = Main()
    main.run()
