import re


def strip_re(string_to_clean, remove_character = " "):
    # Create regex patterns that match one or more occurrences of the character to remove
    # We need to escape special regex characters to treat them as literal characters
    escaped_char = re.escape(remove_character)
    
    # Pattern to match one or more of the character at the beginning (^) and end ($)
    beginning_pattern_finder = re.compile(f'^{escaped_char}+')
    ending_pattern_finder = re.compile(f'{escaped_char}+$')
    
    # First remove characters from the beginning
    beginning_cleaned_string = beginning_pattern_finder.sub("", string_to_clean)
    # Then remove characters from the end of the already beginning-cleaned string
    final_cleaned_string = ending_pattern_finder.sub("", beginning_cleaned_string)
    
    return final_cleaned_string


# Test the function
to_print = strip_re("  spaces are outside now.  ", " ")
print(f"Original: '{to_print}'")
print(f"Expected: 'spaces are outside now.'")

# Test with different characters
test_string = "***hello***"
result = strip_re(test_string, "*")
print(f"Original: '{test_string}'")
print(f"Result: '{result}'")
    