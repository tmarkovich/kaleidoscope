from unittest import TestCase

from kaleidoscope.lexer import (
    CharacterToken,
    DefToken,
    EOFToken,
    ExternToken,
    IdentifierToken,
    NumberToken,
)


class TestIdentifierToken(TestCase):
    def test_name(self):
        token = IdentifierToken('def')
        self.assertEqual(token.name, 'def')


class TestNumberToken(TestCase):
    def test_value(self):
        token = NumberToken(42)
        self.assertEqual(token.value, 42)


class TestCharacterToken(TestCase):
    def test_char(self):
        token = CharacterToken('+')
        self.assertEqual(token.char, '+')

    def test_char_equal(self):
        token = CharacterToken('+')
        token2 = CharacterToken('+')
        self.assertEqual(token, token2)

    def test_char_not_equal(self):
        token = CharacterToken('+')
        token2 = CharacterToken('-')
        self.assertNotEqual(token, token2)
