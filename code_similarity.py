import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to tokenize code
def tokenize_code(code):
    code = re.sub(r'\".*?\"|\'.*?\'|#.*', '', code)
    tokens = re.findall(r'\b\w+\b', code)
    return ' '.join(tokens)


def calculate_similarity(code1, code2):
    code1_tokens = tokenize_code(code1)
    code2_tokens = tokenize_code(code2)

    vectorizer = CountVectorizer().fit_transform([code1_tokens, code2_tokens])
    vectors = vectorizer.toarray()

    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0][1] * 100


# Example usage
code1 = """

"""

code2 = """

"""

similarity_percentage = calculate_similarity(code1, code2)
print(f"The similarity between the two code snippets is: {similarity_percentage:.2f}%")
