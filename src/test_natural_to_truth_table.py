from natural_restricted_to_logical import transform_to_logical
from test_data.natural_sentences import natural_sentences_philosophy
from sentence_table import get_sentence_table
from natural_to_natural_restricted import get_natural_to_natural_restricted

for natural_sentence in natural_sentences_philosophy:
    naturalRestrictedSentence = "if (desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness) then desire_is_the_root_of_all_greatness"
    sentence_table = get_sentence_table(naturalRestrictedSentence)

    print(f"\n{naturalRestrictedSentence}\n")

    for sentence_row in sentence_table:
        print(sentence_row)