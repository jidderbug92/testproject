from app import howdy

def test_return_msg() -> None:
    expected = "hello"
    result = howdy.return_msg('hello')
    print(result)
    assert result == expected