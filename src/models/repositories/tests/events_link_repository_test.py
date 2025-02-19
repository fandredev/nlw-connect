from ..events_link_repository import EventsLinkRepository
import unittest
import pytest


@pytest.mark.skip(reason="This test will create an event in the database")
class EventsLinkRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.events_link_repository = EventsLinkRepository()

    def test_insert_events_link(self):
        event_id = 1
        subscription_id = 1

        link = self.events_link_repository.insert(event_id, subscription_id)

        assert link is not None

    def test_select_events_link(self):
        event_id = 1
        subscription_id = 1

        event_link = self.events_link_repository.select_events_link(
            event_id, subscription_id
        )

        assert event_link is not None
        assert event_link.event_id == event_id
        assert event_link.subscription_id == subscription_id
