import tkapi
from tkapi.stemming import Stemming

from local_settings import USER, PASSWORD

api = tkapi.Api(user=USER, password=PASSWORD, verbose=False)


def example_stemming():
    filter = Stemming.create_filter()
    filter.filter_kamerstuk(vetnummer=33885, ondernummer=16)
    stemmingen = api.get_stemmingen(filter=filter, max_items=100)
    print('stemmingen', len(stemmingen))
    total_votes = 0
    for stemming in stemmingen:
        # zaak = stemming.besluit.zaken[0]
        # print(zaak.dossier.vetnummer, zaak.volgnummer)
        print(stemming.fractie.naam, stemming.fractie_size, stemming.soort)
        total_votes += stemming.fractie_size
    print('totaal stemmen:', total_votes)


if '__main__' == __name__:
    example_stemming()
