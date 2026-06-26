import re
from langdetect import detect, LangDetectException

# Common romanized Bengali words — detect transliterated Bengali
ROMANIZED_BENGALI = {
    'tumi', 'tmi', 'ami', 'amar', 'apnar', 'apni', 'tomar', 'tomr',
    'ki', 'ke', 'keno', 'kothay', 'boro', 'chash', 'dhan', 'poka',
    'rog', 'foshol', 'krishi', 'kemon', 'acho', 'achen', 'bolo',
    'bolun', 'jano', 'janon', 'dhaner', 'shobji', 'alu', 'begun',
    'amn', 'boro', 'rabi', 'kharip', 'shech', 'sar', 'bishi',
    'kharap', 'valo', 'vhalo', 'sundor', 'khub', 'onek', 'ektu',
    'kothake', 'kothai', 'kivabe', 'kore', 'korbo', 'korte'
}

def detect_language(text: str) -> str:
    """Detect if text is Bengali, romanized Bengali, or English."""
    # 1. Check Bengali Unicode characters (strongest signal)
    bengali_chars = sum(1 for c in text if '\u0980' <= c <= '\u09FF')
    if bengali_chars > len(text) * 0.15:
        return 'bn'

    # 2. Check romanized Bengali (transliterated)
    words = set(re.findall(r'\b\w+\b', text.lower()))
    roman_bn_matches = words.intersection(ROMANIZED_BENGALI)
    if len(roman_bn_matches) >= 1 and len(words) <= 6:
        return 'bn'  # short romanized Bengali query

    # 3. Standard language detection
    try:
        lang = detect(text)
        # Correct South Asian language misdetections
        if lang in ['hi', 'ur', 'ne', 'si'] and bengali_chars > 0:
            return 'bn'
        return lang if lang in ['bn', 'en'] else 'en'
    except LangDetectException:
        return 'en'

def get_language_instruction(lang_code: str) -> str:
    if lang_code == 'bn':
        return "Respond entirely in Bengali (বাংলায় উত্তর দিন). Use clear, simple Bengali."
    return "Respond entirely in English."