import datetime

from .core import TKApiTestCase


class TestAgendapunt(TKApiTestCase):

    def test_get_agendapunten(self):
        agendapunten = self.api.get_agendapunten(filter=None, max_items=10)
        for agendapunt in agendapunten:
            if agendapunt.parlementaire_documenten:
                agendapunt.print_json()
            # agendapunt.print_json()
            # for zaak in agendapunt.zaken:
            #     print(zaak)
            # for document in agendapunt.parlementaire_documenten:
            #     document.print_json()
