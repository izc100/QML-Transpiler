import re

class Lexer:
    """
    Goes through the text and turns text content into tokens
    for the parser to consume.
    """
    # Python allows named capturing groups, such as (?P<{name}>{pattern})
    # Patterns will be matched from top -> down
    patterns = [
        # Eat white space first
        r"(?P<WHITE_SPACE>\s+)",

        # Then opening tags
        r"(?P<QUIZ_OPEN><quiz>)",
        r"(?P<TITLE_OPEN><title>)",
        r"(?P<QUESTION_OPEN><question>)",
        r"(?P<TEXT_OPEN><text>)",
        r"(?P<OPTION_OPEN><option>)",
        r'(?P<OPTION_OPEN_CORRECT><option correct="true">)',

        # This captures all characters until a character in [.!?\w] is found, as long as there is a '<' following it.
        r"(?P<TEXT_CONTENT>.*?[.!?\w])(?=\s*<)",

        # Closing tags
        r"(?P<TEXT_CLOSE></text>)",
        r"(?P<OPTION_CLOSE></option>)",
        r"(?P<QUESTION_CLOSE></question>)",
        r"(?P<TITLE_CLOSE></title>)",
        r"(?P<QUIZ_CLOSE></quiz>)",

        # Mismatch
        r"(?P<MISMATCH>.)"
    ]


    def __init__(self, code):
        """
        Default constructor
        """
        self.code = code
        self.tokens: list[tuple[str, str]] = []


    def scan(self):
        """
        Combines patterns into a master pattern, and searches a string
        for matches within the master pattern. It will turn these into tokens
        and return a list[tuple[str, str]] where the first index is the token
        type, and the second index is the token's value.

        :Return: tokens - list[tuple[str, str]]
        """

        combined_patterns = "|".join(self.patterns)

        # re.finditer iterates through a string and finds all of the matches
        for token in re.finditer(combined_patterns, self.code):
            token_type = token.lastgroup or ""
            matched_text = token.group()
            
            # Ignore Whitespace
            if token_type == 'WHITE_SPACE':
                continue
            elif token_type == "MISMATCH":
                raise RuntimeError(f'Unexpected character {matched_text}')
            
            # Add the identified token to our list
            self.tokens.append((token_type, matched_text))
        
        return self.tokens
