from ..events_repository import EventsRepository
import unittest
import pytest


@pytest.mark.skip(reason="This test will create an event in the database")
class EventsRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.events_repository = EventsRepository()

    def test_insert_events(self):
        event_name = "Event Test"
        self.events_repository.insert(event_name)

    def test_select_event(self):
        event_name = "Event Test"

        event = self.events_repository.select_event(event_name)

        assert event.nome == event_name
