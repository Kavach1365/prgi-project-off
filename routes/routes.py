from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
import asyncio
import json
from utils.trie import TitleTrie
from verification_functions.check_anagram import check_anagram
from verification_functions.check_soundex import check_soundex_similarity
from verification_functions.check_spelling_variations import check_spelling_variations
from verification_functions.check_guidelines import check_guidelines
from verification_functions.check_prefix import check_prefix
from verification_functions.check_suffix import check_suffix
from verification_functions.check_combination import check_combination

# Create a global TitleTrie instance
title_trie = TitleTrie()

def initialize_title_trie():
    """
    Populate the TitleTrie with existing titles from a JSON file.
    """
    try:
        with open("titles.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        for title_doc in data:
            title_name = title_doc.get("T_NAME", "").lower()
            if title_name:
                title_trie.insert_title(title_name)
        print(f"Initialized TitleTrie with {len(data)} titles.")
    except Exception as e:
        print(f"Error initializing TitleTrie: {e}")

# Initialize the Trie with JSON data
initialize_title_trie()

router = APIRouter()

# Unified response models
class TitleVerificationResult(BaseModel):
    check_type: str
    status: str
    reason: str | None = None
    similar_titles: List[str] | None = None


class TitleVerificationResponse(BaseModel):
    results: List[TitleVerificationResult]
    acceptance_score: float


@router.post("/verify-title/", response_model=TitleVerificationResponse)
async def verify_title(new_title: str, distance_threshold: int = 80):
    """
    Verifies a new title against various criteria and returns a unified response.
    """
    new_title = new_title.lower()
    existing_titles = title_trie.get_all_titles()

    # Run all checks in parallel
    results = await asyncio.gather(
        check_soundex_similarity(new_title, existing_titles),
        check_anagram(new_title, title_trie),
        check_spelling_variations(new_title, existing_titles, distance_threshold), #380ms
        check_guidelines(new_title),
        check_prefix(new_title, title_trie),
        check_suffix(new_title, title_trie),
        check_combination(new_title, title_trie),
    )
    # tasks = [
    #     asyncio.to_thread(check_soundex_similarity, new_title, existing_titles),
    #     asyncio.to_thread(check_anagram, new_title, title_trie),
    #     asyncio.to_thread(check_spelling_variations, new_title, existing_titles, distance_threshold),
    #     asyncio.to_thread(check_guidelines, new_title),
    #     asyncio.to_thread(check_prefix, new_title, title_trie),
    #     asyncio.to_thread(check_suffix, new_title, title_trie),
    #     asyncio.to_thread(check_combination, new_title, title_trie),
    # ]
    # results = await asyncio.gather(*tasks)
    # Calculate overall acceptance score
    acceptance_score = 1.0 if all(result["status"] == "passed" for result in results) else 0.0

    return TitleVerificationResponse(results=results, acceptance_score=acceptance_score)
