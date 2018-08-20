from vm import run, init, VendingMachine

def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")


def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_coffee_yes_money():
    m = VendingMachine()
    m.run("동전 200")
    assert "커피가 나왔습니다" == m.run("음료 커피")


def test_coffee_no_money():
    m = VendingMachine()
    m.run("동전 150")
    assert "잔액이 부족합니다" == m.run("음료 커피")
