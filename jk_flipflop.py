j = True
k = False
q = False

# create a function to update the output based on the inputs
def flipflop(j, k, q):
    if j and not k:
        # set output to 1
        q = True
    elif not j and k:
        # set output to 0
        q = False
    elif j and k:
        # toggle output
        q = not q
    return q

q = flipflop(False, True, False) # q = False
print(q)

# test the function with various inputs
#q = flipflop(False, False, False) # q = False
#q = flipflop(True, False, False) # q = True
#q = flipflop(False, True, False) # q = False
#q = flipflop(True, True, False) # q = not False = True
#q = flipflop(True, True, True) # q = not True = False
