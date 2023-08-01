import pytest


@pytest.mark.smoke
def test_one():
    assert True


@pytest.mark.regress
def test_two():
    assert True


@pytest.mark.regress
def test_three():
    assert True


@pytest.mark.regress
def test_four():
    assert True
