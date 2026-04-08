import re
from collections import Counter

def extract_keywords(text, num_keywords=5):
    words = re.findall(r'\w+', text.lower())
    stopwords = set(["the", "is", "in", "and", "to", "of", "a"])

    filtered = [w for w in words if w not in stopwords]
    most_common = Counter(filtered).most_common(num_keywords)

    return [word for word, _ in most_common]
