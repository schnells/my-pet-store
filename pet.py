class Pet:
    def __init__(self, name = "None", type = "null", age = -1) -> None:
        self.name = name
        self.type = type
        self.age = age

    def getInfo(self):
        return "Your pets' name is: " + self.name + " and it's " + str(self.age) + " years old, it is it is a " + self.type

