# tests/test_serializer.py

import pytest
import json
from src.generator.serializer import Serializer
from src.parser.parser import Parser

# -------------------------
# Helper token sets
# -------------------------

# Minimal quiz
tokens_minimal = [
    ("QUIZ_OPEN", "<quiz>"),
    ("TITLE_OPEN", "<title>"),
    ("TEXT_CONTENT", "Sample Quiz"),
    ("TITLE_CLOSE", "</title>"),
    ("QUESTION_OPEN", "<question>"),
    ("TEXT_OPEN", "<text>"),
    ("TEXT_CONTENT", "What is 2+2?"),
    ("TEXT_CLOSE", "</text>"),
    ("OPTION_OPEN", "<option>"),
    ("TEXT_CONTENT", "3"),
    ("OPTION_CLOSE", "</option>"),
    ("OPTION_OPEN_CORRECT", '<option correct="true">'),
    ("TEXT_CONTENT", "4"),
    ("OPTION_CLOSE", "</option>"),
    ("QUESTION_CLOSE", "</question>"),
    ("QUIZ_CLOSE", "</quiz>")
]

# Multiple questions
tokens_multiple_questions = [
    ("QUIZ_OPEN", "<quiz>"),
    ("TITLE_OPEN", "<title>"),
    ("TEXT_CONTENT", "Multi Q Quiz"),
    ("TITLE_CLOSE", "</title>"),
    
    ("QUESTION_OPEN", "<question>"),
    ("TEXT_OPEN", "<text>"),
    ("TEXT_CONTENT", "Q1?"),
    ("TEXT_CLOSE", "</text>"),
    ("OPTION_OPEN", "<option>"),
    ("TEXT_CONTENT", "A"),
    ("OPTION_CLOSE", "</option>"),
    ("OPTION_OPEN_CORRECT", '<option correct="true">'),
    ("TEXT_CONTENT", "B"),
    ("OPTION_CLOSE", "</option>"),
    ("QUESTION_CLOSE", "</question>"),

    ("QUESTION_OPEN", "<question>"),
    ("TEXT_OPEN", "<text>"),
    ("TEXT_CONTENT", "Q2?"),
    ("TEXT_CLOSE", "</text>"),
    ("OPTION_OPEN", "<option>"),
    ("TEXT_CONTENT", "X"),
    ("OPTION_CLOSE", "</option>"),
    ("OPTION_OPEN_CORRECT", '<option correct="true">'),
    ("TEXT_CONTENT", "Y"),
    ("OPTION_CLOSE", "</option>"),
    ("QUESTION_CLOSE", "</question>"),

    ("QUIZ_CLOSE", "</quiz>")
]

# Quiz with an empty title (should raise an error)
tokens_empty_title = [
    ("QUIZ_OPEN", "<quiz>"),
    ("TITLE_OPEN", "<title>"),
    ("TEXT_CONTENT", ""),
    ("TITLE_CLOSE", "</title>"),
    ("QUIZ_CLOSE", "</quiz>")
]

# Quiz with missing option text (should raise an error)
tokens_missing_option = [
    ("QUIZ_OPEN", "<quiz>"),
    ("TITLE_OPEN", "<title>"),
    ("TEXT_CONTENT", "Quiz"),
    ("TITLE_CLOSE", "</title>"),
    ("QUESTION_OPEN", "<question>"),
    ("TEXT_OPEN", "<text>"),
    ("TEXT_CONTENT", "Q?"),
    ("TEXT_CLOSE", "</text>"),
    ("OPTION_OPEN", "<option>"),
    ("TEXT_CONTENT", ""),
    ("OPTION_CLOSE", "</option>"),
    ("OPTION_OPEN_CORRECT", '<option correct="true">'),
    ("TEXT_CONTENT", "Correct"),
    ("OPTION_CLOSE", "</option>"),
    ("QUESTION_CLOSE", "</question>"),
    ("QUIZ_CLOSE", "</quiz>")
]

# -------------------------
# Tests
# -------------------------

def test_to_json_minimal():
    serializer = Serializer(tokens_minimal)
    json_str = serializer.to_json()
    data = json.loads(json_str)
    assert data["type"] == "quiz"
    assert data["title"] == "Sample Quiz"
    assert len(data["questions"]) == 1
    assert data["questions"][0]["options"][1]["correct"] is True

def test_write_json_file(tmp_path):
    serializer = Serializer(tokens_minimal)
    output_file = tmp_path / "quiz.json"
    parsed_data = serializer.write_json(output_file)
    assert output_file.exists()
    assert parsed_data["questions"][0]["text"] == "What is 2+2?"

def test_multiple_questions():
    serializer = Serializer(tokens_multiple_questions)
    data = serializer.parser.parse()
    assert data["title"] == "Multi Q Quiz"
    assert len(data["questions"]) == 2
    assert data["questions"][1]["text"] == "Q2?"
    assert data["questions"][1]["options"][1]["correct"] is True

def test_empty_title_raises():
    serializer = Serializer(tokens_empty_title)
    with pytest.raises(SyntaxError, match="Quiz title cannot be empty"):
        serializer.parser.parse()

def test_missing_option_text_raises():
    serializer = Serializer(tokens_missing_option)
    with pytest.raises(SyntaxError, match="Option text cannot be empty"):
        serializer.parser.parse()

def test_json_output_format():
    serializer = Serializer(tokens_multiple_questions)
    json_str = serializer.to_json(indent=2)
    # Ensure output is a JSON string
    assert isinstance(json_str, str)
    # Parse it back and check fields
    data = json.loads(json_str)
    assert data["questions"][0]["options"][0]["text"] == "A"
    assert data["questions"][0]["options"][1]["correct"] is True