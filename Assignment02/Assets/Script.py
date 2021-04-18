def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    # raise NotImplementedError()
    import pandas
    import numpy
    df = pandas.read_csv("MyDataFile.csv", index_col = 0)
    EDUS=df['EDUC1']
    edus=numpy.sort(EDUS.values)
    poe={"less than high school":0, 
        "high school":0,
        "more than high school but not college":0,
        "college":0}
    n=len(edus)
    poe["less than high school"]=numpy.sum(edus==1)/n
    poe["high school"]=numpy.sum(edus==2)/n
    poe["more than high school but not college"]=numpy.sum(edus==3)/n
    poe["college"]=numpy.sum(edus==4)/n
    return poe

assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."