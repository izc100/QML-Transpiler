# QML Transpiler — Quiz Markup Language

A front-end compiler (transpiler) for a custom Quiz Markup Language (QML). Educators write quizzes in simple, human-readable QML; the transpiler validates syntax and outputs structured JSON or YAML for web apps or databases.(For our case JSON)

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

# Alternatively, you can specify the destination file
python main.py sample/midterm.quiz output.json
```

## Tests

To run tests and avoid module import issues with the PYTHON_PATH:
1. Install pytest by running `pip install pytest`
2. Run `pytest` from the root directory to execute tests.

## Milestones

### Lexer

The Lexer was pending review and completed on 3/12/2026 by Brandon Hoggatt. It follows the suggestions
in the instructions and uses named capturing groups with a regex pattern for each token. It then combines
all of these patterns into one master pattern, and parses the entire string, creating match objects for 
each match. Those match objects can then be iterated over to extract the tokens, and returned to the parser.

### Generator

The Serializer was completed on 3/28/26 by Elijah Reyna, along with some tests, and was waiting for review at this time. 
It uses the json library to dump the AST into a file or string.

## Team Workflow


## Development Log

See [docs/DEVELOPMENT_LOG.md](docs/DEVELOPMENT_LOG.md).
