"""
Tai Khamyang Folk Texts and Traditional Narratives
==================================================
Corpus of authentic annotated texts documented from elders
in Powaimukh village (including Chaw Sa Myat Chowlik & Deben Chowlik).
"""

import json
import os
from typing import Dict, List, Optional
from khamyang.core.models import FolkText, InterlinearUnit

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "texts.json")


def get_default_corpus() -> List[FolkText]:
    """Returns foundational annotated corpus texts."""
    return [
        # Text 1: The Migration of the Khamyang (Nora)
        FolkText(
            id="text_001",
            title_khamyang="Pung1 Pu5 Yaa3 Haw1 Maa1 Thaang1 Doi1 Pat4 Kai1",
            title_english="The Migration of Our Ancestors across the Patkai Range",
            genre="migration_history",
            informant="Elder Chaw Sa Myat Chowlik & Deben Chowlik",
            village="Powaimukh, Assam",
            description="Oral historical narrative recounting the migration of the Khamyang (Nora) clans from Mung Mau through the Patkai mountain pass into Upper Assam.",
            sentences=[
                InterlinearUnit(
                    id="t1_s1",
                    text_roman="pu5 yaa3 haw1 khao5 maa1 thaang1 doi1 pat4 kai1",
                    lik_tai="ပူႈယႃႈႁဝ်းၶဝ်မႃးထၢင်ႇလွႆပႅတ်ႇၵၢႆး",
                    assamese_script="পু⁵ য়া³ হাও¹ খাও⁵ মা¹ থাং¹ দৈ¹ পেত⁴ কাই¹",
                    morphemes=["pu5-yaa3", "haw1", "khao5", "maa1", "thaang1", "doi1", "pat4-kai1"],
                    glosses=["ancestor", "1PL", "3PL", "come", "path", "mountain", "Patkai"],
                    free_translation_en="Our ancestors crossed over and came along the path of the Patkai mountains.",
                    free_translation_as="আমাৰ পূৰ্বপুৰুষসকল পাতকাই পাহাৰৰ বাটেৰে পাৰ হৈ আহিছিল।",
                ),
                InterlinearUnit(
                    id="t1_s2",
                    text_roman="khaw1 maa1 yu5 rim1 nam6 jin1",
                    lik_tai="ၶဝ်မႃးယူႇရိမ်ႇၼမ်ႉၵျိၼ်း",
                    assamese_script="খাও¹ মা¹ য়ু⁵ ৰিম¹ নাম⁶ জিন¹",
                    morphemes=["khaw1", "maa1", "yu5", "rim1", "nam6", "jin1"],
                    glosses=["3PL", "come", "live", "bank", "water", "Dihing"],
                    free_translation_en="They came and settled along the banks of the Buridihing river (Nam Jin).",
                    free_translation_as="তেওঁলোকে আহি বুঢ়ীদিহিং (নাম জিন) নদীৰ পাৰত বসতি স্থাপন কৰিছিল।",
                ),
                InterlinearUnit(
                    id="t1_s3",
                    text_roman="maan3 nai6 hɔng3 maan3 paa1 waai6",
                    lik_tai="မၢၼ်ႈၼႆႉႁွင်ႉမၢၼ်ႈပႃႉဝၢႆး",
                    assamese_script="মান³ নাই⁶ হং³ মান³ পা¹ ৱাই⁶",
                    morphemes=["maan3", "nai6", "hɔng3", "maan3", "paa1", "waai6"],
                    glosses=["village", "this", "call", "village", "mouth", "rattan"],
                    free_translation_en="This village was named Powaimukh (Village at the River-Mouth of Rattan).",
                    free_translation_as="এই গাঁওখনৰ নাম পোৱাইমুখ (বেতগছৰ নৈৰ মুখৰ গাঁও) ৰখা হ'ল।",
                ),
            ],
        ),

        # Text 2: The Folktale of the Buffalo and the Tiger
        FolkText(
            id="text_002",
            title_khamyang="Lik4 Pung1: Kwaai1 Kap4 Sɯa1",
            title_english="The Folktale of the Water Buffalo and the Tiger",
            genre="folktale",
            informant="Deben Chowlik",
            village="Powaimukh, Assam",
            description="Traditional Tai moral tale explaining how wit triumphs over brute strength.",
            sentences=[
                InterlinearUnit(
                    id="t2_s1",
                    text_roman="mi1 kwaai1 nɯŋ5 to1 kin1 yaa3 yu5 rim1 paa5",
                    lik_tai="မီႈၵႂၢႆးၼိုင်ႈတူဝ်ၵိၼ်ယႃႈယူႇရိမ်ႇပႃႈ",
                    assamese_script="মি¹ ক্ৱাই¹ নুং⁵ টো¹ কিন¹ য়া³ য়ু⁵ ৰিম¹ পা⁵",
                    morphemes=["mi1", "kwaai1", "nɯŋ5", "to1", "kin1", "yaa3", "yu5", "rim1", "paa5"],
                    glosses=["EXIST", "buffalo", "one", "CLF:animal", "eat", "grass", "PROG", "edge", "forest"],
                    free_translation_en="There was a buffalo eating grass at the edge of the forest.",
                    free_translation_as="হাবিৰ কাষত এটা ম'হে ঘাহ খাই আছিল।",
                ),
                InterlinearUnit(
                    id="t2_s2",
                    text_roman="sɯa1 luang1 nɯŋ5 to1 han1 kwaai1 an1 nan6",
                    lik_tai="သိူဝ်လူင်ၼိုင်ႈတူဝ်ႁၼ်ၵႂၢႆးဢၼ်ၼၼ်ႉ",
                    assamese_script="সুৱা¹ লুং¹ নুং⁵ টো¹ হান¹ ক্ৱাই¹ আন¹ নান⁶",
                    morphemes=["sɯa1", "luang1", "nɯŋ5", "to1", "han1", "kwaai1", "an1-nan6"],
                    glosses=["tiger", "large", "one", "CLF:animal", "see", "buffalo", "DEM:that"],
                    free_translation_en="A big tiger saw that buffalo.",
                    free_translation_as="এটা ডাঙৰ বাঘে সেই ম'হটোক দেখিলে।",
                ),
                InterlinearUnit(
                    id="t2_s3",
                    text_roman="kwaai1 hu3 panyaa1 am1 kwaa1 sɯa1",
                    lik_tai="ၵႂၢႆးႁူႉပၺ်ႇၺႃႇဢမ်ႇၵႂႃႇသိူဝ်",
                    assamese_script="ক্ৱাই¹ হু³ পঞ্ঞা¹ আম¹ ক্ৱা¹ সুৱা¹",
                    morphemes=["kwaai1", "hu3", "panyaa1", "am1", "kwaa1", "sɯa1"],
                    glosses=["buffalo", "know", "wisdom", "NEG", "fear", "tiger"],
                    free_translation_en="The buffalo had wisdom and was not afraid of the tiger.",
                    free_translation_as="ম'হটোৰ বুদ্ধি আছিল আৰু সি বাঘক ভয় নকৰিলে।",
                ),
            ],
        ),

        # Text 3: Buddhist Blessing & Water Festival Prayer
        FolkText(
            id="text_003",
            title_khamyang="Kham1 Wai1 Saa1 Poy1 Sangken1",
            title_english="Chant of Blessing for the Sangken Water Festival",
            genre="buddhist_chant",
            informant="Chaw Sa Myat Chowlik",
            village="Powaimukh, Assam",
            description="Traditional benediction chanted during the cleansing of Buddha images at Poy-Sangken.",
            sentences=[
                InterlinearUnit(
                    id="t3_s1",
                    text_roman="haw1 aw1 nam6 kat4 suk4 phaa3 tsaw3",
                    lik_tai="ႁဝ်းဢဝ်ၼမ်ႉၵတ်းသုၵ်ႈၽြႃးၸဝ်ႈ",
                    assamese_script="হাও¹ আও¹ নাম⁶ কত⁴ চুক⁴ ফা³ চাউ³",
                    morphemes=["haw1", "aw1", "nam6", "kat4", "suk4", "phaa3-tsaw3"],
                    glosses=["1PL", "take", "water", "cool/pure", "wash/cleanse", "Buddha"],
                    free_translation_en="We bring pure cool water to wash and bathe the Buddha images.",
                    free_translation_as="আমি বুদ্ধ ভগৱানৰ মূৰ্তি পৱিত্ৰ শীতল পানীৰে অভিষেক কৰোঁ।",
                ),
                InterlinearUnit(
                    id="t3_s2",
                    text_roman="hɯ3 khon1 maan3 yu5 di1 kin1 waan1",
                    lik_tai="ႁႂ်ႈၶူၼ်မၢၼ်ႈယူႇလီၵိၼ်ဝၢၼ်",
                    assamese_script="হু³ খুন¹ মান³ য়ু⁵ দি¹ কিন¹ ৱান¹",
                    morphemes=["hɯ3", "khon1-maan3", "yu5", "di1", "kin1", "waan1"],
                    glosses=["CAUSE/MAY", "villager", "live", "well", "eat", "sweet"],
                    free_translation_en="May all villagers live in health and prosperity (eat sweet).",
                    free_translation_as="সকলো গাঁওবাসীয়ে যেন কুশলে থাকে আৰু সুখ-সমৃদ্ধি লাভ কৰে।",
                ),
            ],
        ),
    ]


