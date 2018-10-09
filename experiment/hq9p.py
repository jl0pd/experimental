class hq9p(object):
    def __init__(self):
        self.var = 0
        self.quine_str = ""

    def action(self, command):
        if command in "hH":
            self.hello()
        elif command in "qQ":
            self.quine()
        elif command == "9":
            self.bottles()
        elif command == "+":
            self.plus()

    def hello(self):
        self.quine_str += "h"
        print("Hello World!")

    def quine(self):
        self.quine_str += "q"
        print(self.quine_str)

    def plus(self):
        self.quine_str += "+"
        self.var += 1

    def bottles(self):
        self.quine_str += "9"
        for i in range(99, 1, -1):
            print(f"{i} bottles on the wall")
            print(f"{i} bottles of beer!")
            print("Take one down, pass it around")
            print(f"{i-1} bottles of beer on the wall!")


if __name__ == "__main__":
    hq = hq9p()
    while True:
        print("h: say hi")
        print("q: quine")
        print("9: 99 bottles")
        print("+: increment")

        command = input()
        hq.action(command)
