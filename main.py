import argparse
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.generator.serializer import Serializer

def main():
    parser = argparse.ArgumentParser(description="Convert QML file to JSON")
    parser.add_argument("input_file", help="Path to the QML input file")
    default_output = "output.json"
    parser.add_argument(
        "output_file",
        nargs="?",  # Makes it optional
        default=default_output,
        help="Path to the JSON output file (optional, prints to stdout if missing)"
    )
    args = parser.parse_args()

    # Read input QML file
    with open(args.input_file, "r", encoding="utf-8") as f:
        qml_content = f.read()

    # Lexical analysis
    lexer = Lexer(qml_content)
    tokens = lexer.scan()

    # Parsing and serialization
    serializer = Serializer(tokens)
    if args.output_file:
        serializer.write_json(args.output_file)
        print(f"Successfully converted {args.input_file} to {args.output_file}")
    else:
        serializer.write_json(args.output_file)
        print(f"Successfully converted {args.input_file} to {default_output}")

if __name__ == "__main__":
    main()