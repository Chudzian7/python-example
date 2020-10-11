import hello


def test_says_world():
    assert hello.say_what() == 'world'
    
def test_says_swiat():
    assert hello.say_what() == 'swiat'

def test_1():
    assert 'world' == 'world'

def test_2():
    assert 1 == 1

def test_3():
    assert '1' == '1'
