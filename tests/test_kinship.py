"""Tests for Tai Khamyang kinship and family system engine."""

import unittest
from khamyang.grammar.kinship import KinshipEngine, CLANS


class TestKinshipEngine(unittest.TestCase):

    def test_all_terms_loaded(self):
        terms = KinshipEngine.all_terms()
        self.assertGreaterEqual(len(terms), 30)

    def test_resolve_paternal_grandfather(self):
        pu = KinshipEngine.resolve("FaFa")
        self.assertIsNotNone(pu)
        self.assertEqual(pu["khamyang_roman"], "pu5")
        self.assertEqual(pu["generation"], 2)
        self.assertEqual(pu["side"], "paternal")

    def test_resolve_maternal_grandfather(self):
        taa = KinshipEngine.resolve("MoFa")
        self.assertIsNotNone(taa)
        self.assertEqual(taa["khamyang_roman"], "taa1")
        self.assertEqual(taa["side"], "maternal")

    def test_resolve_father_elder_brother(self):
        lung = KinshipEngine.resolve("FaElBr")
        self.assertIsNotNone(lung)
        self.assertEqual(lung["khamyang_roman"], "lung1")
        self.assertEqual(lung["gender"], "male")

    def test_resolve_junior_uncle(self):
        aao = KinshipEngine.resolve("FaYoBr")
        self.assertIsNotNone(aao)
        self.assertEqual(aao["khamyang_roman"], "aao1")

    def test_resolve_elder_brother(self):
        pi_chai = KinshipEngine.resolve("ElBr")
        self.assertIsNotNone(pi_chai)
        self.assertEqual(pi_chai["khamyang_roman"], "pi5 chaai1")

    def test_resolve_in_laws(self):
        khui = KinshipEngine.resolve("DaHu")
        self.assertIsNotNone(khui)
        self.assertEqual(khui["khamyang_roman"], "khɯi1")

        pae = KinshipEngine.resolve("SoWi")
        self.assertIsNotNone(pae)
        self.assertEqual(pae["khamyang_roman"], "pae1")

    def test_list_by_generation(self):
        parents_gen = KinshipEngine.list_by_generation(1)
        self.assertGreaterEqual(len(parents_gen), 5)
        romans = [p["khamyang_roman"] for p in parents_gen]
        self.assertIn("po5", romans)
        self.assertIn("me5", romans)
        self.assertIn("lung1", romans)

    def test_clans_list(self):
        clans = KinshipEngine.list_clans()
        self.assertEqual(len(clans), 6)
        clan_ids = [c["clan_id"] for c in clans]
        self.assertIn("chowlik", clan_ids)
        self.assertIn("thomung", clan_ids)
        self.assertIn("chaohai", clan_ids)
        self.assertIn("lungking", clan_ids)
        self.assertIn("pailung", clan_ids)
        self.assertIn("chowlu", clan_ids)

    def test_explain_relationship(self):
        expl = KinshipEngine.explain_relationship("FaFa")
        self.assertIn("pu5", expl)
        self.assertIn("Paternal Grandfather", expl)


if __name__ == "__main__":
    unittest.main()
