from natural_restricted_to_logical import transform_to_logical
from test_data.natural_sentences import natural_sentences_philosophy
from sentence_table import get_sentence_table
from natural_to_natural_restricted import get_natural_to_natural_restricted

for natural_sentence in natural_sentences_philosophy:
    naturalRestrictedSentence = get_sentence_table(natural_sentence)
    sentence_table = get_sentence_table(naturalRestrictedSentence)

    print(f"\n{naturalRestrictedSentence}\n")

    for sentence_row in sentence_table:
        print(sentence_row)