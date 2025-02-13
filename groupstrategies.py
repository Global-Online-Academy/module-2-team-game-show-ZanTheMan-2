import random

# YOU ARE THE DRIVER IN PAIR PROGRAMMING
# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH

# Here are some history variables to test your code on. Feel free to create your own.

hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","steal"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 

def strategy1(history):
    if len(history) < 3:
       return "steal"
    else:
        if history[-1] == "steal":
          return "split"
        else:
            return "steal"


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 

'''
For the first 5 games pick random, 
after pick the least played from the oponent 
'''

def strategy2(history):
    global counter
    counter = 0
   
    for steal in history:
        if steal[-1] == "steal":
            counter +=1
         

    if len(history) <= 5:
        return random.choice(["split", "steal"])
    else:
        if counter > (len(history) / 2):
            return "split"
        elif counter < (len(history) / 2):
            return "steal"
        else:
            return random.choice(["split", "steal"])
    

print(strategy2(hist4))

# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
