

from farm.animal import Animal
class Chicken(Animal):
    def __init__(self, gender):
       super().__init__()
       self.gender  = gender
       self.eggs = 0
    def feed(self):
        super().feed()
        if self.gender == "female":
            self.eggs += 2
    def talk(self):
        if self.gender == "female":
            return "cluck cluck"
        if self.gender == "male":
            return "cock-a-doodle-doo"
        raise ValueError("Unknown gender")
