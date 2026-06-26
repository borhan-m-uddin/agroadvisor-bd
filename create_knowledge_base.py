import os
from pathlib import Path

# Create all directories
dirs = [
    "data/knowledge_base/crops/rice",
    "data/knowledge_base/crops/wheat",
    "data/knowledge_base/crops/maize",
    "data/knowledge_base/crops/jute",
    "data/knowledge_base/crops/sugarcane",
    "data/knowledge_base/crops/potato",
    "data/knowledge_base/crops/vegetables",
    "data/knowledge_base/crops/fruits",
    "data/knowledge_base/crops/pulses",
    "data/knowledge_base/crops/oilseeds",
    "data/knowledge_base/crops/spices",
    "data/knowledge_base/diseases/fungal",
    "data/knowledge_base/diseases/bacterial",
    "data/knowledge_base/diseases/viral",
    "data/knowledge_base/diseases/nematode",
    "data/knowledge_base/pests",
    "data/knowledge_base/soil",
    "data/knowledge_base/irrigation",
    "data/knowledge_base/fertilizer",
    "data/knowledge_base/climate",
    "data/knowledge_base/livestock",
    "data/knowledge_base/fisheries",
    "data/knowledge_base/post_harvest",
    "data/knowledge_base/economics",
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

# ═══════════════════════════════════════════════════
# ALL KNOWLEDGE FILES
# ═══════════════════════════════════════════════════

files = {}

# ───────────────────────────────────────────────────
# RICE — Complete Coverage
# ───────────────────────────────────────────────────

files["crops/rice/rice_production_overview.txt"] = """
TOPIC: Rice Production in Bangladesh
SOURCE: BRRI, DAE, FAO
LANGUAGE: English + Bengali

Bangladesh is one of the world's top rice producers. Rice is grown in three seasons:
- Boro (irrigated winter rice): November-May, highest yield, 55% of total production
- Aman (monsoon rice): June-December, largest area, rain-fed
- Aus (pre-monsoon rice): March-August, smallest area, declining

Total rice production: 37-38 million metric tons annually
Rice cultivated area: 11.5-12 million hectares
Average yield: 3.0-3.5 tons/hectare (HYV can give 6-8 tons/hectare)

Major rice growing districts:
Boro: Sylhet, Mymensingh, Rajshahi, Dinajpur, Rangpur
Aman: All districts, especially coastal areas
Aus: Mymensingh, Jamalpur, Kishorgonj

বাংলাদেশে ধান চাষ:
তিনটি মৌসুমে ধান চাষ হয়:
- বোরো: নভেম্বর-মে, সেচনির্ভর, সর্বোচ্চ ফলন
- আমন: জুন-ডিসেম্বর, বৃষ্টিনির্ভর, সবচেয়ে বেশি জমি
- আউশ: মার্চ-আগস্ট, কম জমি, কমছে
"""

files["crops/rice/rice_varieties_complete.txt"] = """
TOPIC: Complete Rice Variety Guide for Bangladesh
SOURCE: BRRI
LANGUAGE: English + Bengali

== BORO RICE VARIETIES (Winter/Irrigated) ==

BRRI dhan28:
- Yield: 6.0-7.0 ton/ha
- Duration: 140-145 days
- Disease resistance: Moderate blast tolerance
- Suitable: All boro growing areas

BRRI dhan29:
- Yield: 7.0-8.0 ton/ha
- Duration: 155-160 days
- Most popular variety in Bangladesh
- Note: Susceptible to late planting

BRRI dhan47:
- Yield: 6.0-7.0 ton/ha
- Salinity tolerant up to 8 dS/m
- Blast resistant
- Suitable: Coastal areas

BRRI dhan58:
- Yield: 7.0-8.0 ton/ha
- Zinc enriched (nutritionally superior)
- Duration: 148-153 days

BRRI dhan74:
- Yield: 7.0-8.0 ton/ha
- Thermo-tolerant (withstands high night temperature)
- Duration: 145-150 days

BRRI dhan84:
- Yield: 8.0-9.0 ton/ha
- Blast resistant
- Duration: 148-155 days

BRRI dhan86:
- Yield: 9.0-10.0 ton/ha
- Duration: 152-158 days
- Heat tolerant

Bangabandhu Dhan100 (BB Dhan100):
- Yield: 6.0-7.0 ton/ha
- Aromatic, premium quality
- Zinc enriched

== AMAN RICE VARIETIES (Monsoon) ==

BRRI dhan49:
- Yield: 5.0-6.0 ton/ha
- Submergence tolerant (flash flood up to 14 days)
- Duration: 135-140 days

BRRI dhan51:
- Yield: 4.5-5.5 ton/ha
- Deep water tolerant
- Suitable: Haor areas

BRRI dhan52:
- Yield: 4.5-5.0 ton/ha
- Late submergence tolerant
- Duration: 143-148 days

BRRI dhan87:
- Yield: 5.0-6.0 ton/ha
- Salinity tolerant (aman season)
- Suitable: Coastal aman areas

BRRI dhan93, BRRI dhan94:
- Newly released flood tolerant
- Duration: 130-140 days

== জাত নির্বাচন গাইড ==
বোরো মৌসুমের সেরা জাত: BRRI dhan29 (সর্বোচ্চ ফলন)
ব্লাস্ট প্রতিরোধী: BRRI dhan28, BRRI dhan47, BRRI dhan84
লবণ সহনশীল: BRRI dhan47, BRRI dhan61, BRRI dhan87
বন্যা সহনশীল: BRRI dhan49, BRRI dhan51, BRRI dhan52
সুগন্ধি: BB Dhan100, BRRI dhan50
"""

files["crops/rice/rice_diseases_complete.txt"] = """
TOPIC: All Rice Diseases in Bangladesh
SOURCE: BRRI, IRRI
LANGUAGE: English + Bengali

== 1. BLAST DISEASE (ব্লাস্ট রোগ) ==
Pathogen: Magnaporthe oryzae
Type: Fungal
Severity: Most destructive rice disease in Bangladesh

Symptoms:
- Leaf blast: Diamond-shaped gray-brown lesions
- Neck blast: Black lesion at neck node, white head (সাদা মাথা)
- Node blast: Black/rotten internodes

Favorable conditions:
- Temperature: 24-28°C
- Humidity: >90%
- Cloudy weather, heavy dew
- Excess nitrogen fertilizer

Management:
Chemical: Tricyclazole 0.75g/L OR Isoprothiolane 1.5ml/L
Apply: 2 sprays at 7-10 day intervals
Resistant varieties: BRRI dhan28, BRRI dhan47, BRRI dhan84
Cultural: Avoid excess nitrogen, maintain water in field

== 2. SHEATH BLIGHT (শিথ ব্লাইট) ==
Pathogen: Rhizoctonia solani
Type: Fungal

Symptoms:
- Oval/irregular greenish-gray lesions on leaf sheath
- White mycelium visible in humid conditions
- Lesions have brown border
- Severe cases cause lodging

Management:
Chemical: Hexaconazole 1ml/L OR Validamycin 2ml/L
Cultural: Reduce plant density, increase potash fertilizer
Avoid: Excess nitrogen

== 3. BACTERIAL LEAF BLIGHT (ব্যাকটেরিয়াল লিফ ব্লাইট) ==
Pathogen: Xanthomonas oryzae pv. oryzae
Type: Bacterial

Symptoms:
- Yellowing from leaf tip/margins
- Water-soaked lesions spread from edges
- Bacterial ooze visible in morning
- Field appears gray-brown

Management:
- Copper-based bactericides
- Reduce nitrogen fertilizer
- Resistant varieties: BRRI dhan29, BRRI dhan50
- Remove infected plants

== 4. BROWN SPOT (বাদামী দাগ রোগ) ==
Pathogen: Bipolaris oryzae
Type: Fungal

Symptoms:
- Circular/oval brown lesions on leaves
- White/gray center with brown margin
- Affects grain causing discoloration

Management:
- Mancozeb 2.5g/L spray
- Improve soil nutrition (potassium)
- Use healthy seeds

== 5. FALSE SMUT (মিথ্যা কাণ্ডপচা / ফলস স্মাট) ==
Pathogen: Ustilaginoidea virens
Type: Fungal

Symptoms:
- Individual grains converted to orange-green spore balls
- Balls enlarge and burst, releasing spores
- Affects grain quality

Management:
- Propiconazole spray at heading
- Avoid dense planting

== 6. SHEATH ROT ==
Pathogen: Sarocladium oryzae
Type: Fungal

Symptoms:
- Irregular lesions on flag leaf sheath
- Causes grain sterility
- Brown discoloration inside sheath

Management:
- Carbendazim spray
- Balanced fertilization

== 7. TUNGRO DISEASE (টুংরো রোগ) ==
Cause: Virus transmitted by green leafhopper
Type: Viral

Symptoms:
- Yellow-orange discoloration of leaves
- Stunted plant growth
- Reduced tillering
- Incomplete panicle emergence

Management:
- Control leafhopper vector: Imidacloprid spray
- Use resistant varieties: BRRI dhan27
- Remove infected plants early

== সংক্ষিপ্ত রোগ চেনার চার্ট ==
সাদা মাথা → ব্লাস্ট রোগ (গলা পচা)
পাতায় হীরা আকৃতির দাগ → ব্লাস্ট
পাতার খোলে ডিম্বাকৃতি দাগ → শিথ ব্লাইট
পাতা ডগা থেকে হলুদ → ব্যাকটেরিয়াল ব্লাইট
পাতায় বাদামী গোলাকার দাগ → ব্রাউন স্পট
দানায় সবুজ বল → ফলস স্মাট
গাছ বামন, পাতা হলুদ-কমলা → টুংরো
"""

files["crops/rice/rice_pest_complete.txt"] = """
TOPIC: All Rice Pests in Bangladesh
SOURCE: BRRI, IRRI, brri_rice_insect_pest_management_bd
LANGUAGE: English + Bengali

== 1. YELLOW STEM BORER (হলুদ মাজরা পোকা) ==
Scientific name: Scirpophaga incertulas
Most damaging pest in Bangladesh

Damage:
- Dead heart in vegetative stage (central shoot dies)
- White ear in reproductive stage (empty panicle)

Management:
- Carbofuran 3G: 20 kg/ha in soil
- Chlorpyrifos 20EC: 2ml/L spray
- Light trap to catch moths
- Remove egg masses from leaves

চেনার উপায়: কেন্দ্রীয় কুশি মরে যায় (ডেড হার্ট), শিষ সাদা হয় (হোয়াইট ইয়ার)

== 2. BROWN PLANTHOPPER (বাদামী গাছফড়িং) ==
Scientific name: Nilaparvata lugens
Can cause complete crop loss (hopper burn)

Damage:
- Sucks sap from base of plants
- Circular brown patches (hopper burn)
- Transmits grassy stunt and ragged stunt viruses

Management:
- Imidacloprid 0.5ml/L spray at base of plants
- Buprofezin 1ml/L (disrupts molting)
- Avoid excess nitrogen
- Maintain water in field
- Preserve natural enemies

== 3. RICE HISPA (পামরি পোকা) ==
Scientific name: Dicladispa armigera

Damage:
- White streaks on leaves (larvae mine inside)
- Adults scrape leaf surface leaving silvery patches

Management:
- Cut and destroy infested leaf tips
- Malathion 2ml/L spray
- Chlorpyrifos spray

== 4. GALL MIDGE (গলমাছি) ==
Scientific name: Orseolia oryzae

Damage:
- Produces silver shoot (tubular gall)
- Tillers converted to hollow tubes
- No grain formation in affected tillers

Management:
- Carbofuran 3G in soil
- Chlorpyrifos spray
- Resistant varieties

== 5. THRIPS (থ্রিপস) ==
Damage: Curled leaves, silvery streaks, reduced tillering

Management:
- Imidacloprid 0.5ml/L
- Keep field flooded

== 6. RICE BUG (ধানের গান্ধি পোকা) ==
Scientific name: Leptocorisa oratorius

Damage: Sucks milky grain, causes empty grains and discoloration

Management:
- Malathion spray at milky stage
- Early morning spray when bugs are less active

== পোকা চেনার চার্ট ==
কেন্দ্রীয় কুশি মরা + শিষ সাদা → মাজরা পোকা
গাছের গোড়ায় বাদামী প্যাচ → বাদামী গাছফড়িং
পাতায় সাদা রেখা → পামরি পোকা
রুপালী টিউব তিলার → গলমাছি
পাতা কুঁকড়ানো + রুপালী দাগ → থ্রিপস
"""

# ───────────────────────────────────────────────────
# WHEAT
# ───────────────────────────────────────────────────

files["crops/wheat/wheat_complete.txt"] = """
TOPIC: Wheat Production and Disease Management in Bangladesh
SOURCE: BARI, USDA, blast_threat_bangladesh.pdf
LANGUAGE: English + Bengali

== PRODUCTION OVERVIEW ==
Annual production: 1.0-1.2 million metric tons
Cultivated area: 0.3-0.4 million hectares
Major districts: Dinajpur, Rajshahi, Jessore, Jashore, Pabna, Kushtia
Season: Rabi (sown November, harvested March-April)
Yield: 2.5-3.5 ton/ha (HYV)

== POPULAR VARIETIES ==
BARI Gom-26: High yield, good quality, most popular
BARI Gom-28: Heat tolerant, good for late planting
BARI Gom-33: BLAST RESISTANT — recommended after 2016
BARI Gom-30: High yield, widely grown
BAW-1143: Good baking quality

== WHEAT BLAST DISEASE (গমের ব্লাস্ট রোগ) ==
Pathogen: Magnaporthe oryzae Triticum pathotype (MoT)
FIRST APPEARED IN BANGLADESH: February 2016
First occurrence outside South America

2016 Outbreak:
- 8 districts affected: Pabna, Kushtia, Meherpur, Chuadanga, Jhenaidah, Jessore, Barisal, Bhola
- 15,000 hectares affected
- Yield loss: 25-100%

Symptoms:
- Premature bleaching of entire wheat head
- Individual spikelets bleach from base
- Seeds are shriveled and light
- No lesions on leaves (unlike rice blast)

Management:
- Use BARI Gom-33 (blast resistant variety) — PRIMARY RECOMMENDATION
- Tebuconazole 1ml/L spray at heading
- Do NOT plant wheat adjacent to rice fields
- Avoid using seeds from infected fields
- Early planting reduces risk

== OTHER WHEAT DISEASES ==
Leaf Rust (পাতার মরিচা):
- Orange-yellow pustules on leaves
- Use Propiconazole spray
- Resistant varieties: BARI Gom-26

Powdery Mildew (পাউডারি মিলডিউ):
- White powdery coating on leaves
- Favored by cool dry weather
- Tebuconazole spray

== সার সুপারিশ (গম) ==
ইউরিয়া: ১৮০-২২০ কেজি/হেক্টর
টিএসপি: ১০০-১২০ কেজি/হেক্টর
এমওপি: ৮০-১০০ কেজি/হেক্টর
জিপসাম: ৪০-৬০ কেজি/হেক্টর
সেচ: ২-৩ বার (সিআরআই, বুটিং, দুধ পর্যায়)
"""

# ───────────────────────────────────────────────────
# VEGETABLES — Complete
# ───────────────────────────────────────────────────

files["crops/vegetables/tomato_complete.txt"] = """
TOPIC: Tomato Production, Diseases and Pest Management Bangladesh
SOURCE: BARI, FAO, fao_eggplant_ipm.pdf
LANGUAGE: English + Bengali

== PRODUCTION ==
Season: Rabi (October-March), some year-round varieties
Major districts: Jessore, Jashore, Bogra, Comilla, Narsingdi
Average yield: 15-20 ton/ha (HYV up to 40-50 ton/ha)

Popular varieties:
- BARI Tomato-14: High yield, heat tolerant
- BARI Tomato-15: Good quality, processing type
- Hybrid varieties: BARI Hybrid Tomato-4, -8

== MAJOR DISEASES ==

1. Late Blight (লেট ব্লাইট):
Pathogen: Phytophthora infestans
Symptoms: Dark water-soaked lesions on leaves, white mold under leaves, fruit rot
Management:
- Mancozeb 2.5g/L spray every 7 days
- Metalaxyl+Mancozeb 2.5g/L
- Avoid overhead irrigation
- Remove infected plants

2. Bacterial Wilt (ব্যাকটেরিয়াল উইল্ট):
Pathogen: Ralstonia solanacearum
Symptoms: Sudden wilting, stem shows brown vascular ring
No chemical cure — prevention only:
- Crop rotation (3-4 years)
- Resistant varieties
- Soil sterilization before planting
- Remove infected plants immediately

3. Early Blight:
Pathogen: Alternaria solani
Symptoms: Brown concentric ring lesions on older leaves
Management: Mancozeb or Chlorothalonil spray

4. Fusarium Wilt:
Pathogen: Fusarium oxysporum
Symptoms: One-sided wilting, yellow streaks in stem
No chemical cure — use resistant varieties

5. Fruit Borer (টমেটো ফলছিদ্রকারী পোকা):
Pest: Helicoverpa armigera
Management:
- Spinosad 0.3ml/L spray
- Emamectin benzoate 0.4g/L
- Pheromone traps

== সার সুপারিশ (টমেটো) ==
গোবর সার: ১৫-২০ টন/হেক্টর
ইউরিয়া: ৩০০-৩৫০ কেজি/হেক্টর
টিএসপি: ২০০-২৫০ কেজি/হেক্টর
এমওপি: ২৫০-৩০০ কেজি/হেক্টর
ক্যালসিয়াম নাইট্রেট: ১৫০ কেজি/হেক্টর
"""

files["crops/vegetables/eggplant_brinjal.txt"] = """
TOPIC: Eggplant/Brinjal (Begun) Production and Disease Management
SOURCE: BARI, fao_eggplant_ipm.pdf
LANGUAGE: English + Bengali

বেগুন বাংলাদেশের সবচেয়ে গুরুত্বপূর্ণ সবজি।
Eggplant is the most important vegetable in Bangladesh.

== PRODUCTION ==
Annual production: 400,000+ metric tons
Year-round crop, peak October-March
Major districts: Jashore, Comilla, Bogra, Dinajpur

Popular varieties:
- BARI Begun-1 to BARI Begun-12
- Bt Brinjal (BARI Bt Begun-1 to -4): Resistant to shoot and fruit borer
- Local varieties: Nayantara, Islampuri, Singnath

== MAJOR DISEASES ==

1. Little Leaf Disease (ছোট পাতা রোগ):
Cause: Phytoplasma, spread by leafhoppers
Symptoms:
- Leaves become very small and narrow
- Bushy plant appearance
- No flowers or fruit
No chemical treatment. Management:
- Remove infected plants
- Control leafhopper with Imidacloprid 0.5ml/L
- Use disease-free seedlings

2. Damping Off (গাছের গোড়া পচা):
Cause: Pythium, Fusarium, Rhizoctonia
Symptoms: Seedlings fall over and die at soil level
Management:
- Seed treatment with Mancozeb
- Improve nursery drainage
- Avoid overwatering

3. Phomopsis Blight:
Symptoms: Water-soaked lesions on fruits and stems
Management: Mancozeb or Copper oxychloride spray

== MAJOR PEST ==
Shoot and Fruit Borer (ডগা ও ফল ছিদ্রকারী পোকা):
Pest: Leucinodes orbonalis
Most serious pest of eggplant in Bangladesh

Symptoms:
- Drooping and drying of shoot tips
- Borer holes in fruits with frass
- Infested fruits drop prematurely

Management:
- Bt Brinjal varieties — BEST SOLUTION
- Spinosad 0.3ml/L spray
- Remove and destroy infested shoots/fruits daily
- Pheromone traps for male moths

== সার সুপারিশ (বেগুন) ==
গোবর সার: ১০-১৫ টন/হেক্টর
ইউরিয়া: ২৫০-৩০০ কেজি/হেক্টর
টিএসপি: ১৫০-২০০ কেজি/হেক্টর
এমওপি: ২০০-২৫০ কেজি/হেক্টর
"""

files["crops/vegetables/potato_complete.txt"] = """
TOPIC: Potato Production and Disease Management Bangladesh
SOURCE: BARI, purdue_late_blight_tomato_potato.pdf
LANGUAGE: English + Bengali

আলু বাংলাদেশের তৃতীয় বৃহত্তম ফসল।
Potato is the 3rd largest crop in Bangladesh.

== PRODUCTION ==
Annual production: 10-11 million metric tons
Cultivated area: 470,000-500,000 hectares
Season: Rabi (October-March)
Major districts: Munshiganj, Bogra, Rangpur, Dinajpur, Comilla
Average yield: 20-22 ton/ha

Popular varieties:
- Diamant: Most popular, high yield
- Cardinal: Early variety
- Granola: Good processing quality
- BARI Alu-25: Disease resistant, local adaptation
- BARI Alu-41: Late blight resistant
- Asterix: Red skin, good quality

== MAJOR DISEASES ==

1. Late Blight (লেট ব্লাইট) — MOST SERIOUS:
Pathogen: Phytophthora infestans
Season: November-February (cold, foggy weather)

Symptoms:
- Water-soaked dark lesions on leaves
- White mold on underside in humid conditions
- Rapid spread — can destroy entire field in 5-7 days
- Tuber rot with reddish-brown discoloration

Management:
Preventive spraying schedule:
- Start spraying 30-35 days after planting
- Mancozeb 2.5g/L every 7 days (dry weather)
- Metalaxyl+Mancozeb 2.5g/L every 10 days
- In rainy weather: spray every 5-7 days
- Use BARI Alu-25 or BARI Alu-41 (resistant varieties)

2. Early Blight:
Pathogen: Alternaria solani
Symptoms: Concentric ring lesions on older leaves
Management: Mancozeb spray

3. Common Scab:
Pathogen: Streptomyces scabies
Symptoms: Rough corky lesions on tubers
Management: Maintain soil pH 5.2-5.5, avoid lime

4. Bacterial Soft Rot:
Pathogen: Pectobacterium carotovorum
Symptoms: Tuber becomes soft and foul-smelling
Management: Proper storage conditions, avoid wounding

== সার সুপারিশ (আলু) ==
গোবর সার: ১০-১৫ টন/হেক্টর
ইউরিয়া: ২৫০-৩০০ কেজি/হেক্টর
টিএসপি: ১৫০-২০০ কেজি/হেক্টর
এমওপি: ২০০-২৫০ কেজি/হেক্টর
প্রয়োগ: রোপণের সময় মূল সার, ৩০ দিন পর ইউরিয়ার অর্ধেক

== সংরক্ষণ ==
তাপমাত্রা: ৩-৫°C
আর্দ্রতা: ৮৫-৯০%
বায়ু চলাচল: পর্যাপ্ত
আলো: অন্ধকার ঘরে রাখুন
"""

files["crops/vegetables/all_vegetables_diseases.txt"] = """
TOPIC: All Vegetable Diseases and Management Guide Bangladesh
SOURCE: BARI, FAO, fao_eggplant_ipm.pdf
LANGUAGE: English + Bengali

== ONION AND GARLIC (পেঁয়াজ ও রসুন) ==

Purple Blotch (বেগুনী দাগ রোগ):
Pathogen: Alternaria porri
Symptoms: Small white lesions turning purple on leaves
Management: Mancozeb 2.5g/L or Iprodione spray

Downy Mildew:
Pathogen: Peronospora destructor
Symptoms: Pale green areas, violet-gray fungal growth
Management: Metalaxyl+Mancozeb spray

Stemphylium Blight:
Symptoms: Yellow-orange lesions on leaves
Management: Mancozeb or Chlorothalonil spray

== CHILI/PEPPER (মরিচ) ==

Anthracnose (কাণ্ড ও ফল পচা):
Pathogen: Colletotrichum capsici
Symptoms: Circular sunken dark lesions on fruit
Management: Carbendazim 1g/L or Mancozeb spray

Bacterial Wilt: Same as tomato bacterial wilt
Chili Leaf Curl Virus:
Cause: Virus spread by whitefly
Symptoms: Curled, distorted leaves, plant stunting
Management: Control whitefly with Imidacloprid, use virus-free seedlings

== GOURD/CUCURBITS (কুমড়া, লাউ, শসা) ==

Downy Mildew:
Symptoms: Yellow angular spots on upper leaf surface, purple mold below
Management: Metalaxyl+Mancozeb 2.5g/L spray

Powdery Mildew:
Symptoms: White powdery coating on leaves
Management: Sulfur 80WP 2g/L or Myclobutanil spray

Gummy Stem Blight:
Pathogen: Didymella bryoniae
Symptoms: Water-soaked stem lesions, gummy exudate
Management: Carbendazim or Thiophanate-methyl spray

Fruit Fly (ফলের মাছি):
Pest: Bactrocera cucurbitae
Management: Protein bait + malathion, pheromone traps

== CABBAGE/CAULIFLOWER (বাঁধাকপি/ফুলকপি) ==

Black Rot:
Pathogen: Xanthomonas campestris
Symptoms: V-shaped yellow lesions from leaf margins
Management: Copper-based spray, use disease-free seeds

Downy Mildew:
Management: Metalaxyl spray

Diamond Back Moth (DBM) — Most serious pest:
Pest: Plutella xylostella
Management:
- Bt spray (Bacillus thuringiensis)
- Spinosad 0.3ml/L
- Yellow sticky traps

== BEAN (শিম) ==

Bean Mosaic Virus: Spread by aphids, causes mosaic discoloration
Management: Control aphids with Imidacloprid

Rust: Orange pustules on leaves
Management: Propiconazole or Mancozeb spray

Pod Borer: Maruca vitrata
Management: Spinosad or Emamectin benzoate spray
"""

# ───────────────────────────────────────────────────
# FRUITS
# ───────────────────────────────────────────────────

files["crops/fruits/mango_complete.txt"] = """
TOPIC: Mango Production and Disease Management Bangladesh
SOURCE: BARI, FAO, fao_mango_production_asia.pdf
LANGUAGE: English + Bengali

আম বাংলাদেশের জাতীয় ফল এবং সবচেয়ে গুরুত্বপূর্ণ বাণিজ্যিক ফল।

== PRODUCTION ==
Annual production: 1.0-1.2 million metric tons
Major districts: Rajshahi, Chapainawabganj, Nawabganj, Dinajpur (Rajshahi division = 60% production)
Popular varieties: Himsagar, Langra, Fazli, Amrapali, BARI Aam-1 to BARI Aam-11

== MAJOR DISEASES ==

1. Anthracnose (অ্যান্থ্রাকনোজ):
Pathogen: Colletotrichum gloeosporioides
Most serious disease of mango
Symptoms: Black lesions on flowers, fruits, leaves
Pre-harvest fruit rot, post-harvest fruit decay
Management:
- Carbendazim 1g/L spray at flower emergence
- 3-4 sprays during flowering
- Hot water treatment of fruits after harvest (52°C for 5 min)

2. Powdery Mildew (পাউডারি মিলডিউ):
Pathogen: Oidium mangiferae
Symptoms: White powdery coating on flowers and young leaves
Management:
- Sulfur 80WP 2g/L spray
- Wettable sulfur at first sign of disease

3. Die-back:
Pathogen: Lasiodiplodia theobromae
Symptoms: Shoots die back from tip, bark cracks
Management:
- Prune infected branches 15cm below affected area
- Carbendazim paste on cut surface

4. Malformation (বিকৃতি):
Cause: Fusarium mangiferae + mite
Symptoms: Bunchy vegetative or floral malformation
Management:
- Pruning malformed parts
- Naphthalene acetic acid spray

== MANGO PESTS ==

Mango Hopper (আমের হপার):
Most serious mango pest in Bangladesh
Management: Imidacloprid or Cypermethrin spray at bud burst

Fruit Fly (ফলের মাছি):
Management:
- Protein bait + malathion spray
- Methyl eugenol pheromone traps
- Bag fruits before maturity

Stem Borer: Xylotrechus stem borer
Management: Inject petrol or Dichlorvos into borer holes

== সার সুপারিশ (আম, বয়স্ক গাছ) ==
গোবর সার: ৩০-৪০ কেজি/গাছ
ইউরিয়া: ৩০০-৪০০ গ্রাম/গাছ
টিএসপি: ৩৫০-৪৫০ গ্রাম/গাছ
এমওপি: ৩৫০-৪৫০ গ্রাম/গাছ
"""

files["crops/fruits/banana_complete.txt"] = """
TOPIC: Banana Production and Disease Management Bangladesh
SOURCE: BARI, FAO, fao_banana_production_disease.pdf
LANGUAGE: English + Bengali

কলা বাংলাদেশের সবচেয়ে বেশি উৎপাদিত ফল।

== PRODUCTION ==
Annual production: 800,000+ metric tons
Year-round production
Major districts: Narail, Jessore, Natore, Bogra, Joypurhat
Popular varieties: Sabri, Amrit Sagar, Champa, Mehersagar, Anajee

== MAJOR DISEASES ==

1. Panama Wilt / Fusarium Wilt (পানামা উইল্ট):
Pathogen: Fusarium oxysporum f.sp. cubense
MOST SERIOUS banana disease worldwide
Symptoms:
- Yellowing of lower leaves starting from margins
- Leaves wilt and hang down
- Internal brown discoloration in pseudostem
- Entire plant dies
No chemical cure. Management:
- Use disease-free suckers or tissue culture plants
- Crop rotation
- Soil fumigation
- Resistant varieties: BARI Kola-1, BARI Kola-2

2. Black Sigatoka / Black Leaf Streak:
Pathogen: Mycosphaerella fijiensis
Symptoms: Dark brown-black streaks on leaves, premature leaf death
Management:
- Mancozeb 2.5g/L spray every 14 days
- Remove infected leaves

3. Bunchy Top Virus (বানচি টপ ভাইরাস):
Spread by banana aphid (Pentalonia nigronervosa)
Symptoms: Narrow, bunched leaves at top, yellow margins, stunted growth
Management:
- Remove and destroy infected plants
- Control aphids with Imidacloprid
- Use virus-free planting material

== সার সুপারিশ (কলা) ==
গোবর সার: ১০-১৫ কেজি/গাছ
ইউরিয়া: ২০০-২৫০ গ্রাম/গাছ
টিএসপি: ১৫০-২০০ গ্রাম/গাছ
এমওপি: ২৫০-৩০০ গ্রাম/গাছ (৩ কিস্তিতে দিন)
"""

# ───────────────────────────────────────────────────
# PULSES
# ───────────────────────────────────────────────────

files["crops/pulses/pulses_complete.txt"] = """
TOPIC: Pulse Crops — Complete Guide for Bangladesh
SOURCE: BARI, FAO
LANGUAGE: English + Bengali

বাংলাদেশে প্রধান ডাল ফসল:
১. মসুর ডাল (Lentil)
২. মুগ ডাল (Mung Bean)
৩. মাসকলাই (Black Gram)
৪. খেসারি (Grass Pea)
৫. ছোলা (Chickpea)
৬. ফেলন (Cowpea)

== মসুর ডাল (LENTIL) ==
Season: Rabi (October-March)
Major districts: Faridpur, Tangail, Pabna, Kushtia
Popular varieties: BARI Masur-1 to BARI Masur-9

Major disease — Stemphylium Blight:
Pathogen: Stemphylium botryosum
Most serious lentil disease in Bangladesh
Symptoms: Gray water-soaked lesions on stems, defoliation
Management:
- Rovral or Iprodione 2ml/L spray
- Seed treatment with fungicide

Rust: Orange pustules on leaves
Management: Propiconazole spray

সার সুপারিশ:
ইউরিয়া: ৪০-৫০ কেজি/হেক্টর
টিএসপি: ৮০-১০০ কেজি/হেক্টর
এমওপি: ৫০-৬০ কেজি/হেক্টর

== মুগ ডাল (MUNG BEAN) ==
Two crops: Pre-kharif (March-June) and Kharif-2 (July-October)
Popular varieties: BARI Mung-5, BARI Mung-6, BARI Mung-8

Major disease — Cercospora Leaf Spot:
Symptoms: Circular brown spots with yellow halo
Management: Mancozeb spray

Mung bean Yellow Mosaic Virus:
Spread by whitefly
Symptoms: Yellow mosaic on leaves, stunted plant
Management: Control whitefly, use resistant varieties

== ছোলা (CHICKPEA) ==
Season: Rabi
Popular varieties: BARI Chola-5, BARI Chola-8, BARI Chola-9

Botrytis Gray Mold: Most serious disease
Symptoms: Water-soaked lesions, gray mold
Management: Iprodione spray, avoid dense planting
"""

# ───────────────────────────────────────────────────
# OILSEEDS
# ───────────────────────────────────────────────────

files["crops/oilseeds/oilseeds_complete.txt"] = """
TOPIC: Oilseed Crops — Complete Guide Bangladesh
SOURCE: BARI, USDA GAIN
LANGUAGE: English + Bengali

বাংলাদেশে প্রধান তেলবীজ ফসল:
১. সরিষা (Mustard) — সবচেয়ে গুরুত্বপূর্ণ
২. তিল (Sesame)
৩. সূর্যমুখী (Sunflower)
৪. চিনাবাদাম (Groundnut)
৫. সয়াবিন (Soybean)

== সরিষা (MUSTARD) — Most Important ==
Annual production: 650,000-700,000 metric tons
Cultivated area: 320,000-350,000 hectares
Season: Rabi (October-November to January-February)
Major districts: Rajshahi, Faridpur, Jessore, Tangail

Popular varieties:
BARI Sarisha-14: High yield, early maturing
BARI Sarisha-15: Heat tolerant
BARI Sarisha-17: High erucic acid
BINA sarisha-4, -9: Improved yield

Major disease — Alternaria Blight (অলটারনারিয়া ব্লাইট):
Most serious mustard disease in Bangladesh
Pathogen: Alternaria brassicae, A. brassicicola
Symptoms:
- Circular brown lesions with concentric rings
- Yellowing and defoliation
- Premature seed pod ripening
Management:
- Iprodione 2ml/L spray at bud formation
- 2-3 sprays at 10-day intervals
- Use certified disease-free seeds

Sclerotinia Stem Rot:
Pathogen: Sclerotinia sclerotiorum
Symptoms: White cottony growth on stems, stem rots
Management: Carbendazim spray, avoid dense planting

White Rust:
Pathogen: Albugo candida
Symptoms: White pustules on leaves and stems
Management: Metalaxyl+Mancozeb spray

সার সুপারিশ (সরিষা):
ইউরিয়া: ১৫০-১৮০ কেজি/হেক্টর
টিএসপি: ৮০-১০০ কেজি/হেক্টর
এমওপি: ৬০-৮০ কেজি/হেক্টর
সালফার: ৩০-৪০ কেজি/হেক্টর
বোরন: ১-২ কেজি/হেক্টর

== সূর্যমুখী (SUNFLOWER) ==
Varieties: BARI Surjamukhi-2, Hysun-33, DK-3849
Disease: Alternaria Blight, Sclerotinia — same management as mustard

== চিনাবাদাম (GROUNDNUT) ==
Varieties: BARI Badam-5, BARI Badam-6, BARI Badam-8
Disease: Early and Late Leaf Spot
Management: Mancozeb or Chlorothalonil spray
"""

# ───────────────────────────────────────────────────
# SOIL MANAGEMENT
# ───────────────────────────────────────────────────

files["soil/soil_management_complete.txt"] = """
TOPIC: Soil Management for Bangladesh Agriculture
SOURCE: SRDI, BARI, FAO
LANGUAGE: English + Bengali

== BANGLADESH SOIL TYPES ==

Highland (উঁচু জমি):
- Red-yellow podzolic soil: Madhupur Tract, Barind Tract
- Sandy loam to clay loam
- Low organic matter
- Suitable: Vegetables, fruits, pulses

Medium Highland:
- Most of Bangladesh
- Loam to clay loam
- Moderately fertile
- Suitable: Rice, vegetables, wheat

Lowland/Floodplain (নিচু জমি):
- Clay to heavy clay
- High fertility
- Subject to flooding
- Suitable: Rice (aman, aus)

Coastal Saline (উপকূলীয় লবণাক্ত):
- High salinity (>4 dS/m)
- Potential area: 3 million hectares
- Suitable: Salt tolerant varieties

== SOIL pH MANAGEMENT ==
Most crops prefer pH 5.5-6.5
Too acidic (below 5.5):
- Apply agricultural lime: 2-4 ton/ha
- Reduces aluminum toxicity
- Improves phosphorus availability

Too alkaline (above 7.0):
- Apply gypsum: 500-1000 kg/ha
- Use sulfur 50-100 kg/ha

pH guide for major crops:
Rice: 5.5-6.5
Wheat: 6.0-7.0
Potato: 5.0-6.0 (lower = less scab)
Vegetables: 5.5-7.0
Mustard: 5.5-6.5

== SOIL HEALTH IMPROVEMENT ==

Organic Matter (জৈব পদার্থ):
Bangladesh soils have very low organic matter (1-2%)
Target: >2.5% organic matter
Methods:
- Apply compost: 5-10 ton/ha
- Vermicompost: 2-3 ton/ha
- Green manuring: Dhaincha (Sesbania)
- Crop residue incorporation
- Avoid burning crop residue

Micronutrient Deficiencies Common in Bangladesh:
Zinc deficiency (জিঙ্ক অভাব):
- Most widespread micronutrient deficiency
- Symptoms: Stunted growth, bronze leaf color in rice
- Treatment: Zinc sulfate 10-15 kg/ha or ZnSO4 spray

Boron deficiency:
- Affects mustard, vegetables
- Symptoms: Hollow stem, poor fruiting
- Treatment: Borax 2-3 kg/ha

Sulfur deficiency:
- Affects mustard, onion, garlic
- Treatment: Gypsum 40-60 kg/ha

== মাটি পরীক্ষা সুপারিশ ==
প্রতি ৩-৪ বছর মাটি পরীক্ষা করুন
নিকটস্থ মৃত্তিকা সম্পদ উন্নয়ন ইনস্টিটিউট (SRDI) কার্যালয়ে যোগাযোগ করুন
"""

# ───────────────────────────────────────────────────
# FERTILIZER
# ───────────────────────────────────────────────────

files["fertilizer/fertilizer_complete_guide.txt"] = """
TOPIC: Complete Fertilizer Guide for Bangladesh Agriculture
SOURCE: BARI, DAE, Krishi Diary 2024
LANGUAGE: English + Bengali

== FERTILIZER TYPES AND NUTRIENT CONTENT ==

Urea (ইউরিয়া): 46% N
- Most common nitrogen fertilizer
- Apply in splits (3 times for rice)
- Do not apply before rain (leaching loss)

TSP (ট্রিপল সুপার ফসফেট): 46% P2O5
- Phosphorus fertilizer
- Apply before planting (basal)
- Slow release, stays in soil

MoP (মিউরেট অব পটাশ): 60% K2O
- Potassium fertilizer
- Important for grain filling and disease resistance

Gypsum (জিপসাম): 18% S + 23% Ca
- Sulfur and calcium source
- Important for mustard, onion, garlic

DAP (ডায়ামোনিয়াম ফসফেট): 18% N + 46% P2O5
- Combined N and P source

== CROP-WISE FERTILIZER RECOMMENDATION ==

ধান (বোরো) / Rice (Boro) per hectare:
Urea: 220-250 kg | TSP: 80-100 kg | MoP: 80-100 kg
Gypsum: 60-80 kg | Zinc sulfate: 8-10 kg
Application: Basal (TSP+MoP+Gypsum+Zinc at planting)
Urea in 3 splits: 7-10 days after transplant, at tillering, at panicle initiation

ধান (আমন) / Rice (Aman):
Urea: 160-200 kg | TSP: 60-80 kg | MoP: 60-80 kg

গম / Wheat:
Urea: 200-220 kg | TSP: 100-120 kg | MoP: 80-100 kg
Gypsum: 40-60 kg
Apply urea in 2 splits

আলু / Potato:
Urea: 250-300 kg | TSP: 150-200 kg | MoP: 200-250 kg
Cowdung: 10-15 ton | Gypsum: 80-100 kg

সরিষা / Mustard:
Urea: 150-180 kg | TSP: 80-100 kg | MoP: 60-80 kg
Gypsum: 100-120 kg | Boron: 2 kg

টমেটো / Tomato:
Urea: 300-350 kg | TSP: 200-250 kg | MoP: 250-300 kg
Cowdung: 15-20 ton | Calcium nitrate: 150 kg

বেগুন / Eggplant:
Urea: 250-300 kg | TSP: 150-200 kg | MoP: 200-250 kg
Cowdung: 10-15 ton

মরিচ / Chili:
Urea: 200-250 kg | TSP: 125-150 kg | MoP: 150-200 kg

পেঁয়াজ / Onion:
Urea: 200-250 kg | TSP: 125-150 kg | MoP: 150-200 kg
Gypsum: 60-80 kg

মুগ ডাল / Mung Bean:
Urea: 40-50 kg | TSP: 80-100 kg | MoP: 50-60 kg
(Rhizobium inoculant reduces nitrogen need)

== সার প্রয়োগের সাধারণ নিয়ম ==
- মূল সার (Basal): রোপণ/বপনের সময় দিন — TSP, MoP, গোবর সার, Gypsum
- পার্শ্ব সার (Top dressing): বাড়ন্ত পর্যায়ে ইউরিয়া দিন
- বৃষ্টির আগে সার দেবেন না (ধুয়ে যায়)
- মাটি ভেজা অবস্থায় ইউরিয়া দিন
- অতিরিক্ত ইউরিয়া দিলে রোগ বাড়ে, ফলন কমে

== জৈব সারের গুরুত্ব ==
গোবর সার: ১০-১৫ টন/হেক্টর — মাটির জৈব পদার্থ বাড়ায়
কম্পোস্ট: ৫-৮ টন/হেক্টর
ভার্মিকম্পোস্ট: ২-৩ টন/হেক্টর
সবুজ সার: ধৈঞ্চা (Sesbania) — ৬০-৮০ কেজি নাইট্রোজেন যোগ করে
"""

# ───────────────────────────────────────────────────
# IRRIGATION
# ───────────────────────────────────────────────────

files["irrigation/irrigation_complete.txt"] = """
TOPIC: Irrigation Management for Bangladesh Agriculture
SOURCE: DAE, BRRI, FAO irrigation guide
LANGUAGE: English + Bengali

== WATER REQUIREMENTS BY CROP ==

Rice (Boro — irrigated):
Total water: 900-1200 mm per season
Method: Continuous flooding OR alternate wetting and drying (AWD)
AWD method: Let soil dry to 15-20cm water depth, then re-flood
AWD saves 20-30% water without yield loss

Rice (Aman): Mostly rain-fed, supplemental irrigation during dry spells

Wheat: 
Total water: 350-450 mm
Critical stages: CRI (seedling), tillering, booting, grain filling
Number of irrigations: 2-3 times

Potato:
Critical stages: Tuber initiation, tuber development
Irrigation interval: Every 10-14 days
Avoid: Waterlogging (causes rot)

Mustard:
Critical stage: Flowering
1-2 irrigations usually sufficient

Vegetables (general):
Irrigate every 3-5 days in summer
Drip irrigation saves 40-50% water

== IRRIGATION METHODS ==

Flood Irrigation (বন্যা সেচ):
Most common method
Suitable: Rice, sugarcane
Efficiency: 40-50%

Furrow Irrigation (নালা সেচ):
Suitable: Vegetables, potato, maize
Efficiency: 50-60%

Sprinkler Irrigation:
Suitable: Wheat, vegetables, groundnut
Efficiency: 70-80%
Investment: Higher cost

Drip Irrigation (ড্রিপ সেচ):
Suitable: Vegetables, fruits, chili
Efficiency: 85-95%
Best for: Water-scarce areas
Government subsidy available in Bangladesh

== GROUNDWATER IRRIGATION ==
Bangladesh relies heavily on groundwater for boro rice
Over-extraction causing falling water table in Barind Tract
Solution: AWD for rice, shift to drought-tolerant crops in dry season

== সেচের সংকেত ==
পাতা মোচড়ানো → পানির প্রয়োজন
মাটি সকালে শুষ্ক → সেচ দিন বিকেলে
ফুল আসার সময় → অবশ্যই সেচ দিন
বৃষ্টির পূর্বাভাস → সেচ বন্ধ রাখুন
"""

# ───────────────────────────────────────────────────
# LIVESTOCK
# ───────────────────────────────────────────────────

files["livestock/livestock_complete.txt"] = """
TOPIC: Livestock Management and Disease in Bangladesh
SOURCE: DLS (Department of Livestock Services), FAO
LANGUAGE: English + Bengali

== CATTLE (গরু) ==

Major diseases:
1. Foot and Mouth Disease (FMD / ক্ষুরারোগ):
Symptoms: Fever, blisters in mouth and hooves, lameness
Very contagious
Management: Vaccination twice yearly, isolation of infected animals

2. Hemorrhagic Septicemia (গলাফুলা):
Symptoms: Sudden fever, swelling of throat, difficulty breathing, death within 24-48 hours
Management: Annual vaccination (most important), Oxytetracycline antibiotic

3. Black Quarter (বাদলা):
Symptoms: Sudden lameness, gas-filled swelling on thigh/shoulder
Management: Annual vaccination, Penicillin antibiotic

4. Brucellosis:
Symptoms: Abortion in late pregnancy, retained placenta
Zoonotic — can spread to humans
Management: Vaccination of calves, test and slaughter policy

Cattle vaccination schedule:
January-February: Foot and Mouth Disease
March: Hemorrhagic Septicemia
May: Black Quarter
October: Repeat FMD

== GOAT (ছাগল) ==

Most important livestock in Bangladesh (25 million goats)
Black Bengal Goat — famous globally

Major diseases:
1. PPR (Peste des Petits Ruminants) / ছাগলের মহামারী:
Symptoms: High fever, nasal discharge, mouth ulcers, severe diarrhea, death
Highly contagious, high mortality
Management: Annual vaccination mandatory

2. Enterotoxemia (পাকস্থলীর বিষক্রিয়া):
Symptoms: Sudden death, bloating
Management: Annual vaccination

Goat production:
Feed: Grass, tree leaves, kitchen waste, concentrate feed
Health check: Monthly deworming essential
Common wormer: Albendazole 7.5mg/kg body weight

== POULTRY (মুরগি) ==

Major diseases:
1. Newcastle Disease (রানীক্ষেত রোগ):
Symptoms: Respiratory distress, nervous signs, green diarrhea, high mortality
Most devastating poultry disease in Bangladesh
Management: Regular vaccination (V4/La Sota strain)

2. Gumboro Disease (IBD):
Symptoms: Sudden mortality in young chicks, prostration
Management: Vaccination at 14 and 28 days

3. Avian Influenza (H5N1 — বার্ড ফ্লু):
Zoonotic risk
Symptoms: Very high mortality, respiratory distress, cyanosis
Management: Report immediately to authorities, culling

Poultry vaccination schedule:
Day 1: Marek's disease (hatchery)
Day 7-10: Gumboro 1st dose
Day 14-18: Newcastle + IBD (eye drop)
Day 21-24: Gumboro 2nd dose
Day 28: Newcastle booster
Week 6-8: Fowl pox

== FISHERIES (মাছ চাষ) ==

Bangladesh is 3rd in world freshwater fish production

Major fish diseases:
1. Bacterial disease (Aeromonas infection):
Symptoms: Hemorrhagic spots, ulcers, fin rot
Management: Salt treatment (2-3%), Oxytetracycline in feed

2. Epizootic Ulcerative Syndrome (EUS / ঘা রোগ):
Most serious disease of carp in Bangladesh
Symptoms: Red ulcers on body, muscle decay
Management: Lime application 200-250 kg/ha, Copper sulfate treatment

Popular fish for farming:
Rui, Katla, Mrigal (Carp) — most popular
Tilapia — fast growing
Pangasius — commercial
Shrimp (bagda, galda) — export commodity

Fish pond management:
Lime application: 200-250 kg/ha before stocking
Fertilizer: Urea 45kg + TSP 50kg per hectare per month
Stocking density: 10,000-25,000 fingerlings/hectare (polyculture)
"""

# ───────────────────────────────────────────────────
# CLIMATE AND AGRICULTURE
# ───────────────────────────────────────────────────

files["climate/climate_agriculture_complete.txt"] = """
TOPIC: Climate Change and Agriculture in Bangladesh — Complete Guide
SOURCE: IUCN, FAO, foresight_bd_climate_2025.pdf, climate_centre_bd_2024.pdf
LANGUAGE: English + Bengali

== CLIMATE THREATS TO BANGLADESH AGRICULTURE ==

1. FLOODING (বন্যা):
Types:
- Flash flood (আকস্মিক বন্যা): Haor areas, destroys Boro
- Monsoon flood: 20-30% of country annually
- Riverine flood: Longer duration

Crop impact:
- 1 million hectares crop loss annually average
- Boro rice in Haor: Complete loss if early flood (May)
- Aman rice: Loss if flood duration >14 days

Solutions:
- Flash flood tolerant varieties: BRRI dhan89, BRRI dhan90
- Submergence tolerant: BRRI dhan49, BRRI dhan51
- Short duration aus varieties to avoid monsoon flood

2. DROUGHT (খরা):
Affected areas: Barind Tract (Rajshahi, Chapainawabganj, Naogaon)
Crop impact: Boro requires irrigation — groundwater depletion
Solutions:
- Drought tolerant varieties: BRRI dhan56, BRRI dhan66
- AWD (Alternate Wetting and Drying) irrigation
- Rainwater harvesting

3. SALINITY (লবণাক্ততা):
Affected area: 1.06 million hectares in coastal Bangladesh
Districts: Satkhira, Khulna, Bagerhat, Barguna, Patuakhali
Problem: Increasing due to sea level rise and reduced freshwater flow
Solutions:
- Salt tolerant varieties: BRRI dhan47, BRRI dhan61, BRRI dhan67, BRRI dhan73
- BINA dhan8, BINA dhan10

4. TEMPERATURE RISE (তাপমাত্রা বৃদ্ধি):
Effect on crops:
- 1°C rise → 5-10% reduction in rice yield
- High night temperature causes spikelet sterility in rice
- Affects wheat ripening

Solutions:
- Heat tolerant varieties: BRRI dhan74, BRRI dhan84
- Adjust planting time to cooler periods

5. ERRATIC RAINFALL (অনিয়মিত বৃষ্টিপাত):
- Delayed monsoon onset
- Intense rainfall events
- Longer dry spells
Impact: Unpredictable pest and disease outbreaks

== DISEASE-CLIMATE CONNECTIONS ==
High temperature + high humidity → Blast disease risk increases
Flooding → Bacterial blight outbreak after flood
Drought + heat → Increase in insect pest populations
Cyclone + storm surge → Salinity intrusion, destroys crops

== CLIMATE-SMART AGRICULTURE PRACTICES ==
1. Crop diversification — don't rely on single crop
2. Use of climate-resilient varieties
3. Conservation agriculture — minimum tillage
4. Integrated pest management (IPM)
5. Water harvesting and efficient irrigation
6. Agroforestry systems

জলবায়ু পরিবর্তনে কৃষকের করণীয়:
- আবহাওয়ার পূর্বাভাস দেখুন (Bangladesh Meteorological Department)
- সহনশীল জাত ব্যবহার করুন
- মৌসুমী পঞ্জিকা মেনে চলুন
- কৃষি বীমা গ্রহণ করুন
"""

# ───────────────────────────────────────────────────
# INTEGRATED PEST MANAGEMENT
# ───────────────────────────────────────────────────

files["pests/ipm_complete_guide.txt"] = """
TOPIC: Integrated Pest Management (IPM) Complete Guide Bangladesh
SOURCE: DAE, FAO, IRRI
LANGUAGE: English + Bengali

== WHAT IS IPM? ==
IPM combines multiple pest management methods to:
- Minimize pesticide use
- Reduce cost
- Protect environment and health
- Maintain sustainable crop production

IPM components (সমন্বিত বালাই ব্যবস্থাপনা):
1. Cultural control (সাংস্কৃতিক পদ্ধতি)
2. Biological control (জৈব পদ্ধতি)
3. Physical/mechanical control (যান্ত্রিক পদ্ধতি)
4. Chemical control (রাসায়নিক পদ্ধতি) — last resort

== BIOLOGICAL CONTROL AGENTS ==

Beneficial insects that eat pests (উপকারী পোকা):
- Spiders (মাকড়সা): Eat planthoppers, leafhoppers
- Mirid bug (Cyrtorhinus): Eats planthopper eggs
- Dragonfly (ফড়িং): Eats stem borer moths
- Lady bird beetle (লেডিবার্ড): Eats aphids

How to protect natural enemies:
- Avoid broad-spectrum insecticides
- Maintain field bunds with flowering plants
- Use selective pesticides

Biocontrol products:
- Trichoderma: Soil application, controls root rot diseases
- Bacillus thuringiensis (Bt): Spray for caterpillar pests
- Beauveria bassiana: Controls stem borer
- Neem (Azadirachtin): Natural pesticide, very safe

== CULTURAL CONTROL METHODS ==
- Crop rotation: Break pest and disease cycle
- Resistant varieties: Most cost-effective
- Proper spacing: Reduces humidity, prevents disease spread
- Balanced fertilization: Excess N increases pest attraction
- Sanitation: Remove crop debris after harvest
- Adjust planting date: Avoid peak pest periods

== PHYSICAL/MECHANICAL CONTROL ==
Yellow sticky traps: Catches whitefly, aphids, thrips
Blue sticky traps: Catches thrips specifically
Pheromone traps: Species-specific catch for moths (stem borer, fruit borer)
Light traps: Catches moths at night
Hand picking: Remove egg masses, caterpillars

== PESTICIDE SAFETY (নিরাপদ কীটনাশক ব্যবহার) ==
Always:
- Read label before use
- Wear protective gear (mask, gloves, glasses)
- Spray early morning or late afternoon
- Keep children away from spraying area
- Wash hands and face after spraying

Never:
- Mix pesticides without recommendation
- Spray near water bodies
- Use expired pesticides
- Use food containers for pesticides
- Spray against wind direction

Pre-harvest interval (PHI) — পূর্ব-মৌসুম নিষেধাজ্ঞা:
Imidacloprid: 30 days before harvest
Cypermethrin: 7 days
Chlorpyrifos: 14 days
Mancozeb: 7 days

== COMMON PESTICIDES IN BANGLADESH ==
Insecticides:
Imidacloprid: Sucking insects (aphids, whitefly, leafhopper)
Chlorpyrifos: Broad spectrum (soil and foliar)
Cypermethrin: Caterpillars, beetles
Spinosad: Caterpillars (safe for bees)
Emamectin benzoate: Very effective for caterpillars

Fungicides:
Mancozeb: Preventive, broad spectrum
Carbendazim: Systemic, rice diseases
Tebuconazole: Systemic, wheat, rice blast
Propiconazole: Systemic, rice and wheat
Iprodione: Botrytis, Alternaria
Metalaxyl: Downy mildew, late blight

Herbicides:
2,4-D amine: Broadleaf weeds in rice
Butachlor: Grass weeds in transplanted rice
Fenoxaprop: Grass weeds in wheat
"""

# ───────────────────────────────────────────────────
# POST HARVEST
# ───────────────────────────────────────────────────

files["post_harvest/post_harvest_guide.txt"] = """
TOPIC: Post-Harvest Management and Storage Guide Bangladesh
SOURCE: DAE, BARI, FAO
LANGUAGE: English + Bengali

== RICE POST-HARVEST ==

Harvesting:
- Harvest when 85-90% grains are golden/straw colored
- Do not delay — reduces grain quality and causes shattering
- Use sickle or reaper machine

Threshing:
- Pedal thresher or power thresher
- Reduces grain loss compared to hand threshing

Drying:
- Dry to moisture content of 12-14% for storage
- Sun drying: 2-3 days on clean surface
- Mechanical dryer: More uniform
- Do NOT dry on road (contamination, breakage)

Storage:
- Clean storage bags (jute or polypropylene)
- Apply malathion 5% dust on bags
- Keep away from walls and floor (use pallet or wooden platform)
- Hermetic storage bags (PICS bags): Keep moisture <14%, prevent insects without chemicals
- Maximum storage period: 6-8 months

Quality test: Bite a grain — if hard and not chewy, moisture is acceptable

== POTATO STORAGE ==
Temperature: 3-5°C (cold storage) or cool shaded room
Humidity: 85-90%
Keep in darkness (light causes greening and solanine)
Ventilation: Adequate air circulation
Remove: Infected/damaged tubers before storage
Storage loss (without cold storage): 20-30%

== ONION STORAGE ==
Cure onions at 25-30°C for 2 weeks before storage
Temperature: 1-5°C cold storage OR warm well-ventilated room
Humidity: Low 60-70%
Spread in single layer or use mesh bags
Common loss: Bacterial soft rot, fusarium rot
Prevent: Use cured, dry, disease-free bulbs

== GRAIN STORAGE INSECTS ==
Common pests:
Weevil (ধানের পোকা): Sitophilus oryzae — bores into grain
Lesser grain borer: Destroys grain from inside
Khapra beetle: Larvae destroy stored products

Management:
- Aluminum phosphide (ALP) tablets for large stores
- Hermetic bags for small quantities
- Pyrethroid spray on walls
- Temperature <15°C kills most storage insects

== POST-HARVEST LOSSES IN BANGLADESH ==
Total food loss: 20-30% of production
Rice: 10-15% loss
Vegetables: 25-40% loss (huge due to poor storage)
Fruits: 20-40% loss

Reducing vegetable losses:
- Harvest early morning
- Cool immediately after harvest
- Use perforated plastic bags for transport
- Evaporative cooling storage (bamboo/sand cooler)
- Process excess into pickles, dried products
"""

# ───────────────────────────────────────────────────
# ECONOMICS
# ───────────────────────────────────────────────────

files["economics/agricultural_economics.txt"] = """
TOPIC: Agricultural Economics and Market Information Bangladesh
SOURCE: DAE, BBS, USDA GAIN
LANGUAGE: English + Bengali

== CROP PRODUCTION STATISTICS ==

Rice:
Annual production: 37-38 million metric tons
Area: 11.5-12 million hectares
Bangladesh is self-sufficient in rice since 2000s
Export: Small quantity of aromatic rice (BB Dhan100)

Wheat:
Production: 1.0-1.2 million metric tons
Requirement: 6-7 million metric tons
Deficit: Import 5-6 million metric tons annually (mainly from India, Russia)

Vegetables:
Annual production: 17-18 million metric tons
Growing rapidly due to demand and urbanization
Export: $100+ million annually (potato, chili, leafy vegetables to Middle East)

Potato:
Production: 10-11 million metric tons
Surplus: Export to Malaysia, Singapore, Sri Lanka

== FERTILIZER PRICES (APPROXIMATE) ==
Urea: Tk 22/kg (subsidized government price)
TSP: Tk 27/kg
MoP: Tk 20/kg
DAP: Tk 35-40/kg

Government subsidy on fertilizer: Significant, to support farmers

== CROP INSURANCE ==
Sadharan Bima Corporation offers crop insurance
Coverage: Natural disasters, flood, drought
Premium: 2-3% of crop value
Claim: Requires documented loss

== AGRICULTURAL CREDIT ==
Bangladesh Krishi Bank (BKB): Primary agricultural bank
RAKUB: For Rajshahi and Rangpur divisions
Commercial banks: Now required to give agricultural loans
Interest rate: 4-9% for farmers (subsidized)

Loan products:
- Crop loan: Short term (6-12 months)
- Equipment loan: Medium term
- Fisheries/livestock loan

== MARKET INFORMATION ==
Digital tools:
- Krishibazar app: Real-time market prices
- e-krishi: Extension service mobile app
- 16123 hotline: Agricultural helpline DAE

Major wholesale markets:
Dhaka: Karwan Bazar (vegetables, fruits)
Chittagong: Khatunganj (onion, garlic, pulses)
Rajshahi: Saheb Bazar (mango, vegetables)
Bogra: Mahiganj (potato market)

== PROFITABLE CROPS FOR BANGLADESH FARMERS ==
High value crops:
1. Dragon fruit: Tk 150-300/kg
2. Strawberry: Tk 200-400/kg
3. Capsicum/Bell pepper: Tk 60-100/kg
4. Cherry tomato: Tk 80-120/kg
5. Mushroom: Tk 150-300/kg
6. Aromatic rice (BB Dhan100): Tk 60-80/kg

Medium value:
1. Tomato: Tk 15-40/kg
2. Eggplant: Tk 15-30/kg
3. Potato: Tk 15-25/kg
4. Onion: Tk 25-50/kg
5. Garlic: Tk 80-150/kg
"""

# ═══════════════════════════════════════════════════
# WRITE ALL FILES
# ═══════════════════════════════════════════════════

total = 0
total_chars = 0

for filepath, content in files.items():
    full_path = f"data/knowledge_base/{filepath}"
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    size = len(content)
    total_chars += size
    total += 1
    print(f"Created: {filepath} ({size:,} chars)")

print(f"\n{'='*50}")
print(f"Total files created: {total}")
print(f"Total content: {total_chars:,} characters (~{total_chars//4:,} tokens)")
print(f"\nNow run: python ingest.py to add to your database")