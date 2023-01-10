"""
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

"""

strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

def matchingStrings(strings, queries):
    
    ArrResults = []

    for query in queries:
        ArrResults.append(strings.count(query))

    print(ArrResults) 
    return ArrResults
            
        
if __name__ == '__main__':
    matchingStrings(strings, queries)