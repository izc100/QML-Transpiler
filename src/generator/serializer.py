# src/generator/serializer.py

import json

from src.lexer.lexer import Lexer
from src.parser.parser import Parser

class Serializer:
    def __init__(self, tokens):
        self.parser = Parser(tokens)

    def to_json(self, indent=4):
        return json.dumps(self.parser.parse(), indent=indent)

    def write_json(self, output_file, indent=4):
        parsed_data = self.parser.parse()
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=indent)
        return parsed_data