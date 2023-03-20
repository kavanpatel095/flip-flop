state = False  # initial state

# read inputs
s = int(input("Enter S: "))
r = int(input("Enter R: "))

# update state
if s == 1 and r == 0:
    state = True
elif s == 0 and r == 1:
    state = False
elif s == 1 and r == 1:
    state = None  # undefined state
# else, s == 0 and r == 0, state is unchanged

# output state
if state is None:
    print("Undefined state")
elif state:
    print("Q = 1")
else:
    print("Q = 0")
