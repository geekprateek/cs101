# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    ret_val = []
    for entry in index:
        if entry[0] == keyword:
            ret_val = entry[1]
    return ret_val

def new_lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

print lookup(index,'udacity')
print new_lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']