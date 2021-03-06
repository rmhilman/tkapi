import datetime

from tkapi.fractie import Fractie, FractieOrganisatie, FractieLid

from .core import TKApiTestCase


class TestFractie(TKApiTestCase):
    # start_datetime = datetime.datetime(year=2017, month=1, day=1)
    # end_datetime = datetime.datetime(year=2017, month=2, day=1)

    def test_get_fractie(self):
        fractie = self.api.get_item(Fractie, id='97d432a7-8a64-4db9-9189-cc9f70a4109b')
        print('fractie:', fractie.naam)
        self.assertEqual('GroenLinks', fractie.naam)
        self.assertEqual('GL', fractie.afkorting)
        self.assertEqual(datetime.date(year=1990, month=11, day=24), fractie.datum_actief)
        self.assertEqual(None, fractie.datum_inactief)
        # fractie.print_json()
        leden = fractie.leden
        for lid in leden:
            # lid.print_json()
            print(lid.van, '-', lid.tot_en_met)
            if lid.persoon:
                print(lid.persoon)
        print('fractieleden:', len(leden))
        self.assertGreater(len(leden), 53)

    def test_get_fracties(self):
        fracties = self.api.get_fracties(max_items=50)
        for fractie in fracties:
            # fractie.print_json()
            print('fractie:', fractie.naam, '| zetels:', fractie.zetels)
        self.assertEqual(39, len(fracties))

    def test_filter_fracties_actief(self):
        filter = Fractie.create_filter()
        filter.filter_actief()
        fracties = self.api.get_fracties(max_items=50, filter=filter)
        for fractie in fracties:
            # fractie.print_json()
            print('fractie:', fractie.naam, '| zetels:', fractie.zetels)
        self.assertEqual(13, len(fracties))

    def test_filter_actieve_leden(self):
        fractie = self.api.get_item(Fractie, id='97d432a7-8a64-4db9-9189-cc9f70a4109b')
        leden_actief = fractie.leden_actief
        print(fractie.naam, fractie.zetels)
        for lid in leden_actief:
            print('\t', lid.persoon)
        self.assertEqual(fractie.zetels, len(leden_actief))


class TestFractieLid(TKApiTestCase):

    def test_get_fractie_leden(self):
        leden = self.api.get_fractie_leden(max_items=10)
        print('fractieleden:', len(leden))
        self.assertEqual(10, len(leden))
        for lid in leden:
            print(lid.persoon.voornamen, lid.persoon.achternaam)
            # lid.print_json()

    def test_get_fractie_leden_actief(self):
        filter = FractieLid.create_filter()
        filter.filter_actief()
        leden = self.api.get_fractie_leden(max_items=10, filter=filter)
        print('fractieleden:', len(leden))
        for lid in leden:
            # lid.print_json()
            self.assertEqual(lid.tot_en_met, None)
            self.assertEqual(lid.is_actief, True)


class TestFractieOrganisatie(TKApiTestCase):

    def test_get_organisatie(self):
        uid = '96cd98f6-7cd5-408d-b699-2af03404be7b'
        organisatie = self.api.get_item(FractieOrganisatie, id=uid)
        self.assertEqual('Tweede Kamer der Staten-Generaal', organisatie.naam)
        self.assertEqual('7682ced0-84ea-46f1-8e27-294b272af931', organisatie.fractie.id)