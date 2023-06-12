class GymAccount():

   def __init__(self, initial = 10):
       self.bal = initial

   def usepass(self, num):
       self.bal -= num

   def addpass(self, num):
       self.bal += num

   def balance(self):
       return self.bal

gym = GymAccount(50)
gym.usepass(1)
gym.addpass(12)
print(gym.balance())