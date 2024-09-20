import pytest

# Test 1: This test will pass
def test_pass_1():
    assert 1 == 1  # Simple passing condition

# Test 2: This test will pass
def test_pass_2():
    assert "hello".upper() == "HELLO"  # Another passing condition

# Test 3: This test will fail
def test_fail_1():
    assert 2 == 3  # This will fail

# Test 4: This test will fail
def test_fail_2():
    assert len([1, 2, 3]) == 2  # This will also fail
