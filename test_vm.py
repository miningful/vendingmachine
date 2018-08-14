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
    run("동전 100")
    run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")
