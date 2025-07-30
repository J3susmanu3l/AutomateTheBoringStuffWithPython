import email
import pyperclip as pc, re

# Get text from clipboard
text_from_clipboard = pc.paste()

# Improved phone number pattern that matches various formats
phone_number_pattern = re.compile(r'''(
    # Optional country code (1-3 digits, may be in parentheses)
    (\+?\d{1,3}\s?)?  # Country code with optional + and space
    # Optional opening parenthesis for area code
    (\()?
    # Area code (3 digits)
    (\d{3})
    # Optional closing parenthesis for area code
    (\))?
    # Separator (space, dash, dot, or nothing)
    [\s\-\.]?
    # First 3 digits
    (\d{3})
    # Separator (space, dash, dot, or nothing)
    [\s\-\.]?
    # Last 4 digits
    (\d{4})
    # Optional extension
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?
    )''', re.IGNORECASE | re.VERBOSE)

# Find all phone numbers in the text
phones_found_unclean = phone_number_pattern.findall(text_from_clipboard)

# Email pattern to find email addresses
email_pattern = re.compile(r'\b[a-zA-Z0-9\S]+@{1}\w+\.\w{2,6}\b') 
emails_found = email_pattern.findall(text_from_clipboard)

# Clean up phone numbers - extract the full match (group 0)
phones_found_cleaned = []
for match in phones_found_unclean:
    # Get the full matched string (group 0)
    full_match = match[0]
    # Only add if it's not empty
    if full_match.strip():
        phones_found_cleaned.append(full_match)

# Print results
print("Email addresses found:")
print(emails_found)
print("\nPhone numbers found:")
print(phones_found_cleaned)

# Copy phone numbers to clipboard
if phones_found_cleaned:
    pc.copy('\n'.join(phones_found_cleaned))
    print(f"\nCopied {len(phones_found_cleaned)} phone number(s) to clipboard")
else:
    print("\nNo phone numbers found in the text")






# def main():





# if __name__ == "__main__":
#     main()



