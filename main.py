from lexer import Lexer
from parser import Parser

SIMPLE_EXAMPLE = "(+ 1 2.3)"
COMPLEX_EXAMPLE = "(if (> x (+ 1.33 5.7)) (* x 2) 0)"
SPACES_EXAMPLE = "(defvar x \"hello() 33.23 world\")"

LEXER = Lexer()
PARSER = Parser()

def run_lexer_tests():
    print("Lexer Tests:")

    lexer_simple_example = LEXER.tokenize(SIMPLE_EXAMPLE)
    print(lexer_simple_example)
    assert lexer_simple_example == ['(', '+', '1', '2.3', ')']
    
    lexer_complex_example = LEXER.tokenize(COMPLEX_EXAMPLE)
    print(lexer_complex_example)
    assert lexer_complex_example == ["(", "if", "(", ">", "x", "(", "+", "1.33", "5.7", ")", ")", "(", "*", "x", "2", ")", "0", ")"]

    lexer_example_with_spaces = LEXER.tokenize(SPACES_EXAMPLE)
    print(lexer_example_with_spaces)
    assert lexer_example_with_spaces == ["(", "defvar", "x", "\"hello() 33.23 world\"", ")"]


def run_parser_atomize_tests():
    print("Parser Atomize Tests:")

    parser_atomize_simple_example = PARSER.atomize(LEXER.tokenize(SIMPLE_EXAMPLE))
    print(parser_atomize_simple_example)
    assert parser_atomize_simple_example == ["(", "+", 1, 2.3, ")"]

    parser_atomize_complex_example = PARSER.atomize(LEXER.tokenize(COMPLEX_EXAMPLE))
    print(parser_atomize_complex_example)
    assert parser_atomize_complex_example == ["(", "if", "(", ">", "x", "(", "+", 1.33, 5.7, ")", ")", "(", "*", "x", 2, ")", 0, ")"]

    parser_atomize_example_with_spaces = PARSER.atomize(LEXER.tokenize(SPACES_EXAMPLE))
    print(parser_atomize_example_with_spaces)
    assert parser_atomize_example_with_spaces == ["(", "defvar", "x", "\"hello() 33.23 world\"", ")"]
    

def run_parser_ast_tests():
    print("Parser AST Tests:")
    
    parser_ast_simple_example = PARSER.build_ast(PARSER.atomize(LEXER.tokenize(SIMPLE_EXAMPLE)))
    print(parser_ast_simple_example)
    assert parser_ast_simple_example == ["+", 1, 2.3]

    parser_ast_complex_example = PARSER.build_ast(PARSER.atomize(LEXER.tokenize(COMPLEX_EXAMPLE)))
    print(parser_ast_complex_example)
    assert parser_ast_complex_example == ["if", [">", "x", ["+", 1.33, 5.7]], ["*", "x", 2], 0]

    parser_ast_example_with_spaces = PARSER.build_ast(PARSER.atomize(LEXER.tokenize(SPACES_EXAMPLE)))
    print(parser_ast_example_with_spaces)
    assert parser_ast_example_with_spaces == ["defvar", "x", "\"hello() 33.23 world\""]
    
    
if __name__ == "__main__":
    run_lexer_tests()
    print()

    run_parser_atomize_tests()
    print()

    run_parser_ast_tests()
    print()
