"""
test_main
----------------------------------
Tests for `main` module.
"""
from bplus import main


def test_main():
    assert main.main() == 'hello'
