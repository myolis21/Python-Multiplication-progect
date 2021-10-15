import random 
SCORE = [0, 0, 0]
class question:

        x = 0
        y = 0  
        realans = 0
        ans = 0
        def __init__(self, Dif) -> None:
             if Dif == "easy":
              self.y = random.randint(-10, 10)
              self.x = random.randint(-10, 10)
              self.realans = self.x*self.y
             elif Dif == "medium":
              self.y = random.randint(-20, 20)
              self.x = random.randint(-20, 20)
              self.realans = self.x*self.y   
             elif Dif == "hard":
              self.y = random.randint(-30, 30) 
              self.x = random.randint(-30, 30)
              self.realans = self.x*self.y                     
        def Answer(self) -> None: 
                print(self.y, " x ", self.x, " = ")     
                self.ans =  int(input())
        def __del__(self) -> None:
             global SCORE
             if self.ans == -11: 
                     pass
             elif self.ans == self.realans:
                     print("Score Increased!")
                     SCORE = SCORE + 1
             else:
                     print("Fail")
q = 0
while 1:
        diffuculty = input("Diffuculty: easy, medium, hard: ")
                while diffuculty == "easy" or "medium" or "hard": #this shoudnt run, but it does
                print(diffuculty, " is not a value") 
                diffuculty = input("Please input correct value: ")
        while 1:
                q = question(diffuculty)
                q.Answer()
                if q.ans == -11:
                 print("Score is: ", SCORE)
                 break
                del q
