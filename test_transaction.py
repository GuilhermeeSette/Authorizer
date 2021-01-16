from transaction import *
import pytest


def test_create_transaction():
    assert create_transaction("BK", 30, "2019-02-13T10:00:00.000Z") == Transaction("BK", 30, "2019-02-13T10:00:00.000Z")