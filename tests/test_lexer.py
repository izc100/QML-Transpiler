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
        assert tokens == expected_tokens


def test_minimal_success():
    input = """
            <quiz>
              <title> Test Quiz </title>
              <question>
                  <text> Is this valid? </text>
                  <option correct="true"> Yes </option>
                  <option> No </option>
              </question>
            </quiz>
            """

    expected_tokens = [
        ('QUIZ_OPEN', '<quiz>'),
        ('TITLE_OPEN', '<title>'),
        ('TEXT_CONTENT', 'Test Quiz'),
        ('TITLE_CLOSE', '</title>'),
        ('QUESTION_OPEN', '<question>'),
        ('TEXT_OPEN', '<text>'),
        ('TEXT_CONTENT', 'Is this valid?'),
        ('TEXT_CLOSE', '</text>'),
        ('OPTION_OPEN_CORRECT', '<option correct="true">'),
        ('TEXT_CONTENT', 'Yes'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', 'No'),
        ('OPTION_CLOSE', '</option>'),
        ('QUESTION_CLOSE', '</question>'),
        ('QUIZ_CLOSE', '</quiz>')
    ]

    lexer = lex.Lexer(input)
    tokens = lexer.scan()
    assert tokens == expected_tokens


def test_multi_question_success():
    input = """
            <quiz>
                <title> Math Quiz </title>
                <question>
                    <text> What is 2 + 2? </text>
                    <option> 3 </option>
                    <option correct="true"> 4 </option>
                    <option> 5 </option>
                </question>
                <question>
                    <text> Is 5 an even number? </text>
                    <option> Yes </option>
                    <option correct="true"> No </option>
                </question>
            </quiz>
            """
    
    expected_tokens = [
        ('QUIZ_OPEN', '<quiz>'),
        ('TITLE_OPEN', '<title>'),
        ('TEXT_CONTENT', 'Math Quiz'),
        ('TITLE_CLOSE', '</title>'),
        ('QUESTION_OPEN', '<question>'),
        ('TEXT_OPEN', '<text>'),
        ('TEXT_CONTENT', 'What is 2 + 2?'),
        ('TEXT_CLOSE', '</text>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', '3'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN_CORRECT', '<option correct="true">'),
        ('TEXT_CONTENT', '4'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', '5'),
        ('OPTION_CLOSE', '</option>'),
        ('QUESTION_CLOSE', '</question>'),
        ('QUESTION_OPEN', '<question>'),
        ('TEXT_OPEN', '<text>'),
        ('TEXT_CONTENT', 'Is 5 an even number?'),
        ('TEXT_CLOSE', '</text>'),
        ('OPTION_OPEN', '<option>'),
        ('TEXT_CONTENT', 'Yes'),
        ('OPTION_CLOSE', '</option>'),
        ('OPTION_OPEN_CORRECT', '<option correct="true">'),
        ('TEXT_CONTENT', 'No'),
        ('OPTION_CLOSE', '</option>'),
        ('QUESTION_CLOSE', '</question>'),
        ('QUIZ_CLOSE', '</quiz>')
    ]
    
    lexer = lex.Lexer(input)
    tokens = lexer.scan()
    assert tokens == expected_tokens

