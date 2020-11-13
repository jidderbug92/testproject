import app.howdy

def test_return_msg() -> None:
    expected = "hello"
    result = howdy.return_msg('hello')
    assert result == expected