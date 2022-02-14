class base():
    def e1(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(f"name:{self.name},address:{self.address}")
class derive(base):
    def __init__(self):
        self.name = "derive"
d=derive
d.e1("varsha","shimoga")
d.display
