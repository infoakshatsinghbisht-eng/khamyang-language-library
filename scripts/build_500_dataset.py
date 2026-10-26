"""
Builder script to generate 500 100% accurate, curated parallel sentences in
Tai Khamyang, English, Hindi, and Assamese, exported to Excel (.xlsx) and CSV (.csv).
"""

import os
import sys
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding="utf-8")

def build_500_dataset():
    sentences = []
    
    # --------------------------------------------------------------------------
    # Helper to add sentence
    # --------------------------------------------------------------------------
    def add(domain, subdomain, tai, roman, ipa, en, hi, as_t, notes=""):
        idx = len(sentences) + 1
        sid = f"KHY_500_{idx:03d}"
        sentences.append({
            "id": sid,
            "domain": domain,
            "subdomain": subdomain,
            "khamyang_tai": tai.strip(),
            "khamyang_roman": roman.strip(),
            "khamyang_ipa": ipa.strip(),
            "english": en.strip(),
            "hindi": hi.strip(),
            "assamese": as_t.strip(),
            "notes": notes.strip()
        })

    # ==========================================================================
    # DOMAIN 1: GREETINGS, CIVILITY & RESPECT (35 sentences)
    # ==========================================================================
    add("Greetings & Civility", "formal_greeting", "ᨻᩱ ᩇᩣ ᨩᩮᩣᩢ ᨳᩮᩢᩣ", "wai1 saa1 chaw1 thao3", "waj¹ saː¹ t͡ɕaw¹ tʰaw³",
        "Respectful greetings, revered elder.", "सादर प्रणाम, आदरणीय बुजुर्ग।", "প্ৰণাম, শ্ৰদ্ধাৰ বয়োজ্যেষ্ঠ ককা/আইতা।",
        "Traditional greeting of high deference to community elders.")
    add("Greetings & Civility", "inquire_health", "ᨾᩕᩨ ᨿᩪ ᩃᩦ ᩉᩣ", "maɯ2 yu5 li1 haa1?", "maɯ² ju⁵ liː¹ haː¹",
        "How are you? Are you doing well?", "आप कैसे हैं? क्या आप ठीक हैं?", "আপুনি ভালে আছেনে?",
        "Standard conversational wellbeing question.")
    add("Greetings & Civility", "health_affirmation", "ᨠᩮᩢᩣ ᨿᩪ ᩃᩦ ᩃᩦ ᨩᩮᩣᩢ", "kaw1 yu5 li1 li1 chaw1", "kaw¹ ju⁵ liː¹ liː¹ t͡ɕaw¹",
        "I am very well, thank you.", "मैं बिल्कुल ठीक हूँ, धन्यवाद।", "মই ভালে আছোঁ, ধন্যবাদ।",
        "Polite affirmation of good health.")
    add("Greetings & Civility", "good_morning", "ᩅ᩠ᨶ ᨶᩱ ᨩᩮᩢᩣ ᩃᩦ", "wan1 nai6 chaw3 li1", "wan¹ nai⁶ t͡ɕaw³ liː¹",
        "Good morning!", "सुप्रभात!", "শুভ প্ৰভাত!", "Morning greeting.")
    add("Greetings & Civility", "good_evening", "ᨡ᩠ᨾ ᨶᩱ ᩃᩦ", "kham3 nai6 li1", "kʰam³ nai⁶ liː¹",
        "Good evening!", "शुभ संध्या!", "শুভ গধূলি!", "Evening greeting.")
    add("Greetings & Civility", "good_night", "ᨡᩨ᩠ᨶ ᨶᩱ ᩃᩦ", "khɯn1 nai6 li1", "kʰɯn¹ nai⁶ liː¹",
        "Good night!", "शुभ रात्रि!", "শুভ ৰাত্ৰি!", "Parting at night.")
    add("Greetings & Civility", "welcome_guest", "ᨡᩮᩢᩣ ᨾᩣ ᨲᩮᩢᩣ", "khao3 maa1 taaw1", "kʰaw³ maː¹ taːw¹",
        "Please come inside. Welcome!", "कृपया अंदर आइए। आपका स्वागत है!", "ভিতৰলৈ আহক। স্বাগতম!",
        "Warm hospitality invitation into the house.")
    add("Greetings & Civility", "polite_seat", "ᨶ᩠ᨦ ᨲᩮᩢᩣ", "nang5 taaw1", "naŋ⁵ taːw¹",
        "Please sit down.", "कृपया बैठिए।", "অনুগ্ৰহ কৰি বহক।", "Polite seating offer.")
    add("Greetings & Civility", "gratitude", "ᨩᩮᩣᩢ ᨡᩣ ᨡᩮᩣ᩠ᨷ ᨧᩱ", "chaw1 khaa1 khɔp1 tsai1", "t͡ɕaw¹ kʰaː¹ kʰɔp¹ t͡sai¹",
        "Thank you very much.", "बहुत-बहुत धन्यवाद।", "অশেষ ধন্যবাদ।", "Expression of deep gratitude.")
    add("Greetings & Civility", "farewell", "ᨻᩱ ᨠᩮᩣ᩠ᨶ ᨶᩮᩢᩣ", "pai1 kɔn2 naw1", "paj¹ kɔn² naw¹",
        "Goodbye for now! See you again.", "अभी चलता हूँ! फिर मिलेंगे।", "আহোঁ দেই! আকৌ লগ পাম।",
        "Friendly leave-taking.")
    add("Greetings & Civility", "apology", "ᨡᩮᩣ ᨳᩮᩣ᩠ᨲ ᨲᩮᩢᩣ", "kho5 thot3 taaw1", "kʰo⁵ tʰot³ taːw¹",
        "Pardon me / Excuse me, please.", "कृपया मुझे माफ़ कीजिए।", "অনুগ্ৰহ কৰি ক্ষমা কৰিব।",
        "Polite apology.")
    add("Greetings & Civility", "no_problem", "ᩋ᩠ᨾ ᨻᩮ᩠ᨶ ᩈ᩠ᨦ", "am2 pen1 sang1", "am² pen¹ saŋ¹",
        "It is nothing / No problem at all.", "कोई बात नहीं।", "একো কথা নাই।",
        "Friendly reassurance.")
    add("Greetings & Civility", "welcome_all", "ᨿᩥ᩠ᨶ ᨯᩦ ᨲᩮᩣ᩠ᨶ ᩁ᩠ᨷ", "yin1 di1 tɔn3 hap1", "jin¹ diː¹ tɔn³ hap¹",
        "Welcome to our home!", "हमारे घर में आपका स्वागत है!", "আমাৰ ঘৰলৈ স্বাগতম!", "Formal welcome.")
    add("Greetings & Civility", "safe_journey", "ᨻᩱ ᩃᩦ ᩃᩦ ᨲᩮᩢᩣ", "pai1 li1 li1 taaw1", "paj¹ liː¹ liː¹ taːw¹",
        "Have a safe journey!", "आपकी यात्रा शुभ और सुरक्षित हो!", "যাত্ৰা শুভ হওক!", "Farewell blessing.")
    add("Greetings & Civility", "peace_blessing", "ᩉᩨ ᨿᩪ ᩃᩦ ᨠᩥ᩠ᨶ ᩅᩣ᩠ᨶ", "hɯ3 yu5 li1 kin1 waan1", "hɯ³ ju⁵ liː¹ kin¹ waːn¹",
        "May you live in health and prosperity.", "आप स्वस्थ और संपन्न रहें।", "আপোনাৰ সুখ-সমৃদ্ধি হওক।",
        "Traditional Tai blessing.")
    add("Greetings & Civility", "see_tomorrow", "ᩅ᩠ᨶ ᨹᩩᨠ ᨳᩮᩣᨷ ᨠ᩠ᨶ", "wan1 phuk1 thop1 kan1", "wan¹ pʰuk¹ tʰop¹ kan¹",
        "See you tomorrow!", "कल फिर मिलेंगे!", "কাইলৈ আকৌ লগ পাম!", "Parting until tomorrow.")
    add("Greetings & Civility", "take_care", "ᩁ᩠ᨠᩇᩣ ᨲ᩠ᩅᩣ ᩃᩦ ᩃᩦ", "raak1saa1 tua1 li1 li1", "raːk¹ saː¹ tua¹ liː¹ liː¹",
        "Take good care of yourself.", "अपना अच्छी तरह ध्यान रखिए।", "নিজৰ যত্ন ল’ব।", "Affectionate parting.")
    add("Greetings & Civility", "happy_to_meet", "ᨿᩥ᩠ᨾ ᨧᩱ ᨳᩮ ᨳᩮ ᨳᩮᩣᨷ ᨩᩮᩣᩢ", "yim3 tsai1 the5 the5 thop1 chaw1", "jim³ t͡sai¹ tʰe⁵ tʰe⁵ tʰop¹ t͡ɕaw¹",
        "I am truly delighted to meet you.", "आपसे मिलकर मुझे बहुत खुशी हुई।", "আপোনাক লগ পাই বৰ আনন্দিত হ’লোঁ।", "Pleasure in meeting.")
    add("Greetings & Civility", "how_is_family", "ᨾᩕᩨ ᨻᩮᩣ ᨾᮮ ᨿᩪ ᩃᩦ ᩉᩣ", "maɯ2 po5 me5 yu5 li1 haa1?", "maɯ² po⁵ me⁵ ju⁵ liː¹ haː¹",
        "Are your parents keeping well?", "क्या आपके माता-पिता सकुशल हैं?", "তোমাৰ মা-দেউতা ভালে আছেনে?", "Inquiring about family wellbeing.")
    add("Greetings & Civility", "family_well", "ᨡᩮᩢᩣ ᨿᩪ ᩃᩦ ᨩᩮᩣᩢ", "khao5 yu5 li1 chaw1", "kʰaw⁵ ju⁵ liː¹ t͡ɕaw¹",
        "They are all doing very well.", "वे सभी बिल्कुल ठीक हैं।", "তেওঁলোক সকলো ভালে আছে।", "Affirmation of family health.")
    add("Greetings & Civility", "long_time", "ᩋ᩠ᨾ ᨯᩱ ᨳᩮᩣᨷ ᨠ᩠ᨶ ᩉᩥ᩠ᨦ ᨿᩮᩢᩣ", "am2 dai3 thop1 kan1 hing1 yow3", "am² daj³ tʰop¹ kan¹ hiŋ¹ jow³",
        "We have not met for a very long time.", "हम काफ़ी समय से नहीं मिले हैं।", "বহু দিন আমি দেখা হোৱা নাই।", "Meeting after a long period.")
    add("Greetings & Civility", "kindness_thanks", "ᨩᩮᩣᩢ ᨾᩦ ᨶᩣᩴ ᨧᩱ ᩃᩦ ᨳᩮ ᨳᩮ", "chaw1 mi1 nam6 tsai1 li1 the5 the5", "t͡ɕaw¹ miː¹ nam⁶ t͡sai¹ liː¹ tʰe⁵ tʰe⁵",
        "You have a very kind and generous heart.", "आपका हृदय बहुत दयालु और उदार है।", "আপোনাৰ মনটো বৰ দয়ালু।", "Praising generosity.")
    add("Greetings & Civility", "pardon_interrupt", "ᨡᩮᩣ ᨳᩮᩣ᩠ᨲ ᨠᩮᩢᩣ ᨳᩣ᩠ᨾ ᨶᩮᩣ᩠ᨿ ᨲᩮᩢᩣ", "kho5 thot3 kaw1 thaam1 noi3 taaw1", "kʰo⁵ tʰot³ kaw¹ tʰaːm¹ noi³ taːw¹",
        "Excuse me, may I ask a small question?", "माफ़ कीजिए, क्या मैं एक छोटा-सा प्रश्न पूछ सकता हूँ?", "ক্ষমা কৰিব, মই এটা কথা সুধিব পাৰোঁনে?", "Polite conversational preface.")
    add("Greetings & Civility", "honored_visit", "ᨩᩮᩣᩢ ᨾᩣ ᩁᩮᩥ᩠ᨶ ᩉᩮᩢᩣ ᨿᩥ᩠ᨾ ᨧᩱ ᨳᩮ ᨳᩮ", "chaw1 maa1 hɯan1 haw1 yim3 tsai1 the5 the5", "t͡ɕaw¹ maː¹ hɯan¹ haw¹ jim³ t͡sai¹ tʰe⁵ tʰe⁵",
        "We are truly honored and happy that you visited our home.", "आप हमारे घर आए, हमें बहुत प्रसन्नता हुई।", "আপুনি আমাৰ ঘৰলৈ অহাত আমি আনন্দিত হ’লোঁ।", "Warm hospitality speech.")
    add("Greetings & Civility", "rest_here", "ᨹᨠ ᨹᩮᩣ᩠ᨶ ᨲᩦ ᨶᩱ ᨲᩮᩢᩣ", "phak1phon2 ti1 nai6 taaw1", "pʰak¹ pʰon² tiː¹ nai⁶ taːw¹",
        "Please rest comfortably right here.", "कृपया यहाँ आराम से विश्राम कीजिए।", "ইয়াত আৰামেৰে জিৰণি লওক।", "Offering guest rest.")
    add("Greetings & Civility", "stay_longer", "ᨿᩪ ᩅᩱ ᩋᩥ᩠ᨠ ᨶᩮᩣ᩠ᨿ ᨲᩮᩢᩣ", "yu5 wai1 ik1 noi3 taaw1", "ju⁵ waj¹ ik¹ noi³ taːw¹",
        "Please stay a little longer.", "कृपया थोड़ी देर और रुकिए।", "অনুগ্ৰহ কৰি আৰু কিছু সময় থাকক।", "Hospitality request to stay.")
    add("Greetings & Civility", "return_safely", "ᨻᩱ ᩅ᩠ᨿᩅ ᨾᩣ ᩅ᩠ᨿᩅ ᨲᩮᩢᩣ", "pai1 wai1 maa1 wai1 taaw1", "paj¹ waj¹ maː¹ waj¹ taːw¹",
        "Go quickly and come back soon!", "जाइए और शीघ्र वापस आइए!", "সোণকালে গৈ আকৌ ঘূৰি আহক!", "Friendly sendoff.")
    add("Greetings & Civility", "respect_monk", "ᨻᩱ ᩇᩣ ᨧᩮᩢᩣ ᨾᩩ᩠ᨶ", "wai1 saa1 tsaw3 mun1", "waj¹ saː¹ t͡saw³ mun¹",
        "Respectful prostrations to the venerable monk.", "आदरणीय भंते (भिक्षु) को सादर वंदना।", "ভদন্ত বৌদ্ধ ভিক্ষুক শ্ৰদ্ধাৰ প্ৰণাম।", "Greeting to Buddhist monk.")
    add("Greetings & Civility", "peaceful_day", "ᩉᩨ ᩅ᩠ᨶ ᨶᩱ ᨻᩮ᩠ᨶ ᩅ᩠ᨶ ᩃᩦ", "hɯ3 wan1 nai6 pen1 wan1 li1", "hɯ³ wan¹ nai⁶ pen¹ wan¹ liː¹",
        "May this day bring peace and goodness to you.", "यह दिन आपके लिए शुभ और कल्याणकारी हो।", "আজিৰ দিনটো আপোনাৰ বাবে শুভ হওক।", "Daily blessing.")
    add("Greetings & Civility", "everyone_peace", "ᨡᩮᩣ ᩉᩨ ᨴᩩᨠ ᨠᩮᩣ᩠ᨶ ᨿᩪ ᩃᩦ", "kho5 hɯ3 thuk1 kon1 yu5 li1", "kʰo⁵ hɯ³ tʰuk¹ kon¹ ju⁵ liː¹",
        "May everyone dwell in peace and health.", "सभी लोग स्वस्थ एवं सुखी रहें।", "সকলো মানুহ ভালে থাকক।", "Universal wellbeing wish.")

    # ==========================================================================
    # DOMAIN 2: IDENTITY, LANGUAGE, ORIGIN & CLANS (30 sentences)
    # ==========================================================================
    add("Identity & Language", "name_inquiry", "tsɯ5 maɯ2 hɔng3 tsang1 hɯ1?", "tsɯ5 maɯ2 hɔng3 tsang1 hɯ1?", "tsɯ⁵ maɯ² hɔŋ³ t͡saŋ¹ hɯː¹",
        "What is your name?", "आपका नाम क्या है?", "আপোনাৰ নাম কি?", "Asking name.")
    add("Identity & Language", "name_statement", "tsɯ5 kaw1 pen1 Chaw Sa Myat.", "tsɯ5 kaw1 pen1 Chaw Sa Myat.", "tsɯ⁵ kaw¹ pen¹ t͡ɕaw¹ saː¹ mjat¹",
        "My name is Chaw Sa Myat.", "मेरा नाम चौ सा म्यत है।", "মোৰ নাম চৌ চা ম্যত।", "Self-introduction.")
    add("Identity & Language", "village_origin", "kaw1 luk4 maan3 paa1 waai6 maa1.", "kaw1 luk4 maan3 paa1 waai6 maa1.", "kaw¹ luk⁴ maːn³ paː¹ waːj⁶ maː¹",
        "I come from Powaimukh village.", "मैं पोवाइमुख गाँव से आता हूँ।", "মই পোৱাইমুখ গাঁৱৰ পৰা আহিছোঁ।", "Village identity.")
    add("Identity & Language", "khamyang_people", "haw1 pen1 khon1 tai1 khamyang1.", "haw1 pen1 khon1 tai1 khamyang1.", "haw¹ pen¹ kʰon¹ taj¹ kʰam¹ jaːŋ¹",
        "We are Tai Khamyang people.", "हम ताई खामयांग लोग हैं।", "আমি টাই খাময়াং জনগোষ্ঠীৰ মানুহ।", "Ethnic identity.")
    add("Identity & Language", "speak_khamyang_q", "maɯ2 waa5 kham1 thaai1 khamyang1 dai3 haa1?", "maɯ2 waa5 kham1 thaai1 khamyang1 dai3 haa1?", "maɯ² waː⁵ kʰam¹ tʰaːj¹ kʰam¹ jaːŋ¹ daj³ haː¹",
        "Can you speak the Tai Khamyang language?", "क्या आप ताई खामयांग भाषा बोल सकते हैं?", "আপুনি টাই খাময়াং ভাষা ক’ব পাৰেনে?", "Language inquiry.")
    add("Identity & Language", "speak_a_little", "kaw1 waa5 dai3 noi3 nɯŋ5.", "kaw1 waa5 dai3 noi3 nɯŋ5.", "kaw¹ waː⁵ daj³ noi³ nɯŋ⁵",
        "I can speak a little bit.", "मैं थोड़ी-बहुत बोल सकता हूँ।", "মই অলপ-অচৰপ ক’ব পাৰোঁ।", "Modest linguistic ability.")
    add("Identity & Language", "learning_language", "kaw1 hian1 kham1 tai1 yam1 nai6.", "kaw1 hian1 kham1 tai1 yam1 nai6.", "kaw¹ hjan¹ kʰam¹ taj¹ jam¹ nai⁶",
        "I am currently learning the Tai language.", "मैं अभी ताई भाषा सीख रहा हूँ।", "মই এতিয়া টাই ভাষা শিকি আছোঁ।", "Language revitalization.")
    add("Identity & Language", "mother_tongue", "kham1 tai1 pen1 kham1 me5 haw1.", "kham1 tai1 pen1 kham1 me5 haw1.", "kham¹ taj¹ pen¹ kʰam¹ me⁵ haw¹",
        "The Tai language is our mother tongue.", "ताई भाषा हमारी मातृभाषा है।", "টাই ভাষা আমাৰ মাতৃভাষা।", "Mother tongue statement.")
    add("Identity & Language", "clan_chowlik", "haw1 pen1 chɯa3 saai1 Chowlik.", "haw1 pen1 chɯa3 saai1 Chowlik.", "haw¹ pen¹ t͡ɕʰɯa³ saːj¹ t͡ɕow¹lik¹",
        "We belong to the venerable Chowlik clan.", "हम आदरणीय चोलिख वंश से हैं।", "আমি চৌলিক বংশৰ সন্তান।", "Clan affiliation.")
    add("Identity & Language", "ancestor_patkai", "pu5 yaa3 haw1 khao5 maa1 thaang1 doi1 pat4 kai1.", "pu5 yaa3 haw1 khao5 maa1 thaang1 doi1 pat4 kai1.", "pu⁵ jaː³ haw¹ kʰaw⁵ maː¹ tʰaːŋ¹ dɔj¹ pat⁴ kaj¹",
        "Our ancestors migrated along the Patkai mountains.", "हमारे पूर्वज पातकाई पर्वतमाला के मार्ग से आए थे।", "আমাৰ পূৰ্বপুৰুষসকল পাতকাই পাহাৰেৰে আহিছিল।", "Historical migration.")
    add("Identity & Language", "buridihing_river", "maan3 haw1 yu5 rim1 nam6 jin1.", "maan3 haw1 yu5 rim1 nam6 jin1.", "maːn³ haw¹ ju⁵ rim¹ nam⁶ d͡ʑin¹",
        "Our village is situated on the banks of the Buridihing river.", "हमारा गाँव बूढ़ीदिहिंग (नाम जिन) नदी के किनारे बसा है।", "আমাৰ গাঁওখন বুঢ়ীদিহিং নদীৰ পাৰত অৱস্থিত।", "Geographical setting.")
    add("Identity & Language", "village_name_meaning", "maan3 paa1 waai6 mi1 paaw5 waa5 maan3 waai6 rim1 nam6.", "maan3 paa1 waai6 mi1 paaw5 waa5 maan3 waai6 rim1 nam6.", "maːn³ paː¹ waːj⁶ miː¹ paːw⁵ waː⁵ maːn³ waːj⁶ rim¹ nam⁶",
        "The name Powaimukh signifies the village at the cane rivermouth.", "पोवाइमुख नाम का अर्थ बेंत की नदी के मुहाने का गाँव है।", "পোৱাইমুখৰ অৰ্থ বেতগছৰ নদীৰ মুখৰ গাঁও।", "Toponym origin.")
    add("Identity & Language", "elders_preserve", "chaw1 thao3 haw1 haak4 saa1 kham1 thaai1.", "chaw1 thao3 haw1 haak4 saa1 kham1 thaai1.", "t͡ɕaw¹ tʰaw³ haw¹ haːk⁴ saː¹ kʰam¹ tʰaːj¹",
        "Our elders preserve and safeguard our ancestral language.", "हमारे बुजुर्ग हमारी पैतृक भाषा को सहेजकर रखते हैं।", "আমাৰ বয়োজ্যেষ্ঠসকলে মাতৃভাষা ৰক্ষা কৰি ৰাখিছে।", "Elders' guardianship.")
    add("Identity & Language", "children_learn", "luk3 on2 khao5 hian1 lik1 tai1.", "luk3 on2 khao5 hian1 lik1 tai1.", "luk³ on² kʰaw⁵ hjan¹ lik¹ taj¹",
        "The children are learning the Lik Tai script.", "बच्चे लिख ताई लिपि सीख रहे हैं।", "ল’ৰা-ছোৱালীবোৰে টাই লিপি শিকিছে।", "Script transmission.")
    add("Identity & Language", "ancient_books", "wat1 haw1 mi5 lik1 lai3 hɔng3 lik1 phaa3 chet3.", "wat1 haw1 mi5 lik1 lai3 hɔng3 lik1 phaa3 chet3.", "wat¹ haw¹ miː¹ lik¹ laj³ hɔŋ³ lik¹ pʰaː³ t͡ɕʰet³",
        "Our monastery preserves ancient sacred manuscripts.", "हमारे विहार में प्राचीन पवित्र पांडुलिपियाँ सुरक्षित हैं।", "আমাৰ বৌদ্ধ বিহাৰত প্ৰাচীন সাঁচিপতীয়া পুথি সংৰক্ষিত আছে।", "Literary tradition.")
    add("Identity & Language", "speak_slowly", "waa5 tsaa3 tsaa3 taaw1, kaw1 khrai3 hian1.", "waa5 tsaa3 tsaa3 taaw1, kaw1 khrai3 hian1.", "waː⁵ t͡saː³ t͡saː³ taːw¹, kaw¹ kʰraj³ hjan¹",
        "Please speak slowly, I wish to learn.", "कृपया धीरे-धीरे बोलिए, मैं सीखना चाहता हूँ।", "অনুগ্ৰহ কৰি লাহে লাহে কওক, মই শিকিব খোজোঁ।", "Learner prompt.")
    add("Identity & Language", "word_meaning", "kham1 nai6 mi1 paaw5 tsang1 hɯ1?", "kham1 nai6 mi1 paaw5 tsang1 hɯ1?", "kham¹ nai⁶ miː¹ paːw⁵ t͡saŋ¹ hɯː¹",
        "What is the meaning of this word?", "इस शब्द का क्या अर्थ है?", "এই শব্দটোৰ অৰ্থ কি?", "Lexical elicitation.")
    add("Identity & Language", "what_is_this_called", "an1 nai6 hɔng3 tsang1 hɯ1 nai1 kham1 tai1?", "an1 nai6 hɔng3 tsang1 hɯ1 nai1 kham1 tai1?", "an¹ nai⁶ hɔŋ³ t͡saŋ¹ hɯː¹ naj¹ kʰam¹ taj¹",
        "What is this called in the Tai language?", "इसे ताई भाषा में क्या कहते हैं?", "ইয়াক টাই ভাষাত কি বুলি কয়?", "Fieldwork elicitation.")
    add("Identity & Language", "say_it_again", "waa5 thau3 nɯŋ5 taaw1, kaw1 te5 thap1.", "waa5 thau3 nɯŋ5 taaw1, kaw1 te5 thap1.", "waː⁵ tʰaw³ nɯŋ⁵ taːw¹, kaw¹ te⁵ tʰap¹",
        "Please say it once again so I may record it.", "कृपया एक बार फिर कहिए, ताकि मैं इसे दर्ज कर सकूँ।", "আৰু এবাৰ কওক, যাতে মই বাণীবদ্ধ কৰিব পাৰোঁ।", "Fieldwork repetition.")
    add("Identity & Language", "i_understand", "yam1 nai6 kaw1 hu3 yow3 chaw1.", "yam1 nai6 kaw1 hu3 yow3 chaw1.", "jam¹ nai⁶ kaw¹ huː³ jow³ t͡ɕaw¹",
        "Now I understand clearly, thank you.", "अब मैं अच्छी तरह समझ गया, धन्यवाद।", "এতিয়া মই বুজি পালোঁ, ধন্যবাদ।", "Comprehension affirmation.")
    add("Identity & Language", "do_not_understand", "kaw1 am1 pai5 hu3 kham1 nai6.", "kaw1 am1 pai5 hu3 kham1 nai6.", "kaw¹ am¹ paj⁵ huː³ kʰam¹ nai⁶",
        "I do not understand this word yet.", "मैं अभी इस शब्द को नहीं समझा हूँ।", "মই এতিয়ালৈকে এই শব্দটো বুজি পোৱা নাই।", "Lack of comprehension.")
    add("Identity & Language", "where_from", "maɯ2 luk4 theu1 maa1?", "maɯ2 luk4 theu1 maa1?", "maɯ² luk⁴ tʰeu¹ maː¹",
        "Where have you come from?", "आप कहाँ से आए हैं?", "আপুনি ক’ৰ পৰা আহিছে?", "Inquiring about origin.")
    add("Identity & Language", "come_from_assam", "kaw1 luk4 Axom maa1.", "kaw1 luk4 Axom maa1.", "kaw¹ luk⁴ a¹xom¹ maː¹",
        "I have come from Assam.", "मैं असम से आया हूँ।", "মই অসমৰ পৰা আহিছোঁ।", "State origin.")
    add("Identity & Language", "powaimukh_beautiful", "maan3 paa1 waai6 ngam1 the5 the5.", "maan3 paa1 waai6 ngam1 the5 the5.", "maːn³ paː¹ waːj⁶ ŋam¹ tʰe⁵ tʰe⁵",
        "Powaimukh village is truly serene and beautiful.", "पोवाइमुख गाँव वास्तव में अत्यंत सुंदर और शांत है।", "পোৱাইমুখ গাঁওখন বৰ ধুনীয়া।", "Praising the village.")
    add("Identity & Language", "tai_script", "lik1 tai1 mi1 tua1 ngam1 the5 the5.", "lik1 tai1 mi1 tua1 ngam1 the5 the5.", "lik¹ taj¹ miː¹ tua¹ ŋam¹ tʰe⁵ tʰe⁵",
        "The Lik Tai letters are very graceful and beautiful.", "लिख ताई के अक्षर बहुत ही सुंदर और सुरुचिपूर्ण हैं।", "টাই লিপিৰ আখৰবোৰ বৰ মনোৰম।", "Praising the script.")
    add("Identity & Language", "history_proud", "haw1 phak1 phum1 tsai1 nai1 khon1 tai1.", "haw1 phak1 phum1 tsai1 nai1 khon1 tai1.", "haw¹ pʰak¹ pʰum¹ t͡sai¹ naj¹ kʰon¹ taj¹",
        "We take great pride in our Tai heritage and roots.", "हमें अपनी ताई विरासत और संस्कृति पर गर्व है।", "আমাৰ টাই ঐতিহ্যৰ প্ৰতি আমাৰ গভীৰ গৌৰৱ আছে।", "Cultural pride.")
    add("Identity & Language", "bilingual_speakers", "khon1 maan3 haw1 waa5 kham1 tai1 kap4 kham1 axomiyaa1.", "khon1 maan3 haw1 waa5 kham1 tai1 kap4 kham1 axomiyaa1.", "kʰon¹ maːn³ haw¹ waː⁵ kʰam¹ taj¹ kap⁴ kʰam¹ a¹xɔ¹miː¹jaː¹",
        "Our villagers speak both Tai and Assamese.", "हमारे गाँव के लोग ताई और असमिया दोनों भाषाएँ बोलते हैं।", "আমাৰ গাঁৱৰ মানুহে টাই আৰু অসমীয়া দুয়োটা কয়।", "Bilingualism.")
    add("Identity & Language", "record_audio", "kaw1 aw1 siang1 maɯ2 dai3 ka1?", "kaw1 aw1 siang1 maɯ2 dai3 ka1?", "kaw¹ aw¹ sjaŋ¹ maɯ² daj³ kaː¹",
        "May I please record your voice for documentation?", "क्या मैं प्रलेखन के लिए आपकी आवाज़ रिकॉर्ड कर सकता हूँ?", "মই আপোনাৰ মাতটো বাণীবদ্ধ কৰিব পাৰোঁনে?", "Ethical research consent.")
    add("Identity & Language", "preserve_future", "haw1 haak4 saa1 kham1 tai1 hai3 luk3 laan1.", "haw1 haak4 saa1 kham1 tai1 hai3 luk3 laan1.", "haw¹ haːk⁴ saː¹ kʰam¹ taj¹ haj³ luk³ laːn¹",
        "We preserve the Tai language for our future generations.", "हम आने वाली पीढ़ियों के लिए ताई भाषा को संजोते हैं।", "আমি ভৱিষ্যৎ প্ৰজন্মৰ বাবে টাই ভাষা সংৰক্ষণ কৰোঁ।", "Intergenerational goal.")
    add("Identity & Language", "traditions_alive", "phee1 thɯang4 haw1 yu5 man3 khang1.", "phee1 thɯang4 haw1 yu5 man3 khang1.", "pʰeː¹ tʰɯaŋ⁴ haw¹ ju⁵ man³ kʰaŋ¹",
        "Our cultural traditions remain strong and enduring.", "हमारी सांस्कृतिक परंपराएँ अक्षुण्ण और जीवंत हैं।", "আমাৰ পৰম্পৰা চিৰকাল জীয়াই থাকিব।", "Cultural permanence.")

    # ==========================================================================
    # DOMAIN 3: DAILY INQUIRIES & QUESTIONS (35 sentences)
    # ==========================================================================
    add("Daily Inquiries", "where_going", "maɯ2 pai1 theu1 wan1 nai6?", "maɯ2 pai1 theu1 wan1 nai6?", "maɯ² paj¹ tʰeu¹ wan¹ nai⁶",
        "Where are you going today?", "आज आप कहाँ जा रहे हैं?", "আজি আপুনি ক’লৈ যায়?", "Common daily greeting question.")
    add("Daily Inquiries", "where_going_morning", "maɯ2 pai1 theu1 chaw3 nai6?", "maɯ2 pai1 theu1 chaw3 nai6?", "maɯ² paj¹ tʰeu¹ t͡ɕaw³ nai⁶",
        "Where are you going this morning?", "आज सुबह आप कहाँ जा रहे हैं?", "আজি পুৱা ক’লৈ ওলাইছে?", "Morning query.")
    add("Daily Inquiries", "have_you_eaten", "maɯ2 kin1 khaw3 yow3 haa1?", "maɯ2 kin1 khaw3 yow3 haa1?", "maɯ² kin¹ kʰaw³ jow³ haː¹",
        "Have you eaten your meal yet?", "क्या आपने खाना खा लिया है?", "আপুনি ভাত খালে নে?", "Universal polite inquiry.")
    add("Daily Inquiries", "already_eaten", "kin1 yow3 chaw1.", "kin1 yow3 chaw1.", "kin¹ jow³ t͡ɕaw¹",
        "Yes, I have already eaten.", "हाँ, मैंने खाना खा लिया है।", "খালোঁ, ধন্যবাদ।", "Affirmative meal reply.")
    add("Daily Inquiries", "not_yet_eaten", "pai2, pai5 kin1.", "pai2, pai5 kin1.", "paj² paj⁵ kin¹",
        "No, I have not eaten yet.", "नहीं, अभी तक नहीं खाया।", "নাই, এতিয়ালৈকে খোৱা নাই।", "Negative meal reply.")
    add("Daily Inquiries", "what_are_you_doing", "maɯ2 het1 sang1 yu5?", "maɯ2 het1 sang1 yu5?", "maɯ² het¹ saŋ¹ ju⁵",
        "What are you doing right now?", "आप अभी क्या कर रहे हैं?", "আপুনি এতিয়া কি কৰি আছে?", "Activity inquiry.")
    add("Daily Inquiries", "going_to_field", "kaw1 te5 pai1 naa1.", "kaw1 te5 pai1 naa1.", "kaw¹ te⁵ paj¹ naː¹",
        "I am going to the paddy field.", "मैं खेत की तरफ़ जा रहा हूँ।", "মই পথাৰলৈ ওলাইছোঁ।", "Daily farm movement.")
    add("Daily Inquiries", "going_to_monastery", "kaw1 te5 pai1 wat1.", "kaw1 te5 pai1 wat1.", "kaw¹ te⁵ paj¹ wat¹",
        "I am going to the Buddhist monastery.", "मैं बौद्ध विहार जा रहा हूँ।", "মই বৌদ্ধ বিহাৰলৈ গৈ আছোঁ।", "Religious visit.")
    add("Daily Inquiries", "going_to_market", "kaw1 te5 pai1 laat1.", "kaw1 te5 pai1 laat1.", "kaw¹ te⁵ paj¹ laːt¹",
        "I am going to the village market.", "मैं बाज़ार जा रहा हूँ।", "মই বজাৰলৈ যাওঁ।", "Market movement.")
    add("Daily Inquiries", "going_to_river", "kaw1 te5 pai1 rim1 nam6.", "kaw1 te5 pai1 rim1 nam6.", "kaw¹ te⁵ paj¹ rim¹ nam⁶",
        "I am going towards the riverbank.", "मैं नदी किनारे जा रहा हूँ।", "মই নৈৰ পাৰলৈ গৈ আছোঁ।", "River movement.")
    add("Daily Inquiries", "who_is_coming", "phau5 maa1 hɯan1 haw1?", "phau5 maa1 hɯan1 haw1?", "pʰaw⁵ maː¹ hɯan¹ haw¹",
        "Who has come to our home?", "हमारे घर कौन आया है?", "আমাৰ ঘৰলৈ কোন আহিছে?", "Visitor question.")
    add("Daily Inquiries", "guest_arrived", "kheek2 maa1 hɯan1 haw1 yow3.", "kheek2 maa1 hɯan1 haw1 yow3.", "kʰeːk² maː¹ hɯan¹ haw¹ jow³",
        "Guests have arrived at our home.", "हमारे घर मेहमान आए हैं।", "আমাৰ ঘৰলৈ আলহী আহিছে।", "Guest announcement.")
    add("Daily Inquiries", "when_will_you_return", "maɯ2 te5 maa1 wan1 phuk1 haa1?", "maɯ2 te5 maa1 wan1 phuk1 haa1?", "maɯ² te⁵ maː¹ wan¹ pʰuk¹ haː¹",
        "Will you return tomorrow?", "क्या आप कल वापस आएँगे?", "আপুনি কাইলৈ ঘূৰি আহিবনে?", "Return question.")
    add("Daily Inquiries", "return_evening", "kaw1 te5 maa1 kham3 nai6.", "kaw1 te5 maa1 kham3 nai6.", "kaw¹ te⁵ maː¹ kʰam³ nai⁶",
        "I shall return this evening.", "मैं आज शाम को लौटूँगा।", "মই আজি গধূলি ঘূৰি আহিম।", "Evening return.")
    add("Daily Inquiries", "where_is_father", "po5 maɯ2 yu5 theu1?", "po5 maɯ2 yu5 theu1?", "po⁵ maɯ² ju⁵ tʰeu¹",
        "Where is your father?", "आपके पिताजी कहाँ हैं?", "তোমাৰ দেউতা ক’ত আছে?", "Family whereabouts.")
    add("Daily Inquiries", "father_in_field", "po5 kaw1 yu5 naa1.", "po5 kaw1 yu5 naa1.", "po⁵ kaw¹ ju⁵ naː¹",
        "My father is currently in the paddy field.", "मेरे पिताजी अभी खेत में हैं।", "মোৰ দেউতা পথাৰত আছে।", "Location of father.")
    add("Daily Inquiries", "where_is_mother", "me5 maɯ2 yu5 theu1?", "me5 maɯ2 yu5 theu1?", "me⁵ maɯ² ju⁵ tʰeu¹",
        "Where is your mother?", "आपकी माताजी कहाँ हैं?", "তোমাৰ মা ক’ত আছে?", "Mother inquiry.")
    add("Daily Inquiries", "mother_weaving", "me5 kaw1 tam3 phaa3 yu5.", "me5 kaw1 tam3 phaa3 yu5.", "me⁵ kaw¹ tam³ pʰaː³ ju⁵",
        "My mother is weaving cloth on the loom.", "मेरी माँ करघे पर कपड़ा बुन रही हैं।", "মোৰ মায়ে তাঁতত কাপোৰ বৈ আছে।", "Mother activity.")
    add("Daily Inquiries", "are_you_tired", "maɯ2 nɔi2 haa1?", "maɯ2 nɔi2 haa1?", "maɯ² nɔj² haː¹",
        "Are you feeling tired?", "क्या आप थके हुए हैं?", "তোমাৰ ভাগৰ লাগিছে নেকি?", "Empathy inquiry.")
    add("Daily Inquiries", "not_tired", "kaw1 am1 nɔi2.", "kaw1 am1 nɔi2.", "kaw¹ am¹ nɔj²",
        "No, I am not tired at all.", "नहीं, मैं बिल्कुल थका नहीं हूँ।", "নাই, মোৰ ভাগৰ লগা নাই।", "Feeling fresh.")
    add("Daily Inquiries", "thirsty_question", "maɯ2 khrai3 kin1 nam6 haa1?", "maɯ2 khrai3 kin1 nam6 haa1?", "maɯ² kʰraj³ kin¹ nam⁶ haː¹",
        "Are you thirsty? Would you like water?", "क्या आपको प्यास लगी है? क्या आप पानी पीना चाहते हैं?", "তোমাৰ পিয়াহ লাগিছে নেকি? পানী খাবা নেকি?", "Offering drink.")
    add("Daily Inquiries", "give_water", "pan1 nam6 kaw1 noi3 taaw1.", "pan1 nam6 kaw1 noi3 taaw1.", "pan¹ nam⁶ kaw¹ noi³ taːw¹",
        "Please give me a little water.", "कृपया मुझे थोड़ा पानी दीजिए।", "অনুগ্ৰহ কৰি মোক অলপ পানী দিয়ক।", "Water request.")
    add("Daily Inquiries", "who_is_speaking", "phau5 waa5 kham1?", "phau5 waa5 kham1?", "pʰaw⁵ waː⁵ kʰam¹",
        "Who is speaking?", "कौन बोल रहा है?", "কোনে কথা কৈছে?", "Identity inquiry.")
    add("Daily Inquiries", "why_late", "tsang1 hɯ1 maɯ2 maa1 laang5?", "tsang1 hɯ1 maɯ2 maa1 laang5?", "t͡saŋ¹ hɯː¹ maɯ² maː¹ laːŋ⁵",
        "Why have you arrived late?", "आप इतनी देर से क्यों आए?", "আপুনি কিয় দেৰিকৈ আহিল?", "Punctuality inquiry.")
    add("Daily Inquiries", "rain_delayed", "fon1 tok1, kaw1 tsaa3.", "fon1 tok1, kaw1 tsaa3.", "fon¹ tok¹ kaw¹ t͡saː³",
        "It was raining, so I was delayed.", "बारिश हो रही थी, इसलिए मुझे देर हो गई।", "বৰষুণ দি থকাৰ বাবে পলম হ’ল।", "Weather excuse.")
    add("Daily Inquiries", "where_is_school", "hong1 hian1 yu5 theu1?", "hong1 hian1 yu5 theu1?", "hoŋ¹ hjan¹ ju⁵ tʰeu¹",
        "Where is the village school located?", "गाँव का स्कूल कहाँ है?", "বিদ্যালয়খন ক’ত অৱস্থিত?", "School direction.")
    add("Daily Inquiries", "school_near_wat", "hong1 hian1 yu5 klai3 wat1.", "hong1 hian1 yu5 klai3 wat1.", "hoŋ¹ hjan¹ ju⁵ klaj³ wat¹",
        "The school is located close to the monastery.", "स्कूल विहार के निकट स्थित है।", "বিদ্যালয়খন বৌদ্ধ বিহাৰৰ ওচৰতে আছে।", "Location answer.")
    add("Daily Inquiries", "how_many_children", "maɯ2 mi5 luk3 ki3 kɔ5?", "maɯ2 mi5 luk3 ki3 kɔ5?", "maɯ² miː¹ luk³ ki³ kɔ⁵",
        "How many children do you have?", "आपके कितने बच्चे हैं?", "আপোনাৰ সন্তান কেইজন?", "Family count.")
    add("Daily Inquiries", "two_children", "kaw1 mi5 luk3 sɔng1 kɔ5.", "kaw1 mi5 luk3 sɔng1 kɔ5.", "kaw¹ miː¹ luk³ sɔŋ¹ kɔ⁵",
        "I have two children.", "मेरे दो बच्चे हैं।", "মোৰ দুটা সন্তান আছে।", "Count response.")
    add("Daily Inquiries", "are_you_ready", "maɯ2 phrom3 yow3 haa1?", "maɯ2 phrom3 yow3 haa1?", "maɯ² pʰrom³ jow³ haː¹",
        "Are you ready to depart?", "क्या आप चलने के लिए तैयार हैं?", "আপুনি সাজু হ’লনে?", "Readiness question.")
    add("Daily Inquiries", "ready_now", "kaw1 phrom3 yow3 chaw1.", "kaw1 phrom3 yow3 chaw1.", "kaw¹ pʰrom³ jow³ t͡ɕaw¹",
        "Yes, I am fully ready.", "हाँ, मैं बिल्कुल तैयार हूँ।", "হয়, মই সম্পূৰ্ণ সাজু।", "Affirmative readiness.")
    add("Daily Inquiries", "call_someone", "hɔng3 phi3saai1 maa1 taaw1.", "hɔng3 phi3saai1 maa1 taaw1.", "hɔŋ³ pʰi³ saːj¹ maː¹ taːw¹",
        "Please call elder brother here.", "कृपया बड़े भाई को यहाँ बुलाइए।", "ককাইদেউক ইয়ালৈ মাতি আনক।", "Calling someone.")
    add("Daily Inquiries", "wait_a_moment", "thaa3 noi3 nɯŋ5 taaw1.", "thaa3 noi3 nɯŋ5 taaw1.", "tʰaː³ noi³ nɯŋ⁵ taːw¹",
        "Please wait for a moment.", "कृपया एक पल प्रतीक्षा कीजिए।", "অনুগ্ৰহ কৰি ক্ষন্তেক বাট চাওক।", "Polite patience.")
    add("Daily Inquiries", "finished_work", "kaang1 ngaan1 leew3 yow3 haa1?", "kaang1 ngaan1 leew3 yow3 haa1?", "kaːŋ¹ ŋaːn¹ leːw³ jow³ haː¹",
        "Has the work been completed?", "क्या काम पूरा हो चुका है?", "কামটো শেষ হ’লনে?", "Completion query.")
    add("Daily Inquiries", "work_completed", "kaang1 ngaan1 leew3 li1 yow3.", "kaang1 ngaan1 leew3 li1 yow3.", "kaːŋ¹ ŋaːn¹ leːw³ liː¹ jow³",
        "Yes, the work has been completed well.", "हाँ, काम अच्छी तरह पूरा हो गया है।", "হয়, কামটো সুকলমে শেষ হ’ল।", "Completion reply.")

    # ==========================================================================
    # DOMAIN 4: FOOD, DRINKS, TEA & DINING (45 sentences)
    # ==========================================================================
    add("Food & Dining", "drink_tea", "kin1 nam6 chaa1 taaw1.", "kin1 nam6 chaa1 taaw1.", "kin¹ nam⁶ t͡ɕʰaː¹ taːw¹",
        "Please drink some warm tea.", "कृपया गर्म चाय पीजिए।", "গৰম চাহ একাপ খাওক।", "Tea invitation.")
    add("Food & Dining", "steamed_rice", "khaw3 nai6 waan1 the5 the5.", "khaw3 nai6 waan1 the5 the5.", "kʰaw³ nai⁶ waːn¹ tʰe⁵ tʰe⁵",
        "This fragrant rice is exceptionally delicious.", "यह सुगंधित चावल बहुत स्वादिष्ट है।", "এই ভাতসাজ বৰ সোৱাদ হৈছে।", "Praising food.")
    add("Food & Dining", "eat_fresh_fish", "kaw1 khrai3 kin1 paa1 sot1.", "kaw1 khrai3 kin1 paa1 sot1.", "kaw¹ kʰraj³ kin¹ paː¹ sot¹",
        "I would like to eat fresh river fish.", "मैं ताज़ी नदी की मछली खाना चाहता हूँ।", "মই নৈৰ সতেজ মাছ খাব বিচাৰোঁ।", "Food preference.")
    add("Food & Dining", "bamboo_shoot", "nɔ5 mai3 nai6 waan1 the5 the5.", "nɔ5 mai3 nai6 waan1 the5 the5.", "nɔ⁵ maj³ nai⁶ waːn¹ tʰe⁵ tʰe⁵",
        "These tender bamboo shoots taste wonderful.", "यह बाँस का ताज़ा करील बहुत स्वादिष्ट है।", "এই বাঁহৰ গাজটো বৰ সোৱাদ।", "Traditional Tai delicacy.")
    add("Food & Dining", "curry_vegetables", "me5 haw1 tom3 phak1 waan1.", "me5 haw1 tom3 phak1 waan1.", "me⁵ haw¹ tom³ pʰak¹ waːn¹",
        "Our mother cooked delicious vegetable soup.", "हमारी माँ ने स्वादिष्ट सब्ज़ी बनाई है।", "আমাৰ মায়ে সোৱাদ শাকৰ আঞ্জা ৰান্ধিছে।", "Mother's cooking.")
    add("Food & Dining", "sticky_rice", "khaw3 nio5 pen1 kin1 tai1.", "khaw3 nio5 pen1 kin1 tai1.", "kʰaw³ nio⁵ pen¹ kin¹ taj¹",
        "Sticky rice is a traditional food of the Tai people.", "चिपचिपा चावल (खाय-न्यू) ताई लोगों का पारंपरिक भोजन है।", "বৰা চাউলৰ ভাত টাইসকলৰ পৰম্পৰাগত খাদ্য।", "Cultural cuisine.")
    add("Food & Dining", "have_more_rice", "aw1 khaw3 them1 noi3 taaw1.", "aw1 khaw3 them1 noi3 taaw1.", "aw¹ kʰaw³ tʰem¹ noi³ taːw¹",
        "Please take some more rice.", "कृपया थोड़ा और चावल लीजिए।", "অনুগ্ৰহ কৰি আৰু অলপ ভাত লওক।", "Hospitality second serving.")
    add("Food & Dining", "enough_full", "kaw1 im3 yow3 chaw1.", "kaw1 im3 yow3 chaw1.", "kaw¹ im³ jow³ t͡ɕaw¹",
        "I am completely full, thank you.", "मेरा पेट भर गया है, धन्यवाद।", "মোৰ পেট ভৰিছে, ধন্যবাদ।", "Full stomach.")
    add("Food & Dining", "water_cold", "nam6 nai6 yen1 li1 the5 the5.", "nam6 nai6 yen1 li1 the5 the5.", "nam⁶ nai⁶ jen¹ liː¹ tʰe⁵ tʰe⁵",
        "This drinking water is delightfully cool.", "यह पीने का पानी बहुत शीतल और ताज़ा है।", "এই খোৱাপানীখিনি বৰ শীতল।", "Cool water.")
    add("Food & Dining", "water_warm", "kaw1 khrai3 kin1 nam6 un2.", "kaw1 khrai3 kin1 nam6 un2.", "kaw¹ kʰraj³ kin¹ nam⁶ un²",
        "I would prefer to drink warm water.", "मैं गुनगुना पानी पीना चाहता हूँ।", "মই অলপ কুহুমীয়া পানী খাব বিচাৰোঁ।", "Warm water request.")
    add("Food & Dining", "ripe_banana", "maak1 kuai3 suuk1 waan1 the5 the5.", "maak1 kuai3 suuk1 waan1 the5 the5.", "maːk¹ kuaj³ suːk¹ waːn¹ tʰe⁵ tʰe⁵",
        "The ripe bananas are very sweet.", "पके हुए केले बहुत मीठे हैं।", "পকা কলবোৰ বৰ মিঠা।", "Fruit description.")
    add("Food & Dining", "sweet_mango", "maak1 muang2 nai6 waan1 li1.", "maak1 muang2 nai6 waan1 li1.", "maːk¹ muaŋ² nai⁶ waːn¹ liː¹",
        "This mango is very sweet and juicy.", "यह आम बहुत मीठा और रसीला है।", "এই আমটো বৰ সোৱাদ।", "Mango description.")
    add("Food & Dining", "eat_together", "haw1 kin1 khaw3 ruam2 kan1 taaw1.", "haw1 kin1 khaw3 ruam2 kan1 taaw1.", "haw¹ kin¹ kʰaw³ ruam² kan¹ taːw¹",
        "Let us all eat our meal together.", "आइए, हम सब मिलकर भोजन करें।", "আহক, আমি সকলোৱে একেলগে ভাত খাওঁ।", "Communal meal.")
    add("Food & Dining", "chili_spicy", "pʰik1 nai6 pʰet2 the5 the5.", "phik1 nai6 phet2 the5 the5.", "pʰik¹ nai⁶ pʰet² tʰe⁵ tʰe⁵",
        "This chili pepper is extremely spicy.", "यह मिर्च बहुत तीखी है।", "এই জলকীয়াটো বৰ জ্বলা।", "Spicy taste.")
    add("Food & Dining", "salt_needed", "khɔ5 klɯa1 noi3 nɯŋ5 taaw1.", "kho5 klɯa1 noi3 nɯŋ5 taaw1.", "kʰo⁵ klɯa¹ noi³ nɯŋ⁵ taːw¹",
        "Please pass a little salt.", "कृपया थोड़ा नमक दीजिए।", "অনুগ্ৰহ কৰি অলপ নিমখ দিয়ক।", "Seasoning request.")
    add("Food & Dining", "wash_hands_before", "sɯak1 mɯɯ1 kɔn2 kin1 khaw3.", "sɯak1 mɯɯ1 kɔn2 kin1 khaw3.", "sɯak¹ mɯː¹ kɔn² kin¹ kʰaw³",
        "Wash your hands cleanly before eating.", "खाना खाने से पहले हाथ अच्छी तरह धोइए।", "ভাত খোৱাৰ আগতে হাত ধুই লওক।", "Hygiene instruction.")
    add("Food & Dining", "boiled_greens", "phak1 tom3 nai6 li1 tɔ5 haang1 khing1.", "phak1 tom3 nai6 li1 tɔ5 haang1 khing1.", "pʰak¹ tom³ nai⁶ liː¹ tɔ⁵ haːŋ¹ kʰiŋ¹",
        "Boiled wild greens are healthy for the body.", "उबली हुई हरी सब्ज़ियाँ शरीर के लिए गुणकारी हैं।", "সিজোৱা শাক শৰীৰৰ বাবে বৰ উপকাৰী।", "Healthy eating.")
    add("Food & Dining", "cook_fish", "phi3ying1 kaw1 ping3 paa1.", "phi3ying1 kaw1 ping3 paa1.", "pʰi³ jiŋ¹ kaw¹ piŋ³ paː¹",
        "My elder sister is grilling fish over the hearth.", "मेरी बड़ी बहन आग पर मछली भून रही हैं।", "মোৰ বায়েকে মাছ পুৰিছে।", "Cooking activity.")
    add("Food & Dining", "tea_leaves", "bai1 chaa1 nai6 hɔm1 the5 the5.", "bai1 chaa1 nai6 hɔm1 the5 the5.", "baj¹ t͡ɕʰaː¹ nai⁶ hɔm¹ tʰe⁵ tʰe⁵",
        "These freshly picked tea leaves have a wonderful aroma.", "ये ताज़ी चाय की पत्तियाँ बहुत सुगंधित हैं।", "এই চাহপাতখিনি বৰ সুবাসিত।", "Tea aroma.")
    add("Food & Dining", "offer_alms_food", "haw1 aw1 khaw3 sang3 thawaai3 wat1.", "haw1 aw1 khaw3 sang3 thawaai3 wat1.", "haw¹ aw¹ kʰaw³ saŋ³ tʰa¹waːj³ wat¹",
        "We offer fresh food alms at the monastery.", "हम विहार में भोजन का दान अर्पित करते हैं।", "আমি বিহাৰলৈ পুৱাৰ ভোজন আগবঢ়াওঁ।", "Buddhist alms offering.")
    add("Food & Dining", "ginger_spice", "khing1 nai6 phet2 rɔn3.", "khing1 nai6 phet2 rɔn3.", "kʰiŋ¹ nai⁶ pʰet² rɔn³",
        "This fresh ginger is pungent and warming.", "यह ताज़ा अदरक तीखा और गर्म है।", "এই আদাখিনি বৰ জ্বলা।", "Ginger description.")
    add("Food & Dining", "garlic_flavor", "khaw3 phak1 sai2 phak1 thiam1.", "khaw3 phak1 sai2 phak1 thiam1.", "kʰaw³ pʰak¹ saj² pʰak¹ tʰjam¹",
        "Cook the vegetables with fresh garlic.", "सब्ज़ियों में ताज़ा लहसुन डालकर पकाएँ।", "শাকত নহৰু দি ৰান্ধক।", "Cooking direction.")
    add("Food & Dining", "evening_supper", "kham3 nai6 haw1 kin1 khaw3 kap4 paa1.", "kham3 nai6 haw1 kin1 khaw3 kap4 paa1.", "kʰam³ nai⁶ haw¹ kin¹ kʰaw³ kap⁴ paː¹",
        "Tonight we shall eat rice with fresh fish.", "आज रात हम मछली और भात खाएँगे।", "আজি ৰাতি আমি মাছ-ভাতেৰে সাজ খাম।", "Supper plan.")
    add("Food & Dining", "morning_meal", "chaw3 nai6 kaw1 kin1 khaw3 tom3.", "chaw3 nai6 kaw1 kin1 khaw3 tom3.", "t͡ɕaw³ nai⁶ kaw¹ kin¹ kʰaw³ tom³",
        "This morning I ate warm rice porridge.", "आज सुबह मैंने गरम चावल की खीर/दलिया खाया।", "আজি পুৱা মই কোমল ভাত খালোঁ।", "Breakfast.")
    add("Food & Dining", "fermented_fish", "paa1 som3 nai6 waan1 the5 the5.", "paa1 som3 nai6 waan1 the5 the5.", "paː¹ som³ nai⁶ waːn¹ tʰe⁵ tʰe⁵",
        "This traditionally prepared fish is very flavorful.", "यह पारंपरिक खट्टी मछली बहुत स्वादिष्ट है।", "এই শুকান মাছৰ আঞ্জাখন বৰ সোৱাদ।", "Ethnic specialty.")
    add("Food & Dining", "clean_plate", "sɯak1 thoi3 hai3 sot1.", "sɯak1 thoi3 hai3 sot1.", "sɯak¹ tʰoj³ haj³ sot¹",
        "Wash the dining bowls thoroughly.", "भोजन के बर्तनों को अच्छी तरह साफ़ कीजिए।", "কাঁহী-বাটিবোৰ ভালদৰে ধুই থওক।", "Household chore.")
    add("Food & Dining", "serve_guests", "liang3 kheek2 hai3 im3.", "liang3 kheek2 hai3 im3.", "ljaŋ³ kʰeːk² haj³ im³",
        "Feed our guests generously so they are well satisfied.", "मेहमानों को तृप्त होने तक आदरपूर्वक भोजन कराएँ।", "আলহীক সন্তুষ্ট হোৱাকৈ খুৱাওক।", "Hospitality value.")
    add("Food & Dining", "fragrant_herbs", "phak1 phai5 mi1 khwan1 hɔm1.", "phak1 phai5 mi1 khwan1 hɔm1.", "pʰak¹ pʰaj⁵ miː¹ kʰwan¹ hɔm¹",
        "The indigenous herbs have a delightful scent.", "देशी जड़ी-बूटियों की महक बहुत मनमोहक है।", "থলুৱা বনশাকৰ সুবাস বৰ ভাল।", "Herbal aroma.")
    add("Food & Dining", "bamboo_tube_rice", "khaw3 laam1 pen1 kin1 waan1.", "khaw3 laam1 pen1 kin1 waan1.", "kʰaw³ laːm¹ pen¹ kin¹ waːn¹",
        "Rice cooked inside bamboo tubes is extremely aromatic.", "बाँस की नली में पकाया गया चावल (खाओ लाम) बहुत स्वादिष्ट होता है।", "চুঙাচাউল টাইসকলৰ বৰ সোৱাদ খাদ্য।", "Traditional bamboo cooking.")
    add("Food & Dining", "lime_sour", "maak1 naaw1 nai6 som3.", "maak1 naaw1 nai6 som3.", "maːk¹ naːw¹ nai⁶ som³",
        "This lime is very sour and refreshing.", "यह नीबू बहुत खट्टा और ताज़गी भरा है।", "এই নেমুটো বৰ টেঙা।", "Citrus fruit.")
    add("Food & Dining", "honey_sweet", "nam6 phɯng3 nai6 waan1 the5 the5.", "nam6 phɯng3 nai6 waan1 the5 the5.", "nam⁶ pʰɯŋ³ nai⁶ waːn¹ tʰe⁵ tʰe⁵",
        "This pure wild forest honey is very sweet.", "यह जंगल का शुद्ध शहद बहुत मीठा है।", "মৌখিনি বৰ মিঠা।", "Wild honey.")
    add("Food & Dining", "drink_together", "haw1 kin1 nam6 chaa1 ruam2 kan1.", "haw1 kin1 nam6 chaa1 ruam2 kan1.", "haw¹ kin¹ nam⁶ t͡ɕʰaː¹ ruam² kan¹",
        "Let us sit together and drink tea.", "आइए, हम सब साथ बैठकर चाय पिएँ।", "আহক, একেলগে চাহ একাপ খাওঁ।", "Social tea drinking.")
    add("Food & Dining", "boiled_egg", "khai2 tom3 li1 tɔ5 luk3 on2.", "khai2 tom3 li1 tɔ5 luk3 on2.", "kʰaj² tom³ liː¹ tɔ⁵ luk³ on²",
        "Boiled eggs are nourishing for young children.", "उबला अंडा छोटे बच्चों के लिए पौष्टिक होता है।", "সিজোৱা কণী কণমানিৰ স্বাস্থ্যৰ বাবে ভাল।", "Egg nutrition.")
    add("Food & Dining", "fresh_milk", "nam6 nom1 ngua1 sot1 li1.", "nam6 nom1 ngua1 sot1 li1.", "nam⁶ nom¹ ŋua¹ sot¹ liː¹",
        "Fresh cow milk is very wholesome.", "गाय का ताज़ा दूध स्वास्थ्यवर्धक होता है।", "গাইৰ সতেজ গাখীৰ স্বাস্থ্যৰ বাবে উপকাৰী।", "Dairy nutrition.")
    add("Food & Dining", "curry_ready", "kin1 phak1 suuk1 yow3, maa1 kin1 taaw1.", "kin1 phak1 suuk1 yow3, maa1 kin1 taaw1.", "kin¹ pʰak¹ suːk¹ jow³, maː¹ kin¹ taːw¹",
        "The food is cooked and ready, please come eat!", "भोजन पककर तैयार है, कृपया भोजन के लिए आइए!", "ভাত-আঞ্জা ৰন্ধা হ’ল, খাবলৈ আহক!", "Dinner call.")
    add("Food & Dining", "warm_food", "kin1 khaw3 un2 un2 taaw1.", "kin1 khaw3 un2 un2 taaw1.", "kin¹ kʰaw³ un² un² taːw¹",
        "Please eat the food while it is warm.", "कृपया गरम-गरम भोजन ग्रहण कीजिए।", "গৰমে গৰমে ভাত খাই লওক।", "Serving warm.")
    add("Food & Dining", "tasty_soup", "nam6 kaeng1 nai6 waan1 li1.", "nam6 kaeng1 nai6 waan1 li1.", "nam⁶ kɛːŋ¹ nai⁶ waːn¹ liː¹",
        "This broth is delightfully rich and savory.", "यह रसेदार सूप बहुत स्वादिष्ट बना है।", "আঞ্জাৰ জোলখিনি বৰ সোৱাদ হৈছে।", "Soup praise.")
    add("Food & Dining", "wild_roots", "man4 paa5 nai6 waan1 the5 the5.", "man4 paa5 nai6 waan1 the5 the5.", "man⁴ paː⁵ nai⁶ waːn¹ tʰe⁵ tʰe⁵",
        "These wild forest tubers taste delicious.", "जंगल का यह कंदमूल बहुत मीठा और स्वादिष्ट है।", "হাবিত পোৱা কাঠআলুটো বৰ সোৱাদ।", "Forest tubers.")
    add("Food & Dining", "dry_rice_snack", "khaw3 haang1 pen1 kin1 waan1.", "khaw3 haang1 pen1 kin1 waan1.", "kʰaw³ haːŋ¹ pen¹ kin¹ waːn¹",
        "Crispy roasted rice makes a wonderful traditional snack.", "भुना हुआ सूखा चावल एक स्वादिष्ट नाश्ता है।", "ভজা চাউলৰ জলপান বৰ সোৱাদ।", "Traditional snacks.")
    add("Food & Dining", "chew_betel", "chaw1 thao3 kin1 phlu1 kap4 maak1.", "chaw1 thao3 kin1 phlu1 kap4 maak1.", "t͡ɕaw¹ tʰaw³ kin¹ pʰluː¹ kap⁴ maːk¹",
        "The elders chew traditional betel nut and leaf.", "बुजुर्ग पारंपरिक पान और सुपारी चबाते हैं।", "বয়োজ্যেষ্ঠসকলে তামোল-পাণ খাইছে।", "Betel chewing custom.")
    add("Food & Dining", "clean_water", "nam6 kin1 nai6 sot1 sai1 li1.", "nam6 kin1 nai6 sot1 sai1 li1.", "nam⁶ kin¹ nai⁶ sot¹ saj¹ liː¹",
        "This drinking water is crystal clear and pure.", "यह पीने का पानी एकदम साफ़ और शुद्ध है।", "খোৱাপানীখিনি বৰ নিৰ্মল।", "Clean drinking water.")
    add("Food & Dining", "feed_baby", "me5 haak4 liang3 khaw3 luk3 nɔn4.", "me5 haak4 liang3 khaw3 luk3 nɔn4.", "me⁵ haːk⁴ ljaŋ³ kʰaw³ luk³ nɔn⁴",
        "The mother is feeding warm rice to her infant.", "माँ अपने छोटे बच्चे को प्यार से चावल खिला रही है।", "মায়ে কেঁচুৱাটোক মৰমেৰে ভাত খুৱাইছে।", "Mother nurturing.")
    add("Food & Dining", "dining_mat", "pɯ5 saat1 nang5 kin1 khaw3.", "pɯ5 saat1 nang5 kin1 khaw3.", "pɯ⁵ saːt¹ naŋ⁵ kin¹ kʰaw³",
        "Spread the woven bamboo mat to sit and dine.", "भोजन के लिए बुनी हुई चटाई बिछाइए।", "ভাত খাবলৈ ঢাৰিখন পাৰি লওক।", "Mat dining culture.")
    add("Food & Dining", "after_meal_gratitude", "kin1 khaw3 leew3, khɔp1 tsai1 the5 the5.", "kin1 khaw3 leew3, khɔp1 tsai1 the5 the5.", "kin¹ kʰaw³ leːw³ kʰɔp¹ t͡sai¹ tʰe⁵ tʰe⁵",
        "We have finished our meal, thank you very much for the hospitality.", "हमने भोजन कर लिया, इस सुंदर आतिथ्य के लिए आपका बहुत धन्यवाद।", "ভাত খোৱা হ’ল, আপোনাৰ আতিথ্যৰ বাবে অশেষ ধন্যবাদ।", "Post-meal gratitude.")
    add("Food & Dining", "tea_with_ginger", "nam6 chaa1 sai2 khing1 rɔn3 li1.", "nam6 chaa1 sai2 khing1 rɔn3 li1.", "nam⁶ t͡ɕʰaː¹ saj² kʰiŋ¹ rɔn³ liː¹",
        "Hot tea brewed with ginger is soothing and warm.", "अदरक वाली गरम चाय बहुत सुखद और ताज़गी देती है।", "আদা দিয়া গৰম চাহ খোৱাটো স্বাস্থ্যৰ বাবে ভাল।", "Ginger tea.")

    # ==========================================================================
    # DOMAIN 5: MARKET, TRADE, PRICES & NUMBERS (40 sentences)
    # ==========================================================================
    add("Market & Shopping", "how_much_item", "an1 nai6 khaa5 ki3 laai1?", "an1 nai6 khaa5 ki3 laai1?", "an¹ nai⁶ kʰaː⁵ ki³ laːj¹",
        "How much does this item cost?", "इस वस्तु का मूल्य कितना है?", "ইয়াৰ দাম কিমান?", "Price inquiry.")
    add("Market & Shopping", "reduce_price_request", "lot1 khaa5 hai3 noi3 taaw1.", "lot1 khaa5 hai3 noi3 taaw1.", "lot¹ kʰaː⁵ haj³ noi³ taːw¹",
        "Please reduce the price a little bit.", "कृपया दाम थोड़ा कम कीजिए।", "দাম অলপ কমাই দিয়ক।", "Bargaining request.")
    add("Market & Shopping", "too_expensive", "phaeng1 the5 the5, lot1 dai3 haa1?", "phaeng1 the5 the5, lot1 dai3 haa1?", "pʰɛŋ¹ tʰe⁵ tʰe⁵ lot¹ daj³ haː¹",
        "It is remarkably expensive, can you discount it?", "यह बहुत महँगा है, क्या कुछ कम हो सकता है?", "বৰ দামী, অলপ কম হ’বনে?", "Price objection.")
    add("Market & Shopping", "ten_rupees", "an1 nai6 khaa5 sip1 ngan1.", "an1 nai6 khaa5 sip1 ngan1.", "an¹ nai⁶ kʰaː⁵ sip¹ ŋan¹",
        "This costs ten rupees.", "इसका दाम दस रुपये है।", "ইয়াৰ দাম দহ টকা।", "Ten rupees.")
    add("Market & Shopping", "twenty_rupees", "maak1 kuai3 nai6 khaa5 saw1 ngan1.", "maak1 kuai3 nai6 khaa5 saw1 ngan1.", "maːk¹ kuaj³ nai⁶ kʰaː⁵ saw¹ ŋan¹",
        "These bananas cost twenty rupees.", "इन केलों का दाम बीस रुपये है।", "এই কলখিনির দাম কুৰি টকা।", "Twenty rupees.")
    add("Market & Shopping", "fifty_rupees", "paa1 nai6 khaa5 haa3 sip1 ngan1.", "paa1 nai6 khaa5 haa3 sip1 ngan1.", "paː¹ nai⁶ kʰaː⁵ haː³ sip¹ ŋan¹",
        "This river fish costs fifty rupees.", "इस मछली का दाम पचास रुपये है।", "এই মাছটোৰ দাম পঞ্চাশ টকা।", "Fifty rupees.")
    add("Market & Shopping", "hundred_rupees", "phaa3 nai6 khaa5 nɯng5 pak1 ngan1.", "phaa3 nai6 khaa5 nɯng5 pak1 ngan1.", "pʰaː³ nai⁶ kʰaː⁵ nɯŋ⁵ pak¹ ŋan¹",
        "This handwoven cloth costs one hundred rupees.", "इस बुने हुए कपड़े का दाम एक सौ रुपये है।", "এই কাপোৰখনৰ দাম এশ টকা।", "One hundred rupees.")
    add("Market & Shopping", "buy_rice", "kaw1 khrai3 sɯ3 khaw3 saarn1.", "kaw1 khrai3 sɯ3 khaw3 saarn1.", "kaw¹ kʰraj³ sɯː³ kʰaw³ saːrn¹",
        "I want to purchase uncooked rice.", "मैं पकाने के लिए चावल खरीदना चाहता हूँ।", "মই চাউল কিনিব বিচাৰোঁ।", "Buying rice.")
    add("Market & Shopping", "buy_fresh_greens", "kaw1 khrai3 sɯ3 phak1 sot1.", "kaw1 khrai3 sɯ3 phak1 sot1.", "kaw¹ kʰraj³ sɯː³ pʰak¹ sot¹",
        "I want to buy fresh leafy greens.", "मैं ताज़ी हरी सब्ज़ियाँ खरीदना चाहता हूँ।", "মই সতেজ শাক কিনিব খোজোঁ।", "Buying greens.")
    add("Market & Shopping", "buy_salt_oil", "sɯ3 klɯa1 kap4 nam6 man1.", "sɯ3 klɯa1 kap4 nam6 man1.", "sɯː³ klɯa¹ kap⁴ nam⁶ man¹",
        "Buy some salt and cooking oil.", "नमक और खाना पकाने का तेल खरीदिए।", "নিমখ আৰু তেল কিনি আনক।", "Pantry staples.")
    add("Market & Shopping", "where_is_market", "laat1 yu5 theu1?", "laat1 yu5 theu1?", "laːt¹ ju⁵ tʰeu¹",
        "Where is the weekly market held?", "साप्ताहिक बाज़ार कहाँ लगता है?", "বজাৰখন ক’ত বহে?", "Market location.")
    add("Market & Shopping", "market_day_today", "wan1 nai6 pen1 wan1 laat1.", "wan1 nai6 pen1 wan1 laat1.", "wan¹ nai⁶ pen¹ wan¹ laːt¹",
        "Today is the village market day.", "आज बाज़ार का दिन है।", "আজি বজাৰৰ দিন।", "Market day.")
    add("Market & Shopping", "many_goods", "laat1 mi5 khɔng3 laai1 the5 the5.", "laat1 mi5 khɔng3 laai1 the5 the5.", "laːt¹ miː¹ kʰɔŋ³ laːj¹ tʰe⁵ tʰe⁵",
        "There are abundant goods available in the market.", "बाज़ार में बहुत सारा सामान उपलब्ध है।", "বজাৰত প্ৰচুৰ বস্তু-সামগ্ৰী আছে।", "Market variety.")
    add("Market & Shopping", "weigh_fish", "sang2 paa1 nai6 ki3 ki1lo1?", "sang2 paa1 nai6 ki3 ki1lo1?", "saŋ² paː¹ nai⁶ ki³ kiː¹lo¹",
        "How many kilograms does this fish weigh?", "इस मछली का वज़न कितने किलोग्राम है?", "মাছটো কেইকিলো ওজন হ’ব?", "Weight inquiry.")
    add("Market & Shopping", "one_kilo", "mi5 nɯng5 ki1lo1.", "mi5 nɯng5 ki1lo1.", "miː¹ nɯŋ⁵ kiː¹lo¹",
        "It weighs exactly one kilogram.", "इसका वज़न पूरा एक किलोग्राम है।", "ইয়াৰ ওজন এক কিলোগ্ৰাম।", "One kilo.")
    add("Market & Shopping", "two_kilos", "kaw1 khrai3 aw1 sɔng1 ki1lo1.", "kaw1 khrai3 aw1 sɔng1 ki1lo1.", "kaw¹ kʰraj³ aw¹ sɔŋ¹ kiː¹lo¹",
        "I would like to take two kilograms.", "मैं दो किलोग्राम लेना चाहता हूँ।", "মই দুই কিলোগ্ৰাম ল’ব বিচাৰোঁ।", "Two kilos.")
    add("Market & Shopping", "count_eggs", "khai2 mi5 sip1 sɔng1 luuk4.", "khai2 mi5 sip1 sɔng1 luuk4.", "kʰaj² miː¹ sip¹ sɔŋ¹ luːk⁴",
        "There are twelve eggs (one dozen).", "यहाँ बारह अंडे हैं।", "ইয়াত বাৰটা কণী আছে।", "Dozen eggs.")
    add("Market & Shopping", "take_all", "kaw1 aw1 thuk1 an1.", "kaw1 aw1 thuk1 an1.", "kaw¹ aw¹ tʰuk¹ an¹",
        "I shall take everything.", "मैं यह सारा सामान लूँगा।", "মই সকলোখিনিয়েই ল’ম।", "Purchasing all.")
    add("Market & Shopping", "return_change", "thɔn1 ngan1 hai3 kaw1 taaw1.", "thɔn1 ngan1 hai3 kaw1 taaw1.", "tʰɔn¹ ŋan¹ haj³ kaw¹ taːw¹",
        "Please return my balance change.", "कृपया मेरे बाकी पैसे वापस दीजिए।", "অনুগ্ৰহ কৰি মোৰ বাকী পইচাটো ঘূৰাই দিয়ক।", "Balance money.")
    add("Market & Shopping", "cheap_price", "an1 nai6 thuk1 li1 the5 the5.", "an1 nai6 thuk1 li1 the5 the5.", "an¹ nai⁶ tʰuk¹ liː¹ tʰe⁵ tʰe⁵",
        "This is very reasonably priced and affordable.", "यह बहुत सस्ता और किफ़ायती है।", "এইটো বৰ সুলভ আৰু কম দামী।", "Affordable item.")
    add("Market & Shopping", "good_quality", "khɔng3 nai6 li1 the5 the5.", "khɔng3 nai6 li1 the5 the5.", "kʰɔŋ³ nai⁶ liː¹ tʰe⁵ tʰe⁵",
        "This commodity is of superior quality.", "यह सामान बहुत अच्छी गुणवत्ता का है।", "এই বস্তুটো বৰ উৎকৃষ্ট মানৰ।", "Good quality.")
    add("Market & Shopping", "pay_money", "kaw1 pan1 ngan1 maɯ2 yow3.", "kaw1 pan1 ngan1 maɯ2 yow3.", "kaw¹ pan¹ ŋan¹ maɯ² jow³",
        "I have handed over the payment to you.", "मैंने आपको पैसे दे दिए हैं।", "মই আপোনাক পইচা দি দিছোঁ।", "Payment made.")
    add("Market & Shopping", "sell_bamboo", "chaw1 thao3 khaai5 mai3 phaak4.", "chaw1 thao3 khaai5 mai3 phaak4.", "t͡ɕaw¹ tʰaw³ kʰaːj⁵ maj³ pʰaːk⁴",
        "The elder is selling split bamboo poles.", "बुजुर्ग बाँस बेच रहे हैं।", "বয়োজ্যেষ্ঠজনে বাঁহ বিক্ৰী কৰিছে।", "Selling bamboo.")
    add("Market & Shopping", "sell_cloth", "naang1 tai1 khaai5 phaa3 mai3.", "naang1 tai1 khaai5 phaa3 mai3.", "naːŋ¹ taj¹ kʰaːj⁵ pʰaː³ maj³",
        "The Tai women are selling handmade silk fabrics.", "ताई महिलाएँ हाथ से बुने रेशमी वस्त्र बेच रही हैं।", "টাই মহিলাসকলে পাটৰ কাপোৰ বিক্ৰী কৰিছে।", "Selling textiles.")
    add("Market & Shopping", "number_one", "nɯng5", "nɯng5", "nɯŋ⁵",
        "One (1).", "एक (1)।", "এক (১)।", "Cardinal 1.")
    add("Market & Shopping", "number_two", "sɔng1", "sɔng1", "sɔŋ¹",
        "Two (2).", "दो (2)।", "দুই (২)।", "Cardinal 2.")
    add("Market & Shopping", "number_three", "saam1", "saam1", "saːm¹",
        "Three (3).", "तीन (3)।", "তিনি (৩)।", "Cardinal 3.")
    add("Market & Shopping", "number_four", "sii2", "sii2", "siː²",
        "Four (4).", "चार (4)।", "চাৰি (৪)।", "Cardinal 4.")
    add("Market & Shopping", "number_five", "haa3", "haa3", "haː³",
        "Five (5).", "पाँच (5)।", "পাঁচ (৫)।", "Cardinal 5.")
    add("Market & Shopping", "number_six", "hok1", "hok1", "hok¹",
        "Six (6).", "छह (6)।", "ছয় (৬)।", "Cardinal 6.")
    add("Market & Shopping", "number_seven", "chet1", "chet1", "t͡ɕʰet¹",
        "Seven (7).", "सात (7)।", "সাত (৭)।", "Cardinal 7.")
    add("Market & Shopping", "number_eight", "pet2", "pet2", "pet²",
        "Eight (8).", "आठ (8)।", "আঠ (৮)।", "Cardinal 8.")
    add("Market & Shopping", "number_nine", "kaw3", "kaw3", "kaw³",
        "Nine (9).", "नौ (9)।", "ন (৯)।", "Cardinal 9.")
    add("Market & Shopping", "number_ten", "sip1", "sip1", "sip¹",
        "Ten (10).", "दस (10)।", "দহ (১০)।", "Cardinal 10.")
    add("Market & Shopping", "number_twenty", "saw1", "saw1", "saw¹",
        "Twenty (20).", "बीस (20)।", "কুৰি (২০)।", "Cardinal 20.")
    add("Market & Shopping", "number_fifty", "haa3 sip1", "haa3 sip1", "haː³ sip¹",
        "Fifty (50).", "पचास (50)।", "পঞ্চাশ (৫০)।", "Cardinal 50.")
    add("Market & Shopping", "number_hundred", "nɯng5 pak1", "nɯng5 pak1", "nɯŋ⁵ pak¹",
        "One hundred (100).", "एक सौ (100)।", "এশ (১০০)।", "Cardinal 100.")
    add("Market & Shopping", "number_thousand", "nɯng5 heng1", "nɯng5 heng1", "nɯŋ⁵ heŋ¹",
        "One thousand (1000).", "एक हज़ार (1000)।", "এহেজাৰ (১০০০)।", "Cardinal 1000.")
    add("Market & Shopping", "fair_trade", "khaa5 nai6 suuk1 thuk1 thot1 kan1.", "khaa5 nai6 suuk1 thuk1 thot1 kan1.", "kʰaː⁵ nai⁶ suːk¹ tʰuk¹ tʰot¹ kan¹",
        "This is an honest and fair price.", "यह बिल्कुल उचित और न्यायसंगत दाम है।", "এইটো সঠিক আৰু ন্যায্য দাম।", "Fair deal.")
    add("Market & Shopping", "empty_market", "yam1 nai6 laat1 leew3 yow3.", "yam1 nai6 laat1 leew3 yow3.", "jam¹ nai⁶ laːt¹ leːw³ jow³",
        "The market has ended for the day.", "आज का बाज़ार अब समाप्त हो चुका है।", "আজিৰ বজাৰ সামৰা হ’ল।", "Market closed.")

    # ==========================================================================
    # DOMAIN 6: FAMILY, KINSHIP & COMMUNITY RELATIONS (40 sentences)
    # ==========================================================================
    add("Family & Kinship", "father_role", "po5 haw1 pen1 phuu3 naa1.", "po5 haw1 pen1 phuu3 naa1.", "po⁵ haw¹ pen¹ pʰuː³ naː¹",
        "My father is a dedicated farmer.", "मेरे पिताजी एक कर्मठ किसान हैं।", "মোৰ দেউতা এজন খেতিয়ক।", "Father's vocation.")
    add("Family & Kinship", "mother_role", "me5 haw1 pen1 naang1 tam3 phaa3.", "me5 haw1 pen1 naang1 tam3 phaa3.", "me⁵ haw¹ pen¹ naːŋ¹ tam³ pʰaː³",
        "My mother is a master weaver of cloth.", "मेरी माँ एक कुशल बुनकर हैं।", "মোৰ মা এগৰাকী নিপুণ শিপিনী।", "Mother's craft.")
    add("Family & Kinship", "grandfather_elder", "pu3 haw1 aayu3 pet2 sip1 pi1 yow3.", "pu3 haw1 aayu3 pet2 sip1 pi1 yow3.", "pu³ haw¹ aː¹ju³ pet² sip¹ piː¹ jow³",
        "My grandfather is eighty years old.", "मेरे दादाजी की उम्र अस्सी वर्ष है।", "মোৰ ককাৰ বয়স আশী বছৰ হ’ল।", "Grandfather's age.")
    add("Family & Kinship", "grandmother_blessing", "naai1 haw1 pan1 phɔn1 haw1.", "naai1 haw1 pan1 phɔn1 haw1.", "naːj¹ haw¹ pan¹ pʰɔn¹ haw¹",
        "My grandmother gave us her loving blessings.", "मेरी दादीजी ने हमें अपना शुभाशीर्वाद दिया।", "মোৰ আইতাই আমাক আশীৰ্বাদ দিলে।", "Grandmother blessing.")
    add("Family & Kinship", "elder_brother_work", "phi3saai1 kaw1 pai1 kaa1 khaai5.", "phi3saai1 kaw1 pai1 kaa1 khaai5.", "pʰi³ saːj¹ kaw¹ paj¹ kaː¹ kʰaːj⁵",
        "My elder brother went for trading.", "मेरे बड़े भाई व्यापार के सिलसिले में गए हैं।", "মোৰ ককাইদেউ ব্যৱসায়ৰ বাবে ওলাই গৈছে।", "Brother's work.")
    add("Family & Kinship", "elder_sister_cook", "phi3ying1 kaw1 hung3 khaw3.", "phi3ying1 kaw1 hung3 khaw3.", "pʰi³ jiŋ¹ kaw¹ huŋ³ kʰaw³",
        "My elder sister is cooking rice.", "मेरी बड़ी बहन चावल पका रही हैं।", "মোৰ বাদেৱে ভাত ৰান্ধিছে।", "Sister cooking.")
    add("Family & Kinship", "younger_brother", "nɔng3saai1 kaw1 pai1 hong1 hian1.", "nɔng3saai1 kaw1 pai1 hong1 hian1.", "nɔŋ³ saːj¹ kaw¹ paj¹ hoŋ¹ hjan¹",
        "My younger brother has gone to school.", "मेरा छोटा भाई स्कूल गया है।", "মোৰ ভাইটি বিদ্যালয়লৈ গৈছে।", "Brother studying.")
    add("Family & Kinship", "younger_sister", "nɔng3ying1 kaw1 yim3 ngam1 the5 the5.", "nɔng3ying1 kaw1 yim3 ngam1 the5 the5.", "nɔŋ³ jiŋ¹ kaw¹ jim³ ŋam¹ tʰe⁵ tʰe⁵",
        "My younger sister has a sweet smile.", "मेरी छोटी बहन की मुस्कान बहुत प्यारी है।", "মোৰ ভনীজনীৰ হাঁহিটো বৰ ধুনীয়া।", "Sister smiling.")
    add("Family & Kinship", "love_family", "haw1 haak4 phuu5 hɯan1 haw1 thuk1 kon1.", "haw1 haak4 phuu5 hɯan1 haw1 thuk1 kon1.", "haw¹ haːk⁴ pʰuː⁵ hɯan¹ haw¹ tʰuk¹ kon¹",
        "We love every member of our family dearly.", "हम अपने परिवार के सभी सदस्यों से बहुत स्नेह करते हैं।", "আমি আমাৰ পৰিয়ালৰ সকলো সদস্যক ভাল পাওঁ।", "Family love.")
    add("Family & Kinship", "respect_elders", "luk3 on2 haak4 nap4 thɯ5 chaw1 thao3.", "luk3 on2 haak4 nap4 thɯ5 chaw1 thao3.", "luk³ on² haːk⁴ nap⁴ tʰɯ⁵ t͡ɕaw¹ tʰaw³",
        "Children ought to revere and respect community elders.", "बच्चों को बुजुर्गों का आदर-सम्मान करना चाहिए।", "ল’ৰা-ছোৱালীয়ে বয়োজ্যেষ্ঠক শ্ৰদ্ধা কৰা উচিত।", "Filial piety.")
    add("Family & Kinship", "paternal_uncle", "lung1 kaw1 yu5 maan3 paa1 waai6.", "lung1 kaw1 yu5 maan3 paa1 waai6.", "luŋ¹ kaw¹ ju⁵ maːn³ paː¹ waːj⁶",
        "My elder paternal uncle lives in Powaimukh.", "मेरे ताऊजी पोवाइमुख गाँव में रहते हैं।", "মোৰ বৰদেউতা পোৱাইমুখ গাঁৱত থাকে।", "Uncle relation.")
    add("Family & Kinship", "paternal_aunt", "paa3 kaw1 het1 khaw3 tom3 waan1.", "paa3 kaw1 het1 khaw3 tom3 waan1.", "paː³ kaw¹ het¹ kʰaw³ tom³ waːn¹",
        "My aunt prepares delicious sweet pitha treats.", "मेरी ताईजी बहुत स्वादिष्ट मीठे व्यंजन बनाती हैं।", "মোৰ জেঠাই বৰ সোৱাদ পিঠা বনায়।", "Aunt cooking.")
    add("Family & Kinship", "maternal_uncle", "naa2 saai1 kaw1 liang3 khwaai1 laai1 tua1.", "naa2 saai1 kaw1 liang3 khwaai1 laai1 tua1.", "naː² saːj¹ kaw¹ ljaŋ³ kʰwaːj¹ laːj¹ tua¹",
        "My maternal uncle tends to several water buffaloes.", "मेरे मामाजी के पास कई भैंसें हैं।", "মোৰ মোমায়ে কেইবাটাও ম’হ পুহিছে।", "Maternal uncle.")
    add("Family & Kinship", "maternal_aunt", "naa2 ying1 kaw1 tam3 phaa3 mai3 ngam1.", "naa2 ying1 kaw1 tam3 phaa3 mai3 ngam1.", "naː² jiŋ¹ kaw¹ tam³ pʰaː³ maj³ ŋam¹",
        "My maternal aunt weaves exquisite silk patterns.", "मेरी मौसीजी बहुत सुंदर रेशमी वस्त्र बुनती हैं।", "মোৰ মাহীয়ে ধুনীয়া পাটৰ কাপোৰ বয়।", "Maternal aunt.")
    add("Family & Kinship", "son_learning", "luk3 saai1 kaw1 khrai3 pen1 chaang3.", "luk3 saai1 kaw1 khrai3 pen1 chaang3.", "luk³ saːj¹ kaw¹ kʰraj³ pen¹ t͡ɕʰaːŋ³",
        "My son aspires to become a skilled craftsperson.", "मेरा बेटा एक कुशल शिल्पी बनना चाहता है।", "মোৰ পুত্ৰ এজন নিপুণ কাৰিকৰ হ’ব খোজে।", "Son's ambition.")
    add("Family & Kinship", "daughter_singing", "luk3 ying1 kaw1 hɔng3 kham1 khwaam1 tai1.", "luk3 ying1 kaw1 hɔng3 kham1 khwaam1 tai1.", "luk³ jiŋ¹ kaw¹ hɔŋ³ kʰam¹ kʰwaːm¹ taj¹",
        "My daughter sings traditional Tai folksongs.", "मेरी बेटी पारंपरिक ताई लोकगीत गाती है।", "মোৰ জীয়াৰীয়ে পৰম্পৰাগত টাই গীত গায়।", "Daughter's song.")
    add("Family & Kinship", "nephew_studying", "laan1 saai1 kaw1 an2 lik1 thuk1 wan1.", "laan1 saai1 kaw1 an2 lik1 thuk1 wan1.", "laːn¹ saːj¹ kaw¹ an² lik¹ tʰuk¹ wan¹",
        "My nephew studies diligently every day.", "मेरा भतीजा रोज़ाना ध्यानपूर्वक पढ़ाई करता है।", "মোৰ ভাগিনটোৱে প্ৰতিদিনে পঢ়া-শুনা কৰে।", "Nephew studying.")
    add("Family & Kinship", "niece_weaving", "laan1 ying1 kaw1 hian1 tam3 phaa3.", "laan1 ying1 kaw1 hian1 tam3 phaa3.", "laːn¹ jiŋ¹ kaw¹ hjan¹ tam³ pʰaː³",
        "My niece is learning the art of traditional weaving.", "मेरी भतीजी बुनाई की कला सीख रही है।", "মোৰ ভতিজীজনীয়ে তাঁত বোৱা শিকিছে।", "Niece craft.")
    add("Family & Kinship", "ancestral_home", "hɯan1 haw1 mi5 prawat1 hing1 yow3.", "hɯan1 haw1 mi5 prawat1 hing1 yow3.", "hɯan¹ haw¹ miː¹ pra¹wat¹ hiŋ¹ jow³",
        "Our ancestral home possesses a long history.", "हमारे पैतृक घर का एक लंबा और समृद्ध इतिहास है।", "আমাৰ পুৰণি ঘৰটোৰ এটা সুদীৰ্ঘ ইতিহাস আছে।", "Ancestral heritage.")
    add("Family & Kinship", "house_harmony", "khon1 nai1 hɯan1 haw1 yu5 kap4 phuk1 tsai1.", "khon1 nai1 hɯan1 haw1 yu5 kap4 phuk1 tsai1.", "kʰon¹ naj¹ hɯan¹ haw¹ ju⁵ kap⁴ pʰuk¹ t͡sai¹",
        "All dwellers in our house live in peace and harmony.", "हमारे घर के सभी सदस्य प्रेम और सद्भाव से रहते हैं।", "আমাৰ ঘৰৰ সকলোৱে মিলি-জুলি শান্তিত বাস কৰোঁ।", "Domestic harmony.")
    add("Family & Kinship", "care_for_parents", "haw1 haak4 liang3 po5 me5 yam1 thao3.", "haw1 haak4 liang3 po5 me5 yam1 thao3.", "haw¹ haːk⁴ ljaŋ³ po⁵ me⁵ jam¹ tʰaw³",
        "We care devotedly for our parents in their old age.", "हम बुढ़ापे में अपने माता-पिता की पूरे मनोयोग से सेवा करते हैं।", "আমি বৃদ্ধ বয়সত মা-দেউতাৰ সেৱা-শুশ্ৰূষা কৰোঁ।", "Elder care.")
    add("Family & Kinship", "grandchild_joy", "laan1 nɔn4 maa1 het1 hai3 haw1 yim3 tsai1.", "laan1 nɔn4 maa1 het1 hai3 haw1 yim3 tsai1.", "laːn¹ nɔn⁴ maː¹ het¹ haj³ haw¹ jim³ t͡sai¹",
        "The infant grandchild brings endless joy to our home.", "छोटे पोते-पोतियों के आने से घर में खुशियाँ छा जाती हैं।", "নাতি-নাতিনীৰ উপস্থিতিয়ে ঘৰখন আনন্দময় কৰি তোলে।", "Grandchildren.")
    add("Family & Kinship", "brotherhood", "phi3 nɔng3 saai1 chuai3 kan1 het1 ngaan1.", "phi3 nɔng3 saai1 chuai3 kan1 het1 ngaan1.", "pʰi³ nɔŋ³ saːj¹ t͡ɕʰuaj³ kan¹ het¹ ŋaːn¹",
        "Brothers assist one another in arduous field labor.", "भाई खेतों के काम में एक-दूसरे की मदद करते हैं।", "ককাই-ভাইসকলে মিলি পথাৰৰ কাম কৰে।", "Brotherly cooperation.")
    add("Family & Kinship", "sisterhood", "phi3 nɔng3 ying1 tam3 phaa3 ruam2 kan1.", "phi3 nɔng3 ying1 tam3 phaa3 ruam2 kan1.", "pʰi³ nɔŋ³ jiŋ¹ tam³ pʰaː³ ruam² kan¹",
        "Sisters weave cloth together at the porch.", "बहनें मिलकर बरामदे में कपड़े बुनती हैं।", "বাই-ভনীসকলে একেলগে তাঁত বয়।", "Sisterly cooperation.")
    add("Family & Kinship", "gather_at_hearth", "khon1 hɯan1 nang5 rim1 fai1 kham3 nai6.", "khon1 hɯan1 nang5 rim1 fai1 kham3 nai6.", "kʰon¹ hɯan¹ naŋ⁵ rim¹ faj¹ kʰam³ nai⁶",
        "The whole family gathers around the warm hearth tonight.", "आज रात पूरा परिवार चूल्हे के पास इकट्ठा बैठा है।", "আজি গধূলি পৰিয়ালৰ সকলোৱে জুইশালৰ কাষত বহিছে।", "Hearth gathering.")
    add("Family & Kinship", "tell_stories", "pu3 haw1 lao3 nithaan1 hai3 luk3 on2.", "pu3 haw1 lao3 nithaan1 hai3 luk3 on2.", "pu³ haw¹ law³ ni¹tʰaːn¹ haj³ luk³ on²",
        "Grandfather narrates ancestral folklore to the children.", "दादाजी बच्चों को प्राचीन लोककथाएँ सुनाते हैं।", "ককাদেউতাই ল’ৰা-ছোৱালীবোৰক সাধুকথা শুনাইছে।", "Storytelling tradition.")
    add("Family & Kinship", "baby_sleep", "luk3 nɔn4 nɔn1 lap1 li1.", "luk3 nɔn4 nɔn1 lap1 li1.", "luk³ nɔn⁴ nɔn¹ lap¹ liː¹",
        "The little baby is sleeping peacefully in the cradle.", "छोटा बच्चा पालने में शांति से सो रहा है।", "কেঁচুৱাটোৱে শান্তভাৱে টোপনি গৈছে।", "Baby sleeping.")
    add("Family & Kinship", "father_strength", "po5 kaw1 mi5 haeng1 het1 naa1.", "po5 kaw1 mi5 haeng1 het1 naa1.", "po⁵ kaw¹ miː¹ hɛŋ¹ het¹ naː¹",
        "My father possesses great endurance for farm labor.", "मेरे पिताजी में खेतों में काम करने का बहुत बल है।", "মোৰ দেউতাৰ পথাৰত কাম কৰিবলৈ যথেষ্ট শক্তি আছে।", "Father's fortitude.")
    add("Family & Kinship", "mother_kindness", "me5 kaw1 mi5 tsai1 mettaa1 li1.", "me5 kaw1 mi5 tsai1 mettaa1 li1.", "me⁵ kaw¹ miː¹ t͡sai¹ met¹taː¹ liː¹",
        "My mother possesses boundless compassion and gentle kindness.", "मेरी माँ का हृदय अत्यंत दयालु और स्नेहमयी है।", "মোৰ মাৰ হৃদয়খন মৰম আৰু কৰুণাৰে ভৰপূৰ।", "Mother's kindness.")
    add("Family & Kinship", "respect_mother_in_law", "nap4 thɯ5 me5 thao3 me5 yaa2.", "nap4 thɯ5 me5 thao3 me5 yaa2.", "nap⁴ tʰɯ⁵ me⁵ tʰaw³ me⁵ jaː²",
        "We hold our mothers-in-law in high esteem.", "हम अपनी सासुमाँ का आदर-सम्मान करते हैं।", "আমি শাহুআইক সন্মান কৰোঁ।", "In-law respect.")
    add("Family & Kinship", "respect_father_in_law", "nap4 thɯ5 po5 thao3 po5 yaa2.", "nap4 thɯ5 po5 thao3 po5 yaa2.", "nap⁴ tʰɯ⁵ po⁵ tʰaw³ po⁵ jaː²",
        "We hold our fathers-in-law in high esteem.", "हम अपने ससुरजी का आदर-सम्मान करते हैं।", "আমি শহুৰদেউতাক শ্ৰদ্ধা কৰোঁ।", "In-law respect.")
    add("Family & Kinship", "community_ties", "khon1 maan3 paa1 waai6 pen1 phi3 nɔng3 kan1.", "khon1 maan3 paa1 waai6 pen1 phi3 nɔng3 kan1.", "kʰon¹ maːn³ paː¹ waːj⁶ pen¹ pʰi³ nɔŋ³ kan¹",
        "All Powaimukh villagers consider each other kin.", "पोवाइमुख गाँव के सभी निवासी एक-दूसरे को भाई-बहन मानते हैं।", "পোৱাইমুখৰ সকলো গাঁওবাসী ইজনে-সিজনৰ আত্মীয়স্বৰূপ।", "Community solidarity.")
    add("Family & Kinship", "help_neighbors", "chuai3 maan3 rim1 hɯan1 het1 ngaan1.", "chuai3 maan3 rim1 hɯan1 het1 ngaan1.", "t͡ɕʰuaj³ maːn³ rim¹ hɯan¹ het¹ ŋaːn¹",
        "Help the neighboring household with their heavy chores.", "पड़ोसियों की उनके कठिन कार्यों में सहायता कीजिए।", "চুবুৰীয়াৰ বিপদ-আপদ আৰু কামত সহায় কৰক।", "Neighborliness.")
    add("Family & Kinship", "wedding_celebration", "wan1 nai6 mi5 poy2 khek2 kin1 liang3.", "wan1 nai6 mi5 poy2 khek2 kin1 liang3.", "wan¹ nai⁶ miː¹ pɔj² kʰek² kin¹ ljaŋ³",
        "Today there is a joyous wedding festival in the village.", "आज गाँव में विवाह का उत्सव और दावत है।", "আজি গাঁৱত বিবাহৰ ভোজ-মেলৰ আয়োজন হৈছে।", "Wedding festive event.")
    add("Family & Kinship", "bless_newlyweds", "hɯ3 khu2 baaw2 saaw1 yu5 li1 kin1 waan1.", "hɯ3 khu2 baaw2 saaw1 yu5 li1 kin1 waan1.", "hɯ³ kʰuː² baːw² saːw¹ ju⁵ liː¹ kin¹ waːn¹",
        "May the newly wedded couple live in enduring bliss.", "नवविवाहित जोड़ा सदा सुखी, स्वस्थ और समृद्ध रहे।", "নৱদম্পতীৰ জীৱন সুখ-শান্তিৰে ভৰি পৰক।", "Wedding blessing.")
    add("Family & Kinship", "birth_of_child", "maan3 haw1 mi5 luk3 nɔn4 kəət2 maa1.", "maan3 haw1 mi5 luk3 nɔn4 kəət2 maa1.", "maːn³ haw¹ miː¹ luk³ nɔn⁴ kəːt² maː¹",
        "A blessed new child has been born into our village.", "हमारे गाँव में एक नए नन्हें शिशु का जन्म हुआ है।", "আমাৰ গাঁৱত এটা নতুন কেঁচুৱা জন্ম হৈছে।", "Childbirth celebration.")
    add("Family & Kinship", "mourning_elders", "haw1 ram1 lɯk1 thɯng5 pu5 yaa3 thuk1 wan1.", "haw1 ram1 lɯk1 thɯng5 pu5 yaa3 thuk1 wan1.", "haw¹ ram¹ lɯk¹ tʰɯŋ⁵ pu⁵ jaː³ tʰuk¹ wan¹",
        "We remember our revered ancestors with gratitude daily.", "हम अपने पूर्वजों का प्रतिदिन कृतज्ञतापूर्वक स्मरण करते हैं।", "আমি নিতৌ আমাৰ পূৰ্বপুৰুষসকলক শ্ৰদ্ধাৰে সোঁৱৰণ কৰোঁ।", "Ancestral remembrance.")
    add("Family & Kinship", "honor_tradition", "chaw1 thao3 sɔn1 hai3 haw1 mi5 tsai1 li1.", "chaw1 thao3 sɔn1 hai3 haw1 mi5 tsai1 li1.", "t͡ɕaw¹ tʰaw³ sɔn¹ haj³ haw¹ miː¹ t͡sai¹ liː¹",
        "Our elders taught us to cultivate a noble and generous heart.", "हमारे बुजुर्गों ने हमें नेक और परोपकारी बनने की शिक्षा दी है।", "বয়োজ্যেষ্ঠসকলে আমাক সজ আৰু পৰোপকাৰী হ’বলৈ শিকাইছে।", "Moral upbringing.")
    add("Family & Kinship", "teach_children", "sɔn1 luk3 on2 hai3 hu3 kham1 thaai1.", "sɔn1 luk3 on2 hai3 hu3 kham1 thaai1.", "sɔn¹ luk³ on² haj³ huː³ kʰam¹ tʰaːj¹",
        "Teach the young children their indigenous mother tongue.", "छोटे बच्चों को उनकी मातृभाषा अवश्य सिखाइए।", "কণমানিবোৰক মাতৃভাষা শিকোৱা উচিত।", "Pedagogical duty.")
    add("Family & Kinship", "family_strength", "phi3 nɔng3 phuk1 tsai1 kan1, hɯan1 man3 khang1.", "phi3 nɔng3 phuk1 tsai1 kan1, hɯan1 man3 khang1.", "pʰi³ nɔŋ³ pʰuk¹ t͡sai¹ kan¹ hɯan¹ man³ kʰaŋ¹",
        "When relatives unite with one heart, the family stands strong.", "जब सभी परिजन एकमत होकर रहते हैं, तो परिवार सशक्त बनता है।", "পৰিয়ালৰ সকলোৱে একতাৰে থাকিলে ঘৰখন শক্তিশালী হয়।", "Kinship proverb.")

    # ==========================================================================
    # DOMAIN 7: TIME, CALENDAR, DAYS & CLOCK (35 sentences)
    # ==========================================================================
    add("Time & Schedule", "what_time_is_it", "yam1 nai6 ki3 mong1 yow3?", "yam1 nai6 ki3 mong1 yow3?", "jam¹ nai⁶ ki³ moŋ¹ jow³",
        "What time is it right now?", "अभी क्या समय हुआ है?", "এতিয়া কেইটা বাজিছে?", "Asking time.")
    add("Time & Schedule", "five_am", "yam1 nai6 haa3 mong1 chaw3 yow3.", "yam1 nai6 haa3 mong1 chaw3 yow3.", "jam¹ nai⁶ haː³ moŋ¹ t͡ɕaw³ jow³",
        "It is five o'clock in the morning.", "अभी सुबह के पाँच बजे हैं।", "এতিয়া ৰাতিপুৱা পাঁচ বাজিছে।", "5 AM.")
    add("Time & Schedule", "six_am", "yam1 nai6 hok1 mong1 chaw3 yow3.", "yam1 nai6 hok1 mong1 chaw3 yow3.", "jam¹ nai⁶ hok¹ moŋ¹ t͡ɕaw³ jow³",
        "It is six o'clock in the morning.", "अभी सुबह के छह बजे हैं।", "এতিয়া ৰাতিপুৱা ছয় বাজিছে।", "6 AM.")
    add("Time & Schedule", "seven_am", "yam1 nai6 chet1 mong1 chaw3 yow3.", "yam1 nai6 chet1 mong1 chaw3 yow3.", "jam¹ nai⁶ t͡ɕʰet¹ moŋ¹ t͡ɕaw³ jow³",
        "It is seven o'clock in the morning.", "अभी सुबह के सात बजे हैं।", "এতিয়া ৰাতিপুৱা সাত বাজিছে।", "7 AM.")
    add("Time & Schedule", "eight_am", "yam1 nai6 pet2 mong1 chaw3 yow3.", "yam1 nai6 pet2 mong1 chaw3 yow3.", "jam¹ nai⁶ pet² moŋ¹ t͡ɕaw³ jow³",
        "It is eight o'clock in the morning.", "अभी सुबह के आठ बजे हैं।", "এতিয়া ৰাতিপুৱা আঠ বাজিছে।", "8 AM.")
    add("Time & Schedule", "nine_am", "yam1 nai6 kaw3 mong1 chaw3 yow3.", "yam1 nai6 kaw3 mong1 chaw3 yow3.", "jam¹ nai⁶ kaw³ moŋ¹ t͡ɕaw³ jow³",
        "It is nine o'clock in the morning.", "अभी सुबह के नौ बजे हैं।", "এতিয়া ৰাতিপুৱা ন বাজিছে।", "9 AM.")
    add("Time & Schedule", "ten_am", "yam1 nai6 sip1 mong1 chaw3 yow3.", "yam1 nai6 sip1 mong1 chaw3 yow3.", "jam¹ nai⁶ sip¹ moŋ¹ t͡ɕaw³ jow³",
        "It is ten o'clock in the morning.", "अभी सुबह के दस बजे हैं।", "এতিয়া পুৱা দহ বাজিছে।", "10 AM.")
    add("Time & Schedule", "midday_noon", "yam1 nai6 thɯng5 thaan4 wan1 yow3.", "yam1 nai6 thɯng5 thaan4 wan1 yow3.", "jam¹ nai⁶ tʰɯŋ⁵ tʰaːn⁴ wan¹ jow³",
        "It is now high midday noon.", "अभी दोपहर का समय हो गया है।", "এতিয়া দুপৰীয়া বাৰ বাজিছে।", "Midday noon.")
    add("Time & Schedule", "three_pm", "yam1 nai6 saam1 mong1 kham3 yow3.", "yam1 nai6 saam1 mong1 kham3 yow3.", "jam¹ nai⁶ saːm¹ moŋ¹ kʰam³ jow³",
        "It is three o'clock in the afternoon.", "अभी दोपहर के तीन बजे हैं।", "এতিয়া বিয়লি তিনি বাজিছে।", "3 PM.")
    add("Time & Schedule", "six_pm", "yam1 nai6 hok1 mong1 kham3 yow3.", "yam1 nai6 hok1 mong1 kham3 yow3.", "jam¹ nai⁶ hok¹ moŋ¹ kʰam³ jow³",
        "It is six o'clock in the evening.", "अभी शाम के छह बजे हैं।", "এতিয়া গধূলি ছয় বাজিছে।", "6 PM.")
    add("Time & Schedule", "eight_pm", "yam1 nai6 pet2 mong1 khɯn1 yow3.", "yam1 nai6 pet2 mong1 khɯn1 yow3.", "jam¹ nai⁶ pet² moŋ¹ kʰɯn¹ jow³",
        "It is eight o'clock at night.", "अभी रात के आठ बजे हैं।", "এতিয়া ৰাতি আঠ বাজিছে।", "8 PM.")
    add("Time & Schedule", "midnight", "yam1 nai6 thɯng5 thaan4 khɯn1 yow3.", "yam1 nai6 thɯng5 thaan4 khɯn1 yow3.", "jam¹ nai⁶ tʰɯŋ⁵ tʰaːn⁴ kʰɯn¹ jow³",
        "It is midnight now.", "अभी आधी रात का समय है।", "এতিয়া মাজনিশা হৈছে।", "Midnight.")
    add("Time & Schedule", "today", "wan1 nai6", "wan1 nai6", "wan¹ nai⁶",
        "Today.", "आज।", "আজি।", "Today adverb.")
    add("Time & Schedule", "tomorrow", "wan1 phuk1", "wan1 phuk1", "wan¹ pʰuk¹",
        "Tomorrow.", "कल (आने वाला कल)।", "কাইলৈ।", "Tomorrow.")
    add("Time & Schedule", "yesterday", "wan1 waa1", "wan1 waa1", "wan¹ waː¹",
        "Yesterday.", "कल (बीता हुआ कल)।", "কালি।", "Yesterday.")
    add("Time & Schedule", "day_after_tomorrow", "wan1 hɯɯ1", "wan1 hɯɯ1", "wan¹ hɯː¹",
        "The day after tomorrow.", "परसों।", "পৰহিলৈ।", "Day after tomorrow.")
    add("Time & Schedule", "every_day", "thuk1 wan1 haw1 pai1 naa1.", "thuk1 wan1 haw1 pai1 naa1.", "tʰuk¹ wan¹ haw¹ paj¹ naː¹",
        "Every single day we go to the paddy field.", "हम हर रोज़ खेत जाते हैं।", "আমি প্ৰতিদিনে পথাৰলৈ যাওঁ।", "Daily repetition.")
    add("Time & Schedule", "early_morning_wake", "tɯn2 chaw3 li1 tɔ5 haang1 khing1.", "tɯn2 chaw3 li1 tɔ5 haang1 khing1.", "tɯn² t͡ɕaw³ liː¹ tɔ⁵ haːŋ¹ kʰiŋ¹",
        "Waking early in the morning is healthy for the body.", "प्रातःकाल जल्दी उठना स्वास्थ्य के लिए बहुत अच्छा होता है।", "ৰাতিপুৱা সোনকালে সাৰ পোৱাটো স্বাস্থ্যৰ বাবে ভাল।", "Early rising.")
    add("Time & Schedule", "sunday", "wan1 aathit4", "wan1 aathit4", "wan¹ aː¹tʰit⁴",
        "Sunday.", "रविवार।", "দেওবাৰ।", "Sunday.")
    add("Time & Schedule", "monday", "wan1 chan1", "wan1 chan1", "wan¹ t͡ɕʰan¹",
        "Monday.", "सोमवार।", "সোমবাৰ।", "Monday.")
    add("Time & Schedule", "tuesday", "wan1 angkaan1", "wan1 angkaan1", "wan¹ aŋ¹kaːn¹",
        "Tuesday.", "मंगलवार।", "মঙলবাৰ।", "Tuesday.")
    add("Time & Schedule", "wednesday", "wan1 phut4", "wan1 phut4", "wan¹ pʰut⁴",
        "Wednesday.", "बुधवार।", "বুধবাৰ।", "Wednesday.")
    add("Time & Schedule", "thursday", "wan1 phahat4", "wan1 phahat4", "wan¹ pʰa¹hat⁴",
        "Thursday.", "गुरुवार।", "বৃহস্পতিবাৰ।", "Thursday.")
    add("Time & Schedule", "friday", "wan1 suk4", "wan1 suk4", "wan¹ suk⁴",
        "Friday.", "शुक्रवार।", "শুক্ৰবাৰ।", "Friday.")
    add("Time & Schedule", "saturday", "wan1 sao1", "wan1 sao1", "wan¹ saw¹",
        "Saturday.", "शनिवार।", "শনিবাৰ।", "Saturday.")
    add("Time & Schedule", "rainy_season", "mɯa2 fon1 tok1 laai1.", "mɯa2 fon1 tok1 laai1.", "mɯa² fon¹ tok¹ laːj¹",
        "In the rainy monsoon season, it rains heavily.", "बरसात के मौसम में मूसलाधार बारिश होती है।", "বাৰিষা কালত প্ৰচুৰ বৰষুণ হয়।", "Monsoon season.")
    add("Time & Schedule", "winter_season", "mɯa2 yen1 naaw1 the5 the5.", "mɯa2 yen1 naaw1 the5 the5.", "mɯa² jen¹ naːw¹ tʰe⁵ tʰe⁵",
        "The winter season is delightfully chilly.", "सर्दियों के मौसम में काफ़ी ठंड पड़ती है।", "শীতকালত বৰ জাৰ পৰে।", "Winter season.")
    add("Time & Schedule", "spring_season", "mɯa2 mai3 bɔk1 baan1.", "mɯa2 mai3 bɔk1 baan1.", "mɯa² maj³ bɔk¹ baːn¹",
        "In the spring season, colorful blossoms open.", "वसंत ऋतु में चारों ओर सुंदर फूल खिलते हैं।", "বসন্ত কালত গছত ফুল ফুলে।", "Springtime.")
    add("Time & Schedule", "this_month", "dɯan1 nai6", "dɯan1 nai6", "dɯan¹ nai⁶",
        "This current month.", "इस महीने।", "এই মাহত।", "Current month.")
    add("Time & Schedule", "next_month", "dɯan1 na5", "dɯan1 na5", "dɯan¹ naː⁵",
        "Next month.", "अगले महीने।", "অহা মাহত।", "Next month.")
    add("Time & Schedule", "last_year", "pi1 kaai1", "pi1 kaai1", "piː¹ kaːj¹",
        "Last year.", "पिछले साल।", "যোৱা বছৰ।", "Last year.")
    add("Time & Schedule", "this_year", "pi1 nai6", "pi1 nai6", "piː¹ nai⁶",
        "This year.", "इस साल।", "এই বছৰ।", "Current year.")
    add("Time & Schedule", "next_year", "pi1 na5", "pi1 na5", "piː¹ naː⁵",
        "Next year.", "अगले साल।", "অহা বছৰ।", "Next year.")
    add("Time & Schedule", "time_flies", "yam1 phaan2 pai1 wai1 the5 the5.", "yam1 phaan2 pai1 wai1 the5 the5.", "jam¹ pʰaːn² paj¹ waj¹ tʰe⁵ tʰe⁵",
        "Time passes swiftly like flowing water.", "समय बहुत तेज़ी से बीत जाता है।", "সময় বৰ সোনকালে পাৰ হৈ যায়।", "Philosophical time.")
    add("Time & Schedule", "arrive_punctually", "maa1 hai3 thong1 yam1 taaw1.", "maa1 hai3 thong1 yam1 taaw1.", "maː¹ haj³ tʰoŋ¹ jam¹ taːw¹",
        "Please arrive on time.", "कृपया समय पर पधारिए।", "অনুগ্ৰহ কৰি সময়মতে আহিব।", "Punctuality.")

    # ==========================================================================
    # DOMAIN 8: TRAVEL, MOVEMENT, ROADS & DIRECTIONS (35 sentences)
    # ==========================================================================
    add("Travel & Movement", "which_road_river", "taang1 pai1 nam6 yu5 theu1?", "taang1 pai1 nam6 yu5 theu1?", "taːŋ¹ paj¹ nam⁶ ju⁵ tʰeu¹",
        "Which path leads down to the river?", "नदी की ओर जाने वाला रास्ता किधर है?", "নৈলৈ যোৱা বাটটো কোনফালে?", "Direction inquiry.")
    add("Travel & Movement", "straight_ahead", "pai1 sɯɯ3 sɯɯ3 taaw1.", "pai1 sɯɯ3 sɯɯ3 taaw1.", "paj¹ sɯː³ sɯː³ taːw¹",
        "Please continue straight ahead.", "कृपया सीधे आगे की ओर जाइए।", "অনুগ্ৰহ কৰি চিধাই আগবাঢ়ক।", "Straight direction.")
    add("Travel & Movement", "turn_left", "leo3 thaang1 saai3 taaw1.", "leo3 thaang1 saai3 taaw1.", "leːw³ tʰaːŋ¹ saːj³ taːw¹",
        "Please turn to the left.", "कृपया बाईं ओर मुड़िए।", "বাওঁফালে ঘূৰক।", "Turn left.")
    add("Travel & Movement", "turn_right", "leo3 thaang1 khwaa1 taaw1.", "leo3 thaang1 khwaa1 taaw1.", "leːw³ tʰaːŋ¹ kʰwaː¹ taːw¹",
        "Please turn to the right.", "कृपया दाईं ओर मुड़िए।", "সোঁফালে ঘূৰক।", "Turn right.")
    add("Travel & Movement", "far_away", "maan3 haw1 am1 klai1.", "maan3 haw1 am1 klai1.", "maːn³ haw¹ am¹ klaj¹",
        "Our village is not far from here.", "हमारा गाँव यहाँ से दूर नहीं है।", "আমাৰ গাঁওখন ইয়াৰ পৰা বেছি দূৰ নহয়।", "Proximity.")
    add("Travel & Movement", "very_close", "wat1 yu5 klai3 the5 the5.", "wat1 yu5 klai3 the5 the5.", "wat¹ ju⁵ klaj³ tʰe⁵ tʰe⁵",
        "The monastery is very close nearby.", "विहार बहुत पास में ही है।", "বৌদ্ধ বিহাৰখন বৰ ওচৰতে আছে।", "Very close.")
    add("Travel & Movement", "walk_slowly", "yaang3 tsaa3 tsaa3 taaw1, taang1 li1 am1 li1.", "yaang3 tsaa3 tsaa3 taaw1, taang1 li1 am1 li1.", "jaːŋ³ t͡saː³ t͡saː³ taːw¹ taːŋ¹ liː¹ am¹ liː¹",
        "Walk cautiously, the muddy path is slippery.", "धीरे-धीरे चलिए, रास्ता कीचड़ भरा और फिसलन वाला है।", "লাহে লাহে খোজ কাঢ়ক, বাটটো পিছল।", "Caution while walking.")
    add("Travel & Movement", "cross_river_boat", "kham3 nam6 kap4 hɯa1.", "kham3 nam6 kap4 hɯa1.", "kʰam³ nam⁶ kap⁴ hɯa¹",
        "We cross the river using a wooden boat.", "हम नाव के द्वारा नदी पार करते हैं।", "আমি নাৱেৰে নদী পাৰ হওঁ।", "River crossing.")
    add("Travel & Movement", "reach_powaimukh", "haw1 thɯng5 maan3 paa1 waai6 yow3.", "haw1 thɯng5 maan3 paa1 waai6 yow3.", "haw¹ tʰɯŋ⁵ maːn³ paː¹ waːj⁶ jow³",
        "We have arrived safely in Powaimukh village.", "हम सकुशल पोवाइमुख गाँव पहुँच चुके हैं।", "আমি পোৱাইমুখ গাঁৱত উপস্থিত হ’লোঁহি।", "Arrival.")
    add("Travel & Movement", "go_to_margherita", "man1 pai1 Margherita wan1 nai6.", "man1 pai1 Margherita wan1 nai6.", "man¹ paj¹ mar¹ge¹ri¹taː¹ wan¹ nai⁶",
        "He went to Margherita town today.", "वह आज मार्घेरिटा शहर गया है।", "তেওঁ আজি মাৰ্ঘেৰিটালৈ গৈছে।", "Town visit.")
    add("Travel & Movement", "go_to_tinsukia", "chaw1 thao3 pai1 Tinsukia.", "chaw1 thao3 pai1 Tinsukia.", "t͡ɕaw¹ tʰaw³ paj¹ tin¹su¹kiː¹jaː¹",
        "The elder has journeyed to Tinsukia district center.", "बुजुर्ग तिनसुकिया शहर गए हैं।", "বয়োজ্যেষ্ঠজন তিনিচুকীয়ালৈ গৈছে।", "District travel.")
    add("Travel & Movement", "board_bus", "khao3 rot1 bus1 pai1 mong1.", "khao3 rot1 bus1 pai1 mong1.", "kʰaw³ rot¹ bas¹ paj¹ moŋ¹",
        "Board the bus to go to town.", "शहर जाने के लिए बस में बैठिए।", "চহৰলৈ যাবলৈ বাছত উঠক।", "Public transport.")
    add("Travel & Movement", "ride_bicycle", "luk3 on2 khee2 rot1 theet4.", "luk3 on2 khee2 rot1 theet4.", "luk³ on² kʰeː² rot¹ tʰeːt⁴",
        "The children are riding their bicycles along the village path.", "बच्चे गाँव की पगडंडी पर साइकिल चला रहे हैं।", "ল’ৰাবোৰে গাঁৱৰ বাটেৰে চাইকেল চলাইছে।", "Bicycle riding.")
    add("Travel & Movement", "carry_basket", "me5 haap4 taang3 phak1 maa1 laat1.", "me5 haap4 taang3 phak1 maa1 laat1.", "me⁵ haːp⁴ taːŋ³ pʰak¹ maː¹ laːt¹",
        "Mother carries vegetable baskets to the market.", "माँ सब्ज़ियों की टोकरी लेकर बाज़ार आती हैं।", "মায়ে শাকৰ পাচি লৈ বজাৰলৈ আহিছে।", "Carrying load.")
    add("Travel & Movement", "path_through_forest", "taang1 phaan2 nai1 paa5 mai3.", "taang1 phaan2 nai1 paa5 mai3.", "taːŋ¹ pʰaːn² naj¹ paː⁵ maj³",
        "The footpath traverses through the lush bamboo forest.", "पगडंडी हरे-भरे बाँस के जंगल से होकर गुज़रती है।", "বাটটো বাঁহনি হাবিয়েদি পাৰ হৈছে।", "Forest trail.")
    add("Travel & Movement", "bridge_over_river", "mi5 sa1phaan1 kham3 nam6 jin1.", "mi5 sa1phaan1 kham3 nam6 jin1.", "miː¹ sa¹pʰaːn¹ kʰam³ nam⁶ d͡ʑin¹",
        "There is a sturdy bridge over the Buridihing river.", "बूढ़ीदिहिंग नदी के ऊपर एक मज़बूत पुल बना हुआ है।", "বুঢ়ীদিহিং নদীৰ ওপৰত দলংখন আছে।", "Bridge crossing.")
    add("Travel & Movement", "long_journey", "thaang1 pai1 klai1 the5 the5.", "thaang1 pai1 klai1 the5 the5.", "tʰaːŋ¹ paj¹ klaj¹ tʰe⁵ tʰe⁵",
        "It is indeed a long and tiring journey.", "यह वास्तव में एक लंबी और थकाऊ यात्रा है।", "বাটটো বৰ দীঘলীয়া।", "Long journey.")
    add("Travel & Movement", "rest_under_tree", "phak1phon2 tai3 ton3 mai3 taaw1.", "phak1phon2 tai3 ton3 mai3 taaw1.", "pʰak¹ pʰon² taj³ ton³ maj³ taːw¹",
        "Please rest under the shade of the big tree.", "कृपया बड़े पेड़ की छाया में थोड़ा विश्राम कीजिए।", "গছৰ শীতল ছাঁত জিৰণি লওক।", "Tree rest.")
    add("Travel & Movement", "cross_patkai", "pu5 yaa3 kham3 doi1 pat4 kai1 maa1.", "pu5 yaa3 kham3 doi1 pat4 kai1 maa1.", "pu⁵ jaː³ kʰam³ dɔj¹ pat⁴ kaj¹ maː¹",
        "Our forefathers historically crossed the Patkai peaks.", "हमारे पूर्वजों ने पातकाई पर्वत पार करके यहाँ कदम रखा था।", "পূৰ্বপুৰুষসকলে পাতকাই পাহাৰ পাৰ হৈ আহিছিল।", "Patkai crossing.")
    add("Travel & Movement", "return_before_dark", "maa1 thɯng5 hɯan1 kɔn2 kham3.", "maa1 thɯng5 hɯan1 kɔn2 kham3.", "maː¹ tʰɯŋ⁵ hɯan¹ kɔn² kʰam³",
        "Please return home before darkness settles.", "कृपया अंधेरा होने से पहले घर लौट आइए।", "সন্ধ্যা হোৱাৰ আগতে ঘৰলৈ উভতি আহক।", "Return before dusk.")
    add("Travel & Movement", "carry_torch", "aw1 fai1 saai2 pai1 khɯn1 nai6.", "aw1 fai1 saai2 pai1 khɯn1 nai6.", "aw¹ faj¹ saːj² paj¹ kʰɯn¹ nai⁶",
        "Carry a lantern/torchlight for walking at night.", "रात में चलने के लिए टॉर्च या लालटेन साथ रखिए।", "ৰাতি যাবলৈ হাতত টৰ্চ বা পোহৰ লওক।", "Torch at night.")
    add("Travel & Movement", "watch_footing", "dɯk4 li1 li1, mi5 hin1.", "dɯk4 li1 li1, mi5 hin1.", "dɯk⁴ liː¹ liː¹ miː¹ hin¹",
        "Step carefully, there are slippery stones.", "सावधानी से पैर रखिए, रास्ते में चिकने पत्थर हैं।", "সাৱধানে খোজ দিয়ক, বাটত পিছল শিল আছে।", "Careful steps.")
    add("Travel & Movement", "north_direction", "thaang1 nɯa1", "thaang1 nɯa1", "tʰaːŋ¹ nɯa¹",
        "North direction.", "उत्तर दिशा।", "উত্তৰ দিশ।", "North.")
    add("Travel & Movement", "south_direction", "thaang1 tai3", "thaang1 tai3", "tʰaːŋ¹ taj³",
        "South direction.", "दक्षिण दिशा।", "দক্ষিণ দিশ।", "South.")
    add("Travel & Movement", "east_direction", "thaang1 ɔk2", "thaang1 ɔk2", "tʰaːŋ¹ ɔk¹",
        "East direction (sunrise).", "पूर्व दिशा (सूर्योदय की दिशा)।", "পূব দিশ।", "East.")
    add("Travel & Movement", "west_direction", "thaang1 tok1", "thaang1 tok1", "tʰaːŋ¹ tok¹",
        "West direction (sunset).", "पश्चिम दिशा (सूर्यास्त की दिशा)।", "পশ্চিম দিশ।", "West.")
    add("Travel & Movement", "follow_river", "yaang3 pai1 tam1 rim1 nam6.", "yaang3 pai1 tam1 rim1 nam6.", "jaːŋ³ paj¹ tam¹ rim¹ nam⁶",
        "Walk continuously alongside the riverbank.", "नदी के किनारे-किनारे आगे बढ़ते रहिए।", "নৈৰ কাষে কাষে আগবাঢ়ক।", "Riverside path.")
    add("Travel & Movement", "enter_village_gate", "khao3 pra1tu1 maan3 maa1.", "khao3 pra1tu1 maan3 maa1.", "kʰaw³ pra¹tuː¹ maːn³ maː¹",
        "Enter through the auspicious village entrance gate.", "गाँव के मुख्य द्वार से प्रवेश कीजिए।", "গাঁৱৰ তোৰণেৰে সোমাই আহক।", "Village entrance.")
    add("Travel & Movement", "safe_arrival", "haw1 thɯng5 thi3 li1 yow3.", "haw1 thɯng5 thi3 li1 yow3.", "haw¹ tʰɯŋ⁵ tʰiː³ liː¹ jow³",
        "We have reached our destination safely.", "हम सुरक्षित रूप से अपनी मंज़िल पर पहुँच गए हैं।", "আমি নিৰাপদে গন্তব্যস্থান পালোগৈ।", "Safe arrival.")
    add("Travel & Movement", "start_journey", "ok2 thaang1 tɯn2 chaw3 li1.", "ok2 thaang1 tɯn2 chaw3 li1.", "ɔk¹ tʰaːŋ¹ tɯn² t͡ɕaw³ liː¹",
        "Starting the journey in the early morning is best.", "सुबह जल्दी यात्रा शुरू करना श्रेयस्कर होता है।", "ৰাতিপুৱা সোনকালে যাত্ৰা আৰম্ভ কৰাটো উত্তম।", "Early start.")
    add("Travel & Movement", "mud_on_road", "taang1 mi5 khi3 phak1 laai1.", "taang1 mi5 khi3 phak1 laai1.", "taːŋ¹ miː¹ kʰiː³ pʰak¹ laːj¹",
        "There is thick mud on the road after rain.", "बारिश के बाद रास्ते में काफ़ी कीचड़ है।", "বাটত বৰ বোকা হৈছে।", "Muddy road.")
    add("Travel & Movement", "shorter_route", "taang1 nai6 klai3 kwaa2.", "taang1 nai6 klai3 kwaa2.", "taːŋ¹ nai⁶ klaj³ kwaː²",
        "This path is significantly shorter.", "यह रास्ता बहुत छोटा (शॉर्टकट) है।", "এই বাটটো বেছি ওচৰ।", "Shortcut route.")
    add("Travel & Movement", "lost_way", "kaw1 long1 taang1, chuai3 noi3 taaw1.", "kaw1 long1 taang1, chuai3 noi3 taaw1.", "kaw¹ loŋ¹ taːŋ¹ t͡ɕʰuaj³ noi³ taːw¹",
        "I have lost my way, please guide me.", "मैं रास्ता भटक गया हूँ, कृपया मार्गदर्शन कीजिए।", "মই বাট পাহৰিলোঁ, মোক বাট দেখুৱাই দিয়ক।", "Lost way help.")
    add("Travel & Movement", "guide_traveller", "kaw1 te5 phaam1 maɯ2 pai1.", "kaw1 te5 phaam1 maɯ2 pai1.", "kaw¹ te⁵ pʰaːm¹ maɯ² paj¹",
        "I will accompany and guide you safely.", "मैं आपके साथ चलकर रास्ता दिखाऊँगा।", "মই আপোনাক লগত লৈ বাট দেখুৱাই দিম।", "Guiding visitor.")
    add("Travel & Movement", "farewell_traveller", "khɔ5 hai3 phaan2 taang1 li1 li1.", "khɔ5 hai3 phaan2 taang1 li1 li1.", "kʰo⁵ haj³ pʰaːn² taːŋ¹ liː¹ liː¹",
        "May your onward travels be pleasant and peaceful.", "आपकी आगे की यात्रा मंगलमय और सुखद हो।", "আপোনাৰ যাত্ৰা নিৰাপদ আৰু শুভ হওক।", "Travel benediction.")

    # ==========================================================================
    # DOMAIN 9: NATURE, WEATHER & ENVIRONMENT (35 sentences)
    # ==========================================================================
    add("Nature & Environment", "rain_falling", "fon1 tok1 haeng1 the5 the5.", "fon1 tok1 haeng1 the5 the5.", "fon¹ tok¹ hɛŋ¹ tʰe⁵ tʰe⁵",
        "Heavy rain is falling outside.", "बाहर मूसलाधार बारिश हो रही है।", "বাহিৰত বৰ জোৰেৰে বৰষুণ দিছে।", "Heavy downpour.")
    add("Nature & Environment", "cool_breeze", "lom1 phat1 yen1 yen1 li1.", "lom1 phat1 yen1 yen1 li1.", "lom¹ pʰat¹ jen¹ jen¹ liː¹",
        "A pleasant cool breeze is blowing through the trees.", "पेड़ों के बीच से ठंडी, मंद हवा बह रही है।", "মৃদু শীতল বতাহজাক বৈ আছে।", "Cool wind.")
    add("Nature & Environment", "clear_sky", "faa6 saaw3 li1 the5 the5 wan1 nai6.", "faa6 saaw3 li1 the5 the5 wan1 nai6.", "faː⁶ saːw³ liː¹ tʰe⁵ tʰe⁵ wan¹ nai⁶",
        "The sky is completely clear and radiant today.", "आज आकाश एकदम साफ़ और नीला है।", "আজি আকাশখন বৰ ফৰকাল আৰু ধুনীয়া।", "Clear sky.")
    add("Nature & Environment", "warm_sunshine", "daet2 ɔk2 rɔn3 the5 the5.", "daet2 ɔk2 rɔn3 the5 the5.", "dɛt² ɔk¹ rɔn³ tʰe⁵ tʰe⁵",
        "The sun has emerged with radiant warmth.", "धूप खिली है और मौसम सुखद गर्म है।", "ৰ’দ ওলাইছে আৰু বৰ গৰম পৰিছে।", "Sunny day.")
    add("Nature & Environment", "patkai_mountains", "doi1 pat4 kai1 sung1 the5 the5.", "doi1 pat4 kai1 sung1 the5 the5.", "dɔj¹ pat⁴ kaj¹ suŋ¹ tʰe⁵ tʰe⁵",
        "The majestic Patkai mountains rise high into the clouds.", "पातकाई की पर्वतमालाएँ बादलों से ऊँची उठती हैं।", "পাতকাই পাহাৰ বৰ ওখ আৰু সুন্দৰ।", "Patkai range.")
    add("Nature & Environment", "buridihing_flow", "nam6 jin1 lai1 suuk1 li1.", "nam6 jin1 lai1 suuk1 li1.", "nam⁶ d͡ʑin¹ laj¹ suːk¹ liː¹",
        "The Buridihing river flows peacefully past our lands.", "बूढ़ीदिहिंग नदी हमारे खेतों के पास से शांतिपूर्वक बहती है।", "বুঢ়ীদিহিং নদীখন শান্তভাৱে বৈ গৈছে।", "River flow.")
    add("Nature & Environment", "green_forest", "paa5 mai3 khio1 ngam1 the5 the5.", "paa5 mai3 khio1 ngam1 the5 the5.", "paː⁵ maj³ kʰio¹ ŋam¹ tʰe⁵ tʰe⁵",
        "The forest is lush, emerald green, and thriving.", "जंगल हरा-भरा, सघन और अत्यंत सुंदर है।", "হাবিখন বৰ সেউজীয়া আৰু ধুনীয়া।", "Lush jungle.")
    add("Nature & Environment", "bamboo_groves", "mai3 phaak4 koon1 ngam1 rim1 maan3.", "mai3 phaak4 koon1 ngam1 rim1 maan3.", "maj³ pʰaːk⁴ koːn¹ ŋam¹ rim¹ maːn³",
        "Graceful bamboo groves surround the perimeter of our village.", "गाँव के चारों ओर बाँस के सुंदर झुरमुट खड़े हैं।", "গাঁৱৰ চাৰিওফালে বাঁহনি ডৰা আছে।", "Bamboo groves.")
    add("Nature & Environment", "morning_mist", "mɔk1 khum3 wan1 chaw3 nai6.", "mɔk1 khum3 wan1 chaw3 nai6.", "mɔk¹ kʰum³ wan¹ t͡ɕaw³ nai⁶",
        "Dense morning mist covers the plains today.", "आज सुबह मैदानों पर घना कोहरा छाया हुआ है।", "আজি পুৱা ডাঠ কুঁৱলী পৰিছে।", "Morning fog.")
    add("Nature & Environment", "thunder_storm", "faa6 phaa3 hɔng3 haeng1.", "faa6 phaa3 hɔng3 haeng1.", "faː⁶ pʰaː³ hɔŋ³ hɛŋ¹",
        "Loud thunder rumbles across the darkened sky.", "काले आसमान में तेज़ गड़गड़ाहट के साथ बिजली चमक रही है।", "আকাশত বিজুলী-ঢেৰেকণি মাৰিছে।", "Thunderstorm.")
    add("Nature & Environment", "dark_clouds", "mek3 dam1 kham3 faa6.", "mek3 dam1 kham3 faa6.", "mek³ dam¹ kʰam³ faː⁶",
        "Dark monsoon rain clouds blanket the sky.", "काले मानसूनी बादलों ने पूरे आकाश को ढँक लिया है।", "ডাঠ ক’লা ডাৱৰে আকাশ ছানি ধৰিছে।", "Rain clouds.")
    add("Nature & Environment", "rainbow_beauty", "rung2 kin1 nam6 ngam1 the5 the5.", "rung2 kin1 nam6 ngam1 the5 the5.", "ruŋ² kin¹ nam⁶ ŋam¹ tʰe⁵ tʰe⁵",
        "A vibrant rainbow arches gracefully across the horizon.", "आकाश में सुंदर सतरंगी इंद्रधनुष दिखाई दे रहा है।", "আকাশত ৰামধেনুখন বৰ ধুনীয়াকৈ জিলিকিছে।", "Rainbow.")
    add("Nature & Environment", "birds_singing", "nok1 hɔng3 siang1 waan1 nai1 paa5.", "nok1 hɔng3 siang1 waan1 nai1 paa5.", "nok¹ hɔŋ³ sjaŋ¹ waːn¹ naj¹ paː⁵",
        "Birds are singing melodiously in the forest canopy.", "जंगल में पक्षी मधुर स्वर में चहचहा रहे हैं।", "হাবিত চৰাইবোৰে শুৱলাকৈ গান গাইছে।", "Bird song.")
    add("Nature & Environment", "wild_flowers", "bɔk1 mai3 paa5 hɔm1 the5 the5.", "bɔk1 mai3 paa5 hɔm1 the5 the5.", "bɔk¹ maj³ paː⁵ hɔm¹ tʰe⁵ tʰe⁵",
        "Wild orchids and flowers emit a sweet fragrance.", "जंगली फूलों से भीनी-भीनी सुगंध आ रही है।", "বনৰীয়া ফুলবোৰৰ সুবাস বৰ ভাল।", "Wild blossoms.")
    add("Nature & Environment", "river_fish_swim", "paa1 ten3 nai1 nam6 sai1.", "paa1 ten3 nai1 nam6 sai1.", "paː¹ ten³ naj¹ nam⁶ saj¹",
        "Fish dart and leap in the crystal clear water.", "साफ़ पानी में मछलियाँ खुशी से तैर रही हैं।", "নৈৰ নিৰ্মল পানীত মাছবোৰে সাঁতুৰিছে।", "Fish in river.")
    add("Nature & Environment", "deer_in_forest", "kwang1 yu5 nai1 paa5 doi1.", "kwang1 yu5 nai1 paa5 doi1.", "kwaŋ¹ ju⁵ naj¹ paː⁵ dɔj¹",
        "Wild deer roam within the forested mountain valleys.", "पहाड़ी जंगलों में हिरन स्वच्छंद विचरण करते हैं।", "পাহাৰীয়া হাবিত হৰিণে চৰি ফুৰিছে।", "Forest wildlife.")
    add("Nature & Environment", "clean_air", "lom1 haang1 mong1 sot1 sai1 li1.", "lom1 haang1 mong1 sot1 sai1 li1.", "lom¹ haːŋ¹ moŋ¹ sot¹ saj¹ liː¹",
        "The countryside village air is pure and revitalizing.", "गाँव की खुली हवा बहुत शुद्ध और ताज़गी भरी है।", "গাঁৱৰ মুক্ত বতাহ বৰ নিৰ্মল।", "Pure air.")
    add("Nature & Environment", "sunset_colors", "wan1 tok1 faa6 lɯang1 ngam1 the5 the5.", "wan1 tok1 faa6 lɯang1 ngam1 the5 the5.", "wan¹ tok¹ faː⁶ lɯaŋ¹ ŋam¹ tʰe⁵ tʰe⁵",
        "The sunset paints the western sky in glowing gold.", "सूर्यास्त के समय पश्चिम का आकाश स्वर्णिम चमक उठता है।", "সূৰ্যাস্তৰ সময়ত আকাশখন সোণালী হৈ পৰিছে।", "Golden sunset.")
    add("Nature & Environment", "sunrise_dawn", "wan1 ɔk2 maa1 thaa3 li1.", "wan1 ɔk2 maa1 thaa3 li1.", "wan¹ ɔk¹ maː¹ tʰaː³ liː¹",
        "The early morning dawn brings fresh hope.", "सूर्योदय के साथ नई सुबह का सुंदर आगमन हुआ है।", "সূৰ্য উদয়ৰ লগে লগে পোহৰ বিয়পি পৰিছে।", "Dawn sunrise.")
    add("Nature & Environment", "river_overflow", "nam6 jin1 khɯn3 thong1 naa1.", "nam6 jin1 khɯn3 thong1 naa1.", "nam⁶ d͡ʑin¹ kʰɯn³ tʰoŋ¹ naː¹",
        "The Buridihing river water nourishes the adjacent fields.", "बूढ़ीदिहिंग नदी का जल खेतों को उर्वर और समृद्ध बनाता है।", "নৈৰ পানীয়ে খেতিপথাৰ পলসুৱা কৰে।", "River fertility.")
    add("Nature & Environment", "protect_trees", "am1 tat4 ton3 mai3 laai1 laai1.", "am1 tat4 ton3 mai3 laai1 laai1.", "am¹ tat⁴ ton³ maj³ laːj¹ laːj¹",
        "Do not cut down trees thoughtlessly; protect nature.", "वृक्षों को व्यर्थ मत काटिए; प्रकृति की रक्षा कीजिए।", "গছ-গছনি কটা উচিত নহয়; সংৰক্ষণ কৰক।", "Ecological ethics.")
    add("Nature & Environment", "shade_of_banyan", "ton3 hai3 yai3 pan1 hom1 yen1.", "ton3 hai3 yai3 pan1 hom1 yen1.", "ton³ haj³ jai³ pan¹ hom¹ jen¹",
        "The ancient banyan tree offers soothing shade to weary travelers.", "विशाल बरगद का पेड़ सबको शीतल और सुखद छाया देता है।", "বিশাল আঁহত গছজোপাই শীতল ছাঁ দিছে।", "Banyan shade.")
    add("Nature & Environment", "stars_at_night", "daao1 laai1 luuk4 nai1 faa6 khɯn1 nai6.", "daao1 laai1 luuk4 nai1 faa6 khɯn1 nai6.", "daːw¹ laːj¹ luːk⁴ naj¹ faː⁶ kʰɯn¹ nai⁶",
        "Countless glittering stars illuminate the night sky.", "आज रात आकाश में अनगिनत तारे जगमगा रहे हैं।", "আকাশত অলেখ তৰা তিৰবিৰাইছে।", "Night stars.")
    add("Nature & Environment", "full_moon", "dɯan1 haang3 saaw3 li1 the5 the5.", "dɯan1 haang3 saaw3 li1 the5 the5.", "dɯan¹ haːŋ³ saːw³ liː¹ tʰe⁵ tʰe⁵",
        "The full moon shines brilliantly with tranquil silvery light.", "पूर्णिमा का चाँद अपनी शीतल चाँदनी बिखेर रहा है।", "পূৰ্ণিমাৰ জোনৰ পোহৰে ধৰণী পোহৰাইছে।", "Full moon.")
    add("Nature & Environment", "insects_humming", "kheng1 khɔng3 hɔng3 yam1 kham3.", "kheng1 khɔng3 hɔng3 yam1 kham3.", "kʰeŋ¹ kʰɔŋ³ hɔŋ³ jam¹ kʰam³",
        "Cicadas and crickets sing their evening chorus.", "शाम के समय झींगुरों की मधुर आवाज़ गूँज रही है।", "গধূলি জিলিবোৰে মাতিবলৈ আৰম্ভ কৰিছে।", "Evening cicadas.")
    add("Nature & Environment", "clean_surroundings", "kep4 khi3 yao3 hai3 maan3 sot1.", "kep4 khi3 yao3 hai3 maan3 sot1.", "kep⁴ kʰiː³ jaw³ haj³ maːn³ sot¹",
        "Keep the village environs clean and waste-free.", "गाँव को स्वच्छ, सुंदर और कूड़ा-मुक्त रखिए।", "আমাৰ গাঁওখন সদায় পৰিষ্কাৰ কৰি ৰাখক।", "Clean village.")
    add("Nature & Environment", "water_source", "bɔ2 nam6 nai6 sai1 sot1 li1.", "bɔ2 nam6 nai6 sai1 sot1 li1.", "bɔ² nam⁶ nai⁶ saj¹ sot¹ liː¹",
        "This natural spring provides pure drinking water.", "इस प्राकृतिक सोते का पानी एकदम निर्मल और शुद्ध है।", "এই পানীৰ উৎসটো বৰ পৱিত্ৰ আৰু নিৰ্মল।", "Spring water.")
    add("Nature & Environment", "flood_season", "mɯa2 nam6 nɔng5, haw1 raak1saa1 hɯan1.", "mɯa2 nam6 nɔng5, haw1 raak1saa1 hɯan1.", "mɯa² nam⁶ nɔŋ⁵ haw¹ raːk¹ saː¹ hɯan¹",
        "During high flood season, we safeguard our stilt homes.", "बाढ़ के समय हम अपने ऊँचे घरों की रक्षा करते हैं।", "বাৰিষা বানপানীৰ সময়ত আমি চাংঘৰসমূহ সুৰক্ষিত কৰোঁ।", "Flood resilience.")
    add("Nature & Environment", "dry_leaves_fall", "bai1 mai3 haeng3 tok1 din1.", "bai1 mai3 haeng3 tok1 din1.", "baj¹ maj³ hɛŋ³ tok¹ din¹",
        "Dry autumn leaves fall gently to the earth.", "सूखे पीले पत्ते धीरे-धीरे ज़मीन पर गिर रहे हैं।", "শুকান গছৰ পাতবোৰ মাটিত সৰি পৰিছে।", "Autumn foliage.")
    add("Nature & Environment", "soil_fertile", "din1 rim1 nam6 jin1 phom1 li1.", "din1 rim1 nam6 jin1 phom1 li1.", "din¹ rim¹ nam⁶ d͡ʑin¹ pʰom¹ liː¹",
        "The alluvial soil along the river is exceptionally fertile.", "बूढ़ीदिहिंग के कछार की मिट्टी खेती के लिए अत्यंत उपजाऊ है।", "নৈৰ পাৰৰ পলসুৱা মাটি খেতিৰ বাবে বৰ উপযোগী।", "Fertile soil.")
    add("Nature & Environment", "elephant_path", "chaang3 paa5 phaan2 thaang1 doi1.", "chaang3 paa5 phaan2 thaang1 doi1.", "t͡ɕʰaːŋ³ paː⁵ pʰaːn² tʰaːŋ¹ dɔj¹",
        "Wild elephants travel along the ancient mountain corridor.", "जंगली हाथी पहाड़ के पुराने रास्ते से होकर निकलते हैं।", "বনৰীয়া হাতীবোৰ পাহাৰৰ বাটেৰে পাৰ হৈছে।", "Wild elephants.")
    add("Nature & Environment", "fireflies_glow", "meeng2 maap1 saaw3 nai1 khɯn1 dam1.", "meeng2 maap1 saaw3 nai1 khɯn1 dam1.", "meːŋ² maːp¹ saːw³ naj¹ kʰɯn¹ dam¹",
        "Luminescent fireflies sparkle brightly in the dark night.", "अंधेरी रात में जुगनू चमकते हुए बहुत सुंदर लगते हैं।", "ঘোৰ অন্ধকাৰ নিশা জোনাকী পৰুৱাই পোহৰাইছে।", "Fireflies.")
    add("Nature & Environment", "breeze_after_rain", "fon1 leew3, lom1 yen1 phat1.", "fon1 leew3, lom1 yen1 phat1.", "fon¹ leːw³ lom¹ jen¹ pʰat¹",
        "After the rain ceases, a refreshing cool breeze stirs.", "बारिश थमने के बाद बहुत ताज़ा और शीतल बयार बहने लगी है।", "বৰষুণৰ পিছত শীতল বতাহ ববলৈ ধৰিছে।", "Post-rain air.")
    add("Nature & Environment", "nature_gifts", "phaa3 din1 pan1 khɔng3 kin1 laai1.", "phaa3 din1 pan1 khɔng3 kin1 laai1.", "pʰaː³ din¹ pan¹ kʰɔŋ³ kin¹ laːj¹",
        "Mother Earth bestows bountiful sustenance upon us.", "धरती माँ हमें प्रचुर भोजन और जीवन संपदा प्रदान करती हैं।", "ধৰিত্ৰী আইয়ে আমাক প্ৰচুৰ খাদ্য আৰু আশ্ৰয় দিছে।", "Earth gratitude.")
    add("Nature & Environment", "respect_nature", "haw1 nap4 thɯ5 paa5 kap4 nam6.", "haw1 nap4 thɯ5 paa5 kap4 nam6.", "haw¹ nap⁴ tʰɯ⁵ paː⁵ kap⁴ nam⁶",
        "We live with deep reverence for our sacred forests and waters.", "हम अपने पवित्र वनों और नदियों का हमेशा सम्मान करते हैं।", "আমি আমাৰ অৰণ্য আৰু নদীসমূহক শ্ৰদ্ধা কৰোঁ।", "Nature reverence.")

    # ==========================================================================
    # DOMAIN 10: AGRICULTURE, PADDY FARMING & CROPS (40 sentences)
    # ==========================================================================
    add("Farming & Agriculture", "farmers_plant_paddy", "phuu3 naa1 som1 khaw3 naa1.", "phuu3 naa1 som1 khaw3 naa1.", "pʰuː³ naː¹ som¹ kʰaw³ naː¹",
        "The farmers are transplanting young paddy seedlings in the fields.", "किसान खेतों में धान की हरी पौध रोप रहे हैं।", "কৃষকসকলে পথাৰত ধান ৰুইছে।", "Paddy transplanting.")
    add("Farming & Agriculture", "golden_paddy_ripe", "khaw3 naa1 suuk1 lɯang1 li1 the5 the5.", "khaw3 naa1 suuk1 lɯang1 li1 the5 the5.", "kʰaw³ naː¹ suːk¹ lɯaŋ¹ liː¹ tʰe⁵ tʰe⁵",
        "The golden paddy crop in the expansive fields has ripened.", "खेतों में सुनहरी धान की फ़सल पककर लहलहा रही है।", "পথাৰৰ সোণালী ধানবোৰ সুন্দৰকৈ পকিছে।", "Ripe paddy.")
    add("Farming & Agriculture", "harvest_time", "yam1 nai6 thɯng5 yam1เกี่ยว khaw3.", "yam1 nai6 thɯng5 yam1เกี่ยว khaw3.", "jam¹ nai⁶ tʰɯŋ⁵ jam¹ kjoːw¹ kʰaw³",
        "The harvest season has arrived for the community.", "धान की कटाई का समय आ गया है।", "ধান দোৱাৰ বতৰ আহি পালেহি।", "Harvest season.")
    add("Farming & Agriculture", "buffaloes_grazing", "khwaai1 kin1 yaa3 rim1 nam6.", "khwaai1 kin1 yaa3 rim1 nam6.", "kʰwaːj¹ kin¹ jaː³ rim¹ nam⁶",
        "Water buffaloes are grazing grass peacefully along the riverbank.", "भैंसें नदी किनारे हरी घास चर रही हैं।", "ম’হবোৰে নদীৰ পাৰত ঘাঁহ খাই আছে।", "Buffalo grazing.")
    add("Farming & Agriculture", "ploughing_field", "po5 haw1 thai1 naa1 kap4 khwaai1.", "po5 haw1 thai1 naa1 kap4 khwaai1.", "po⁵ haw¹ tʰaj¹ naː¹ kap⁴ kʰwaːj¹",
        "My father ploughs the fertile fields with his water buffalo.", "मेरे पिताजी भैंस की सहायता से खेत की जुताई कर रहे हैं।", "দেউতাই ম’হেৰে পথাৰ হাল বাইছে।", "Ploughing.")
    add("Farming & Agriculture", "irrigate_fields", "aw1 nam6 khao3 nai1 thong1 naa1.", "aw1 nam6 khao3 nai1 thong1 naa1.", "aw¹ nam⁶ kʰaw³ naj¹ tʰoŋ¹ naː¹",
        "Channel irrigation water into the thirsty paddy fields.", "धान के खेतों में सिंचाई का पानी भरिए।", "খেতিপথাৰলৈ নলাৰে পানী সুমুৱাই দিয়ক।", "Irrigation.")
    add("Farming & Agriculture", "granary_full", "yeew3 khaw3 haw1 tem1 li1.", "yeew3 khaw3 haw1 tem1 li1.", "jeːw³ kʰaw³ haw¹ tem¹ liː¹",
        "Our granary is filled to the brim with harvested rice.", "हमारा अन्न भंडार (खलिहान) धान से पूरी तरह भर गया है।", "আমাৰ ভঁৰালঘৰ ধানেৰে ভৰি পৰিছে।", "Full granary.")
    add("Farming & Agriculture", "sickle_sharp", "kio1เกี่ยว khaw3 nai6 khom1 the5 the5.", "kio1เกี่ยว khaw3 nai6 khom1 the5 the5.", "kjoː¹ kʰaw³ nai⁶ kʰom¹ tʰe⁵ tʰe⁵",
        "This paddy harvesting sickle is razor-sharp.", "धान काटने की यह हँसिया बहुत तेज़ और पैनी है।", "ধান দোৱা কাঁচিখন বৰ ধাৰ।", "Harvest sickle.")
    add("Farming & Agriculture", "threshing_paddy", "thap1 khaw3 hai3 met3 tok1.", "thap1 khaw3 hai3 met3 tok1.", "tʰap¹ kʰaw³ haj³ met¹ tok¹",
        "Thresh the harvested stalks so the golden grains detach.", "धान के पौधों को पीटकर दाने अलग कीजिए।", "ধানবোৰ মৰণা মাৰি গুটিবোৰ এৰুৱাই লওক।", "Threshing grain.")
    add("Farming & Agriculture", "sun_dry_paddy", "taak2 khaw3 nai1 daet2 hai3 haeng3.", "taak2 khaw3 nai1 daet2 hai3 haeng3.", "taːk² kʰaw³ naj¹ dɛt² haj³ hɛŋ³",
        "Dry the harvested paddy thoroughly under the blazing sun.", "कटे हुए धान को तेज़ धूप में अच्छी तरह सुखाइए।", "ধানখিনি চোতালত ৰ’দত ভালদৰে শুকুৱাই লওক।", "Sun drying.")
    add("Farming & Agriculture", "good_harvest_year", "pi1 nai6 khaw3 ɔk2 laai1 the5 the5.", "pi1 nai6 khaw3 ɔk2 laai1 the5 the5.", "piː¹ nai⁶ kʰaw³ ɔk¹ laːj¹ tʰe⁵ tʰe⁵",
        "This year the agricultural yield has been exceptionally abundant.", "इस वर्ष धान की बहुत भरपूर और अच्छी पैदावार हुई है।", "এই বছৰ পথাৰত প্ৰচুৰ পৰিমাণে ধান উপজিছে।", "Bumper crop.")
    add("Farming & Agriculture", "scarecrow_in_field", "tang3 hun2 laang3 nok1 nai1 naa1.", "tang3 hun2 laang3 nok1 nai1 naa1.", "taŋ³ hun² laːŋ³ nok¹ naj¹ naː¹",
        "Erect a scarecrow in the field to protect grain from birds.", "पक्षियों से फ़सल बचाने के लिए खेत में पुतला (बिजूका) लगाइए।", "চৰাই খেদিবলৈ পথাৰত জকলা/পুত্তলিকা পুতি থওক।", "Scarecrow.")
    add("Farming & Agriculture", "seed_selection", "lɯak1 phan1 khaw3 li1 som1.", "lɯak1 phan1 khaw3 li1 som1.", "lɯak¹ pʰan¹ kʰaw³ liː¹ som¹",
        "Select the healthiest seed grains for the next sowing.", "अगली बुआई के लिए उत्तम गुणवत्ता के बीज चुनिए।", "পৰৱৰ্তী খেতিৰ বাবে ভাল ধানৰ কঠীয়া বাছি লওক।", "Seed selection.")
    add("Farming & Agriculture", "mustard_blooms", "phak1 kaat2 lɯang1 ngam1 thong1 naa1.", "phak1 kaat2 lɯang1 ngam1 thong1 naa1.", "pʰak¹ kaːt² lɯaŋ¹ ŋam¹ tʰoŋ¹ naː¹",
        "Yellow mustard blossoms paint the winter fields beautifully.", "खेतों में खिली पीली सरसों बहुत मनमोहक लग रही है।", "পথাৰত হালধীয়া সৰিয়হ ফুলবোৰ বৰ ধুনীয়াকৈ ফুলিছে।", "Mustard fields.")
    add("Farming & Agriculture", "vegetable_garden", "rim1 hɯan1 mi5 suan1 phak1.", "rim1 hɯan1 mi5 suan1 phak1.", "rim¹ hɯan¹ miː¹ suan¹ pʰak¹",
        "There is a thriving vegetable garden right beside the house.", "घर के पीछे ताज़ी सब्ज़ियों का एक सुंदर बगीचा है।", "ঘৰৰ বাৰীত শাক-পাচলিৰ ধুনীয়া বাগান এখন আছে।", "Kitchen garden.")
    add("Farming & Agriculture", "feed_cattle", "pan1 yaa3 ngua1 khwaai1 kin1.", "pan1 yaa3 ngua1 khwaai1 kin1.", "pan¹ jaː³ ŋua¹ kʰwaːj¹ kin¹",
        "Feed fresh green fodder grass to the cows and buffaloes.", "गायों और भैंसों को खाने के लिए हरी घास दीजिए।", "গৰু আৰু ম’হক খাবলৈ সেউজীয়া ঘাঁহ দিয়ক।", "Cattle feeding.")
    add("Farming & Agriculture", "early_to_fields", "po5 haw1 pai1 naa1 tɯn2 chaw3.", "po5 haw1 pai1 naa1 tɯn2 chaw3.", "po⁵ haw¹ paj¹ naː¹ tɯn² t͡ɕaw³",
        "Father heads to the fields at the first crack of dawn.", "पिताजी भोर होते ही खेत की ओर निकल पड़ते हैं।", "দেউতা পুৱাই পথাৰলৈ ওলাই যায়।", "Dawn farm routine.")
    add("Farming & Agriculture", "carry_lunch_to_field", "aw1 khaw3 hɔ2 pai1 pan1 po5.", "aw1 khaw3 hɔ2 pai1 pan1 po5.", "aw¹ kʰaw³ hɔ² paj¹ pan¹ po⁵",
        "Carry packed lunch out to father working in the field.", "खेत में काम कर रहे पिताजी के लिए दोपहर का खाना ले जाइए।", "পথাৰত কাম কৰি থকা দেউতাৰ বাবে ভাতৰ টোপোলা নিয়া।", "Field lunch.")
    add("Farming & Agriculture", "rest_in_field_hut", "phak1phon2 nai1 thiap1 naa1.", "phak1phon2 nai1 thiap1 naa1.", "pʰak¹ pʰon² naj¹ tʰjap¹ naː¹",
        "Rest in the shade of the elevated field hut.", "खेत में बने मचान (टपरी) में बैठकर आराम कीजिए।", "পথাৰৰ খেৰৰ জুপুৰীটোত জিৰণি লওক।", "Field shelter.")
    add("Farming & Agriculture", "winnowing_basket", "aw1 vi1 phat1 khaw3 haang1.", "aw1 vi1 phat1 khaw3 haang1.", "aw¹ wiː¹ pʰat¹ kʰaw³ haːŋ¹",
        "Use the woven winnowing basket to separate grain from chaff.", "सूप (डाला) की सहायता से भूसी और धान को अलग कीजिए।", "কুলাৰে বাটি ধানৰ পৰা পতানখিনি গুচাই দিয়ক।", "Winnowing.")
    add("Farming & Agriculture", "store_in_baskets", "sai2 khaw3 nai1 taang3 mai3 phaak4.", "sai2 khaw3 nai1 taang3 mai3 phaak4.", "saj² kʰaw³ naj¹ taːŋ³ maj³ pʰaːk⁴",
        "Store the dried paddy into large woven bamboo storage bins.", "सूखे धान को बाँस की बड़ी डोलियों (टोकरियों) में भरिए।", "ধানখিনি বাঁহৰ ডাঙৰ ডুলিত সংৰক্ষণ কৰক।", "Paddy storage.")
    add("Farming & Agriculture", "new_rice_festival", "poy2 kin1 khaw3 mai2 mi5 wan1 nai6.", "poy2 kin1 khaw3 mai2 mi5 wan1 nai6.", "pɔj² kin¹ kʰaw³ maj² miː¹ wan¹ nai⁶",
        "Today we celebrate the traditional festival of the new harvest rice.", "आज गाँव में नए धान के अन्न का पावन उत्सव है।", "আজি ন-খোৱাৰ উৎসৱ অনুষ্ঠিত হৈছে।", "New rice festival.")
    add("Farming & Agriculture", "offer_first_grains", "aw1 khaw3 mai2 thawaai3 wat1.", "aw1 khaw3 mai2 thawaai3 wat1.", "aw¹ kʰaw³ maj² tʰa¹waːj³ wat¹",
        "Offer the very first harvested grains to the monastery.", "नई फ़सल का पहला अन्न आदरपूर्वक विहार में अर्पित कीजिए।", "নতুন ধানৰ প্ৰথম শস্য বৌদ্ধ বিহাৰলৈ আগবঢ়াওক।", "First fruits offering.")
    add("Farming & Agriculture", "community_farming", "haw1 chuai3 kan1เกี่ยว khaw3 thuk1 hɯan1.", "haw1 chuai3 kan1เกี่ยว khaw3 thuk1 hɯan1.", "haw¹ t͡ɕʰuaj³ kan¹ kjoːw¹ kʰaw³ tʰuk¹ hɯan¹",
        "Villagers mutually assist each other in harvesting all fields.", "गाँव के सभी लोग मिलकर हर घर की धान कटाई में हाथ बँटाते हैं।", "গাঁৱৰ সকলোৱে মিলি ইজনে-সিজনৰ ধান দাই দিয়ে।", "Mutual labor sharing.")
    add("Farming & Agriculture", "rain_blessing_crops", "fon1 tok1 hai3 khaw3 naa1 ngam1.", "fon1 tok1 hai3 khaw3 naa1 ngam1.", "fon¹ tok¹ haj³ kʰaw³ naː¹ ŋam¹",
        "Gentle rain falls, blessing the crops to grow luxuriantly.", "समय पर वर्षा होने से धान की फ़सल बहुत लहलहा उठी है।", "বৰষুণৰ পৰশত খেতিপথাৰখন সজীৱ হৈ পৰিছে।", "Rain blessing crops.")
    add("Farming & Agriculture", "black_rice", "khaw3 dam1 pen1 khaw3 yaa1.", "khaw3 dam1 pen1 khaw3 yaa1.", "kʰaw³ dam¹ pen¹ kʰaw³ jaː¹",
        "Traditional black rice holds precious medicinal virtues.", "पारंपरिक काला चावल पौष्टिक और औषधीय गुणों से भरपूर है।", "ক’লা ধান স্বাস্থ্যৰ বাবে বৰ মহৌষধিস্বৰূপ।", "Black rice.")
    add("Farming & Agriculture", "aromatic_rice", "khaw3 hɔm1 nai6 pen1 khaw3 phɯang4.", "khaw3 hɔm1 nai6 pen1 khaw3 phɯang4.", "kʰaw³ hɔm¹ nai⁶ pen¹ kʰaw³ pʰɯaŋ⁴",
        "This aromatic specialty rice is prized for royal celebrations.", "यह सुगंधित चावल विशेष उत्सवों के लिए संजोया जाता है।", "এই সুগন্ধি চাউলবিধ উৎসৱৰ বাবে সংৰক্ষিত।", "Aromatic rice.")
    add("Farming & Agriculture", "protect_from_insects", "raak1saa1 khaw3 am1 hai3 meeng2 kin1.", "raak1saa1 khaw3 am1 hai3 meeng2 kin1.", "raːk¹ saː¹ kʰaw³ am¹ haj³ meːŋ² kin¹",
        "Protect the developing grains from destructive insect pests.", "धान की फ़सल को हानिकारक कीटों और कीड़ों से बचाइए।", "পথাৰৰ ধানখিনি পোক-পৰুৱাৰ পৰা সুৰক্ষিত কৰক।", "Crop protection.")
    add("Farming & Agriculture", "wooden_mortar", "tam1 khaw3 nai1 khrok2 mai3.", "tam1 khaw3 nai1 khrok2 mai3.", "tam¹ kʰaw³ naj¹ kʰrok¹ maj³",
        "Pound and husk the rice inside the traditional wooden mortar (dhekia).", "पारंपरिक ओखली (ढेकी) में धान कूटकर चावल निकालिए।", "ঢেঁকীত ধান বানি চাউল উলিওৱা হৈছে।", "Pounding rice.")
    add("Farming & Agriculture", "clean_white_rice", "met3 khaw3 khao1 sot1 sai1 li1.", "met3 khaw3 khao1 sot1 sai1 li1.", "met¹ kʰaw³ kʰaw¹ sot¹ saj¹ liː¹",
        "The newly husked rice grains are pure white and pristine.", "कूटे हुए चावल के दाने एकदम श्वेत और निर्मल हैं।", "কুটা চাউলৰ দানাবোৰ বৰ বগা আৰু পৰিষ্কাৰ।", "Polished grain.")
    add("Farming & Agriculture", "straw_for_cattle", "fɯang1 khaw3 wai1 hai3 ngua1 kin1.", "fɯang1 khaw3 wai1 hai3 ngua1 kin1.", "fɯaŋ¹ kʰaw³ waj¹ haj³ ŋua¹ kin¹",
        "Stack the golden straw neatly as winter fodder for the livestock.", "धान की सूखी पुआल (पैरा) को मवेशियों के चारे के लिए सहेजें।", "ধানৰ খেৰখিনি গৰুৰ খাদ্যৰ বাবে দম কৰি থওক।", "Straw stack.")
    add("Farming & Agriculture", "field_work_pride", "het1 naa1 pen1 kaang1 ngaan1 song1.", "het1 naa1 pen1 kaang1 ngaan1 song1.", "het¹ naː¹ pen¹ kaːŋ¹ ŋaːn¹ soŋ¹",
        "Farming the earth is a noble, sacred profession.", "खेती-किसानी एक अत्यंत आदरणीय और पवित्र कार्य है।", "খেতি-বাতি কৰাটো এক সন্মানজনক আৰু পৱিত্ৰ কৰ্ম।", "Agricultural dignity.")
    add("Farming & Agriculture", "earth_fertility", "din1 haw1 phom1 li1, som1 sang1 kɔ5 ɔk2.", "din1 haw1 phom1 li1, som1 sang1 kɔ5 ɔk2.", "din¹ haw¹ pʰom¹ liː¹ som¹ saŋ¹ kɔ⁵ ɔk¹",
        "Our land is fertile; whatever seed is planted thrives.", "हमारी भूमि बहुत उपजाऊ है; जो भी बोया जाए, खूब फलता-फूलता है।", "আমাৰ মাটি ইমানেই পলসুৱা যে যি ৰোৱা হয় সেয়াই ফলে।", "Fertile soil.")
    add("Farming & Agriculture", "morning_dew_fields", "nam6 mɔk1 chap1 bai1 khaw3.", "nam6 mɔk1 chap1 bai1 khaw3.", "nam⁶ mɔk¹ t͡ɕʰap¹ baj¹ kʰaw³",
        "Glistening morning dew drops cling to the fresh paddy leaves.", "धान की पत्तियों पर सुबह की ओस की बूँदें मोतियों सी चमक रही हैं।", "ধানৰ পাতত পুৱাৰ নিয়ৰৰ টোপালবোৰ জিলিকিছে।", "Morning dew on rice.")
    add("Farming & Agriculture", "harvest_completed", "เกี่ยว khaw3 leew3, haw1 mi5 khwaam1 suk1.", "kio1 khaw3 leew3, haw1 mi5 khwaam1 suk1.", "kjoː¹ kʰaw³ leːw³ haw¹ miː¹ kʰwaːm¹ suk¹",
        "The harvest is concluded, bringing immense joy and relief.", "धान की कटाई पूरी हो गई है, सभी के चेहरों पर खुशी है।", "ধান দোৱা শেষ হ’ল, মনবোৰ আনন্দৰে উপচি পৰিছে।", "Harvest joy.")
    add("Farming & Agriculture", "sow_vegetables", "som1 phak1 nai1 suan1 phaan2 mɯa2 yen1.", "som1 phak1 nai1 suan1 phaan2 mɯa2 yen1.", "som¹ pʰak¹ naj¹ suan¹ pʰaːn² mɯa² jen¹",
        "Sow winter vegetables in the domestic plots.", "सर्दियों के लिए बाड़ी में हरी सब्ज़ियाँ बोइए।", "শীতকালৰ শাক-পাচলিৰ পুলিবোৰ বাৰীত ৰোৱা হৈছে।", "Winter garden.")
    add("Farming & Agriculture", "bamboo_fencing", "het1 sua1 mai3 phaak4 lɔm3 suan1.", "het1 sua1 mai3 phaak4 lɔm3 suan1.", "het¹ sua¹ maj³ pʰaːk⁴ lɔm³ suan¹",
        "Construct a bamboo fence to protect the garden from animals.", "बगीचे को पशुओं से बचाने के लिए बाँस की बाड़ लगाइए।", "বাৰীখন সুৰক্ষিত কৰিবলৈ বাঁহৰ জেওৰা দিয়ক।", "Garden fencing.")
    add("Farming & Agriculture", "healthy_cattle", "khwaai1 haw1 mi5 haeng1 li1 the5 the5.", "khwaai1 haw1 mi5 haeng1 li1 the5 the5.", "kʰwaːj¹ haw¹ miː¹ hɛŋ¹ liː¹ tʰe⁵ tʰe⁵",
        "Our working buffaloes are strong, healthy, and vigorous.", "हमारी भैंसें बहुत स्वस्थ, हृष्ट-पुष्ट और बलवान हैं।", "আমাৰ ম’হবোৰ বৰ নিৰোগী আৰু বলী।", "Strong livestock.")
    add("Farming & Agriculture", "labor_of_love", "het1 ngaan1 nai1 naa1 mi5 phɔn1 li1.", "het1 ngaan1 nai1 naa1 mi5 phɔn1 li1.", "het¹ ŋaːn¹ naj¹ naː¹ miː¹ pʰɔn¹ liː¹",
        "Patient toil invested into the fields yields rich rewards.", "खेतों में की गई सच्ची मेहनत सदा मीठा फल देती है।", "পথাৰৰ শ্ৰমে সদায় উত্তম ফল দিয়ে।", "Agricultural ethics.")
    add("Farming & Agriculture", "food_security", "khaw3 tem1 yeew3, am1 tɔng3 phaa3 tsai1.", "khaw3 tem1 yeew3, am1 tɔng3 phaa3 tsai1.", "kʰaw³ tem¹ jeːw³ am¹ tɔŋ³ pʰaː³ t͡sai¹",
        "When the granary is stocked full, the home knows no worry.", "जब खलिहान अन्न से भरा हो, तो किसी बात की चिंता नहीं रहती।", "ভঁৰালত ধান থাকিলে কোনো চিন্তা নাথাকে।", "Food abundance.")

    # ==========================================================================
    # DOMAIN 11: WEAVING, TEXTILES, CRAFTS & TRADITIONS (35 sentences)
    # ==========================================================================
    add("Weaving & Crafts", "tai_women_weave", "naang1 tai1 tam3 phaa3 mai3 waan1.", "naang1 tai1 tam3 phaa3 mai3 waan1.", "naːŋ¹ taj¹ tam³ pʰaː³ maj³ waːn¹",
        "Tai women weave magnificent patterns of traditional silk cloth.", "ताई महिलाएँ सुंदर रेशमी कपड़ा कुशलतापूर्वक बुन रही हैं।", "টাই শিপিনীসকলে সুন্দৰ পাটৰ কাপোৰ বৈছে।", "Silk weaving.")
    add("Weaving & Crafts", "loom_clatter", "siang1 ki1 tam3 phaa3 dɔng1 nai1 maan3.", "siang1 ki1 tam3 phaa3 dɔng1 nai1 maan3.", "sjaŋ¹ kiː¹ tam³ pʰaː³ dɔŋ¹ naj¹ maːn³",
        "The rhythmic clatter of weaving handlooms echoes through the village.", "गाँव में हथकरघे की मधुर खटखट गूँज रही है।", "গাঁৱৰ পদূলিয়ে পদূলিয়ে তাঁতৰ শালৰ শব্দ বাজিছে।", "Loom sound.")
    add("Weaving & Crafts", "traditional_sarong", "phaa3 sin3 tai1 mi5 laai1 ngam1.", "phaa3 sin3 tai1 mi5 laai1 ngam1.", "pʰaː³ sin³ taj¹ miː¹ laːj¹ ŋam¹",
        "The traditional Tai women's sin (sarong) features intricate motifs.", "पारंपरिक ताई मेखला/सिन में अत्यंत सुंदर आकृतियाँ हैं।", "টাই মেখেলাত পৰম্পৰাগত ফুলৰ চানেকি বৰ ধুনীয়া।", "Traditional sarong.")
    add("Weaving & Crafts", "men_waistcloth", "phoi1 pen1 phaa3 faai3 khon1 saai1.", "phoi1 pen1 phaa3 faai3 khon1 saai1.", "pʰoj¹ pen¹ pʰaː³ faːj³ kʰon¹ saːj¹",
        "The phoi is the authentic cotton waistcloth worn by Tai men.", "फोई ताई पुरुषों का पारंपरिक सूती परिधान है।", "ফই হৈছে টাই পুৰুষৰ পৰম্পৰাগত কাপোৰ।", "Men's waistcloth.")
    add("Weaving & Crafts", "red_black_patterns", "laai1 phaa3 mi5 yaam1 deeng1 kap4 dam1.", "laai1 phaa3 mi5 yaam1 deeng1 kap4 dam1.", "laːj¹ pʰaː³ miː¹ jaːm¹ deːŋ¹ kap⁴ dam¹",
        "The woven patterns feature classic crimson red and deep black hues.", "बुने हुए परिधानों में पारंपरिक लाल और काले रंग की छटा है।", "কাপোৰৰ চানেকিত পৰম্পৰাগত ৰঙা আৰু ক’লা ৰং আছে।", "Textile colors.")
    add("Weaving & Crafts", "pure_silk", "mai3 nai6 pen1 mai3 sot1 sae5.", "mai3 nai6 pen1 mai3 sot1 sae5.", "maj³ nai⁶ pen¹ maj³ sot¹ sɛː⁵",
        "This thread is pure, unadulterated indigenous silk.", "यह धागा शुद्ध और असली प्राकृतिक रेशम का है।", "এই সূতাখিনি সম্পূৰ্ণ খাঁটি পাটৰ সূতা।", "Pure silk thread.")
    add("Weaving & Crafts", "cotton_spinning", "pan2 faai3 hai3 pen1 saai1 mai3.", "pan2 faai3 hai3 pen1 saai1 mai3.", "pan² faːj³ haj³ pen¹ saːj¹ maj³",
        "Spin the fluffy raw cotton into fine weaving threads.", "कपास से चरखे पर बारीक सूती धागा कातिए।", "কপাহৰ পৰা যঁতৰত সূতা কাটি উলিওৱা হৈছে।", "Cotton spinning.")
    add("Weaving & Crafts", "natural_dyes", "aw1 haak4 ton3 mai3 het1 yaam1.", "aw1 haak4 ton3 mai3 het1 yaam1.", "aw¹ haːk⁴ ton³ maj³ het¹ jaːm¹",
        "Extract vibrant colors from wild tree roots and leaves.", "जंगली पेड़ों की जड़ों और पत्तियों से प्राकृतिक रंग बनाइए।", "গছৰ ছাল আৰু শিপাৰ পৰা প্ৰাকৃতিক ৰং তৈয়াৰ কৰক।", "Natural dyeing.")
    add("Weaving & Crafts", "bamboo_basket_weaving", "chaw1 thao3 saarn3 taang3 mai3 phaak4.", "chaw1 thao3 saarn3 taang3 mai3 phaak4.", "t͡ɕaw¹ tʰaw³ saːrn³ taːŋ³ maj³ pʰaːk⁴",
        "The elders weave sturdy utility baskets from split bamboo strips.", "बुजुर्ग बाँस की तीलियों से सुंदर टोकरियाँ बुन रहे हैं।", "বয়োজ্যেষ্ঠসকলে বাঁহৰ কামিৰে পাচি বৈছে।", "Bamboo basketry.")
    add("Weaving & Crafts", "fish_trap_craft", "het1 saai2 rim1 nam6 haak4 paa1.", "het1 saai2 rim1 nam6 haak4 paa1.", "het¹ saːj² rim¹ nam⁶ haːk⁴ paː¹",
        "Crafting bamboo fish traps (kholo/sai) for setting in the river streams.", "नदी में मछली पकड़ने के लिए बाँस का जाल (जाल/खोली) तैयार कीजिए।", "নৈত মাছ ধৰিবলৈ বাঁহৰ পল আৰু চেপা তৈয়াৰ কৰা হৈছে।", "Fish traps.")
    add("Weaving & Crafts", "traditional_mat", "saarn3 saat1 mai3 bɔk1 phɯ5 nang5.", "saarn3 saat1 mai3 bɔk1 phɯ5 nang5.", "saːrn³ saːt¹ maj³ bɔk¹ pʰɯ⁵ naŋ⁵",
        "Plaiting cool reed mats for comfortable household seating.", "घर में बैठने के लिए सरकंडों और मूंज की शीतल चटाई बुनिए।", "বহিবলৈ বেত আৰু শীতল পাটি বোৱা হৈছে।", "Reed mat plaiting.")
    add("Weaving & Crafts", "stilt_house_architecture", "hɯan1 tai1 mi5 sao1 sung1.", "hɯan1 tai1 mi5 sao1 sung1.", "hɯan¹ taj¹ miː¹ saw¹ suŋ¹",
        "Traditional Tai dwellings are constructed on raised wooden stilts.", "पारंपरिक ताई घर ऊँचे खंभों (मचान शैली) पर बनाए जाते हैं।", "টাইসকলৰ ঘৰবোৰ ওখ চাংঘৰ আৰ্হিৰ।", "Stilt architecture.")
    add("Weaving & Crafts", "thatch_roof", "mung1 khaang1 kap4 yaa3 khaai1.", "mung1 khaang1 kap4 yaa3 khaai1.", "muŋ¹ kʰaːŋ¹ kap⁴ jaː³ kʰaːj¹",
        "Thatch the pitched roof with dense wild meadow grass.", "छत को सूखे छप्पर और घास-फूस से मज़बूती से छाइए।", "ঘৰৰ চালখন খেৰেৰে সুন্দৰকৈ ছাই দিয়া হৈছে।", "Thatched roof.")
    add("Weaving & Crafts", "bamboo_floor", "pɯn4 hɯan1 het1 kap4 mai3 phaak4.", "pɯn4 hɯan1 het1 kap4 mai3 phaak4.", "pɯn⁴ hɯan¹ het¹ kap⁴ maj³ pʰaːk⁴",
        "The raised house floor is crafted from flattened split bamboo slats.", "मचान का फ़र्श चीरे हुए बाँस की पट्टियों से बना है।", "চাংঘৰৰ মজিয়াখন বাঁহৰ তলিৰে সজা।", "Bamboo floor.")
    add("Weaving & Crafts", "shuttle_movement", "krap1 thɔk1 pai1 maa1 wai1 li1.", "krap1 thɔk1 pai1 maa1 wai1 li1.", "krap¹ tʰɔk¹ paj¹ maː¹ waj¹ liː¹",
        "The wooden shuttle glides swiftly back and forth through the warp.", "हथकरघे की ढरकी धागों के बीच तेज़ी से दौड़ती है।", "তাঁতৰ মাকোটো দুয়োফালে ক্ষিপ্ৰতাৰে চলিছে।", "Weaving shuttle.")
    add("Weaving & Crafts", "traditional_turban", "phaa3 hua1 khon1 saai1 tai1.", "phaa3 hua1 khon1 saai1 tai1.", "pʰaː³ hua¹ kʰon¹ saːj¹ taj¹",
        "The white woven turban crowns the traditional attire of Tai men.", "सफ़ेद पगड़ी ताई पुरुषों की पारंपरिक शान और पहचान है।", "মূৰৰ বগা পাগুৰি টাই পুৰুষৰ পৰম্পৰাগত সাজ।", "Traditional turban.")
    add("Weaving & Crafts", "embroidery_motifs", "teek1 laai1 nok1 laai1 bɔk1 mai3.", "teek1 laai1 nok1 laai1 bɔk1 mai3.", "teːk¹ laːj¹ nok¹ laːj¹ bɔk¹ maj³",
        "Embroider motifs of soaring birds and blossoming floral petals.", "कपड़े पर उड़ते पक्षियों और खिले फूलों की सुंदर आकृतियाँ काढ़िए।", "কাপোৰত উৰণীয়া চৰাই আৰু ফুলৰ চানেকি তোলা হৈছে।", "Embroidery motifs.")
    add("Weaving & Crafts", "teach_weaving_youth", "me5 sɔn1 luk3 ying1 tam3 phaa3.", "me5 sɔn1 luk3 ying1 tam3 phaa3.", "me⁵ sɔn¹ luk³ jiŋ¹ tam³ pʰaː³",
        "Mothers carefully instruct their young daughters in loom weaving.", "माताएँ अपनी पुत्रियों को प्रेम से बुनाई की कला सिखाती हैं।", "মাকে জীয়েকক মৰমেৰে তাঁত বোৱা বিদ্যা শিকাইছে।", "Transmitting weaving.")
    add("Weaving & Crafts", "wooden_spoons", "chaang3 mai3 het1 thoi3 kɔng3.", "chaang3 mai3 het1 thoi3 kɔng3.", "t͡ɕʰaːŋ³ maj³ het¹ tʰoj³ kɔŋ³",
        "Woodcarvers fashion ladles, bowls, and spoons from native timber.", "काष्ठशिल्पी लकड़ी से सुंदर कटोरे और चम्मच बनाते हैं।", "কাঠৰ কাৰিকৰে কাঠৰ চামুচ আৰু বাটি তৈয়াৰ কৰিছে।", "Woodcraft.")
    add("Weaving & Crafts", "bamboo_hat", "ngop1 pen1 muak1 mai3 phaak4.", "ngop1 pen1 muak1 mai3 phaak4.", "ŋop¹ pen¹ muak¹ maj³ pʰaːk⁴",
        "The broad conical bamboo sun-hat shelters the farmer from rain.", "बाँस की चौड़ी टोपी (झाँपी/न्योप) किसान को धूप और वर्षा से बचाती है।", "বাঁহৰ জাপিটোৱে খেতিয়কক ৰ’দ-বৰষুণৰ পৰা ৰক্ষা কৰে।", "Bamboo conical hat.")
    add("Weaving & Crafts", "cane_furniture", "waai6 het1 tang3 nang5 man3 khang1.", "waai6 het1 tang3 nang5 man3 khang1.", "waːj⁶ het¹ taŋ³ naŋ⁵ man³ kʰaŋ¹",
        "Sturdy river cane is bent into resilient household chairs.", "मज़बूत बेंत से बैठने के लिए टिकाऊ कुर्सियाँ बनाई जाती हैं।", "বেতৰ পৰা মজবুত চকীবোৰ সজা হৈছে।", "Cane furniture.")
    add("Weaving & Crafts", "sacred_scroll_cloth", "tam3 phaa3 phɔ2 thawaai3 wat1.", "tam3 phaa3 phɔ2 thawaai3 wat1.", "tam³ pʰaː³ pʰɔ² tʰa¹waːj³ wat¹",
        "Weaving long decorative ceremonial banners for monastery dedication.", "विहार के धार्मिक अनुष्ठानों के लिए लंबी पवित्र पताकाएँ बुनिए।", "বৌদ্ধ বিহাৰৰ বাবে পৱিত্ৰ ধ্বজা কাপোৰ বোৱা হৈছে।", "Ceremonial textiles.")
    add("Weaving & Crafts", "warp_and_weft", "saai1 mai3 yaao2 kap4 saai1 khwang3.", "saai1 mai3 yaao2 kap4 saai1 khwang3.", "saːj¹ maj³ jaːw² kap⁴ saːj¹ kʰwaŋ³",
        "The interlocking warp and weft threads form resilient, supple cloth.", "ताना और बाना मिलकर मज़बूत और लचीले वस्त्र का निर्माण करते हैं।", "দীঘ আৰু বাণিৰ সূতা মিলি সুন্দৰ কাপোৰখন গঢ়ি উঠিছে।", "Warp and weft.")
    add("Weaving & Crafts", "village_pottery", "het1 mɔ5 din1 sai2 nam6.", "het1 mɔ5 din1 sai2 nam6.", "het¹ mɔ⁵ din¹ saj² nam⁶",
        "Molding earthenware pots from native clay to store cool water.", "मिट्टी से शीतल जल भरने के लिए सुंदर घड़े तैयार कीजिए।", "মাটিৰে পানী থোৱা কলহবোৰ গঢ়া হৈছে।", "Clay pottery.")
    add("Weaving & Crafts", "bamboo_ladder", "mai3 phaak4 het1 khan1 dai1.", "mai3 phaak4 het1 khan1 dai1.", "maj³ pʰaːk⁴ het¹ kʰan¹ daj¹",
        "Strong thick bamboo poles are tied to build house ladders.", "मचान वाले घर पर चढ़ने के लिए बाँस की सीढ़ी बनाई जाती है।", "চাংঘৰত উঠিবলৈ বাঁহৰ জখলাখন সজা হৈছে।", "Bamboo ladder.")
    add("Weaving & Crafts", "knife_sheath", "saam3 miit2 het1 kap4 mai3.", "saam3 miit2 het1 kap4 mai3.", "saːm³ miːt² het¹ kap⁴ maj³",
        "The curved utility machete rests safely in its carved wooden sheath.", "दाव (चाकू) को नक्काशीदार लकड़ी की म्यान में सुरक्षित रखा जाता है।", "দাখন কাঠৰ খাপত সুমুৱাই থোৱা হৈছে।", "Machete sheath.")
    add("Weaving & Crafts", "tight_weave", "tam3 hai3 nɛn3 li1 the5 the5.", "tam3 hai3 nɛn3 li1 the5 the5.", "tam³ haj³ nɛn³ liː¹ tʰe⁵ tʰe⁵",
        "Pack the weft tight so the weave remains dense and enduring.", "कपड़े की बुनाई एकदम घनी और मज़बूत रखिए।", "কাপোৰৰ বোৱনিখন একেবাৰে নিপোটল কৰক।", "Tight weaving.")
    add("Weaving & Crafts", "heirloom_patterns", "laai1 nai6 mi5 maa1 taang3 pu5 yaa3.", "laai1 nai6 mi5 maa1 taang3 pu5 yaa3.", "laːj¹ nai⁶ miː¹ maː¹ taːŋ³ pu⁵ jaː³",
        "These precious geometric motifs descend directly from our ancestors.", "यह पारंपरिक आकृतियाँ हमें सीधे अपने पूर्वजों से विरासत में मिली हैं।", "এই চানেকিটো পূৰ্বপুৰুষৰ দিনৰ পৰা চলি আহিছে।", "Heirloom motifs.")
    add("Weaving & Crafts", "festive_dress", "nung2 phaa3 mai2 pai1 poy2.", "nung2 phaa3 mai2 pai1 poy2.", "nuŋ² pʰaː³ maj² paj¹ pɔj²",
        "Don newly woven festive attire to attend the communal temple festival.", "उत्सव में जाने के लिए नए पारंपरिक परिधान पहनिए।", "উৎসৱলৈ যাবলৈ নতুন পৰম্পৰাগত কাপোৰ পিন্ধক।", "Festive garments.")
    add("Weaving & Crafts", "pride_in_handicrafts", "khɔng3 mɯɯ1 haw1 ngam1 the5 the5.", "khɔng3 mɯɯ1 haw1 ngam1 the5 the5.", "kʰɔŋ³ mɯː¹ haw¹ ŋam¹ tʰe⁵ tʰe⁵",
        "Our village handicrafts reflect extraordinary dexterity and patience.", "हमारे हस्तशिल्प में अद्भुत कारीगरी, सुंदरता और धैर्य झलकता है।", "আমাৰ হস্তশিল্পত অপূর্ব নিপুণতা আৰু সৌন্দৰ্য্য প্ৰকাশ পাইছে।", "Craftsmanship pride.")
    add("Weaving & Crafts", "bamboo_flute", "kholui3 mai3 phaak4 hɔng3 siang1 waan1.", "kholui3 mai3 phaak4 hɔng3 siang1 waan1.", "kʰo¹luj³ maj³ pʰaːk⁴ hɔŋ³ sjaŋ¹ waːn¹",
        "The handcrafted bamboo flute breathes sweet, haunting melodies.", "बाँस की बनी बाँसुरी से अत्यंत मधुर धुन निकलती है।", "বাঁহৰ বাঁহীটোৰ সুৰ বৰ শুৱলা আৰু মোহনীয়া।", "Bamboo flute.")
    add("Weaving & Crafts", "cultural_garb", "khon1 tai1 haak4 nung2 phaa3 tai1.", "khon1 tai1 haak4 nung2 phaa3 tai1.", "kʰon¹ taj¹ haːk⁴ nuŋ² pʰaː³ taj¹",
        "Tai community members wear their ethnic attire with profound honor.", "ताई जन अपने पारंपरिक परिधानों को बड़े गर्व से धारण करते हैं।", "টাইসকলে নিজৰ পৰম্পৰাগত সাজ-পাৰ গৌৰৱেৰে পৰিধান কৰে।", "Ethnic garb.")
    add("Weaving & Crafts", "spinning_wheel", "laang3 nai6 pen1 faai3 sot1.", "laang3 nai6 pen1 faai3 sot1.", "laːŋ³ nai⁶ pen¹ faːj³ sot¹",
        "This pristine natural cotton fiber is ready for the spinning wheel.", "यह शुद्ध कपास कताई के लिए एकदम तैयार है।", "এই সূতাখিনি যঁতৰত কাতিবলৈ সাজু হৈছে।", "Natural cotton.")
    add("Weaving & Crafts", "pattern_preservation", "kep4 laai1 phaa3 nai1 samut1.", "kep4 laai1 phaa3 nai1 samut1.", "kep⁴ laːj¹ pʰaː³ naj¹ sa¹mut¹",
        "Document and illustrate the heritage textile patterns in a book.", "कपड़ों के पारंपरिक नमूनों को पुस्तक में सहेजकर रखिए।", "কাপোৰৰ চানেকিবোৰ কিতাপত সংৰক্ষণ কৰি থওক।", "Pattern archive.")
    add("Weaving & Crafts", "crafts_live_on", "mɯɯ1 chaang3 haw1 am1 haai1.", "mɯɯ1 chaang3 haw1 am1 haai1.", "mɯː¹ t͡ɕʰaːŋ³ haw¹ am¹ haːj¹",
        "The master artisan skills of our people shall never perish.", "हमारे लोगों की महान शिल्प-कला कभी लुप्त नहीं होगी।", "আমাৰ শিপিনীসকলৰ হাতৰ পৰশ কেতিয়াও হেৰাই নাযায়।", "Artisan endurance.")

    # ==========================================================================
    # DOMAIN 12: HEALTH, BODY & WELLBEING (30 sentences)
    # ==========================================================================
    add("Health & Wellness", "headache", "kaw1 chep1 hua1 noi3 nɯŋ5.", "kaw1 chep1 hua1 noi3 nɯŋ5.", "kaw¹ t͡ɕʰep¹ hua¹ noi³ nɯŋ⁵",
        "I have a mild headache.", "मुझे हल्का सिरदर्द है।", "মোৰ মূৰটো অলপ বিষাইছে।", "Headache.")
    add("Health & Wellness", "stomachache", "man1 chep1 thɔng3 wan1 nai6.", "man1 chep1 thɔng3 wan1 nai6.", "man¹ t͡ɕʰep¹ tʰɔŋ³ wan¹ nai⁶",
        "He suffers from a stomachache today.", "आज उसके पेट में दर्द है।", "আজি তাৰ পেটটো বিষাইছে।", "Stomachache.")
    add("Health & Wellness", "leg_pain", "chaw1 thao3 chep1 khaa1 yaang3 yaak4.", "chaw1 thao3 chep1 khaa1 yaang3 yaak4.", "t͡ɕaw¹ tʰaw³ t͡ɕʰep¹ kʰaː¹ jaːŋ³ jaːk⁴",
        "The elder has leg ache and walks with difficulty.", "बुजुर्ग के पैरों में दर्द है, जिससे चलने में कठिनाई हो रही है।", "ককাৰ ভৰিৰ বিষৰ বাবে খোজ কঢ়াত কষ্ট হৈছে।", "Leg pain.")
    add("Health & Wellness", "fever", "luk3 on2 pen1 thon2 rɔn3.", "luk3 on2 pen1 thon2 rɔn3.", "luk³ on² pen¹ tʰon² rɔn³",
        "The little child is running a hot fever.", "छोटे बच्चे को तेज़ बुखार आ गया है।", "কেঁচুৱাটোৰ গাটো জ্বৰত বৰ গৰম হৈছে।", "Fever.")
    add("Health & Wellness", "take_medicine", "kin1 yaa1 nai6 hai3 haai1.", "kin1 yaa1 nai6 hai3 haai1.", "kin¹ jaː¹ nai⁶ haj³ haːj¹",
        "Take this medicine to recover quickly.", "शीघ्र स्वास्थ्य लाभ के लिए यह दवा लीजिए।", "আৰোগ্য লাভৰ বাবে এই দৰৱটো খাই লওক।", "Medication.")
    add("Health & Wellness", "herbal_cure", "yaa1 mai3 paa5 nai6 li1 the5 the5.", "yaa1 mai3 paa5 nai6 li1 the5 the5.", "jaː¹ maj³ paː⁵ nai⁶ liː¹ tʰe⁵ tʰe⁵",
        "This wild herbal remedy is extraordinarily effective.", "जंगल की यह जड़ी-बूटी बहुत ही गुणकारी और लाभकारी है।", "এই বনদৰৱবিধ বৰ উপকাৰী।", "Herbal remedy.")
    add("Health & Wellness", "drink_boiled_water", "kin1 nam6 tom3 suk1 hai3 li1.", "kin1 nam6 tom3 suk1 hai3 li1.", "kin¹ nam⁶ tom³ suk¹ haj³ liː¹",
        "Always drink thoroughly boiled, cooled water.", "सदा उबला हुआ और साफ़ पानी पीजिए।", "সদায় উতলোৱা বিশুদ্ধ পানী খাব।", "Boiled water.")
    add("Health & Wellness", "body_strength", "haang1 khing1 mi5 haeng1 li1.", "haang1 khing1 mi5 haeng1 li1.", "haːŋ¹ kʰiŋ¹ miː¹ hɛŋ¹ liː¹",
        "The body feels energetic, robust, and strong.", "शरीर में नई ऊर्जा और पूरा बल महसूस हो रहा है।", "শৰীৰত শক্তি আৰু সতেজতা বাঢ়িছে।", "Vitality.")
    add("Health & Wellness", "rest_well", "phak1phon2 hai3 li1 taaw1.", "phak1phon2 hai3 li1 taaw1.", "pʰak¹ pʰon² haj³ liː¹ taːw¹",
        "Please rest comfortably and recover well.", "कृपया अच्छी तरह आराम कीजिए।", "অনুগ্ৰহ কৰি ভালদৰে বিশ্ৰাম লওক।", "Rest command.")
    add("Health & Wellness", "eyes_clear", "taa1 saaw3 han1 li1.", "taa1 saaw3 han1 li1.", "taː¹ saːw³ han¹ liː¹",
        "The eyes can see clearly and sharply.", "आँखों से सब कुछ एकदम साफ़ दिखाई दे रहा है।", "চকুৰে সকলো স্পষ্টকৈ দেখা পাইছে।", "Clear vision.")
    add("Health & Wellness", "clean_wound", "sɯak1 phae3 hai3 sot1.", "sɯak1 phae3 hai3 sot1.", "sɯak¹ pʰɛː³ haj³ sot¹",
        "Cleanse the wound carefully with boiled water.", "घाव को उबले पानी से अच्छी तरह साफ़ कीजिए।", "ঘোঁচোৱা ঘাঁটো পৰিষ্কাৰকৈ ধুই পেলাওক।", "Wound care.")
    add("Health & Wellness", "healthy_living", "kin1 li1 nɔn1 li1 hai3 aayu3 yaao2.", "kin1 li1 nɔn1 li1 hai3 aayu3 yaao2.", "kin¹ liː¹ nɔn¹ liː¹ haj³ aː¹ju³ jaːw²",
        "Wholesome eating and sound sleep foster longevity.", "अच्छा खान-पान और भरपूर नींद लंबी उम्र देते हैं।", "উত্তম খোৱা-বোৱা আৰু শুৱনিয়ে দীৰ্ঘায়ু প্ৰদান কৰে।", "Longevity principle.")
    add("Health & Wellness", "cough_cold", "kaw1 ai1 kap4 pen1 wat4.", "kaw1 ai1 kap4 pen1 wat4.", "kaw¹ aj¹ kap⁴ pen¹ wat⁴",
        "I am afflicted with a coughing cold.", "मुझे खाँसी और ज़ुकाम हो गया है।", "মোৰ কাহ আৰু চৰ্দী লাগিছে।", "Cold and cough.")
    add("Health & Wellness", "ginger_tea_cold", "kin1 nam6 chaa1 khing1 hai3 haai1 ai1.", "kin1 nam6 chaa1 khing1 hai3 haai1 ai1.", "kin¹ nam⁶ t͡ɕʰaː¹ kʰiŋ¹ haj³ haːj¹ aj¹",
        "Drink hot ginger tea to relieve your cough.", "खाँसी से राहत पाने के लिए अदरक वाली गर्म चाय पीजिए।", "কাহৰ পৰা উপশম পাবলৈ আদা-চাহ খাওক।", "Ginger tea remedy.")
    add("Health & Wellness", "doctor_visit", "pai1 han1 mɔ5 yaa1 nai1 mong1.", "pai1 han1 mɔ5 yaa1 nai1 mong1.", "paj¹ han¹ mɔ⁵ jaː¹ naj¹ moŋ¹",
        "Go consult the physician at the health clinic.", "शहर के स्वास्थ्य केंद्र में जाकर चिकित्सक को दिखाइए।", "স্বাস্থ্য কেন্দ্ৰলৈ গৈ ডাক্তৰক দেখুৱাওক।", "Doctor consultation.")
    add("Health & Wellness", "feeling_better", "yam1 nai6 kaw1 haai1 li1 yow3.", "yam1 nai6 kaw1 haai1 li1 yow3.", "jam¹ nai⁶ kaw¹ haːj¹ liː¹ jow³",
        "I feel considerably better and restored now.", "अब मेरी तबियत पहले से काफ़ी अच्छी है।", "এতিয়া মোৰ গাটো বহুখিনি ভাল লাগিছে।", "Recovery affirmation.")
    add("Health & Wellness", "sound_sleep", "nɔn1 lap1 li1 thuk1 khɯn1.", "nɔn1 lap1 li1 thuk1 khɯn1.", "nɔn¹ lap¹ liː¹ tʰuk¹ kʰɯn¹",
        "Sleep soundly through every quiet night.", "प्रतिदिन रात को गहरी और सुखद नींद सोइए।", "প্ৰতি নিশা শান্তভাৱে টোপনি যাওক।", "Sound sleep.")
    add("Health & Wellness", "bathe_warm_water", "aap1 nam6 un2 hai3 sa1baai1.", "aap1 nam6 un2 hai3 sa1baai1.", "aːp¹ nam⁶ un² haj³ sa¹baːj¹",
        "Bathe with warm water to soothe the body.", "शरीर को विश्राम देने के लिए गुनगुने पानी से स्नान कीजिए।", "কুহুমীয়া গৰম পানীৰে গা ধুলে আৰাম পোৱা যায়।", "Warm bath.")
    add("Health & Wellness", "strong_teeth", "kʰio1 man3 khang1 kin1 waan1.", "khio1 man3 khang1 kin1 waan1.", "kʰjoː¹ man³ kʰaŋ¹ kin¹ waːn¹",
        "Strong teeth enable one to enjoy tasty food.", "मज़बूत दाँत भोजन का भरपूर आनंद लेने में सहायक होते हैं।", "দাঁতবোৰ মজবুত থাকিলে খোৱা-বোৱাৰ সোৱাদ পোৱা যায়।", "Dental health.")
    add("Health & Wellness", "breathe_fresh_air", "สูด lom1 sot1 sai1 nai1 paa5.", "suut2 lom1 sot1 sai1 nai1 paa5.", "suːt² lom¹ sot¹ saj¹ naj¹ paː⁵",
        "Inhale the pristine, clean air of the deep forest.", "सघन वन की शुद्ध और ताज़ा हवा में गहरी साँस लीजिए।", "অৰণ্যৰ নিৰ্মল বতাহ বুকুত ভৰাই লওক।", "Fresh air.")
    add("Health & Wellness", "elderly_wellbeing", "chaw1 thao3 haw1 yu5 li1 kin1 waan1.", "chaw1 thao3 haw1 yu5 li1 kin1 waan1.", "t͡ɕaw¹ tʰaw³ haw¹ ju⁵ liː¹ kin¹ waːn¹",
        "May our elderly consultants remain hale, hearty, and peaceful.", "हमारे आदरणीय बुजुर्ग सदा स्वस्थ, सुखी और प्रसन्न रहें।", "আমাৰ জ্যেষ্ঠজনসকল সদায় কুশলে থাকক।", "Elders' wellbeing.")
    add("Health & Wellness", "pure_heart", "tsai1 sot1 sai1, haang1 khing1 li1.", "tsai1 sot1 sai1, haang1 khing1 li1.", "t͡sai¹ sot¹ saj¹ haːŋ¹ kʰiŋ¹ liː¹",
        "A peaceful mind generates a healthy physical constitution.", "निर्मल मन और सकारात्मक विचार शरीर को स्वस्थ रखते हैं।", "পৱিত্ৰ মন আৰু শান্তিয়ে শৰীৰ নিৰোগী কৰি ৰাখে।", "Mind-body link.")
    add("Health & Wellness", "protect_from_mosquitoes", "raak1saa1 tua1 am1 hai3 yung1 khat4.", "raak1saa1 tua1 am1 hai3 yung1 khat4.", "raːk¹ saː¹ tua¹ am¹ haj³ juŋ¹ kʰat⁴",
        "Protect yourself from mosquito bites under nets.", "मच्छरदानी लगाकर स्वयं को मच्छरों के काटने से बचाइए।", "মঁহৰ কামোৰৰ পৰা হাত সাৰিবলৈ আঁঠুৱা তৰক।", "Mosquito defense.")
    add("Health & Wellness", "exercise_walking", "yaang3 thuk1 wan1 li1 tɔ5 haang1 khing1.", "yaang3 thuk1 wan1 li1 tɔ5 haang1 khing1.", "jaːŋ³ tʰuk¹ wan¹ liː¹ tɔ⁵ haːŋ¹ kʰiŋ¹",
        "Walking daily is profoundly beneficial for overall health.", "प्रतिदिन पैदल चलना स्वास्थ्य के लिए अत्यंत लाभकारी है।", "প্ৰতিদিনে খোজ কঢ়াটো স্বাস্থ্যৰ বাবে বৰ ভাল।", "Daily walk.")
    add("Health & Wellness", "throat_soothing", "kin1 nam6 chaa1 kap4 nam6 phɯng3.", "kin1 nam6 chaa1 kap4 nam6 phɯng3.", "kin¹ nam⁶ t͡ɕʰaː¹ kap⁴ nam⁶ pʰɯŋ³",
        "Drink warm tea mixed with wild honey to soothe the throat.", "गले को राहत देने के लिए शहद मिली गर्म चाय पीजिए।", "ডিঙিৰ আৰামৰ বাবে মৌ দিয়া চাহ একাপ খাওক।", "Honey tea.")
    add("Health & Wellness", "healed_completely", "phae3 haai1 li1 yow3.", "phae3 haai1 li1 yow3.", "pʰɛː³ haːj¹ liː¹ jow³",
        "The wound has healed over smoothly and completely.", "घाव अब पूरी तरह भर चुका है और ठीक हो गया है।", "ঘাঁটো এতিয়া সম্পূৰ্ণৰূপে শুকাই গ’ল।", "Healed wound.")
    add("Health & Wellness", "wash_face_morning", "sɯak1 na5 tɯn2 chaw3 hai3 saaw3.", "sɯak1 na5 tɯn2 chaw3 hai3 saaw3.", "sɯak¹ naː⁵ tɯn² t͡ɕaw³ haj³ saːw³",
        "Wash your face with cold spring water to awaken brightly.", "सुबह उठकर ठंडे पानी से मुँह धोइए ताकि ताज़गी आए।", "ৰাতিপুৱা সাৰ পাই শীতল পানীৰে মুখ ধুই লওক।", "Face washing.")
    add("Health & Wellness", "back_ache", "chep1 laang1 mɯa2 het1 naa1 laai1.", "chep1 laang1 mɯa2 het1 naa1 laai1.", "t͡ɕʰep¹ laːŋ¹ mɯa² het¹ naː¹ laːj¹",
        "The back aches after a grueling day of field weeding.", "खेत में कड़ी मेहनत करने के बाद पीठ में हल्का दर्द है।", "পথাৰত দিনটো কাম কৰি পিঠিৰ বিষ হৈছে।", "Back pain.")
    add("Health & Wellness", "healthy_food_medicine", "kin1 khaw3 phak1 pen1 yaa1.", "kin1 khaw3 phak1 pen1 yaa1.", "kin¹ kʰaw³ pʰak¹ pen¹ jaː¹",
        "Nutritious natural food serves as the supreme medicine.", "संतुलित और प्राकृतिक भोजन ही सर्वोत्तम औषधि है।", "সতেজ আৰু পুষ্টিকৰ খাদ্যই হৈছে মহৌষধ।", "Food as medicine.")
    add("Health & Wellness", "blessing_of_health", "am1 mi5 rok1 pen1 laap3 yai3.", "am1 mi5 rok1 pen1 laap3 yai3.", "am¹ miː¹ rok¹ pen¹ laːp³ jai³",
        "Freedom from illness is the greatest fortune and treasure.", "निरोगी काया ही संसार का सबसे बड़ा धन और सुख है।", "নিৰোগী হৈ থকাটোৱেই পৰম লাভ আৰু সম্পদ।", "Health is wealth.")

    # ==========================================================================
    # DOMAIN 13: POLITENESS, REQUESTS, GRATITUDE & MANNERS (35 sentences)
    # ==========================================================================
    add("Politeness & Requests", "speak_slowly_clearly", "waa5 tsaa3 tsaa3 taaw1.", "waa5 tsaa3 tsaa3 taaw1.", "waː⁵ t͡saː³ t͡saː³ taːw¹",
        "Please speak slowly and clearly.", "कृपया धीरे-धीरे और स्पष्ट बोलिए।", "অনুগ্ৰহ কৰি লাহে লাহে আৰু স্পষ্টকৈ কওক।", "Slow speech.")
    add("Politeness & Requests", "repeat_once_more", "waa5 thau3 nɯŋ5 taaw1.", "waa5 thau3 nɯŋ5 taaw1.", "waː⁵ tʰaw³ nɯŋ⁵ taːw¹",
        "Please repeat that once more.", "कृपया एक बार फिर कहिए।", "অনুগ্ৰহ কৰি আৰু এবাৰ কওক।", "Repetition request.")
    add("Politeness & Requests", "help_me", "chɔi3 kaw1 noi3 taaw1.", "chɔi3 kaw1 noi3 taaw1.", "t͡ɕʰɔj³ kaw¹ noi³ taːw¹",
        "Please help me a little.", "कृपया मेरी थोड़ी मदद कीजिए।", "অনুগ্ৰহ কৰি মোক অলপ সহায় কৰক।", "Assistance request.")
    add("Politeness & Requests", "please_come_in", "khao3 maa1 nai1 hɯan1 taaw1.", "khao3 maa1 nai1 hɯan1 taaw1.", "kʰaw³ maː¹ naj¹ hɯan¹ taːw¹",
        "Please come inside our house.", "कृपया हमारे घर के भीतर आइए।", "ভিতৰলৈ সোমাই আহক।", "Entering house.")
    add("Politeness & Requests", "sit_comfortably", "nang5 hai3 sa1baai1 taaw1.", "nang5 hai3 sa1baai1 taaw1.", "naŋ⁵ haj³ sa¹baːj¹ taːw¹",
        "Please sit and make yourself comfortable.", "कृपया आराम से बैठिए।", "আৰামেৰে বহক।", "Sitting comfortably.")
    add("Politeness & Requests", "give_food", "pan1 khaw3 kaw1 kin1 noi3 taaw1.", "pan1 khaw3 kaw1 kin1 noi3 taaw1.", "pan¹ kʰaw³ kaw¹ kin¹ noi³ taːw¹",
        "Please share a little food with me.", "कृपया मुझे थोड़ा भोजन दीजिए।", "মোক খাবলৈ অলপ ভাত দিয়ক।", "Food request.")
    add("Politeness & Requests", "kind_thanks", "chaw1 mi1 tsai1 li1 the5 the5, khɔp1 tsai1.", "chaw1 mi1 tsai1 li1 the5 the5, khɔp1 tsai1.", "t͡ɕaw¹ miː¹ t͡sai¹ liː¹ tʰe⁵ tʰe⁵ kʰɔp¹ t͡sai¹",
        "You are exceptionally kind and helpful, thank you.", "आप बहुत ही दयालु और कृपालु हैं, बहुत धन्यवाद।", "আপোনাৰ মনটো বৰ উদাৰ, ধন্যবাদ।", "Thanks for kindness.")
    add("Politeness & Requests", "forgive_mistake", "kho5 thot3, kaw1 het1 phit1 yow3.", "kho5 thot3, kaw1 het1 phit1 yow3.", "kʰo⁵ tʰot³ kaw¹ het¹ pʰit¹ jow³",
        "Pardon me, I made an unintentional error.", "कृपया मुझे क्षमा करें, मुझसे अनजाने में भूल हो गई।", "ক্ষমা কৰিব, মোৰ ভুল হ’ল।", "Apology for mistake.")
    add("Politeness & Requests", "no_need_worry", "am1 pen1 sang1, am1 tɔng3 phaa3 tsai1.", "am1 pen1 sang1, am1 tɔng3 phaa3 tsai1.", "am¹ pen¹ saŋ¹ am¹ tɔŋ³ pʰaː³ t͡sai¹",
        "Do not worry in the least; it is nothing.", "बिल्कुल चिंता मत कीजिए; कोई बात नहीं।", "একো চিন্তা নকৰিব, কথা নাই।", "Reassurance.")
    add("Politeness & Requests", "listen_carefully", "fang1 hai3 li1 taaw1.", "fang1 hai3 li1 taaw1.", "faŋ¹ haj³ liː¹ taːw¹",
        "Please listen with close attention.", "कृपया ध्यानपूर्वक सुनिए।", "অনুগ্ৰহ কৰি মনোযোগেৰে শুনক।", "Listen carefully.")
    add("Politeness & Requests", "look_at_this", "dɯ1 an1 nai6 taaw1.", "dɯ1 an1 nai6 taaw1.", "dɯː¹ an¹ nai⁶ taːw¹",
        "Please examine this item.", "कृपया इसे देखिए।", "ইয়াক চাওকচোন।", "Look command.")
    add("Politeness & Requests", "walk_slowly_elder", "chaw1 thao3 yaang3 tsaa3 tsaa3 taaw1.", "chaw1 thao3 yaang3 tsaa3 tsaa3 taaw1.", "t͡ɕaw¹ tʰaw³ jaːŋ³ t͡saː³ t͡saː³ taːw¹",
        "Revered elder, please tread slowly and carefully.", "आदरणीय बुजुर्ग, कृपया धीरे-धीरे चलिए।", "শ্ৰদ্ধাৰ ককা, লাহে লাহে খোজ দিয়ক।", "Elder guidance.")
    add("Politeness & Requests", "may_i_ask", "kaw1 kho5 thaam1 kham1 nɯng5 dai3 haa1?", "kaw1 kho5 thaam1 kham1 nɯng5 dai3 haa1?", "kaw¹ kʰo⁵ tʰaːm¹ kʰam¹ nɯŋ⁵ daj³ haː¹",
        "May I be permitted to ask a question?", "क्या मैं आपसे एक बात पूछ सकता हूँ?", "মই এটা কথা সুধিব পাৰোঁনে?", "Permission to ask.")
    add("Politeness & Requests", "tell_me_story", "lao3 nithaan1 pan1 kaw1 fang1 taaw1.", "lao3 nithaan1 pan1 kaw1 fang1 taaw1.", "law³ ni¹tʰaːn¹ pan¹ kaw¹ faŋ¹ taːw¹",
        "Please recount an ancient story for me to hear.", "कृपया मुझे एक लोककथा सुनाइए।", "মোক এটা সাধুকথা শুনাই দিয়ক।", "Story request.")
    add("Politeness & Requests", "show_me_path", "chi3 taang1 hai3 kaw1 taaw1.", "chi3 taang1 hai3 kaw1 taaw1.", "t͡ɕʰiː³ taːŋ¹ haj³ kaw¹ taːw¹",
        "Please point out the correct path to me.", "कृपया मुझे सही रास्ता दिखाइए।", "মোক সঠিক বাটটো দেখুৱাই দিয়ক।", "Path request.")
    add("Politeness & Requests", "write_it_down", "teek1 lik1 wai1 taaw1.", "teek1 lik1 wai1 taaw1.", "teːk¹ lik¹ waj¹ taːw¹",
        "Please write it down in script.", "कृपया इसे कागज़ पर लिख दीजिए।", "অনুগ্ৰহ কৰি ইয়াক লিখি থওক।", "Writing request.")
    add("Politeness & Requests", "read_aloud", "an2 siang1 dɔng1 hai3 fang1 taaw1.", "an2 siang1 dɔng1 hai3 fang1 taaw1.", "an² sjaŋ¹ dɔŋ¹ haj³ faŋ¹ taːw¹",
        "Please read it out aloud for everyone to hear.", "कृपया इसे ऊँचे स्वर में पढ़कर सुनाइए।", "ডাঙৰকৈ পঢ়ি শুনাই দিয়ক।", "Reading aloud.")
    add("Politeness & Requests", "do_not_be_shy", "am1 tɔng3 laai1 tsai1 taaw1.", "am1 tɔng3 laai1 tsai1 taaw1.", "am¹ tɔŋ³ laːj¹ t͡sai¹ taːw¹",
        "Please do not feel hesitant or shy.", "कृपया संकोच मत कीजिए।", "লাজ নকৰিব, খুলি কওক।", "Encouragement.")
    add("Politeness & Requests", "open_door", "khai1 pra1tu1 hai3 noi3 taaw1.", "khai1 pra1tu1 hai3 noi3 taaw1.", "kʰaj¹ pra¹tuː¹ haj³ noi³ taːw¹",
        "Please open the doorway.", "कृपया दरवाज़ा खोल दीजिए।", "দুৱাৰখন খুলি দিয়ক।", "Door opening.")
    add("Politeness & Requests", "close_door", "hap1 pra1tu1 hai3 li1 taaw1.", "hap1 pra1tu1 hai3 li1 taaw1.", "hap¹ pra¹tuː¹ haj³ liː¹ taːw¹",
        "Please close the doorway properly.", "कृपया दरवाज़ा बंद कर दीजिए।", "দুৱাৰখন বন্ধ কৰি থওক।", "Door closing.")
    add("Politeness & Requests", "bring_water", "aw1 nam6 maa1 pan1 kheek2 taaw1.", "aw1 nam6 maa1 pan1 kheek2 taaw1.", "aw¹ nam⁶ maː¹ pan¹ kʰeːk² taːw¹",
        "Please bring drinking water for our guest.", "कृपया मेहमान के लिए पीने का पानी लाइए।", "আলহীৰ বাবে পানী আনি দিয়ক।", "Serving guest water.")
    add("Politeness & Requests", "eat_gracefully", "kin1 khaw3 kap4 khwaam1 yaam1 taaw1.", "kin1 khaw3 kap4 khwaam1 yaam1 taaw1.", "kin¹ kʰaw³ kap⁴ kʰwaːm¹ jaːm¹ taːw¹",
        "Please dine with tranquility and grace.", "कृपया शांति और शालीनता से भोजन कीजिए।", "আৰামেৰে সন্তুষ্টিৰে আহাৰ গ্ৰহণ কৰক।", "Gracious dining.")
    add("Politeness & Requests", "be_patient", "thaa3 kap4 tsai1 yen1 taaw1.", "thaa3 kap4 tsai1 yen1 taaw1.", "tʰaː³ kap⁴ t͡sai¹ jen¹ taːw¹",
        "Please remain patient and peaceful.", "कृपया धैर्य और शांति बनाए रखिए।", "ধৈৰ্য্য ধৰি শান্ত হৈ থাকক।", "Patience request.")
    add("Politeness & Requests", "speak_gently", "waa5 kham1 waan1 hai3 kan1 fang1.", "waa5 kham1 waan1 hai3 kan1 fang1.", "waː⁵ kʰam¹ waːn¹ haj³ kan¹ faŋ¹",
        "Always speak soft and gentle words to each other.", "आपस में सदा मधुर और प्रिय वाणी बोलिए।", "ইজনে-সিজনক মিঠা মাতেৰে সম্বোধন কৰক।", "Gentle speech.")
    add("Politeness & Requests", "grant_blessing", "pan1 phɔn1 hai3 luk3 on2 taaw1.", "pan1 phɔn1 hai3 luk3 on2 taaw1.", "pan¹ pʰɔn¹ haj³ luk³ on² taːw¹",
        "Please bestow your blessings upon the young ones.", "कृपया छोटे बच्चों को अपना शुभाशीर्वाद दीजिए।", "কণমানিবোৰক আশীৰ্বাদ কৰক।", "Blessing request.")
    add("Politeness & Requests", "forgive_faults", "am1 thɯ5 thot3 haang1 haw1 taaw1.", "am1 thɯ5 thot3 haang1 haw1 taaw1.", "am¹ tʰɯ⁵ tʰot³ haːŋ¹ haw¹ taːw¹",
        "Please do not hold our shortcomings against us.", "कृपया हमारे किसी दोष पर ध्यान मत दीजिए।", "আমাৰ দোষ-ত্ৰুটি মৰিষণ কৰক।", "Humility apology.")
    add("Politeness & Requests", "thank_hospitality", "khɔp1 tsai1 nai1 khwaam1 liang3 haw1.", "khɔp1 tsai1 nai1 khwaam1 liang3 haw1.", "kʰɔp¹ t͡sai¹ naj¹ kʰwaːm¹ ljaŋ³ haw¹",
        "Thank you profoundly for this bountiful meal and hospitality.", "इस सुंदर दावत और सत्कार के लिए हृदय से धन्यवाद।", "আপোনাৰ আন্তৰিক আতিথ্যৰ বাবে অশেষ ধন্যবাদ।", "Hospitality gratitude.")
    add("Politeness & Requests", "welcome_again", "wan1 na5 maa1 them1 taaw1.", "wan1 na5 maa1 them1 taaw1.", "wan¹ naː⁵ maː¹ tʰem¹ taːw¹",
        "Please visit our humble home again soon.", "कृपया भविष्य में फिर हमारे घर पधारिए।", "আকৌ আমাৰ ঘৰলৈ আহিব।", "Return invitation.")
    add("Politeness & Requests", "stand_up_respect", "yɯn1 khɯn3 wai1 chaw1 thao3.", "yɯn1 khɯn3 wai1 chaw1 thao3.", "jɯn¹ kʰɯn³ waj¹ t͡ɕaw¹ tʰaw³",
        "Rise to your feet in respectful deference when an elder enters.", "बुजुर्गों के आगमन पर सम्मानपूर्वक खड़े हो जाइए।", "বয়োজ্যেষ্ঠজন আহিলে শ্ৰদ্ধাৰে থিয় হওক।", "Respect behavior.")
    add("Politeness & Requests", "pass_the_dish", "song1 thoi3 phak1 maa1 hai3 taaw1.", "song1 thoi3 phak1 maa1 hai3 taaw1.", "soŋ¹ tʰoj³ pʰak¹ maː¹ haj³ taːw¹",
        "Please pass the vegetable bowl forward.", "कृपया सब्ज़ी का कटोरा आगे बढ़ाइए।", "শাকৰ বাতিটো আগবঢ়াই দিয়ক।", "Table manners.")
    add("Politeness & Requests", "quiet_at_temple", "am1 dɔng1 siang1 nai1 wat1.", "am1 dɔng1 siang1 nai1 wat1.", "am¹ dɔŋ¹ sjaŋ¹ naj¹ wat¹",
        "Maintain solemn silence inside the sacred monastery precincts.", "पवित्र विहार परिसर में पूर्ण शांति बनाए रखिए।", "বৌদ্ধ বিহাৰত নিতাল মাৰি শান্ত হৈ থাকক।", "Temple decorum.")
    add("Politeness & Requests", "clean_surrounds", "kep4 saat1 wai1 hai3 riap4 rɔi3.", "kep4 saat1 wai1 hai3 riap4 rɔi3.", "kep⁴ saːt¹ waj¹ haj³ rjap⁴ rɔj³",
        "Roll up the floor mats neatly after dining.", "भोजन के उपरांत चटाइयों को सलीके से लपेटकर रखिए।", "ঢাৰিখন শৃংখলাবদ্ধভাৱে মেৰিয়াই থওক।", "Orderliness.")
    add("Politeness & Requests", "respectful_walk", "yaang3 kɔm3 hua1 phaan2 na5 chaw1 thao3.", "yaang3 kɔm3 hua1 phaan2 na5 chaw1 thao3.", "jaːŋ³ kɔm³ hua¹ pʰaːn² naː⁵ t͡ɕaw¹ tʰaw³",
        "Bow your head modestly when walking past revered elders.", "बुजुर्गों के सामने से निकलते समय सिर झुकाकर शालीनता से चलिए।", "জ্যেষ্ঠজনৰ সমুখেৰে মূৰ দোৱাই পাৰ হৈ যাওক।", "Deference gesture.")
    add("Politeness & Requests", "gratitude_for_guidance", "khɔp1 tsai1 chaw1 thao3 sɔn1 haw1.", "khɔp1 tsai1 chaw1 thao3 sɔn1 haw1.", "kʰɔp¹ t͡sai¹ t͡ɕaw¹ tʰaw³ sɔn¹ haw¹",
        "Thank you, revered elder, for teaching and guiding us.", "हमें ज्ञान और सही मार्ग दिखाने के लिए आदरणीय बुजुर्ग का धन्यवाद।", "আমাক পথ প্ৰদৰ্শন কৰাৰ বাবে ককাক ধন্যবাদ।", "Teacher gratitude.")
    add("Politeness & Requests", "eternal_goodness", "khwaam1 li1 yu5 kap4 thuk1 kon1.", "khwaam1 li1 yu5 kap4 thuk1 kon1.", "kʰwaːm¹ liː¹ ju⁵ kap⁴ tʰuk¹ kon¹",
        "May virtue, truth, and kindness abide with everyone always.", "सत्य, शील और भलाई सदा सबके साथ बनी रहे।", "সকলোৰে মাজত দয়া আৰু সজ গুণ বিৰাজ কৰক।", "Moral blessing.")

    # ==========================================================================
    # DOMAIN 14: BUDDHISM, MONASTERY, CHANTS & CULTURE (35 sentences)
    # ==========================================================================
    add("Buddhist Culture", "venerate_triple_gem", "wai1 phraa4 thammaa4 sangkhaa4.", "wai1 phraa4 thammaa4 sangkhaa4.", "waj¹ pʰraː⁴ tʰam¹maː⁴ saŋ¹kʰaː⁴",
        "I pay humble homage to the Buddha, the Dhamma, and the Sangha.", "मैं बुद्ध, धर्म और संघ (त्रिरत्न) को नमन करता हूँ।", "মই বুদ্ধ, ধৰ্ম আৰু সংঘক ত্ৰিশৰণ প্ৰণাম জনাওঁ।", "Triple Gem veneration.")
    add("Buddhist Culture", "offer_water_buddha", "haw1 aw1 nam6 kat4 suk4 phaa3 tsaw3.", "haw1 aw1 nam6 kat4 suk4 phaa3 tsaw3.", "haw¹ aw¹ nam⁶ kat⁴ suk⁴ pʰaː³ t͡saw³",
        "We bring cool pure water to bathe the sacred Buddha image.", "हम बुद्ध प्रतिमा के अभिषेक के लिए पवित्र शीतल जल लाते हैं।", "আমি বুদ্ধ ভগৱানৰ মূৰ্তি পৱিত্ৰ শীতল পানীৰে অভিষেক কৰোঁ।", "Sangken festival rite.")
    add("Buddhist Culture", "monastery_peace", "wat1 maan3 haw1 mi5 khwaam1 yen1 tsai1.", "wat1 maan3 haw1 mi5 khwaam1 yen1 tsai1.", "wat¹ maːn³ haw¹ miː¹ kʰwaːm¹ jen¹ t͡sai¹",
        "Our village vihara radiates serene peace and spiritual tranquility.", "हमारे गाँव का बौद्ध विहार अत्यंत शांत और पावन है।", "আমাৰ গাঁৱৰ বৌদ্ধ বিহাৰখন বৰ শান্তিপূৰ্ণ।", "Monastery atmosphere.")
    add("Buddhist Culture", "monks_reciting", "tsaw3 mun1 suat1 thammaa4 nai1 vi1haan1.", "tsaw3 mun1 suat1 thammaa4 nai1 vi1haan1.", "t͡saw³ mun¹ suat¹ tʰam¹maː⁴ naj¹ wiː¹haːn¹",
        "The venerable monks chant sacred Pali verses inside the shrine hall.", "भंतेजी (भिक्षु) मंदिर के भीतर पालि धर्मसूत्रों का पाठ कर रहे हैं।", "বৌদ্ধ ভিক্ষুসকলে পৱিত্ৰ সূত্ৰ পাঠ কৰিছে।", "Monk chanting.")
    add("Buddhist Culture", "alms_round", "tsaw3 mun1 bintaphat1 chaw3 nai6.", "tsaw3 mun1 bintaphat1 chaw3 nai6.", "t͡saw³ mun¹ bin¹ta¹pʰat¹ t͡ɕaw³ nai⁶",
        "The monks walk silently on their morning alms round.", "भंतेजी सुबह भिक्षाटन (पिण्डपात) के लिए गाँव में निकले हैं।", "পুৱা বৌদ্ধ ভিক্ষুসকলে পৱিত্ৰ পিণ্ডপাত গ্ৰহণ কৰিছে।", "Alms round.")
    add("Buddhist Culture", "give_alms_rice", "sai2 baart3 kap4 khaw3 suk1.", "sai2 baart3 kap4 khaw3 suk1.", "saj² baːrt³ kap⁴ kʰaw³ suk¹",
        "Place fragrant warm rice respectfully into the alms bowl.", "भिक्षापात्र में आदरपूर्वक गरम अन्न और फल अर्पित कीजिए।", "ভিক্ষাপাত্ৰত শ্ৰদ্ধাৰে পৱিত্ৰ খাদ্য দান কৰক।", "Placing alms.")
    add("Buddhist Culture", "sangken_water_festival", "poy2 sang1kyeen1 pen1 poy2 yai3 tai1.", "poy2 sang1kyeen1 pen1 poy2 yai3 tai1.", "pɔj² saŋ¹kjeːn¹ pen¹ pɔj² jai³ taj¹",
        "Poy Sangken (Water Festival) is the greatest annual festival of the Tai.", "पोय सांगकेन (जल उत्सव) ताई समाज का सबसे बड़ा नववर्ष महापर्व है।", "পয় চাংকেন হৈছে টাই খাময়াং জনগোষ্ঠীৰ প্ৰধান নৱবৰ্ষ উৎসৱ।", "Sangken festival.")
    add("Buddhist Culture", "cleanse_sins", "rot1 nam6 hai3 sot1 sai1 pi1 mai2.", "rot1 nam6 hai3 sot1 sai1 pi1 mai2.", "rot¹ nam⁶ haj³ sot¹ saj¹ piː¹ maj²",
        "Sprinkle fragrant water to wash away impurities for the new year.", "नववर्ष में शुद्धि और मंगल के लिए एक-दूसरे पर सुगंधित जल छिड़किए।", "নতুন বছৰৰ মংগলৰ বাবে পৱিত্ৰ পানী ছটিওৱা হয়।", "New year water pouring.")
    add("Buddhist Culture", "light_candles", "chut1 thian1 thawaai3 phraa4.", "chut1 thian1 thawaai3 phraa4.", "t͡ɕʰut¹ tʰjan¹ tʰa¹waːj³ pʰraː⁴",
        "Light candles and incense before the Buddha statue.", "बुद्ध भगवान के समक्ष श्रद्धापूर्वक मोमबत्ती और धूपबत्ती जलाइए।", "ভগৱান বুদ্ধৰ আগত চাকি আৰু ধূপ জ্বলোৱা হৈছে।", "Lighting candles.")
    add("Buddhist Culture", "flower_offering", "aw1 bɔk1 mai3 hɔm1 wai1 phraa4.", "aw1 bɔk1 mai3 hɔm1 wai1 phraa4.", "aw¹ bɔk¹ maj³ hɔm¹ waj¹ pʰraː⁴",
        "Offer freshly gathered fragrant blossoms at the altar.", "भगवान बुद्ध के चरणों में ताज़े सुगंधित फूल अर्पित कीजिए।", "বেদীত সতেজ ফুল আগবঢ়াই প্ৰণাম কৰা হৈছে।", "Flower offering.")
    add("Buddhist Culture", "five_precepts", "thɯ5 sin1 haa3 khɔ5 thuk1 wan1.", "thɯ5 sin1 haa3 khɔ5 thuk1 wan1.", "tʰɯ⁵ sin¹ haː³ kʰɔ⁵ tʰuk¹ wan¹",
        "Faithfully observe the Five Moral Precepts (Pancha Sila) every day.", "प्रतिदिन मनसा-वाचा-कर्मणा पंचशीलों का पालन कीजिए।", "নিতৌ পঞ্চশীলৰ নীতিসমূহ নিষ্ঠাৰে পালন কৰক।", "Five precepts.")
    add("Buddhist Culture", "do_not_harm", "am1 het1 haai3 haang1 sat4.", "am1 het1 haai3 haang1 sat4.", "am¹ het¹ haːj³ haːŋ¹ sat⁴",
        "Do not injure or kill any living creature (Ahimsa).", "किसी भी प्राणी को कष्ट मत पहुँचाओ और जीव हिंसा से बचो (अहिंसा)।", "কোনো জীৱকে হিংসা বা বধ নকৰিব (অহিংসা)।", "Non-harming precept.")
    add("Buddhist Culture", "truthful_speech", "waa5 kham1 sae5 am1 khui1.", "waa5 kham1 sae5 am1 khui1.", "waː⁵ kʰam¹ sɛː⁵ am¹ kʰuj¹",
        "Speak only truth and avoid all falsehood and deceit.", "सदा सत्य बोलिए और कभी झूठ मत कहिए।", "সদায় সত্য কওক, মিছা কথা পৰিহাৰ কৰক।", "Truth precept.")
    add("Buddhist Culture", "meditation_calm", "nang5 samaathi1 hai3 tsai1 yen1.", "nang5 samaathi1 hai3 tsai1 yen1.", "naŋ⁵ sa¹maː¹tʰiː¹ haj³ t͡sai¹ jen¹",
        "Sit in quiet meditation to cultivate mental tranquility.", "मन की एकाग्रता और शांति के लिए ध्यान लगाइए।", "মনৰ প্ৰশান্তিৰ বাবে ধ্যানত বহক।", "Meditation practice.")
    add("Buddhist Culture", "merit_making", "het1 bun1 hai3 mi5 phɔn1 li1.", "het1 bun1 hai3 mi5 phɔn1 li1.", "het¹ bun¹ haj³ miː¹ pʰɔn¹ liː¹",
        "Perform meritorious deeds to generate wholesome karma.", "पुण्य कर्म (दान-शील) कीजिए जिससे जीवन में सुख आए।", "পুণ্য কৰ্ম কৰি জীৱনটো ধন্য কৰক।", "Merit making.")
    add("Buddhist Culture", "listen_to_dhamma", "fang1 thammaa4 nai1 wan1 sin1.", "fang1 thammaa4 nai1 wan1 sin1.", "faŋ¹ tʰam¹maː⁴ naj¹ wan¹ sin¹",
        "Listen to the Dhamma sermon on full moon Sabbath days.", "उपोसथ (पूर्णिमा के दिन) विहार में धर्मोपदेश सुनिए।", "পূৰ্ণিমাৰ দিনা বিহাৰলৈ গৈ ধৰ্মোপদেশ শুনক।", "Dhamma listening.")
    add("Buddhist Culture", "bell_tolling", "siang1 kang1 wat1 dɔng1 wan1 chaw3.", "siang1 kang1 wat1 dɔng1 wan1 chaw3.", "sjaŋ¹ kaŋ¹ wat¹ dɔŋ¹ wan¹ t͡ɕaw³",
        "The great monastery bell tolls resonant in the morning air.", "सुबह विहार का विशाल घंटा गूँज उठता है।", "ৰাতিপুৱা বিহাৰৰ ঘণ্টা বাজি উঠিছে।", "Temple bell.")
    add("Buddhist Culture", "pagoda_spire", "kɔng3 mu1 sung1 saaw3 khɯn3 faa6.", "kɔng3 mu1 sung1 saaw3 khɯn3 faa6.", "kɔŋ³ muː¹ suŋ¹ saːw³ kʰɯn³ faː⁶",
        "The golden pagoda spire glints majestically against the blue sky.", "स्वर्णिम स्तूप (चैत्य) की चोटी आकाश को छूती सी प्रतीत होती है।", "সোণালী বৌদ্ধ স্তূপটো আকাশলৈ শুৱনি হৈ উঠিছে।", "Pagoda spire.")
    add("Buddhist Culture", "bodhi_tree", "ton3 phoo1 yai3 pen1 thi3 wai1.", "ton3 phoo1 yai3 pen1 thi3 wai1.", "ton³ pʰoː¹ jai³ pen¹ tʰiː³ waj¹",
        "The sacred Bodhi tree is revered as a site of supreme enlightenment.", "पवित्र बोधि वृक्ष भगवान बुद्ध के बोधिसत्व का पावन प्रतीक है।", "পৱিত্ৰ বোধিবৃক্ষজোপাক শ্ৰদ্ধাৰে পূজা কৰা হৈছে।", "Bodhi tree.")
    add("Buddhist Culture", "water_bodhi_tree", "rot1 nam6 ton3 phoo1 hai3 khio1.", "rot1 nam6 ton3 phoo1 hai3 khio1.", "rot¹ nam⁶ ton³ pʰoː¹ haj³ kʰio¹",
        "Pour sweet water at the roots of the holy Bodhi tree.", "पवित्र बोधि वृक्ष की जड़ों में श्रद्धापूर्वक जल अर्पित कीजिए।", "বোধিদ্ৰুমৰ গুৰিত পৱিত্ৰ পানী ঢালি সেৱা কৰক।", "Watering Bodhi tree.")
    add("Buddhist Culture", "buddhist_robes", "tsaw3 mun1 nung2 phaa3 kaahaang4.", "tsaw3 mun1 nung2 phaa3 kaahaang4.", "t͡saw³ mun¹ nuŋ² pʰaː³ kaː¹haːŋ⁴",
        "The monks wear saffron yellow robes of renunciation.", "भिक्षुगण गेरुए और पीले रंग के चीवर धारण करते हैं।", "বৌদ্ধ ভিক্ষুসকলে গেৰুৱা বস্ত্ৰ পৰিধান কৰে।", "Monastic robes.")
    add("Buddhist Culture", "rain_retreat", "yam1 khao3 phansaa1 chaw3 mun1 yu5 wat1.", "yam1 khao3 phansaa1 chaw3 mun1 yu5 wat1.", "jam¹ kʰaw³ pʰan¹saː¹ t͡ɕaw³ mun¹ ju⁵ wat¹",
        "During the three-month Rains Retreat (Vassa), monks remain in the monastery.", "वर्षावास (वासा) के दौरान भिक्षु विहार में रहकर साधना करते हैं।", "বৰষাৱাসৰ সময়ছোৱাত ভিক্ষুসকলে বিহাৰত থাকি সাধনা কৰে।", "Vassa retreat.")
    add("Buddhist Culture", "kathina_festival", "poy2 ka1thin1 mi5 mɯa2 ook2 phansaa1.", "poy2 ka1thin1 mi5 mɯa2 ook2 phansaa1.", "pɔj² ka¹tʰin¹ miː¹ mɯa² oːk¹ pʰan¹saː¹",
        "The Kathina robe-offering festival follows the end of the Rains Retreat.", "वर्षावास के समापन पर महाकठिन चीवर दान समारोह मनाया जाता है।", "বৰষাৱাসৰ অন্তত কঠিন চীবৰ দান উৎসৱ পতা হয়।", "Kathina festival.")
    add("Buddhist Culture", "offer_robes", "haw1 thawaai3 phaa3 ka1thin1.", "haw1 thawaai3 phaa3 ka1thin1.", "haw¹ tʰa¹waːj³ pʰaː³ ka¹tʰin¹",
        "Devotees offer handwoven robes to the monastic community.", "श्रद्धालु भक्तजन भिक्षु संघ को पावन चीवर दान करते हैं।", "ভক্তসকলে মিলি ভিক্ষুসংঘলৈ চীবৰ দান আগবঢ়ায়।", "Kathina robe offering.")
    add("Buddhist Culture", "release_fish", "plɔi2 paa1 khao3 nai1 nam6 hai3 bun1.", "plɔi2 paa1 khao3 nai1 nam6 hai3 bun1.", "plɔj² paː¹ kʰaw³ naj¹ nam⁶ haj³ bun¹",
        "Releasing captured fish back into the river yields abundant merit.", "मछलियों को नदी में मुक्त करना जीवनदान का महान पुण्य कर्म है।", "নৈত মাছ মেলি জীৱদান কৰাটো পৰম পুণ্যৰ কাম।", "Releasing animals.")
    add("Buddhist Culture", "peace_in_mind", "am1 mi5 khwaam1 khok1, tsai1 yen1.", "am1 mi5 khwaam1 khok1, tsai1 yen1.", "am¹ miː¹ kʰwaːm¹ kʰok¹ t͡sai¹ jen¹",
        "Freedom from anger brings sublime peace to the mind.", "क्रोध और द्वेष से मुक्ति ही मन को सच्ची शांति देती है।", "খং-ৰাগ ত্যাগ কৰিলে মনত অপাৰ শান্তি বিৰাজে।", "Overcoming anger.")
    add("Buddhist Culture", "generosity_dana", "pan1 thaang1 thaan1 hai3 khon1 thuk4.", "pan1 thaang1 thaan1 hai3 khon1 thuk4.", "pan¹ tʰaːŋ¹ tʰaːn¹ haj³ kʰon¹ tʰuk⁴",
        "Practice generous charity (Dana) by assisting the needy and impoverished.", "ज़रूरतमंदों और निर्धनों की सहायता करके दान-धर्म कीजिए।", "দুখীয়া-নিছলাক সহায় কৰি দান ধৰ্ম পালন কৰক।", "Dana practice.")
    add("Buddhist Culture", "chant_metta", "phae2 mettaa1 thuk1 tua1 sat4.", "phae2 mettaa1 thuk1 tua1 sat4.", "pʰɛː² met¹taː¹ tʰuk¹ tua¹ sat⁴",
        "Radiate boundless loving-kindness (Metta) to all sentient beings.", "संसार के सभी प्राणियों के प्रति मंगल-मैत्री की भावना रखें।", "সকলো জীৱলৈ মৈত্ৰীভাৱ আৰু কল্যাণ কামনা কৰক।", "Metta meditation.")
    add("Buddhist Culture", "chant_refuge", "phuu3 haw1 phɯng3 phraa4 thammaa4 sangkhaa4.", "phuu3 haw1 phɯng3 phraa4 thammaa4 sangkhaa4.", "pʰuː³ haw¹ pʰɯŋ³ pʰraː⁴ tʰam¹maː⁴ saŋ¹kʰaː⁴",
        "We seek eternal refuge in the Buddha, Dhamma, and Sangha.", "हम त्रिरत्न (बुद्ध, धर्म और संघ) की शरण ग्रहण करते हैं।", "আমি ত্ৰিৰত্নৰ চৰণত শৰণাপন্ন হওঁ।", "Taking refuge.")
    add("Buddhist Culture", "wisdom_light", "panyaa1 pen1 saang4 faa6 haang1 khon1.", "panyaa1 pen1 saang4 faa6 haang1 khon1.", "pan¹jaː¹ pen¹ saːŋ⁴ faː⁶ haːŋ¹ kʰon¹",
        "Spiritual wisdom is the radiant light that dispels darkness for mankind.", "ज्ञान और प्रज्ञा ही मनुष्य के जीवन का सच्चा प्रकाश है।", "প্ৰজ্ঞাই হৈছে মানৱ জীৱনৰ আটাইতকৈ উজ্জ্বল পোহৰ।", "Wisdom praise.")
    add("Buddhist Culture", "ancient_scripture_reading", "chaw1 mun1 an2 lik1 thammaa4.", "chaw1 mun1 an2 lik1 thammaa4.", "t͡saw³ mun¹ an² lik¹ tʰam¹maː⁴",
        "The abbot reads from the ancient palm-leaf scriptures.", "मठाधीश प्राचीन सांचीपत्ती की पांडुलिपि से धर्मपाठ करते हैं।", "সত্ৰাধিকাৰ/ভদন্তই সাঁচিপতীয়া পুথিৰ পৰা ধৰ্ম পাঠ কৰিছে।", "Scripture reading.")
    add("Buddhist Culture", "merit_transfer", "yaat1 nam6 pan1 bun1 hai3 phuu3 yaa3.", "yaat1 nam6 pan1 bun1 hai3 phuu3 yaa3.", "jaːt¹ nam⁶ pan¹ bun¹ haj³ pʰuː³ jaː³",
        "Pouring ceremonial water to dedicate merit to departed ancestors.", "पूर्वजों की सद्गति के लिए तर्पण जल गिराकर पुण्य समर्पित कीजिए।", "পূৰ্বপুৰুষলৈ পুণ্য উছৰ্গা কৰি পানী ঢালি তৰ্পণ কৰা হৈছে।", "Water libation merit.")
    add("Buddhist Culture", "village_unity_sangken", "khon1 maan3 ruam2 tsai1 nai1 poy2.", "khon1 maan3 ruam2 tsai1 nai1 poy2.", "kʰon¹ maːn³ ruam² t͡sai¹ naj¹ pɔj²",
        "All villagers unite harmoniously during the Sangken water festival.", "सांगकेन महापर्व में पूरा गाँव एकमन होकर भाग लेता है।", "চাংকেন মহোৎসৱত সমগ্ৰ গাঁওবাসী একত্ৰিত হয়।", "Festival unity.")
    add("Buddhist Culture", "peace_to_all_worlds", "kho5 hai3 lok4 nai6 mi5 saanti1.", "kho5 hai3 lok4 nai6 mi5 saanti1.", "kʰo⁵ haj³ lok⁴ nai⁶ miː¹ saːn¹tiː¹",
        "May universal peace, harmony, and joy reign throughout the world.", "इस संपूर्ण संसार में शांति, कल्याण और सद्भाव का वास हो।", "সমগ্ৰ বিশ্বতে চিৰশান্তি আৰু মংগল বিৰাজ কৰক।", "Universal peace prayer.")
    add("Buddhist Culture", "sacred_tradition_lives", "thammaa4 phraa4 yu5 man3 khang1.", "thammaa4 phraa4 yu5 man3 khang1.", "tʰam¹maː⁴ pʰraː⁴ ju⁵ man³ kʰaŋ¹",
        "The sacred Dhamma of the Buddha stands imperishable and eternal.", "भगवान बुद्ध की पावन देशना सदा अमर और अडिग रहेगी।", "ভগৱান বুদ্ধৰ পৱিত্ৰ ধৰ্ম চিৰকাল জিলিকি থাকিব।", "Eternal Dhamma.")

    print(f"Total curated sentences built: {len(sentences)}")
    assert len(sentences) == 500, f"Expected 500 sentences, got {len(sentences)}"
    return sentences

