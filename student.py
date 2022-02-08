class Student:
   # Instance attribute
   def __init__(self, name,addres,id):
      self.name = name
      self.addres = addres
      self.id=id

   def displayDetails(self):
      print("name:",self.name,"address:",self.addres," id:",self.id)

s1 = Student("varsha","shimoga",24)
s2 = Student("nayana", "tumkur", 25)
s3 = Student("chaita", "bhadravathi",26)
s4 = Student("maina", "soraba", 27)

print("deatils of all student :")
s1.displayDetails()
s2.displayDetails()
s3.displayDetails()
s4.displayDetails()




