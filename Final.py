import random

SCORE = 0
class question:

        x = 0
        y = 0  
        realans = 0
        ans = 0
        def __init__(self) -> None:
             self.y = random.randint(1, 10)
             self.x = random.randint(1, 10)
             self.realans = self.x*self.y
        def Answer(self) -> None: 
                print(self.y, " x ", self.x, " = ")     
                self.ans =  int(input())
        def __del__(self) -> None:
             global SCORE
             if self.ans == -1:
                     pass
             elif self.ans == self.realans:
                     print("Score Increased!")
                     SCORE = SCORE + 1
             else:
                     print("Fail")
q = 0
while 1:
    del q
    q = question()
    q.Answer()
    if q.ans == -1:
            break
print("Final Score is: ", SCORE)