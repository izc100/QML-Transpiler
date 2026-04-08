import argparse
from src.lexer.lexer import Lexer
from src.generator.serializer import Serializer

def main():
    parser = argparse.ArgumentParser(description="Convert QML file to JSON")
    parser.add_argument("input_file", help="Path to the QML input file")
    parser.add_argument(
        "output_file",
        nargs="?",  # Makes it optional
        help="Path to the JSON output file (optional, defaults to output.json)"
    )
    args = parser.parse_args()
    output_file = args.output_file or "output.json"

    # Read input QML file
    with open(args.input_file, "r", encoding="utf-8") as f:
        qml_content = f.read()

    # Lexical analysis
    lexer = Lexer(qml_content)
    tokens = lexer.scan()

    # Parsing and serialization
    serializer = Serializer(tokens)
    serializer.write_json(output_file)
    print(f"Successfully converted {args.input_file} to {output_file}")

if __name__ == "__main__":
    main()