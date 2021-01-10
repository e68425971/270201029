def PascalLastline(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        Lastline = PascalLastline(n-1)
        for index in range(len(Lastline)-1):
            line.append(Lastline[index] + Lastline[index+1])
        line += [1]
        return line
