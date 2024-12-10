import re
import itertools

class LogicalLanguageProcessor:
    def __init__(self):
        self.op_map = {
            "AND": "∧",
            "OR": "∨",
            "NOT": "¬",
        }
        self.predicate_regex = re.compile(r'^[A-Z][a-z]*\([A-Za-z0-9_, ]*\)$')
        self.if_pattern = re.compile(r'(?i)\bif\s+(.*?)\s+then\s+(.*)', re.IGNORECASE)
        self.token_regex = re.compile(r'[A-Z][a-z]*\([A-Za-z0-9_, ]*\)|¬|∧|∨|→|\(|\)|[A-Za-z]+', re.IGNORECASE)

    def is_balanced(self, text):
        stack = []
        for char in text:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def validate_structure(self, sentence):
        """Check if the sentence structure is valid before processing."""
        if not self.is_balanced(sentence):
            raise ValueError("The sentence has unbalanced parentheses.")
        if not re.search(r'\bif\b.*\bthen\b', sentence, re.IGNORECASE) and '(' not in sentence:
            raise ValueError("The sentence does not contain a valid logical structure.")
        return True

    def process_sentence(self, sentence):
        try:
            self.validate_structure(sentence.strip())

            # Wrap top-level If...then... if needed
            sentence = self.preprocess_if_then_top_level(sentence.strip())

            # Fully resolve If...then... inside-out
            sentence = self.preprocess_if_then(sentence)

            tokens = self.tokenize(sentence)
            tokens = self.replace_operators(tokens)
            tokens = self.normalize_expression(tokens)

            if self.needs_top_level_wrapping(tokens):
                tokens = ["("] + tokens + [")"]

            if not self.check_parentheses(tokens):
                return "", "Mismatched parentheses."

            formula, remaining = self.parse_formula(tokens)
            if remaining:
                return " ".join(tokens), "Extra tokens found, not a single well-formed formula."

            logical_form = self.formula_to_string(formula)
            return logical_form, "The sentence follows logical rules."
        except ValueError as e:
            return str(e), "The sentence could not be logically processed."

    def preprocess_if_then_top_level(self, sentence):
        top_level_pattern = re.compile(r'^\s*if\s+(.*?)\s+then\s+(.*?)\s*$', re.IGNORECASE)
        match = top_level_pattern.match(sentence)
        if match:
            sentence = f"({sentence})"
        return sentence

    def preprocess_if_then(self, sentence):
        while True:
            start_pos = sentence.lower().find('(if ')
            if start_pos == -1:
                break  # No '(If ' found, done

            depth = 0
            scan_pos = start_pos + 1  # Skip '('
            scan_pos += 3  # Skip 'If '
            depth = 1

            then_pos = -1
            i = scan_pos
            while i < len(sentence):
                ch = sentence[i]
                if ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
                if depth == 1 and sentence[i:i+5].lower() == ' then':
                    then_pos = i
                    break
                i += 1

            if then_pos == -1:
                break

            start_B = then_pos + 5
            while start_B < len(sentence) and sentence[start_B].isspace():
                start_B += 1

            A = sentence[scan_pos:then_pos].strip()

            depth = 1
            end_pos = -1
            for k, ch in enumerate(sentence[start_B:], start=start_B):
                if ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
                    if depth == 0:
                        end_pos = k
                        break

            if end_pos == -1:
                break

            B = sentence[start_B:end_pos].strip()
            full_segment = sentence[start_pos:end_pos+1]

            A = self.preprocess_if_then(A)
            B = self.preprocess_if_then(B)

            if not self.is_balanced(A) or not self.is_balanced(B):
                break

            transformed = f"({A} → {B})"
            sentence = sentence[:start_pos] + transformed + sentence[end_pos+1:]

        if not self.is_balanced(sentence):
            raise ValueError("Final sentence is not balanced after transformations.")

        return sentence

    def tokenize(self, sentence):
        tokens = self.token_regex.findall(sentence)
        tokens = [t.strip() for t in tokens if t.strip()]
        if not tokens:
            raise ValueError("No recognizable tokens found.")
        return tokens

    def replace_operators(self, tokens):
        result = []
        for t in tokens:
            upper_t = t.upper()
            if upper_t in self.op_map:
                result.append(self.op_map[upper_t])
            else:
                result.append(t)
        return result

    def normalize_expression(self, tokens):
        if len(tokens) == 3 and self.is_predicate(tokens[0]) and self.is_binary_op(tokens[1]) and self.is_predicate(tokens[2]):
            return ["("] + tokens + [")"]
        return tokens

    def needs_top_level_wrapping(self, tokens):
        depth = 0
        for t in tokens:
            if t == "(":
                depth += 1
            elif t == ")":
                depth -= 1
            elif depth == 0 and self.is_binary_op(t):
                return True
        return False

    def check_parentheses(self, tokens):
        stack = []
        for t in tokens:
            if t == "(":
                stack.append(t)
            elif t == ")":
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def parse_formula(self, tokens):
        if not tokens:
            raise ValueError("Incomplete expression.")

        t = tokens[0]

        if t == "¬":
            subtree, rest = self.parse_formula(tokens[1:])
            return ("NOT", subtree), rest

        if t == "(":
            inner_formula, rest = self.parse_formula(tokens[1:])
            if not rest:
                raise ValueError("Missing closing parenthesis.")

            next_token = rest[0]
            if next_token in ["∧", "∨", "→"]:
                right_subtree, rest2 = self.parse_formula(rest[1:])
                if not rest2 or rest2[0] != ")":
                    raise ValueError("Missing closing parenthesis in binary expression.")
                return ("BINOP", next_token, inner_formula, right_subtree), rest2[1:]
            elif next_token == ")":
                return inner_formula, rest[1:]
            else:
                raise ValueError("Expected a binary operator or ')' after formula in parentheses.")

        if self.is_predicate(t):
            return ("PRED", t), tokens[1:]

        raise ValueError(f"Unrecognized token: {t}")

    def formula_to_string(self, tree):
        t = tree[0]
        if t == "PRED":
            return tree[1]
        elif t == "NOT":
            return f"¬ {self.formula_to_string(tree[1])}"
        elif t == "BINOP":
            return f"({self.formula_to_string(tree[2])} {tree[1]} {self.formula_to_string(tree[3])})"
        return "?"

    def is_predicate(self, token):
        return bool(self.predicate_regex.match(token))

    def is_binary_op(self, token):
        return token in ["∧", "∨", "→"]

    def evaluate_formula(self, formula, values):
        if formula[0] == "PRED":
            return values[formula[1]]
        elif formula[0] == "NOT":
            return not self.evaluate_formula(formula[1], values)
        elif formula[0] == "BINOP":
            left = self.evaluate_formula(formula[2], values)
            right = self.evaluate_formula(formula[3], values)
            if formula[1] == "∧":
                return left and right
            elif formula[1] == "∨":
                return left or right
            elif formula[1] == "→":
                return not left or right

    def generate_truth_table(self, formula):
        variables = set()
        self.collect_variables(formula, variables)
        variables = sorted(variables)
        combinations = list(itertools.product([False, True], repeat=len(variables)))

        print(f"{' | '.join(variables)} | Result")
        print("-" * (len(variables) * 4 + 9))
        for combo in combinations:
            values = {var: val for var, val in zip(variables, combo)}
            result = self.evaluate_formula(formula, values)
            row = ' | '.join(str(values[var]) for var in variables)
            print(f"{row} | {result}")

    def collect_variables(self, formula, variables):
        if formula[0] == "PRED":
            variables.add(formula[1])
        elif formula[0] == "NOT":
            self.collect_variables(formula[1], variables)
        elif formula[0] == "BINOP":
            self.collect_variables(formula[2], variables)
            self.collect_variables(formula[3], variables)

