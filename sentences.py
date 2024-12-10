sentences = [
    # # Basic sentences
    "If P(x) then Q(x)",
    "P(x) AND Q(y)",
    "NOT R(z)",
    "(P(x) AND (Q(y) OR R(z)))",
    "NOT (P(x) AND Q(x))",
    "(NOT P(x)) OR (Q(y) AND R(z))",
    "If (P(x) AND Q(y)) then (R(z) OR NOT S(a))",
    
    # # Deeper nesting
    "NOT (P(x) AND (Q(y) OR (R(z) AND S(a))))",
    "((NOT P(x)) AND Q(y)) OR (R(z) AND (NOT S(a)))",
    "If ((P(x) OR Q(y)) AND (NOT R(z))) then (S(a) OR NOT T(b))",
    
    # # Multiple levels of implication
    "If (If P(x) then Q(x)) then (If Q(x) then R(z))",
    "NOT (If (P(x) AND Q(y)) then (R(z) OR S(a)))",
    "If (NOT P(x)) then (NOT (Q(y) OR R(z)))",
    
    # # Combining multiple operators
    "(P(x) OR (Q(y) AND (R(z) → S(a))))",
    "NOT ((P(x) → Q(y)) OR (R(z) AND NOT S(a)))",
    "(If (P(x) AND Q(y)) then R(z)) OR (NOT S(a))",
    
    # # Extreme nesting
    "NOT (If ((P(x) AND (Q(y) OR R(z))) → (S(a) AND T(b))) then (NOT U(c)))",
    "(((P(x) → Q(y)) → R(z)) AND S(a)) OR (NOT (T(b) AND U(c)))",

    # # Simple Sentences
    "If P(x) then Q(x)",
    "P(x) AND Q(y)",
    "NOT R(z)",
    "(P(x) OR Q(y))",
    "NOT (P(x) AND Q(x))",
    
    # # Moderately Nested Sentences
    "If (P(x) AND Q(y)) then (R(z) OR S(a))",
    "NOT (P(x) AND (Q(y) OR R(z)))",
    "(P(x) OR (Q(y) AND R(z)))",
    "If ((P(x) OR Q(y)) AND R(z)) then S(a)",
    "NOT ((P(x) AND Q(y)) OR (R(z) → S(a)))",
    
    # # Deeply Nested Sentences
    "If (If P(x) then Q(x)) then R(z)",
    "If (P(x) → Q(y)) then ((Q(y) → R(z)) → S(a))",
    "NOT (If ((P(x) AND Q(y)) → R(z)) then (S(a) OR T(b)))",
    "(((P(x) → Q(y)) → R(z)) AND S(a)) OR (NOT T(b))",
    "(NOT (P(x) AND Q(y))) OR ((R(z) → S(a)) AND T(b))",
    
    # # Complex Logical Operations
    "If ((P(x) OR Q(y)) AND (R(z) → S(a))) then (T(b) AND U(c))",
    "NOT (((P(x) AND Q(y)) → R(z)) OR (S(a) AND T(b)))",
    "(If (P(x) → Q(y)) then R(z)) OR (NOT S(a))",
    "If ((P(x) AND (Q(y) OR R(z))) → S(a)) then T(b)",
    "NOT ((P(x) AND Q(y)) → (R(z) AND (S(a) OR T(b))))",
]
