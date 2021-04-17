'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''


def nestedList():

    students = []
    #students = [['harry', 37.21], ['berry', 37.21], ['tina', 37.2], ['akriti', 41.0], ['harsh', 39.0]]
    
    for i in range(int(input('Please, digit a total student: '))):
        print('===========',(i+1),'===========')
        name = input('Digit the student name: ')
        score = float(input('Digit the student score: '))

        students.append([name, score])
    
    second_highest = sorted(list(set(marks for name, marks in students)))[1]
    print('\n'.join([a for a,b in sorted(students) if b == second_highest]))


nestedList()