class KhamyangCorpus:
    """Manages annotated text collections."""

    def __init__(self, data_path: Optional[str] = None):
        self.data_path = data_path or DATA_FILE
        self._texts: List[FolkText] = []
        self._load()

    def _load(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for t_dict in data:
                    sentences = [InterlinearUnit(**s) for s in t_dict.get("sentences", [])]
                    t_dict["sentences"] = sentences
                    self._texts.append(FolkText(**t_dict))
        else:
            self._texts = get_default_corpus()

    def get_all(self) -> List[FolkText]:
        return list(self._texts)

    def get_by_id(self, text_id: str) -> Optional[FolkText]:
        for t in self._texts:
            if t.id == text_id:
                return t
        return None

    def search(self, query: str) -> List[FolkText]:
        q = query.strip().lower()
        res = []
        for t in self._texts:
            if q in t.title_khamyang.lower() or q in t.title_english.lower() or q in t.description.lower():
                res.append(t)
        return res

    def save(self, path: Optional[str] = None):
        out_p = path or self.data_path
        with open(out_p, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self._texts], f, ensure_ascii=False, indent=2)


_GLOBAL_CORPUS: Optional[KhamyangCorpus] = None


def get_corpus() -> KhamyangCorpus:
    global _GLOBAL_CORPUS
    if _GLOBAL_CORPUS is None:
        _GLOBAL_CORPUS = KhamyangCorpus()
    return _GLOBAL_CORPUS
