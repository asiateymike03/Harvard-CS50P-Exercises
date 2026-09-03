from twttr import shorten

def test_shorten():
    assert shorten("james") == "jms"
    assert shorten("bond") == "bnd"