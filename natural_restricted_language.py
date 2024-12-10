import re
import string
from typing import List, Dict

def create_function_tokens_dict(strings: List[str]) -> Dict[str, str]:
    """
    Takes an array of strings and returns a dictionary mapping each unique string
    to a unique token in the format "Letter_n(variable_n)". Duplicate strings
    are assigned the same token. Letters cycle from A-Z, and n increments each cycle.

    Args:
        strings (List[str]): The input list of strings.

    Returns:
        Dict[str, str]: A dictionary mapping each unique string to its token.
    """
    # Remove duplicates while preserving order
    seen = {}
    unique_strings = []
    for s in strings:
        if s not in seen:
            seen[s] = True
            unique_strings.append(s)
    
    tokens_dict = {}
    letters = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']
    # Create variable letters: ['x', 'y', 'z', 'a', 'b', ..., 'w']
    variable_letters = ['x', 'y', 'z'] + list(string.ascii_lowercase)
    variable_letters = variable_letters[:26]  # Ensure exactly 26 variables
    
    total_letters = len(letters)  # 26
    total_variables = len(variable_letters)  # 26
    
    for i, unique_str in enumerate(unique_strings):
        # letter_index = i // total_letters  # Determines the 'n' value
        letter = letters[i % total_letters]  # Cycles through A-Z
        variable = variable_letters[i % total_variables]  # Cycles through x, y, z, a, ..., w
        token = f"{letter}({variable})"
        # token = f"{letter}_{letter_index}({variable}_{letter_index})"

        tokens_dict[unique_str] = token
    
    return tokens_dict

def substitute_strings(substitutions: Dict[str, str], source_string: str) -> str:
    """
    Replaces occurrences of dictionary keys in the source string with their corresponding values.

    Args:
        substitutions (Dict[str, str]): A dictionary where keys are substrings to replace,
                                         and values are the substitute strings.
        source_string (str): The string in which to perform substitutions.

    Returns:
        str: The resulting string after substitutions.
    """
    if not substitutions:
        return source_string

    # Sort keys by length in descending order to handle overlapping keys
    sorted_keys = sorted(substitutions.keys(), key=len, reverse=True)
    
    # Escape keys to handle any special regex characters
    escaped_keys = [re.escape(key) for key in sorted_keys]
    
    # Create a regex pattern that matches any of the keys
    pattern = re.compile('|'.join(escaped_keys))
    
    # Define a replacement function that looks up the matched key in the substitutions
    def replacer(match):
        matched_text = match.group(0)
        return substitutions.get(matched_text, matched_text)  # Fallback to original text if not found
    
    # Perform the substitution
    result_string = pattern.sub(replacer, source_string)
    
    return result_string

def get_unrestricted(restrictions: List[str], sentence: str) -> List[str]:
    """
    Splits the sentence into parts that do not contain any of the restriction substrings.

    Args:
        restrictions (List[str]): A list of restriction substrings.
        sentence (str): The sentence to be processed.

    Returns:
        List[str]: A list of substrings from the sentence that are not restricted.
    """
    if not restrictions:
        return [sentence] if sentence else []
    
    # Sort restrictions by length in descending order to handle substrings properly
    sorted_restrictions = sorted(restrictions, key=len, reverse=True)
    
    # Escape each restriction to handle any special regex characters
    escaped_restrictions = [re.escape(r) for r in sorted_restrictions]
    
    # Create a regex pattern that matches any of the restrictions
    pattern = '|'.join(escaped_restrictions)
    
    # Use re.split to split the sentence at each occurrence of any restriction
    parts = re.split(pattern, sentence)
    
    # Remove any empty strings and strip whitespace from each part
    unrestricted_parts = [part.strip() for part in parts if part.strip()]
    
    return unrestricted_parts


def transform_to_logical(sentence):
    normalized_sentence = sentence.lower()
    non_statement = ["(not ", " not ", "not ", " or ", "if (", "if ", " then ", " and ", " → ", " ", "(", ")"]
    filtered_sentence = get_unrestricted(non_statement, normalized_sentence)
    tokens = create_function_tokens_dict(filtered_sentence)
    logical = substitute_strings(tokens, sentence)

    return logical

# logical = transform_to_logical("if (if condition_a then condition_b) then condition_c")

# print(logical)