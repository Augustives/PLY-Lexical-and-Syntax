# PLY - Lexical and Syntax
# INE5622 - Introdução a Compiladores
## Analisador Léxico
Implementação do Analisador Léxico e Sintático

## Rodar lexer
bash
make lexer code_path=./test_codes/code_exemple.lcc

## Rodar parser
bash
make parser code_path=./test_codes/code_exemple.lcc

## Comandos para testes
make parser code_path=./test_codes/examplo1.lcc
make parser code_path=./test_codes/examplo2.lcc
make parser code_path=./test_codes/examplo3.lcc

make lexer code_path=./test_codes/examplo1.lcc
make lexer code_path=./test_codes/examplo2.lcc
make lexer code_path=./test_codes/examplo3.lcc