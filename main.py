import os

#Functions
def line_to_array(line):
    values = []
    values = line.split(",")
    return values

#Union
def U(g1, g2):
    return list(set(g1) | set(g2))
    
#Intersection
def I(g1, g2):
    return list(set(g1) & set(g2))

#Difference
def D(g1,g2):
    temp = g1.copy()
    size = len(g2)
    for i in range(size):
        if g2[i] in temp:
            temp.remove(g2[i])
    return temp

#Cartesian
def C(g1,g2):
    temp = []
    for i in range(len(g1)):
        for j in range(len(g2)):
            element = "(" + g1[i] + "," + g2[j] + ")"
            temp.append(element)
    return temp
    
    
def print_group(g, header):
    print(header, end=" ")
    print("{", end="")
    #print(g)
    for i in range(len(g)):
        if i > 0:
            print(" ", end="")
        print(g[i], end="")
        if i < len(g) - 1:
            print(",", end="")
    print("}", end="")

filedir = "demofile.txt"
valid = False

while not valid:
    print("Welcome! Please enter the name of the file you want to input without the (.txt) extension.")
    print("An empty field will default to 'demofile'!")
    temp_input = str(input(">")).replace(" ","")
    if temp_input == "": #Check for Empty
        valid = True
        break
    temp_input += ".txt"
    if os.path.isfile(temp_input):
        filedir = temp_input
        valid = True
    else:
        print("Error! The file \'" + temp_input + "\' could not be found!")


f = open(filedir, "r")


print("Showing results for \"" + filedir + "\"...")
#Treat lines
lines = []
lines = f.read().split("\n")

to_execute = int(lines.pop(0).strip())

remove_list = ['\n', ' ']
for l in range(len(lines)):
    for c in range(len(remove_list)):
        lines[l] = lines[l].replace(remove_list[c], "")
    


#Logic Variables
i = 0
result_count = 0

#Operation Variables
operator = ""
group1 = []
group2 = []

while(i < len(lines) and result_count < to_execute):
    if operator == ""  and operator in "UIDC":
        operator = lines[i]
    else:
        if len(group1) == 0:
            group1 = line_to_array(lines[i])
        else:
            group2 = line_to_array(lines[i])
            
        
    #Print
    if operator != "" and len(group1) > 0 and len(group2) > 0:
        
        operation = ""
        result = ['INVALID']
        
        match operator:
            case "U":
                operation = "União"
                result = U(group1, group2)
            case "I":
                operation = "Interseção"
                result = I(group1, group2)
            case "D":
                operation = "Diferença"
                result = D(group1, group2)
            case "C":
                operation = "Produto Cartesiano"
                result = C(group1, group2)
        
        #Print Results
        print(operation, end=": ")
        print_group(group1, "conjunto 1")
        print(", ", end="")
        print_group(group2, "conjunto 2")
        print_group(result, ". Resultado:")
        result_count += 1
        print() #Line Break
        
        #Do functions call here
        
        operator = ""
        group1 = []
        group2 = []
    i += 1