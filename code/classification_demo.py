"""Synthetic portfolio demonstration, separate from the original internal script.
Run: python classification_demo.py
A dictionary-based screening aid, not a diagnostic model.
"""
import re
import unicodedata

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.lower())
                   if not unicodedata.combining(c))

TERMS = {
    'diabetes': ['diabetes', 'dm2', 'e11'],
    'hypertension': ['hypertension', 'hipertensao', 'has', 'i10'],
}

def classify(text):
    cleaned = normalize(text)
    matches = [category for category, terms in TERMS.items()
               if any(re.search(r'\b' + re.escape(term) + r'\b', cleaned)
                      for term in terms)]
    return {'text': text, 'categories': matches, 'review_required': True}

if __name__ == '__main__':
    for description in ['Acompanhamento DM2 e HAS', 'Diagnostico E11',
                        'Consulta de rotina', 'Sem diabetes; historia familiar']:
        print(classify(description))
    print('All records are synthetic. Negation and family history need review.')
