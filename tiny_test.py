from natural_restricted_language import transform_to_logical
from rules_maybe import LogicalLanguageProcessor
from natural_restricted_sentences import natural_restricted_sentences_auth_context

for naturalRestrictedSentence in natural_restricted_sentences_auth_context:
    processor = LogicalLanguageProcessor()

    sentence = naturalRestrictedSentence

    semi_logical = transform_to_logical(sentence)


    logical_form, message = processor.process_sentence(semi_logical)

    print(sentence)
    print(semi_logical)
    print(message)
    if message == "The sentence follows logical rules.":
        formula, _ = processor.parse_formula(processor.tokenize(logical_form))
        processor.generate_truth_table(formula)
        print("✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
    else:
        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")

# Area of improvement (sort of): don't use the non_statements when typing conditions
# Area of improvement: variable names are limited to 26ish, they need to be numbered so they can be infinite
# (although statements are not infinite unless 
# they are the reflection of an infinite reality, 
# but finite observers who get to be finite in the end, whitin that infinite "reality" [which only an observer can
# transform it into real as it categorizes it as such],
# don't need an infinite implementation, 
# but still it could be cool to have it, 
# eventhough a finite system such as a 2024 laptop is finite in computing power)
