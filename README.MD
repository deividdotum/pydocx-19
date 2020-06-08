# PyDOCX-19

Projeto com finalidade de ler um diretorio com as fichas sobre covid-19 da região e normalizalas para um formato do tipo JSON



## Install

```
$ pip install docx2txt
$ git clone https://github.com/deividdotum/pydocx-19.git
```
## Configuração

- O script le todos os arquivos presentes na pasta /assets que deve ser criada na raiz do projeto
- O mapeamento de como deve ser extraido os dados esta presente do `schema.py` onde o mesmo ira respeitar a estrutura para gerar o json
- O retorno sera gravado em `output.json`

## Rodando aplicação

```
python3 main.py
```
