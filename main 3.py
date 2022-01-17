for i in range(100):
    a = str(i + 1)
    b = list(a)
    if int(b[-1]) == 1 and i + 1 != 11:
        print('{} процент'.format(i + 1))
    elif int(b[-1]) > 1 and int(b[-1]) <= 4 and i + 1 != 12 and i + 1 != 13 and i + 1 != 14:
        print('{} процентa'.format(i + 1))
    elif int(b[-1]) > 4 and int(b[-1]) <= 21:
        print('{} процентов'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))



