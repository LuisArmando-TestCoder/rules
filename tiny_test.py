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

# don't use the non_statements when typing conditions
