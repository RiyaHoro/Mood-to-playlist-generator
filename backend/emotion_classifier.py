import re

# Emoji → mood mapping
EMOJI_MOOD = {
    "😔": "sad",
    "😭": "sad",
    "😢": "sad",
    "🙂": "happy",
    "😊": "happy",
    "😄": "happy",
    "😍": "romantic",
    "😘": "romantic",
    "😡": "angry",
    "🤬": "angry",
    "😴": "calm",
    "😌": "calm",
    "🤩": "energetic",
    "💪": "energetic"
}

# Keyword → mood mapping
KEYWORD_MOOD = {
    "sad": "sad",
    "tired": "calm",
    "depressed": "sad",
    "happy": "happy",
    "excited": "energetic",
    "angry": "angry",
    "love": "romantic",
    "romantic": "romantic",
    "calm": "calm",
    "peaceful": "calm",
    "energized": "energetic"
}


def detect_from_emoji(text):
    for ch in text:
        if ch in EMOJI_MOOD:
            return EMOJI_MOOD[ch]
    return None


def detect_from_keywords(text):
    text = text.lower()
    for keyword, mood in KEYWORD_MOOD.items():
        if keyword in text:
            return mood
    return None


def get_mood(text):
    # Step 1: Check emojis
    mood = detect_from_emoji(text)
    if mood:
        return mood

    # Step 2: Check keywords
    mood = detect_from_keywords(text)
    if mood:
        return mood

    # Default fallback
    return "neutral"
