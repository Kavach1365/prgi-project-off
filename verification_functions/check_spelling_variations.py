from utils.spelling_variation import find_titles_with_spelling_variations
import asyncio
async def check_spelling_variations(new_title: str, existing_titles: list, distance_threshold: int) -> dict:
    """
    Checks if the given title has spelling variations among existing titles using Levenshtein distance.
    """
    spelling_variations = await asyncio.to_thread(find_titles_with_spelling_variations,
        new_title, existing_titles, method="levenshtein", distance_threshold=distance_threshold
    )
    # spelling_variations_titles = [title for title, _ in spelling_variations]  # Extract only titles

    return {
        "check_type": "Spelling Variations",
        "status": "failed" if spelling_variations else "passed",
        "reason": "Titles with spelling variations found." if spelling_variations else None,
        "similar_titles": spelling_variations,
    }
