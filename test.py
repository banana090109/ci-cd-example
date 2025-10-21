from app import is_even

def test_is_even():
    assert not is_even(1)
    assert is_even(2)