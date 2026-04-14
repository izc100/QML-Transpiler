# QML Transpiler — Quiz Markup Language

A front-end compiler (transpiler) for a custom Quiz Markup Language (QML). Educators can write quizzes in a simple, human-readable format; the transpiler validates syntax and outputs structured JSON for downstream apps or storage.

## Project Overview

- **Input:** `.quiz` files (tag-based, XML-like syntax)
- **Output:** JSON
- **Pipeline:** Lexer → Parser → AST → Serializer

## Setup

```bash
# Clone (if collaborating remotely)
git clone https://github.com/izc100/QML-Transpiler.git
cd QML-Transpiler

# Run from repo root
python main.py sample/midterm.quiz
# Windows launcher alternative
py main.py sample/midterm.quiz

# Alternatively, you can specify the destination file
python main.py sample/midterm.quiz output.json
py main.py sample/midterm.quiz output.json
```

## Tests

1. Install pytest: `pip install pytest` (or `py -m pip install pytest` on Windows).
2. Run tests from the project root: `pytest` (or `py -m pytest` on Windows).

## Milestones

### Lexer

The Lexer was completed on 3/12/2026 by Brandon Hoggatt. It follows the suggestions
in the instructions and uses named capturing groups with a regex pattern for each token. It then combines
all of these patterns into one master pattern, and parses the entire string, creating match objects for 
each match. Those match objects can then be iterated over to extract the tokens, and returned to the parser.

### Parser

The Parser was completed by Andrew Benyacko as a recursive-descent parser that consumes lexer tokens and
builds a nested quiz data structure. It includes descriptive syntax errors when required structures are
missing (for example, missing tags or too few options in a question).

### Generator

The Serializer was completed on 3/28/26 by Elijah Reyna, along with serializer tests.
It uses the json library to dump the AST into a file or string.

## Development Log

See [docs/DEVELOPMENT_LOG.md](docs/DEVELOPMENT_LOG.md).
