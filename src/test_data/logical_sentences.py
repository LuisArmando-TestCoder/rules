logical_sentences = [
    # # Basic sentences
    "if P(x) then Q(x)",
    "P(x) and Q(y)",
    "not R(z)",
    "(P(x) and (Q(y) OR R(z)))",
    "not (P(x) and Q(x))",
    "(not P(x)) OR (Q(y) and R(z))",
    "if (P(x) and Q(y)) then (R(z) OR not S(a))",
    
    # # Deeper nesting
    "not (P(x) and (Q(y) OR (R(z) and S(a))))",
    "((not P(x)) and Q(y)) OR (R(z) and (not S(a)))",
    "if ((P(x) OR Q(y)) and (not R(z))) then (S(a) OR not T(b))",
    
    # # Multiple levels of implication
    "if (if P(x) then Q(x)) then (if Q(x) then R(z))",
    "not (if (P(x) and Q(y)) then (R(z) OR S(a)))",
    "if (not P(x)) then (not (Q(y) OR R(z)))",
    
    # # Combining multiple operators
    "(P(x) OR (Q(y) and (R(z) → S(a))))",
    "not ((P(x) → Q(y)) OR (R(z) and not S(a)))",
    "(if (P(x) and Q(y)) then R(z)) OR (not S(a))",

    # # Extreme nesting
    "not (if ((P(x) and (Q(y) OR R(z))) → (S(a) and T(b))) then (not U(c)))",
    "(((P(x) → Q(y)) → R(z)) and S(a)) OR (not (T(b) and U(c)))",
    
    # # Moderately Nested Sentences
    "if (P(x) and Q(y)) then (R(z) OR S(a))",
    "not (P(x) and (Q(y) OR R(z)))",
    "(P(x) OR (Q(y) and R(z)))",
    "if ((P(x) OR Q(y)) and R(z)) then S(a)",
    "not ((P(x) and Q(y)) OR (R(z) → S(a)))",
    
    # # Deeply Nested Sentences
    "if (if P(x) then Q(x)) then R(z)",
    "if (P(x) → Q(y)) then ((Q(y) → R(z)) → S(a))",
    "not (if ((P(x) and Q(y)) → R(z)) then (S(a) OR T(b)))",
    "(((P(x) → Q(y)) → R(z)) and S(a)) OR (not T(b))",
    "(not (P(x) and Q(y))) OR ((R(z) → S(a)) and T(b))",
    
    # # Complex Logical Operations
    "if ((P(x) OR Q(y)) and (R(z) → S(a))) then (T(b) and U(c))",
    "not (((P(x) and Q(y)) → R(z)) OR (S(a) and T(b)))",
    "(if (P(x) → Q(y)) then R(z)) OR (not S(a))",
    "if ((P(x) and (Q(y) OR R(z))) → S(a)) then T(b)",
    "not ((P(x) and Q(y)) → (R(z) and (S(a) OR T(b))))",
]
