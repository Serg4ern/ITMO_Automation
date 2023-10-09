def test_list_a():
    assert ('home', 'work') == ('home', 'work')


def test_b():
    a = 'QA'
    b = 'QC'
#    assert a == b
    assert a != b


def test_c():
    x = (1, 1, 2, 3, 5)
    y = (2, 3, 5)
#    assert not x == y
    assert x != y
