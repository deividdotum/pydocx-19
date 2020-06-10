# PyDOCX-19 🐍 + 📂

Projeto com finalidade de ler um diretorio com as fichas sobre covid-19 da região e normalizalas para um formato do tipo JSON

## Oque o script faz

- O script le todos os arquivos presentes na pasta /assets que deve ser criada na raiz do projeto
- O mapeamento de como deve ser extraido os dados esta presente do `schema.py` onde o mesmo ira respeitar a estrutura para gerar o json
- O retorno sera gravado em `output.json`

## Rodando Aplicação

### 💻 Em seu PC

```shell
$ git clone https://github.com/deividdotum/pydocx-19.git
$ pip3 install -r requirements.txt
$ pip3 install pandas # Não funcionou para o raspibian
$ python3 app/src/main.py
```
> **Atenção** pode ser que no Arm (raspbarry...) não de para instalar o pandas entao tu faz assim `apt-get install python3-pandas`

### 🐋 Docker

```shell
# Construir
$ docker build -t pydocx-19 .

# Rodar
$ docker run --rm -v $(pwd)/app:/src/pydocx-19 pydocx-19

# Modo interativo
$ docker run -it --rm -v $(pwd)/app:/src/pydocx-19 pydocx-19 /bin/bash
```

### 🫐 Raspbarry PI (Docker + Raspbian)

- No caso e o msm passo que esta na sessão Docker mas com as imagens em _arm32v7_
pode ver la no `Dockerfile` que esta comentado, ai so descomentar e ser feliz



