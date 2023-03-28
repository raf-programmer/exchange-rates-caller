import factory
from factory.fuzzy import FuzzyChoice


class CallDictFactory(factory.DictFactory):
    from_currency = factory.Faker("currency_code")
    to_currency = factory.Faker("currency_code")
    amount = factory.fuzzy.FuzzyInteger(10, 1000)
