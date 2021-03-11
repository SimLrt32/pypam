from unittest import TestCase

from pypam.acoustic_survey import ASA


class TestASA(TestCase):
    def setUp(self) -> None:
        self.asa = ASA({}, 'a_path_there')

    def test_detect_piling_events(self):
        self.asa.detect_piling_events(0.1, 0.5, 0.001)

    def test_detect_ship_events(self):
        # just a smoke test to check if the function can run without errors
        self.asa.detect_ship_events(0.1, 0.5)
