class EOFToken(object):
    pass

class DefToken(object):
    pass

class ExternToken(object):
    pass

class IdentifierToken(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class NumberToken(object):
    """Number token.
    """
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

class CharacterToken(object):
    """The catchall token for our simple lexer.
    """
    def __init__(self, char):
        self._char = char

    @property
    def char(self):
        return self._char

    def __eq__(self, other):
        return (isinstance(other, CharacterToken) and
                (self.char == other.char))

    def __ne__(self, other):
        return not (self == other)
