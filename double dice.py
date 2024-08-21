import random 
from time import sleep

d1 = random.choice([1,2,3,4,5,6])
d2 = random.choice([1,2,3,4,5,6])
d3 = random.choice([1,2,3,4,5,6])
score = d1+d2+d3

print(f"The first die rolled {d1}")
sleep(1)
print(f"The second die rolled {d2}")
sleep(1)
print(f"The third die rolled {d3}")
sleep(1)
print("Your score is ",score)