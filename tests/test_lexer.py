import src.lexer.lexer as lex

def test_regular_quiz():
    expected_tokens = [
        ('QUIZ_OPEN', '<quiz>'),
        ('TITLE_OPEN', '<title>'),
        ('TEXT_CONTENT', 'Programming Languages Midterm'),
        ('TITLE_CLOSE', '</title>'),
        ('QUESTION_OPEN', '<question>'),
        ('TEXT_OPEN', '<text>'),
        ('TEXT_CONTENT', 'Which programming paradigm is based on mathematical functions?'),
        ('TEXT_CLOSE', '</text>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', 'Imperative'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN_CORRECT', '<option correct="true">'),
        ('TEXT_CONTENT', 'Functional'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', 'Object-Oriented'),
        ('OPTION_CLOSE', '</option>'),
        ('QUESTION_CLOSE', '</question>'),
        ('QUESTION_OPEN', '<question>'),
        ('TEXT_OPEN', '<text>'),
        ('TEXT_CONTENT', 'What is the primary purpose of a lexical analyzer?'),
        ('TEXT_CLOSE', '</text>'),
        ('OPTION_OPEN_CORRECT', '<option correct="true">'),
        ('TEXT_CONTENT', 'To group characters into lexemes and assign tokens.'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', 'To generate machine code.'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', 'To build a parse tree.'),
        ('OPTION_CLOSE', '</option>'),
        ('QUESTION_CLOSE', '</question>'),
        ('QUIZ_CLOSE', '</quiz>')
    ]

    with open("sample/midterm.quiz") as file:
        lexer = lex.Lexer(file.read())
        tokens = lexer.scan()

        for i in range(len(tokens)):
            assert tokens[i][0] == expected_tokens[i][0]
            assert tokens[i][1] == expected_tokens[i][1]

if __name__ == "__main__":
    test_regular_quiz()