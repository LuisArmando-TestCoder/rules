natural_restricted_sentences = [
    # Basic sentences
    "if condition_a then condition_b",
    "condition_a and condition_b",
    "not condition_c",
    "(condition_a and (condition_b or condition_c))",
    "not (condition_a and condition_b)",
    "(not condition_a) or (condition_b and condition_c)",
    "if (condition_a and condition_b) then (condition_c or not condition_d)",
    
    # Deeper nesting
    "not (condition_a and (condition_b or (condition_c and condition_d)))",
    "((not condition_a) and condition_b) or (condition_c and (not condition_d))",
    "if ((condition_a or condition_b) and (not condition_c)) then (condition_d or not condition_e)",
    
    # Multiple levels of implication
    "if (if condition_a then condition_b) then (if condition_b then condition_c)",
    "not (if (condition_a and condition_b) then (condition_c or condition_d))",
    "if (not condition_a) then (not (condition_b or condition_c))",
    
    # Combining multiple operators
    "(condition_a or (condition_b and (if condition_c then condition_d)))",
    "not ((if condition_a then condition_b) or (condition_c and not condition_d))",
    "(if (condition_a and condition_b) then condition_c) or (not condition_d)",
    
    # Extreme nesting
    "not (if (condition_a and (condition_b or condition_b)) then ((condition_c and condition_d) → (not condition_e)))",
    
    "(((if condition_a then condition_b) → condition_c) and condition_d) or (not (condition_e and condition_f))",
    
    # Moderately Nested Sentences
    "if (condition_a and condition_b) then (condition_c or condition_d)",
    "not (condition_a and (condition_b or condition_c))",
    "(condition_a or (condition_b and condition_c))",
    "if ((condition_a or condition_b) and condition_c) then condition_d",
    "not ((condition_a and condition_b) or (if condition_c then condition_d))",
    
    # Deeply Nested Sentences
    "if (if condition_a then condition_b) then condition_c",
    "if (if condition_a then condition_b) then ((if condition_b then condition_c) → condition_d)",
    "not (if ((condition_a and condition_b) → condition_c) then (condition_d or condition_e))",
    "(((if condition_a then condition_b) → condition_c) and condition_d) or (not condition_e)",
    "(not (condition_a and condition_b)) or ((if condition_c then condition_d) and condition_e)",
    
    # Complex Logical Operations
    "if ((condition_a or condition_b) and (if condition_c then condition_d)) then (condition_e and condition_f)",
    "not (((condition_a and condition_b) → condition_c) or (condition_d and condition_e))",
    "(if (if condition_a then condition_b) then condition_c) or (not condition_d)",
    "if (((condition_a and (condition_b or condition_c)) → condition_d)) then condition_e",
    "not ((condition_a and condition_b) → (condition_c and (condition_d or condition_e)))",
]

natural_restricted_sentences_auth_context = [
    # Basic sentences
    "if user_is_authenticated then user_has_permission",
    "user_is_authenticated and user_has_permission",
    "not data_is_invalid",
    "(user_is_authenticated and (user_has_permission or data_is_valid))",
    "not (user_is_authenticated and user_has_permission)",
    "(not user_is_authenticated) or (user_has_permission and data_is_valid)",
    "if (user_is_authenticated and user_has_permission) then (data_is_valid or not process_can_continue)",
    
    # Deeper nesting
    "not (user_is_authenticated and (user_has_permission or (data_is_valid and process_can_continue)))",
    "((not user_is_authenticated) and user_has_permission) or (data_is_valid and (not process_can_continue))",
    "if ((user_is_authenticated or user_has_permission) and (not data_is_invalid)) then (process_can_continue or not system_is_operational)",
    
    # Multiple levels of implication
    "if (if user_is_authenticated then user_has_permission) then (if user_has_permission then data_is_valid)",
    "not (if (user_is_authenticated and user_has_permission) then (data_is_valid or process_can_continue))",
    "if (not user_is_authenticated) then (not (user_has_permission or data_is_valid))",
    
    # Combining multiple operators
    "(user_is_authenticated or (user_has_permission and (if data_is_valid then process_can_continue)))",
    "not ((if user_is_authenticated then user_has_permission) or (data_is_valid and not process_can_continue))",
    "(if (user_is_authenticated and user_has_permission) then data_is_valid) or (not process_can_continue)",
    
    # Extreme nesting
    "not (if (user_is_authenticated and (user_has_permission or user_has_permission)) then ((data_is_valid and process_can_continue) → (not system_is_operational)))",
    "(((if user_is_authenticated then user_has_permission) → data_is_valid) and process_can_continue) or (not (system_is_operational and log_is_enabled))",
    
    # Moderately Nested Sentences
    "if (user_is_authenticated and user_has_permission) then (data_is_valid or process_can_continue)",
    "not (user_is_authenticated and (user_has_permission or data_is_valid))",
    "(user_is_authenticated or (user_has_permission and data_is_valid))",
    "if ((user_is_authenticated or user_has_permission) and data_is_valid) then process_can_continue",
    "not ((user_is_authenticated and user_has_permission) or (if data_is_valid then process_can_continue))",
    
    # Deeply Nested Sentences
    "if (if user_is_authenticated then user_has_permission) then data_is_valid",
    "if (if user_is_authenticated then user_has_permission) then ((if user_has_permission then data_is_valid) → process_can_continue)",
    "not (if ((user_is_authenticated and user_has_permission) → data_is_valid) then (process_can_continue or system_is_operational))",
    "(((if user_is_authenticated then user_has_permission) → data_is_valid) and process_can_continue) or (not system_is_operational)",
    "(not (user_is_authenticated and user_has_permission)) or ((if data_is_valid then process_can_continue) and system_is_operational)",
    
    # Complex Logical Operations
    "if ((user_is_authenticated or user_has_permission) and (if data_is_valid then process_can_continue)) then (system_is_operational and log_is_enabled)",
    "not (((user_is_authenticated and user_has_permission) → data_is_valid) or (process_can_continue and system_is_operational))",
    "(if (if user_is_authenticated then user_has_permission) then data_is_valid) or (not process_can_continue)",
    "if (((user_is_authenticated and (user_has_permission or data_is_valid)) → process_can_continue)) then system_is_operational",
    "not ((user_is_authenticated and user_has_permission) → (data_is_valid and (process_can_continue or system_is_operational)))",
]

