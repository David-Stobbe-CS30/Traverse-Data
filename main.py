def dataSplit(file):
    return file.read().splitlines()

def surveyData():
    data = dataSplit(open("survey-results.txt", "r"))
    Yes = 0
    No = 0
    Maybe = 0
    for i in data:
        if(i == "Yes"):
            Yes+=1
        elif (i == "No"):
            No+=1
        else:
            Maybe+=1
    print(f" Yes: ({Yes}), No: ({No}), Maybe: ({Maybe})")
def ageData():
    data = dataSplit(open("age-data.txt", "r"))
    u18 = 0
    u35 = 0
    u65 = 0
    o65 = 0
    for i in data:
        i = int(i)
        if(i < 18):
            u18+=1
        elif(i <= 35):
            u35+=1
        elif(i <= 65):
            u65+=1
        else:
            o65+=1
    print(f" Under 18 ({u18}), 18 to 35 ({u35}), 36 to 65 ({u65}), Above 65 ({o65})")

def numData():
    data = dataSplit(open("number-data.txt", "r"))
    print(data)
    even = 0
    odd = 0
    for i in data:  
        if(int(i) % 2 == 0):
            even+=1
        else:
            odd+=1
    print(f"Even ({even}), Odd ({odd})")

surveyData()
ageData()
numData()