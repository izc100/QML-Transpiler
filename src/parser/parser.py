import json


class Parser:
    """
    Recursive-descent parser for QML.
    Consumes the token list produced by the lexer and builds
    a nested Python dictionary.
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    # -------------------------
    # Helper methods
    # -------------------------

    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def advance(self):
        token = self.peek()
        if token is not None:
            self.current += 1
        return token

    def expect(self, expected_type):
        token = self.peek()

        if token is None:
            raise SyntaxError(f"Expected {expected_type}, but found end of input")

        token_type, token_value = token

        if token_type != expected_type:
            raise SyntaxError(
                f"Expected {expected_type}, but found {token_type} ({token_value})"
            )

        return self.advance()

    # -------------------------
    # Entry point
    # -------------------------

    def parse(self):
        """
        Parse the full QML document and return a nested dictionary.
        """
        result = self.parse_quiz()

        if self.peek() is not None:
            token_type, token_value = self.peek()
            raise SyntaxError(
                f"Unexpected extra token after </quiz>: {token_type} ({token_value})"
            )

        return result

    # -------------------------
    # Grammar rules
    # -------------------------

    def parse_quiz(self):
        """
        quiz = <quiz> title question { question } </quiz>
        """
        self.expect("QUIZ_OPEN")

        title = self.parse_title()

        questions = [self.parse_question()]
        while self.peek() is not None and self.peek()[0] == "QUESTION_OPEN":
            questions.append(self.parse_question())

        self.expect("QUIZ_CLOSE")

        return {
            "type": "quiz",
            "title": title,
            "questions": questions
        }

    def parse_title(self):
        """
        title = <title> TEXT_CONTENT </title>
        """
        self.expect("TITLE_OPEN")
        title_text = self.expect("TEXT_CONTENT")[1].strip()
        self.expect("TITLE_CLOSE")

        if title_text == "":
            raise SyntaxError("Quiz title cannot be empty")

        return title_text

    def parse_question(self):
        """
        question = <question> qtext option option { option } </question>
        """
        self.expect("QUESTION_OPEN")

        question_text = self.parse_qtext()

        options = [self.parse_option(), self.parse_option()]
        while self.peek() is not None and self.peek()[0] in (
            "OPTION_OPEN",
            "OPTION_OPEN_CORRECT"
        ):
            options.append(self.parse_option())

        self.expect("QUESTION_CLOSE")

        return {
            "type": "question",
            "text": question_text,
            "options": options
        }

    def parse_qtext(self):
        """
        qtext = <text> TEXT_CONTENT </text>
        """
        self.expect("TEXT_OPEN")
        text = self.expect("TEXT_CONTENT")[1].strip()
        self.expect("TEXT_CLOSE")

        if text == "":
            raise SyntaxError("Question text cannot be empty")

        return text

    def parse_option(self):
        """
        option = <option> TEXT_CONTENT </option>
               | <option correct="true"> TEXT_CONTENT </option>
        """
        token = self.peek()

        if token is None:
            raise SyntaxError("Expected option, but found end of input")

        token_type, token_value = token

        if token_type == "OPTION_OPEN":
            self.advance()
            is_correct = False
        elif token_type == "OPTION_OPEN_CORRECT":
            self.advance()
            is_correct = True
        else:
            raise SyntaxError(
                f"Expected OPTION_OPEN or OPTION_OPEN_CORRECT, "
                f"but found {token_type} ({token_value})"
            )

        option_text = self.expect("TEXT_CONTENT")[1].strip()
        self.expect("OPTION_CLOSE")

        if option_text == "":
            raise SyntaxError("Option text cannot be empty")

        return {
            "text": option_text,
            "correct": is_correct
        }

    # -------------------------
    # Optional JSON helpers
    # -------------------------

    def to_json(self, indent=4):
        return json.dumps(self.parse(), indent=indent)

    def write_json(self, output_file, indent=4):
        parsed_data = self.parse()
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=indent)
        return parsed_data