from utils.similarity import get_soundex_similarity
import asyncio
async def check_soundex_similarity(new_title: str, existing_titles: list) -> dict:
    """
    Checks if the given title has soundex similarity with existing titles.
    """
    #similar_titles = [title for title in existing_titles if await asyncio.to_thread(get_soundex_similarity(new_title, title))]
    similar_titles = [
    title for title in existing_titles 
    if await asyncio.to_thread(get_soundex_similarity, new_title, title)
]

    return {
        "check_type": "Soundex Similarity",
        "status": "failed" if similar_titles else "passed",
        "reason": "Titles with soundex similarity found." if similar_titles else None,
        "similar_titles": similar_titles,
    }
