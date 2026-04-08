# tests/test_parser.py

import json
import unittest

from src.parser.parser import Parser
from src.lexer.lexer import Lexer


class TestParser(unittest.TestCase):
    def parse_source(self, source_code):
        lexer = Lexer(source_code)
        tokens = lexer.scan()
        parser = Parser(tokens)
        return parser.parse()

    def test_parse_valid_quiz(self):
        source_code = """
<quiz>
    <title> Programming Languages Midterm </title>

    <question>
        <text> Which programming paradigm is based on mathematical functions? </text>
        <option> Imperative </option>
        <option correct="true"> Functional </option>
        <option> Object-Oriented </option>
    </question>

    <question>
        <text> What is the primary purpose of a lexical analyzer? </text>
        <option correct="true"> To group characters into lexemes and assign tokens. </option>
        <option> To generate machine code. </option>
        <option> To build a parse tree. </option>
    </question>
</quiz>
"""
        result = self.parse_source(source_code)

        self.assertEqual(result["type"], "quiz")
        self.assertEqual(result["title"], "Programming Languages Midterm")
        self.assertEqual(len(result["questions"]), 2)

        first_question = result["questions"][0]
        self.assertEqual(first_question["type"], "question")
        self.assertEqual(
            first_question["text"],
            "Which programming paradigm is based on mathematical functions?"
        )
        self.assertEqual(len(first_question["options"]), 3)
        self.assertEqual(first_question["options"][0]["text"], "Imperative")
        self.assertFalse(first_question["options"][0]["correct"])
        self.assertEqual(first_question["options"][1]["text"], "Functional")
        self.assertTrue(first_question["options"][1]["correct"])

    def test_parse_single_question_two_options(self):
        source_code = """
<quiz>
    <title> Simple Quiz </title>
    <question>
        <text> 2 + 2 equals what? </text>
        <option> 3 </option>
        <option correct="true"> 4 </option>
    </question>
</quiz>
"""
        result = self.parse_source(source_code)

        self.assertEqual(result["title"], "Simple Quiz")
        self.assertEqual(len(result["questions"]), 1)
        self.assertEqual(result["questions"][0]["text"], "2 + 2 equals what?")
        self.assertEqual(len(result["questions"][0]["options"]), 2)
        self.assertFalse(result["questions"][0]["options"][0]["correct"])
        self.assertTrue(result["questions"][0]["options"][1]["correct"])

    def test_option_without_correct_defaults_false(self):
        source_code = """
<quiz>
    <title> Default Correct Test </title>
    <question>
        <text> Pick the incorrect default. </text>
        <option> First </option>
        <option> Second </option>
    </question>
</quiz>
"""
        result = self.parse_source(source_code)
        options = result["questions"][0]["options"]

        self.assertFalse(options[0]["correct"])
        self.assertFalse(options[1]["correct"])

    def test_to_json(self):
        source_code = """
<quiz>
    <title> JSON Quiz </title>
    <question>
        <text> Is this JSON-ready? </text>
        <option correct="true"> Yes </option>
        <option> No </option>
    </question>
</quiz>
"""
        lexer = Lexer(source_code)
        tokens = lexer.scan()
        parser = Parser(tokens)

        json_result = parser.to_json()
        parsed_json = json.loads(json_result)

        self.assertEqual(parsed_json["title"], "JSON Quiz")
        self.assertEqual(parsed_json["questions"][0]["text"], "Is this JSON-ready?")
        self.assertTrue(parsed_json["questions"][0]["options"][0]["correct"])

    def test_missing_quiz_close_tag(self):
        source_code = """
<quiz>
    <title> Broken Quiz </title>
    <question>
        <text> Missing closing quiz tag? </text>
        <option> Yes </option>
        <option correct="true"> Definitely </option>
    </question>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        self.assertIn("QUIZ_CLOSE", str(context.exception))

    def test_missing_question_close_tag(self):
        source_code = """
<quiz>
    <title> Broken Question </title>
    <question>
        <text> Missing question end tag? </text>
        <option> Yes </option>
        <option correct="true"> Definitely </option>
</quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        self.assertIn("QUESTION_CLOSE", str(context.exception))

    def test_missing_title(self):
        source_code = """
<quiz>
    <question>
        <text> Where is the title? </text>
        <option> Here </option>
        <option correct="true"> Not here </option>
    </question>
</quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        self.assertIn("TITLE_OPEN", str(context.exception))

    def test_missing_text_block(self):
        source_code = """
<quiz>
    <title> Missing Text Block </title>
    <question>
        <option> A </option>
        <option correct="true"> B </option>
    </question>
</quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        self.assertIn("TEXT_OPEN", str(context.exception))

    def test_only_one_option_should_fail(self):
        source_code = """
<quiz>
    <title> Not Enough Options </title>
    <question>
        <text> Only one option? </text>
        <option correct="true"> One </option>
    </question>
</quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        message = str(context.exception)
        self.assertTrue(
            "OPTION_OPEN" in message or "OPTION_OPEN_CORRECT" in message
        )

    def test_zero_options_should_fail(self):
        source_code = """
<quiz>
    <title> No Options Quiz </title>
    <question>
        <text> Where are the options? </text>
    </question>
</quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        message = str(context.exception)
        self.assertTrue(
            "OPTION_OPEN" in message or "OPTION_OPEN_CORRECT" in message
        )

    def test_empty_title_should_fail(self):
        source_code = """
<quiz>
    <title> </title>
    <question>
        <text> Valid question text </text>
        <option> A </option>
        <option correct="true"> B </option>
    </question>
</quiz>
"""
        with self.assertRaises((SyntaxError, RuntimeError)):
            self.parse_source(source_code)

    def test_empty_question_text_should_fail(self):
        source_code = """
<quiz>
    <title> Empty Question Text </title>
    <question>
        <text> </text>
        <option> A </option>
        <option correct="true"> B </option>
    </question>
</quiz>
"""
        with self.assertRaises((SyntaxError, RuntimeError)):
            self.parse_source(source_code)

    def test_extra_tokens_after_quiz_should_fail(self):
        source_code = """
<quiz>
    <title> Extra Tokens </title>
    <question>
        <text> Valid question? </text>
        <option> A </option>
        <option correct="true"> B </option>
    </question>
</quiz>
<quiz></quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        self.assertIn("Unexpected extra token", str(context.exception))

    def test_invalid_option_location_should_fail(self):
        source_code = """
<quiz>
    <title> Bad Structure </title>
    <option> Wrong place </option>
    <question>
        <text> Valid question text </text>
        <option> A </option>
        <option correct="true"> B </option>
    </question>
</quiz>
"""
        with self.assertRaises(SyntaxError) as context:
            self.parse_source(source_code)

        self.assertIn("QUESTION_OPEN", str(context.exception))

    def test_multiple_questions(self):
        source_code = """
<quiz>
    <title> Multi Question Quiz </title>
    <question>
        <text> First question? </text>
        <option> A </option>
        <option correct="true"> B </option>
    </question>
    <question>
        <text> Second question? </text>
        <option correct="true"> C </option>
        <option> D </option>
        <option> E </option>
    </question>
</quiz>
"""
        result = self.parse_source(source_code)

        self.assertEqual(len(result["questions"]), 2)
        self.assertEqual(result["questions"][0]["text"], "First question?")
        self.assertEqual(result["questions"][1]["text"], "Second question?")
        self.assertEqual(len(result["questions"][1]["options"]), 3)
        self.assertTrue(result["questions"][1]["options"][0]["correct"])
