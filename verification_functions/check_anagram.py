from utils.trie import TitleTrie
import time, asyncio
async def check_anagram(new_title: str, title_trie: TitleTrie) -> dict:
    start_time = time.time()
    print(f"[check_anagram] Started at {start_time}")
    
    matching_title = await asyncio.to_thread(title_trie.is_anagram_of_existing_title, new_title)    
    # matching_title = title_trie.is_anagram_of_existing_title(new_title)    
    end_time = time.time()
    
    print(f"[check_anagram] Finished at {end_time}. Duration: {end_time - start_time:.2f} seconds")
    return {
        "check_type": "Anagram Check",
        "status": "failed" if matching_title else "passed",
        "reason": "An anagram of the title already exists." if matching_title else None,
        "similar_titles": [matching_title] if matching_title else None,
    }
