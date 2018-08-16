# Teste - Yellow Consult
## Sobre
Aplicação desenvolvida com o intuito de testar a aplicação de lógica de programação. Esta aplicação foi desenvolvida por
> Marcio Fernandes Justino | marciojustino@gmail.com | [GitHub](https://github.com/marciojustino/yellowconsult.git)

## Vocabulário e Vetores de Palavras
1. Leitura dos arquivos enviados via parâmetro em linha de comando (file1.txt e file2.txt);
2. Tratamento do conteúdo do arquivo como caixa baixa (*lowercase*);
3. Quebra de todas as palavras contidas no conteúdo do arquivo conforme o seguinte regex, utilizando opção de case insensitive, quebra de linha e acentuação;
```regex
\w[\w|\d]*
```
4. Composição do array de palavras em sequência utilizando o conteúdo de todos os arquivos;
5. Composição do array de palavras isoladas utilizando o conteúdo de todos os arquivos;
6. Composição dos vetores de palavras para cada arquivo, com base nos vocabulários construídos;

## Preparação do Ambiente
A aplicação foi desenvolvida em Python3 utilizando ambiente isolado.

### Requisitos
* Python3

#### Recomendações
Habilitar o ambiente isolado utilizando o virtualenv existente no Python3
```console
foo@bar:~$ python3 -m .venv <environment>
```

## Testando a Aplicação
A aplicação tem como ponto de entrada o arquivo **main.py**. Para executar a aplicação é necessário informar o nome dos arquivos que deseja que sejam utilizados para composição do vocabulário e consequentemente para a composição dos vetores de palavras, como parâmetros de linha de comando:
```console
foo@bar:~$ python main.py <arg1> <arg2> <...>
```

Para utilizar os arquivos pré existentes, utilizar o seguinte comando:
```console
foo@bar:~$ python main.py file1.txt file2.txt
```
