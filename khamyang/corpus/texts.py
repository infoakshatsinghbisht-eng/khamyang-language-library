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

        # Text 4: Calling the Soul (Hong Khwan Ritual Chant)
        FolkText(
            id="text_004",
            title_khamyang="Hong1 Khwan1: Heu3 Khwan1 Maa1 Yu5 Nai1 To1",
            title_english="Calling of the Soul: Return of the Life Spirit",
            genre="ritual_chant",
            informant="Elder Chaw Sa Myat Chowlik",
            village="Powaimukh, Assam",
            description="Ancient Tai healing chant performed to summon back the 32 vital spirit-essences (khwan) when someone is afflicted by sickness or trauma.",
            sentences=[
                InterlinearUnit(
                    id="t4_s1",
                    text_roman="khwan1 hua1 khwan1 chai1 maa1 hɯn1 wan1 nai6",
                    lik_tai="ၶႂၼ်ႁူဝ်ၶႂၼ်ၸႂ်မႃးႁိူၼ်းဝၼ်းၼႆႉ",
                    assamese_script="খ্বন¹ হুৱা¹ খ্বন¹ চাই¹ মা¹ হ্যুন¹ ৱান¹ নাই⁶",
                    morphemes=["khwan1", "hua1", "khwan1", "chai1", "maa1", "hɯn1", "wan1", "nai6"],
                    glosses=["soul", "head", "soul", "heart", "come", "house", "day", "this"],
                    free_translation_en="O soul of the head and spirit of the heart, return home this day!",
                    free_translation_as="হে মূৰৰ প্ৰাণ আৰু হৃদয়ৰ আত্মা, আজি নিজৰ গৃহলৈ ঘূৰি আহা!",
                ),
                InterlinearUnit(
                    id="t4_s2",
                    text_roman="am1 heu3 pai1 nai1 thɯn2 doi1 lɯk4",
                    lik_tai="ဢမ်ႇႁႂ်ႈပႆၼႂ်းထိူၼ်ႇလွႆလိုၵ်ႉ",
                    assamese_script="আম¹ হেউ³ পাই¹ নাই¹ থ্যুন² দৈ¹ ল্যক⁴",
                    morphemes=["am1", "heu3", "pai1", "nai1", "thɯn2", "doi1", "lɯk4"],
                    glosses=["NEG", "allow", "wander", "inside", "forest", "mountain", "deep"],
                    free_translation_en="Do not wander astray into the deep forest and wild mountains.",
                    free_translation_as="গভীৰ অৰণ্য আৰু অচিনাকি পাহাৰত হেৰাই নাথাকিবা।",
                ),
                InterlinearUnit(
                    id="t4_s3",
                    text_roman="maa1 yu5 kap4 po5 me5 phuu5 thau3 haw1",
                    lik_tai="မႃးယူႇၵပ်းပေႃႈမႄႈၽူႈထဝ်ႈႁဝ်း",
                    assamese_script="মা¹ য়ু⁵ কাপ⁴ পৌ⁵ মে⁵ ফু⁵ থাও³ হাও¹",
                    morphemes=["maa1", "yu5", "kap4", "po5", "me5", "phuu5-thau3", "haw1"],
                    glosses=["come", "stay", "with", "father", "mother", "elder", "our"],
                    free_translation_en="Come dwell in safety with your father, mother, and our elders.",
                    free_translation_as="আহি দেউতা, মা আৰু জ্যেষ্ঠসকলৰ সতে সুৰক্ষিত হৈ বাস কৰা।",
                ),
            ],
        ),

        # Text 5: The Origin of the Nora Kingdom in Mung Mau
        FolkText(
            id="text_005",
            title_khamyang="Prawat1 Mung1 Mau1: Khun1 Lung1 tang1 Khun1 Lai1",
            title_english="The Legend of Mung Mau: The Celestial Kings Khun Lung and Khun Lai",
            genre="historical_legend",
            informant="Elder Deben Chowlik",
            village="Powaimukh, Assam",
            description="Sacred Tai chronicle relating the descent of the divine celestial ancestors Khun Lung and Khun Lai from heaven to rule over Mung Mau.",
            sentences=[
                InterlinearUnit(
                    id="t5_s1",
                    text_roman="chaophaa1 lung1 lai1 long1 maa1 luk4 faa3",
                    lik_tai="ၸဝ်ႈၽႃလုင်လၢႆလူင်းမႃးလုၵ်ႉၽႃႉ",
                    assamese_script="চাওফা¹ লুং¹ লাই¹ লং¹ মা¹ লুক⁴ ফা³",
                    morphemes=["chaophaa1", "lung1", "lai1", "long1", "maa1", "luk4", "faa3"],
                    glosses=["king", "Lung", "Lai", "descend", "come", "from", "sky/heaven"],
                    free_translation_en="The celestial royal brothers Khun Lung and Khun Lai descended down from heaven.",
                    free_translation_as="স্বৰ্গৰ পৰা স্বৰ্গীয় ভাতৃদ্বয় খুন লুং আৰু খুন লাই মৰ্ত্যলৈ নামি আহিছিল।",
                ),
                InterlinearUnit(
                    id="t5_s2",
                    text_roman="khao5 tang3 mung1 mau1 rim1 nam6 mau1",
                    lik_tai="ၶဝ်တၢင်ႇမုင်းမၢဝ်ရိမ်ႇၼမ်ႉမၢဝ်",
                    assamese_script="খাও⁵ তাং³ মুং¹ মাও¹ ৰিম¹ নাম⁶ মাও¹",
                    morphemes=["khao5", "tang3", "mung1", "mau1", "rim1", "nam6", "mau1"],
                    glosses=["3PL", "establish", "country", "Mau", "bank", "water", "Shweli"],
                    free_translation_en="They established the glorious kingdom of Mung Mau along the fertile river Mau (Shweli).",
                    free_translation_as="তেওঁলোকে মাও নদীৰ পাৰত সুবিখ্যাত মুং মাও ৰাজ্য প্ৰতিষ্ঠা কৰিলে।",
                ),
                InterlinearUnit(
                    id="t5_s3",
                    text_roman="khɯa1 nora1 luk4 mung1 mau1 khaa3 maa1 pat4kai1",
                    lik_tai="ၶိူဝ်ၼေႃးရႃႉလုၵ်ႉမုင်းမၢဝ်ၶႃႉမႃးပႅတ်ႇၵၢႆး",
                    assamese_script="খুৱা¹ নোৰা¹ লুক⁴ মুং¹ মাও¹ খা³ মা¹ পেত⁴ কাই¹",
                    morphemes=["khɯa1", "nora1", "luk4", "mung1", "mau1", "khaa3", "maa1", "pat4kai1"],
                    glosses=["clan", "Nora", "from", "country", "Mau", "cross", "come", "Patkai"],
                    free_translation_en="From Mung Mau, the ancestral Nora (Khamyang) clan crossed the rugged Patkai to Assam.",
                    free_translation_as="মুং মাওৰ পৰাই নোৰা (খাময়াং) বংশৰ পূৰ্বপুৰুষসকলে পাতকাই পাৰ হৈ অসমলৈ আহিছিল।",
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
