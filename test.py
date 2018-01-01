from nose.tools import *
import requests

def test_pass():
    requests.get("https://google.com")
    assert_equal("a", "a")

def test_fail():
    assert_equal("a", "b")

