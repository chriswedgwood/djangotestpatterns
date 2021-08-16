import datetime
import factory
from polls.models import Question



class QuestionFactory(factory.Factory):
    class Meta:
        model = Question

    question_text = factory.Sequence(lambda n: 'Question %s' % n)
    pub_date = factory.LazyFunction(datetime.datetime.now)