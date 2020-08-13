from reader import Reader

def test():
    try:
        for line in Reader.openWithName("test.csv"):
            assert "test" in line[0]
            continue
    except AssertionError as e:
        print(e)

