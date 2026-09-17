# Bug Hunt

count = 1
total = 0

# BUG: The while statement was missing a colon.
# Added a colon after the condition so the while loop has a valid block.
while count <= 5:

    # BUG: The loop needed to continue through 5.
    # Changed count < 5 to count <= 5 so that 5 is included.
    total = total + count
    count = count + 1

# BUG: total is an integer, so it cannot be directly joined to a string with +.
# Used str(total) to convert the number to text.
print("Sum of 1 to 5 is: " + str(total))

while count <= 5:python bug_hunt.py

