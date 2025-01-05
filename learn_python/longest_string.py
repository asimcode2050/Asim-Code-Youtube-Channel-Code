def longest_substring_without_repeating_characters(s: str) -> int:
    left = 0
    max_length = 0
    char_index_map = {}

    for right in range(len(s)):
        current_char = s[right]

        if current_char in char_index_map and char_index_map[current_char] >= left:
            left = char_index_map[current_char] + 1

        char_index_map[current_char] = right

        max_length = max(max_length, right - left + 1)

    return max_length

example_string = "abcabcbb"
result = longest_substring_without_repeating_characters(example_string)
print(f"Longest substring length for '{example_string}': {result}")
