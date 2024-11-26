DISALLOWED_WORDS = {"police", "crime", "corruption", "cbi", "cid", "army"}
DISALLOWED_PREFIXES = {"the", "a", "an"}

def check_disallowed_words(title: str) -> bool:
    """
    Check if the title contains disallowed words.
    """
    words = set(title.lower().split())
    return bool(words & DISALLOWED_WORDS)

def check_disallowed_prefixes(title: str) -> bool:
    """
    Check if the title starts with disallowed prefixes.
    """
    for prefix in DISALLOWED_PREFIXES:
        if title.lower().startswith(prefix + " "):
            return True
    return False
