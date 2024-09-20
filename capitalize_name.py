def capitalize_title(name):
    """
    Capitalize the movie title following title case rules, except for small words.

    The first word is always capitalized. Small words such as articles, prepositions,
    and conjunctions (e.g., 'and', 'the', 'of') are only capitalized if they appear
    at the beginning of the title.

    Args:
        name (str): The movie title to capitalize.

    Returns:
        str: The title-cased version of the movie title.
    """
    small_words = {'and', 'or', 'the', 'in', 'on', 'at', 'to', 'of', 'a', 'an', 'by', 'for'}

    words = name.split()
    capitalized_words = []

    for i, word in enumerate(words):

        if i == 0 or word.lower() not in small_words:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word.lower())

    return ' '.join(capitalized_words)
