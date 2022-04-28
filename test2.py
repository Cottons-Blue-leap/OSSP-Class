# I'm hungry function
def hungry(status):
    if 0 <= status <= 60:
        print("I'm hungry!!!")
    elif 60 < status <= 100:
        print("I'm Okay!!!")
    else:
        print("Wrong status!!!")
