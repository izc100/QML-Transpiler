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

# Run from repo root (once implemented)
python src/main.py sample/midterm.quiz
```

## Milestones

## Team Workflow


## Development Log

See [docs/DEVELOPMENT_LOG.md](docs/DEVELOPMENT_LOG.md).
