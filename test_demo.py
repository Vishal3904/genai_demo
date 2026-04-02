from demo import degrees_to_fahrenheit


def test_zero_celsius():
    assert degrees_to_fahrenheit(0) == 32
