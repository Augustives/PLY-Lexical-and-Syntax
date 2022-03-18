PYTHON:=
	ifeq ($(OS),Windows_NT)
		PYTHON = python
	else
		PYTHON = python3
	endif

# make lexer code_path=./code_example.lcc
lexer:
	$(PYTHON) lexer.py --code_path $(code_path)

# make parser code_path=./code_example.lcc
parser:
	$(PYTHON) parser.py --code_path $(code_path)