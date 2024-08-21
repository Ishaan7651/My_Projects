import time 

def while_trial():
    i = 0
    while i < 500:
        print(i)
        i = i + 1

def for_trial():
    for j in range(500):
        print(j)



temptime = time.time()

while_trial()
whiletime = time.time() - temptime


temptime2 = time.time()

for_trial()
print(f"The time taken by while loop is {whiletime} ")

print(f"The time taken by for loop is {time.time() - temptime2} ")
time.sleep(1)
t = time.localtime()
formated_time = time.strftime("%d-%m-%Y %H:%M")
print(formated_time)
    