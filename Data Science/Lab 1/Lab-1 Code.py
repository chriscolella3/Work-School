# You should write your answer within the function provided.
# should return a string
def answer_one():

    max_name = "test"
    max_number = 0
    
    for i in range(len(baby_list)):
            
        if baby_list[i][1] == "M":
            if baby_list[i][2] > max_number:
                max_number = baby_list[i][2]
                max_name = baby_list[i][0]
    
    return (max_name, max_number)

answer_one()

# You should write your answer within the function provided.
# should return a list of strings
def answer_two():
    girl_names = []
    max_name = "test"
    max_number = 10000
    
    for i in range(len(baby_list)):
            
        if baby_list[i][1] == "F":
            if baby_list[i][2] > max_number:
                girl_names.append(baby_list[i][0])
    
    return (girl_names)

answer_two()

# You should write your answer within the function provided.
# should return an integer
def answer_three():
    
    boy_names = 0
    max_number = 8000
    
    for i in range(len(baby_list)):
            
        if baby_list[i][1] == "M":
            if baby_list[i][2] > max_number:
                boy_names += 1
    
    return (boy_names)

answer_three()

# You should write your answer within the function provided.
# should return an integer
def answer_four(name,gender):
    
    given_number = []
    
    for i in range(len(baby_list)):

        if name == baby_list[i][0] and gender == baby_list[i][1]:
            given_number.append(baby_list[i][2])
            
                        
            return (given_number)

# Test code for Question 4
# !!! Don't modify this cell !!!
names = ["Emmy","Abc","Allen","Allen","Jacob"]
genders = ["F","F","M","F","M"]
for i in range (0, len(names)):
    print ("Name:",names[i],"Gender:",genders[i],"Number:",answer_four(names[i],genders[i]))