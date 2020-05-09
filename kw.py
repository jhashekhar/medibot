import re


# TODO: Add names of diseases

KW = [
    'pain', 'body', 'severe', 'chest', 'stomach', 'cough', 'hydration',\
    'gas', 'heart', 'liver', 'kidney', 'blood', 'tear', 'vomit', 'nausea', \
    'month', 'muscle', 'bone', 'symptom', 'pregnant', 'cramp', 'period', \
    'gain', 'loss', 'drug']

kw = {
    'itis': re.compile(r"\w+itis"),
    'pain': "pain",
    'severe': "severe",
    'body': "body",
    'chest': "chest",
    'stomach': "stomach"
    }