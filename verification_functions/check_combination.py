from utils.trie import TitleTrie
import time, asyncio
async def check_combination(new_title: str, title_trie: TitleTrie) -> dict:
    """
    Checks if the given title can be formed by combining existing titles in the trie.
    """
    start_time = time.time()
    print(f"[check_combination] Started at {start_time}")
    combination_titles = await asyncio.to_thread(title_trie.find_combination_titles,new_title)
    # combination_titles = title_trie.find_combination_titles(new_title)
    end_time = time.time()
    print(f"[check_combination] Finished at {end_time}. Duration: {end_time - start_time:.2f} seconds")

    return {
        "check_type": "Title Combination",
        "status": "failed" if combination_titles else "passed",
        "reason": "The title can be formed by combining other titles." if combination_titles else None,
        "similar_titles": combination_titles,
    }
