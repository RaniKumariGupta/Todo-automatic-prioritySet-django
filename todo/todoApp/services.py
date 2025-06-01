import re

def detect_priority(title):
    title_lower = title.lower()
    if re.search(r'\bhigh\b[:]?$', title_lower) or re.match(r'^high\b[:]? ', title_lower):
        return 'High'
    elif re.search(r'\bmedium\b[:]?$', title_lower) or re.match(r'^medium\b[:]? ', title_lower):
        return 'Medium'
    elif re.search(r'\blow\b[:]?$', title_lower) or re.match(r'^low\b[:]? ', title_lower):
        return 'Low'
    
