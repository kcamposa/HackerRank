'''
 HackerLand University has the following grading policy:

 Every student receives a grade in the inclusive range from 0 to 100.
 Any grade less than 40 is a failing grade.
 Sam is a professor at the university and likes to round each student's  
 according to these rules:
 If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
 If the value of  is less than , no rounding occurs as the result will still be a failing grade.

 examples:
 grade = 84 round 85(85-84 is less than 3)
 grade = 29 do not round(result is less than 40)
 grade = 57 do not round(60-57 is 3 or higher)
 
'''
def grandingStudents():
    
    grades = [73, 67, 38, 33]
    #grades = [84, 29, 57]
    newGrades = []

    for i in grades:
        count = 1
        if i >= 38:
            if i%5 == 0:
                newGrades.append(i)
            else:
                ver = False
                while(ver==False):
                    local = i + count
                    if local%5==0:
                        if count < 3:
                            newGrades.append(i+count)
                        else:
                            newGrades.append(i)
                        ver = True
                    count += 1
        else:
            newGrades.append(i)

    for j in newGrades:
        print(j)


grandingStudents()
