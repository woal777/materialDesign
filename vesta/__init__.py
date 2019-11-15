with open('filename') as f:
    n = 0
    for l in f:
        if l.__contains__('0.7400 254   3   0 254   3   0 204  0'):
            print(l)