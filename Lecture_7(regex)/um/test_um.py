from um import count

def test_count():
    assert count("um? i was going to eat something yummy, perhaps, um yoghurt") == 2
    assert count("um") == 1
    assert count("um?") == 1