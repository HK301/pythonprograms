# Implement Python Switch Case Statement using Dictionary

def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"
def THURSDAY():
    return "Thursday"
switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday(),
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(4))
print(switch(5))
