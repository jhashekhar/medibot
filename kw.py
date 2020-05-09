import re


KW = ['pain', 'body', 'severe', 'chest', 'stomach']

kw = {
    'itis': re.compile(r"\w+itis"),
    'pain': "pain",
    'severe': "severe",
    'body': "body",
    'chest': "chest",
    'stomach': "stomach"
    }