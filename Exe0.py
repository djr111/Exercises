
class Person:
  def __init__(self, name, height, nationality):
    self.name = name
    self.height = height
    self.nationality = nationality

p1 = Person("Raimond", 182, "Latvian")
next = input("Please type GO to know a little more about me : ")

if next == "GO":
    print(p1.name)
    print(p1.height)
    print(p1.nationality)
else:
    print("\033[1;31m Wrong input Buddy  \n")
