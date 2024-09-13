#Part 2 Syntext 

def is_even(num):
     if num % 2 == True:
        print("Число не четное")
     else:
        print("Число четное")
is_even(2)
class Car():
    def init(self, made, model, year):
        self.made = made
        self.model = model
        self.year = year 
    
    def display_info(self):return f"{self.made},{self.model}, {self.year}" 
    
values = Car("UZB", "2009", "Malibu")
print(values.display_info())

