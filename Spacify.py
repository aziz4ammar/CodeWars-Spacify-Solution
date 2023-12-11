def spacify(string):
    result = ""
    for i in range(len(string)):
        if i < len(string) - 1:
            result += string[i] + " "
        else:
            result += string[i]
    return result