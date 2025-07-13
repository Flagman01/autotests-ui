def test_login():
    print('hello world')


class TestUserLogin:
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 1 == 1


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) != 5"
