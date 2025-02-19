from ..subscribers_repository import SubscribersRepository

import unittest
import pytest


@pytest.mark.skip(reason="This test will create an event in the database")
class SubscribersRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.subscribers_repository = SubscribersRepository()

    def test_insert_subscriber(self):
        subscriber_info = {
            "name": "Test Subscriber",
            "email": "email@test.com",
            "event_id": 1,
        }

        self.subscribers_repository.insert_subscriber(subscriber_info)

    def test_select_subscriber(self):
        subscriber_info = {
            "name": "Test Subscriber",
            "email": "email@test.com",
            "link": "http://test.com",
            "event_id": 1,
        }

        subscriber = self.subscribers_repository.select_subscriber(
            subscriber_info["email"], subscriber_info["event_id"]
        )

        assert subscriber.email == subscriber_info["email"]
        assert subscriber.event_id == subscriber_info["event_id"]
        assert subscriber.name == subscriber_info["name"]

    def test_ranking(self):
        event_id = 1
        ranking = self.subscribers_repository.get_ranking(event_id)
        assert ranking[0].link is not None
        assert ranking[0].count == 1