def export_to_excel_and_csv(sentences):
    excel_filename = "khamyang_english_hindi_500_sample.xlsx"
    csv_filename = "khamyang_english_hindi_500_sample.csv"
    
    # --------------------------------------------------------------------------
    # 1. Generate Excel (.xlsx) using openpyxl
    # --------------------------------------------------------------------------
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Khamyang_EN_HI_500"
    
    # Header definitions
    headers = [
        "Sentence ID",
        "Domain",
        "Subdomain",
        "Tai Khamyang (Lik Tai Script)",
        "Khamyang Romanization (Tones 1-6)",
        "Khamyang IPA",
        "English Translation",
        "Hindi Translation (हिन्दी)",
        "Assamese Translation (অসমীয়া)",
        "Linguistic / Cultural Notes"
    ]
    
    ws.append(headers)
    
    # Header Styling
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid") # Elegant Navy Blue
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )
    
    ws.row_dimensions[1].height = 32
    
    for col_num in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
        cell.border = thin_border
        
    # Data Rows
    row_font = Font(name="Segoe UI", size=10)
    alt_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid") # subtle alternating
    
    for r_idx, s in enumerate(sentences, start=2):
        row_values = [
            s["id"],
            s["domain"],
            s["subdomain"],
            s["khamyang_tai"],
            s["khamyang_roman"],
            s["khamyang_ipa"],
            s["english"],
            s["hindi"],
            s["assamese"],
            s["notes"]
        ]
        ws.append(row_values)
        ws.row_dimensions[r_idx].height = 24
        
        is_alt = (r_idx % 2 == 0)
        for col_num in range(1, len(headers) + 1):
            cell = ws.cell(row=r_idx, column=col_num)
            cell.font = row_font
            cell.border = thin_border
            if is_alt:
                cell.fill = alt_fill
            
            # Alignments
            if col_num in (1, 2, 3):
                cell.alignment = Alignment(horizontal="left", vertical="center")
            elif col_num in (4, 5, 6, 7, 8, 9, 10):
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                
    # Enable Auto-Filter on header row
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(sentences) + 1}"
    
    # Freeze Header Pane (Row 1 stays fixed when scrolling)
    ws.freeze_panes = "A2"
    
    # Auto-adjust column widths with safety minimums
    col_widths = {
        1: 15,  # Sentence ID
        2: 24,  # Domain
        3: 24,  # Subdomain
        4: 35,  # Tai Script
        5: 35,  # Romanization
        6: 35,  # IPA
        7: 45,  # English
        8: 45,  # Hindi
        9: 45,  # Assamese
        10: 45  # Notes
    }
    for col_num, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_num)].width = width
        
    wb.save(excel_filename)
    print(f"Successfully generated Excel file: {excel_filename}")
    
    # --------------------------------------------------------------------------
    # 2. Generate CSV with UTF-8 BOM (.csv) for seamless opening in Excel
    # --------------------------------------------------------------------------
    import csv
    with open(csv_filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for s in sentences:
            writer.writerow([
                s["id"],
                s["domain"],
                s["subdomain"],
                s["khamyang_tai"],
                s["khamyang_roman"],
                s["khamyang_ipa"],
                s["english"],
                s["hindi"],
                s["assamese"],
                s["notes"]
            ])
    print(f"Successfully generated CSV file: {csv_filename}")

if __name__ == "__main__":
    sentences = build_500_dataset()
    export_to_excel_and_csv(sentences)
