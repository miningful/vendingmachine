change = 0


def run(raw):
    global change

    tokens = raw.split(" ")
    cmd, params = tokens[0], tokens[1:]

    if cmd == "잔액":
        return "잔액은" + str(change) + "원입니다"
    else:
        change += int(coin)  #+=은 chanse + int(coin)과 같은 표현 
        return coin + "원을 넣었습니다"
