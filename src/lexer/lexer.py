import re

class Lexer:
    """
    Goes through the text and turns text content into tokens
    for the parser to consume.
    """
    # Python allows named capturing groups, such as (?P<{name}>{pattern})
    # Patterns will be matched from top -> down
    patterns = [
        r"(?P<QUIZ_OPEN><quiz>)",
        r"(?P<QUIZ_CLOSE></quiz>)",
        r"(?P<TITLE_OPEN><title>)",
        r"(?P<TITLE_CLOSE></title>)",
        r"(?P<QUESTION_OPEN><question>)",
        r"(?P<QUESTION_CLOSE></question>)",
        r"(?P<TEXT_OPEN><text>)",
        r"(?P<TEXT_CLOSE></text>)",
        r"(?P<OPTION_OPEN><option>)",
        r'(?P<OPTION_OPEN_CORRECT><option correct="true">)',
        r"(?P<OPTION_CLOSE></option>)",
        r"(?P<WHITE_SPACE>\s+)",
        # This looks for any characters other than a '<', which captures text until it hits a '<'.
        # TODO fix trailing whitespace being captured.
        r"(?P<TEXT_CONTENT>[^<]+)",
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
