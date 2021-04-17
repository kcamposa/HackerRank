'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example:
'alpha':[20,30,40]
'beta':[30,50,70]
query_name = 'beta'

beta = 30+50+70/3 = 50.0

'''

def findingThePercentage():
    '''
    dict_ = {
        "alpha": [20, 30, 40],
        "beta": [30, 50, 70]
    }
    '''
    dict_ = {
        "Krishna " : [67, 68, 69],
        "Arjun" : [70, 98, 63],
        "Malika" : [52, 56, 60]
    }    

    query_name = 'Malika'

    for key, value in dict_.items():
        if key == query_name:
            rsd = sum(value)/len(value)
            print("%.2f" % rsd) # 2 decimals

findingThePercentage()