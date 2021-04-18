import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    namesB=[ ]
    for item in re.finditer("(?P<name>.*)(\: B*)",grades ):
        namesB.append(item.group('name'))
    return namesB
    raise NotImplementedError()
    
    
grades()