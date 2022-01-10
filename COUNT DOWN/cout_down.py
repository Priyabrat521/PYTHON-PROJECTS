#USING GENERATOR CONCEPT

import time
def countdown(num):
    while num>=1:
        yield num
        num=num-1
g=countdown(10)
for x in g:
    print(x)
    time.sleep(1)
print('HAPPY NEW YEAR 2022')