from rapidfuzz import fuzz

# def find_titles_with_spelling_variations(target_title, titles, method="levenshtein", distance_threshold=80):
#     target_title = target_title.lower()
#     similar_titles = []

#     for title in titles:
#         title = title.lower()
#         similarity_score = fuzz.ratio(target_title, title)
#         if similarity_score >= distance_threshold:
#             similar_titles.append((title, similarity_score))

#     return similar_titles

def find_titles_with_spelling_variations(target_title, titles, method="levenshtein", distance_threshold=80):
    target_title = target_title.lower()
    similar_titles = []

    for title in titles:
        title = title.lower()
        similarity_score = fuzz.ratio(target_title, title)
        if similarity_score >= distance_threshold:
            similar_titles.append((title))

    return similar_titles
