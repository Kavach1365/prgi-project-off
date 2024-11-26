from utils.trie import TitleTrie
import asyncio
async def check_prefix(new_title: str, title_trie: TitleTrie) -> dict:
    """
    Checks if the given title has matching prefixes among existing titles in the trie.
    """
    prefix_matches = await asyncio.to_thread(title_trie.search_prefix,new_title)
    # prefix_matches = title_trie.search_prefix(new_title)
    return {
        "check_type": "Prefix Matching",
        "status": "failed" if prefix_matches else "passed",
        "reason": "Titles with matching prefixes found." if prefix_matches else None,
        "similar_titles": prefix_matches,
    }
