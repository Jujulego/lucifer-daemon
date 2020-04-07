import pytest

from lucifer.utils.style import style


# Tests
def test_style_codes():
    style.enabled = True

    # Reset
    assert '\033[m' == str(style.reset)

    # Styles
    assert '\033[1m' == str(style.bold)
    # 2
    assert '\033[3m' == str(style.italic)
    assert '\033[4m' == str(style.underline)

    # Colors
    assert '\033[31m' == str(style.red)
    assert '\033[32m' == str(style.green)
    assert '\033[33m' == str(style.yellow)
    assert '\033[34m' == str(style.blue)
    assert '\033[35m' == str(style.purple)
    # 36
    # 37
    assert '\033[38m' == str(style.white)


def test_style_disabled():
    style.enabled = False

    assert str(style.reset) == ''


def test_style_combine():
    rb = style.red + style.bold

    style.enabled = True
    assert str(rb) == '\033[31;1m'

    style.enabled = False
    assert str(rb) == ''


def test_style_add():
    style.enabled = True
    assert (style.green + 'test') == '\033[32mtest'

    style.enabled = False
    assert (style.green + 'test') == 'test'

    with pytest.raises(TypeError):
        style.green + 5


def test_style_call():
    style.enabled = True
    assert style.green('test') == '\033[32mtest\033[m'
    assert style.green(f't{style.red("es")}t') == '\033[32mt\033[31mes\033[m\033[32mt\033[m'

    style.enabled = False
    assert style.green('test') == 'test'
