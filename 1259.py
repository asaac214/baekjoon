while True:
    inp = str(input())
    if inp == '0':
        break
    else:
        rev = ''
        for c in inp:
            rev = c + rev
        if rev == inp:
            print('yes')
        else:
            print('no')
