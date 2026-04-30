lst = [ '🍇', '🍑', '🍐', '🍊', '🍌', '🍎']
for x in range(0, len(lst)):
    if (x < 1) or (x == len(lst)):
        print(lst[0], lst[-1])
    else:
        pass