natural_restricted_sentences = [
    # Basic sentences
    "if has_pizza then owns_a_unicorn",
    "has_pizza and owns_a_unicorn",
    "not is_sleeping",
    "(has_pizza and (owns_a_unicorn or is_sleeping))",
    "not (has_pizza and owns_a_unicorn)",
    "(not has_pizza) or (owns_a_unicorn and is_sleeping)",
    "if (has_pizza and owns_a_unicorn) then (is_sleeping or not has_dancing_shoes)",
    
    # Deeper nesting
    "not (has_pizza and (owns_a_unicorn or (is_sleeping and has_dancing_shoes)))",
    "((not has_pizza) and owns_a_unicorn) or (is_sleeping and (not has_dancing_shoes))",
    "if ((has_pizza or owns_a_unicorn) and (not is_sleeping)) then (has_dancing_shoes or not can_speak_morse_code)",
    
    # Multiple levels of implication
    "if (if has_pizza then owns_a_unicorn) then (if owns_a_unicorn then is_sleeping)",
    "not (if (has_pizza and owns_a_unicorn) then (is_sleeping or has_dancing_shoes))",
    "if (not has_pizza) then (not (owns_a_unicorn or is_sleeping))",
    
    # Combining multiple operators
    "(has_pizza or (owns_a_unicorn and (if is_sleeping then has_dancing_shoes)))",
    "not ((if has_pizza then owns_a_unicorn) or (is_sleeping and not has_dancing_shoes))",
    "(if (has_pizza and owns_a_unicorn) then is_sleeping) or (not has_dancing_shoes)",
    
    # Extreme nesting
    "not (if (has_pizza and (owns_a_unicorn or owns_a_unicorn)) then ((is_sleeping and has_dancing_shoes) → (not can_speak_morse_code)))",
    "(((if has_pizza then owns_a_unicorn) → is_sleeping) and has_dancing_shoes) or (not (can_speak_morse_code and has_flying_cats))",
    
    # Moderately Nested Sentences
    "if (has_pizza and owns_a_unicorn) then (is_sleeping or has_dancing_shoes)",
    "not (has_pizza and (owns_a_unicorn or is_sleeping))",
    "(has_pizza or (owns_a_unicorn and is_sleeping))",
    "if ((has_pizza or owns_a_unicorn) and is_sleeping) then has_dancing_shoes",
    "not ((has_pizza and owns_a_unicorn) or (if is_sleeping then has_dancing_shoes))",
    
    # Deeply Nested Sentences
    "if (if has_pizza then owns_a_unicorn) then is_sleeping",
    "if (if has_pizza then owns_a_unicorn) then ((if owns_a_unicorn then is_sleeping) → has_dancing_shoes)",
    "not (if ((has_pizza and owns_a_unicorn) → is_sleeping) then (has_dancing_shoes or can_speak_morse_code))",
    "(((if has_pizza then owns_a_unicorn) → is_sleeping) and has_dancing_shoes) or (not can_speak_morse_code)",
    "(not (has_pizza and owns_a_unicorn)) or ((if is_sleeping then has_dancing_shoes) and can_speak_morse_code)",
    
    # Complex Logical Operations
    "if ((has_pizza or owns_a_unicorn) and (if is_sleeping then has_dancing_shoes)) then (can_speak_morse_code and has_flying_cats)",
    "not (((has_pizza and owns_a_unicorn) → is_sleeping) or (has_dancing_shoes and can_speak_morse_code))",
    "(if (if has_pizza then owns_a_unicorn) then is_sleeping) or (not has_dancing_shoes)",
    "if (((has_pizza and (owns_a_unicorn or is_sleeping)) → has_dancing_shoes)) then can_speak_morse_code",
    "not ((has_pizza and owns_a_unicorn) → (is_sleeping and (has_dancing_shoes or can_speak_morse_code)))",
]
