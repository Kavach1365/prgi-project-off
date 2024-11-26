from utils.trie import TitleTrie
import time, asyncio
# import sys

async def check_suffix(new_title: str, title_trie: TitleTrie) -> dict:
    """
    Checks if the given title has matching suffixes among existing titles in the trie.
    """
    start_time = time.time()
    print(f"[check_suffix] Started at {start_time}")
    suffix_matches = await asyncio.to_thread(title_trie.search_suffix,new_title)
    end_time = time.time()

    print(f"[check_suffix] Finished at {end_time}. Duration: {end_time - start_time:.2f} seconds")
    # print(sys.getsizeof(suffix_matches))
    return {
        "check_type": "Suffix Matching",
        "status": "failed" if suffix_matches else "passed",
        "reason": "Titles with matching suffixes found." if suffix_matches else None,
        "similar_titles": suffix_matches,
    }
