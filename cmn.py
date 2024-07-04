def find_max(number):
    maxx = number[0]
    for i in number:
        if i > maxx:
            maxx = i

    return maxx

