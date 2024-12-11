from natural_restricted_language import transform_to_logical
from rules_maybe import LogicalLanguageProcessor
from natural_restricted_sentences import natural_restricted_sentences_auth_context
from sentence_table import get_sentence_table

for naturalRestrictedSentence in natural_restricted_sentences_auth_context:
    processor = LogicalLanguageProcessor()

    sentence_table = get_sentence_table(naturalRestrictedSentence)

    print("✅" * 50)
    print(f"\n{naturalRestrictedSentence}\n")

    for sentence_row in sentence_table:
        print(sentence_row)

# Area of improvement (sort of): don't use the non_statements when typing conditions
# Area of improvement: variable names are limited to 26ish, they need to be numbered so they can be infinite
# (although statements are not infinite unless 
# they are the reflection of an infinite reality, 
# but finite observers who get to be finite in the end, whitin that infinite "reality" [which only an observer can
# transform it into real as it categorizes it as such],
# don't need an infinite implementation, 
# but still it could be cool to have it, 
# eventhough a finite system, such as a 2024 laptop, is finite in computing power)
