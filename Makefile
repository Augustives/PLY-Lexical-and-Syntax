PYTHON :=
	ifeq ($(OS),Windows_NT)
		PYTHON = python
	else
		PYTHON = python3
	endif

# make lexer code_path=./test_codes/code_example.lcc
lexer:
	$(PYTHON) lexer.py --code_path $(code_path)

# make parser code_path=./test_codes/code_example.lcc
parser:
	$(PYTHON) parser.py --code_path $(code_path)