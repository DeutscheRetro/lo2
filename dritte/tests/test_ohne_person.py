"""Ohne Spielerdatenbank kennt die Pipeline keine Personen: zwei Transfers desselben Klubs
dürfen dann nicht als Dublette gelten oder in einem Artikel landen."""
import datetime
import unittest
from pathlib import Path

import storys


def _g(titel):
    a = storys.analysiere(titel)
    return {**a, "titel": titel, "quellen": [{"url": titel}]}


class OhnePerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        storys.init(Path("gibt-es-nicht.json"), {"msv duisburg": "Duisburg", "duisburg": "Duisburg"})
        cls.jetzt = datetime.datetime.now()
        cls.archiv = storys.archiv_vorbereiten([{
            "id": "a1", "title": "MSV Duisburg verpflichtet Innenverteidiger", "summary": "",
            "published_at": (cls.jetzt - datetime.timedelta(days=3)).isoformat(),
            "event_stage": "vollzogen", "main_club": "MSV Duisburg"}], cls.jetzt)

    def test_zweiter_transfer_ist_keine_dublette(self):
        status, _ = storys.archiv_abgleich(_g("MSV Duisburg verpflichtet Stürmer aus Verl"), self.archiv, self.jetzt)
        self.assertNotEqual(status, "doppelt")

    def test_fast_gleiche_schlagzeile_ist_dublette(self):
        status, _ = storys.archiv_abgleich(_g("MSV Duisburg verpflichtet neuen Innenverteidiger"), self.archiv, self.jetzt)
        self.assertEqual(status, "doppelt")

    def test_zwei_transfers_nicht_in_einen_artikel(self):
        schlange = [_g("MSV Duisburg verpflichtet Innenverteidiger")]
        self.assertFalse(storys.einreihen(schlange, _g("MSV Duisburg verpflichtet Stürmer aus Verl")))
        self.assertTrue(storys.einreihen(schlange, _g("MSV Duisburg verpflichtet neuen Innenverteidiger")))


if __name__ == "__main__":
    unittest.main()
