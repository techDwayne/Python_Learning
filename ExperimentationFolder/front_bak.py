def front_back(str):
    if len(str) <= 1:
        return str

    elif len(str)== 2:
        return str[::-1]

    else:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]
print(front_back('eodc'))
