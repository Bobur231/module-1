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


#Part 3
def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]


string = "A man a plan a canal Panama"
print(is_palindrome(string))  

class BankAccount:
    def init(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive") 

    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_balance(self) -> float:
        return self.balance

account = BankAccount()
account.deposit(100.0)
account.withdraw(30.0)
print(account.get_balance())  

def count_characters(s: str) -> dict:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

string = "example"
result = count_characters(string)
print(result)  

# Part 1
class MyClass:
    class_var = 'class variable'

    @classmethod
    def class_method(cls):
        print(f'Class method called. class_var = {cls.class_var}')

MyClass.class_method()  

class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        return arg1 + arg2

print(MyClass.static_method(5, 3))  

class MyClass:
    def init(self, value):
        self._protected = value  
        self.__private = value  

    def get_private(self):
        return self.__private 

obj = MyClass(42)
print(obj.get_private())  
print(obj._protected)     

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog woof")

class Cat(Animal):
    def speak(self):
        print("Cat miaw")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()