from natural_restricted_to_logical import transform_to_logical
from Logical_Language_Processor import Logical_Language_Processor

def sequential_replace(template, replacements):
    for replacement in replacements:
        template = template.replace("{}", replacement, 1)
    return template

def get_sentence_table(sentence):
    sentence_table = []

    # sentence_to_
    semi_logical, tokens = transform_to_logical(sentence)

    processor = Logical_Language_Processor()

    # logic_to_
    logical_form, message = processor.process_sentence(semi_logical)

    if message == "The sentence follows logical rules.":
        formula, _ = processor.parse_formula(processor.tokenize(logical_form))
        
        # truth_table_to_
        truth_table = processor.generate_truth_table(formula)

        # print(tokens.keys())
        # print(truth_table.keys())
        token_keys = tokens.keys()
        sentence_states = {
            "False": "Contradictory",
            "True": "Possible",
        }
        
        # sentence_table
        for combo, result in truth_table.items():
            substitution_template = combo.replace("False", "not {}").replace("True", "{}")
            substitution = sequential_replace(substitution_template, token_keys).replace("|", "while")
            sentence_table.append(f"{sentence_states[str(result)]}: {substitution}")
        
    return sentence_table


# sentence_table = get_sentence_table(
#     "not ((user_is_authenticated and user_has_permission) → (data_is_valid and (process_can_continue or system_is_operational)))"
# )

# for sentence_row in sentence_table:
#     print(sentence_row)