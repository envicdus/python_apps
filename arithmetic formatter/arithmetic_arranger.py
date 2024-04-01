import re
def arithmetic_arranger(problems, solve = False):
    line_1 = "" #line for first number
    line_2 = "" #line for second number
    line_3 = "" #line for the dashes
    line_4 = "" #line for the answer
    arr_problem ="" #string of the whole operation
    #limit problems to 5
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        if(re.search("[^\s0-9.+-]", problem)): #searches numbers and operator
             if(re.search("[/]", problem) or re.search("[*]", problem)):#searches for signs
                 return "Error: Operator must be '+' or '-'."
             return "Error: Numbers must only contain digits."
        
           
        
        oprd_1 = problem.split(" ")[0]
        oprd_2 = problem.split(" ")[2]
        oprtr = problem.split(" ")[1]
        
        #check for number length
        if(len(oprd_1) > 4 or len(oprd_2) > 4):
            return "Error: Numbers cannot be more than four digits."
        
        #operation
        sum = ""
        if(oprtr == "+"):
            sum = str(int(oprd_1) + int(oprd_2))
        elif(oprtr == "-"):
            sum = str(int(oprd_1) - int(oprd_2))
        
        #length of the operation
        length = max(len(oprd_1), len(oprd_2)) + 2
        top = str(oprd_1).rjust(length)
        bot = oprtr + str(oprd_2).rjust(length - 1)
        dash = ""
        answer = str(sum).rjust(length)
        
        #dictates the length of dashes
        for i in range(length):
            dash += "-"
        
        #output format
        if problem != problems[-1]:
            line_1 += top + '    '
            line_2 += bot + '    '
            line_3 += dash + '    '
            line_4 += answer + '    '
        else:
            line_1 += top
            line_2 += bot
            line_3 += dash
            line_4 += answer
      
    if solve:
        arr_problem = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
    else:
        arr_problem = line_1 + "\n" + line_2 + "\n" + line_3
 
    
    return arr_problem