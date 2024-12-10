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
    "not data_is_valid",
    "(user_is_authenticated and (user_has_permission or data_is_valid))",
    "not (user_is_authenticated and user_has_permission)",
    "(not user_is_authenticated) or (user_has_permission and data_is_valid)",
    "if (user_is_authenticated and user_has_permission) then (data_is_valid or not process_can_continue)",
    
    # Deeper nesting
    "not (user_is_authenticated and (user_has_permission or (data_is_valid and process_can_continue)))",
    "((not user_is_authenticated) and user_has_permission) or (data_is_valid and (not process_can_continue))",
    "if ((user_is_authenticated or user_has_permission) and (not data_is_valid)) then (process_can_continue or not system_is_operational)",
    
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
