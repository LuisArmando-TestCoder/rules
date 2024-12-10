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

# current bug is using "if " at the end of a condition but the "if " in the non_statements is neccesary, looking for a workaround

# don't you dare use: alif, aperitif, calif, cluif, coif, cuif, digestif, embelif, fixatif, GIF, gonif, hanif, khalif, kharif, kif, leitmotif, massif, metif, motif, mutasarrif, mutessarif, naif, neif, recitatif, reif, restif, saif, sanserif, SCIF, seif, serif, sharif, sherif, skaif, skeif, sportif, waif, Zif. With a space in the end of a condition