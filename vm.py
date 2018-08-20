class VendingMachine:
    def __init__(self):
        self._change = 0

    def run(self,raw):
            tokens = raw.split(" ")
            cmd, params = tokens[0], tokens[1:]

            if cmd == "음료":
                price = 150
                if self._change >= price:
                    self._change = self._change - 150
                    return "커피가 나왔습니다"
                else:
                    return "잔액이 부족합니다"
            elif cmd == "잔액":
                return "잔액은 " + str(self._change) + "원입니다"
            elif cmd == "동전":
                coin = params[0]
                self._change += int(coin)
                return coin + "원을 넣었습니다"
            else:
                return "알 수 없는 명령입니다"
