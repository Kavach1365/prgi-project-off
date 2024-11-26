import jellyfish

def get_soundex_similarity(new_title: str, existing_title: str) -> bool:
    """
    Compare two titles using Soundex from the jellyfish library.
    Returns True if Soundex codes are the same, indicating similarity.
    """
    new_title = new_title.lower()
    existing_title = existing_title.lower()
    return jellyfish.soundex(new_title) == jellyfish.soundex(existing_title)


# from libindic.soundex import Soundex
# import re
# import unicodedata

# # Initialize Indic Soundex
# soundex_instance = Soundex()

# def normalize_text(text: str) -> str:
#     """
#     Normalize text by removing accents, converting to uppercase,
#     removing special characters, and trimming extra spaces.
#     """
#     text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
#     text = text.upper()
#     text = re.sub(r'[^A-Z0-9\s]', '', text)
#     text = re.sub(r'\s+', ' ', text).strip()
    
#     return text

# def get_soundex_similarity(title1: str, title2: str) -> bool:
#     """
#     Compare two titles using Indic Soundex.
#     Returns True if they are highly similar (score == 1).
#     """
#     # Compare Indic Soundex representations
#     similarity_score = soundex_instance.compare(title1, title2)
#     return similarity_score == 1

