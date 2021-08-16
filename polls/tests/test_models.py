import pytest

from polls.models import Question, Choice
from djangotestpatterns.test import TestCase
from polls.tests.factories import QuestionFactory


class TestQuestion(TestCase):
    def test_factory(self):
        question = QuestionFactory()

        assert question is not None
        assert question.question_text != ""
        
    def test_str(self):
        question = QuestionFactory()

        assert str(question) == question.question_text

