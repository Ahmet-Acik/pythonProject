def add(a,b):
    return a+b

def test_add():
    assert add(1,2) == 3
    assert add(1,1) == 2
    assert add(1,0) == 1
    assert add(1,-1) == 0
    assert add(0,0) == 0
    assert add(0,1) == 1
    assert add(0,-1) == -1
    assert add(-1,-1) == -2
    assert add(-1,0) == -1
    assert add(-1,1) == 0

def check_adult(age : int)-> bool:
    if age >= 18:
        return True
    else:
        return False

def test_check_adult():
    age = 17
    assert check_adult(age) == False
    age = 19
    assert check_adult(age) == True