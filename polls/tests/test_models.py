import datetime
import pytest


from django.utils import timezone

from polls.models import Question, Choice


from djangotestpatterns.test import TestCase
from polls.tests.factories import QuestionFactory


class TestQuestion(TestCase):
    def test_str(self):
        question = QuestionFactory()

        assert str(question) == question.question_text  # pytest
        self.assertEqual(str(question), question.question_text)  # django from testcase

    def test_factory(self):
        question = QuestionFactory()

        assert question is not None
        assert question.question_text != ""

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = QuestionFactory(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = QuestionFactory(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = QuestionFactory(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
