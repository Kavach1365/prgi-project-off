from utils.guideline_check import check_disallowed_words, check_disallowed_prefixes
import asyncio

async def check_guidelines(new_title: str) -> dict:
    """
    Checks if the given title violates any disallowed words or prefixes.
    """
    violates_guidelines = await asyncio.to_thread(check_disallowed_words,new_title) or await asyncio.to_thread(check_disallowed_prefixes,new_title)

    return {
        "check_type": "Guideline Violations",
        "status": "failed" if violates_guidelines else "passed",
        "reason": "Title violates guidelines." if violates_guidelines else None,
    }
