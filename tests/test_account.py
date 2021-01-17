from account import *
import pytest


def test_create_account():
    assert create_account(True, 30) == Account(True, 30)
