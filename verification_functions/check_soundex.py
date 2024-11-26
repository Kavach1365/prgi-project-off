from utils.similarity import get_soundex_similarity
import asyncio, time

async def check_soundex_similarity(new_title: str, existing_titles: list) -> dict:
    """
    Checks if the given title has soundex similarity with existing titles.
    """
    start_time = time.time()
    print(f"[check_soundex_similarity] Started at {start_time}")

    similar_titles = [
    title for title in existing_titles 
    if get_soundex_similarity(new_title, title)
]
    end_time = time.time()
    print(f"[check_soundex_similarity] Finished at {end_time}. Duration: {end_time - start_time:.2f} seconds")
    return {
        "check_type": "Soundex Similarity",
        "status": "failed" if similar_titles else "passed",
        "reason": "Titles with soundex similarity found." if similar_titles else None,
        "similar_titles": similar_titles,
    }
