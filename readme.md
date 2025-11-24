


# PassGenerator

Um gerador de senhas via linha de comando (CLI) simples e eficiente escrito em Python. Este script permite criar senhas aleatórias com comprimento personalizado e filtros específicos de caracteres.

##  Pré-requisitos
* Clonar repositórios
```bash
git clone https://github.com/MarceloAntonio/GeradorDeSenhaPY
````
* Python 3.x instalado.

##  Como usar

Abra o terminal na pasta do projeto e utilize os comandos abaixo.

### Comandos Básicos

**Ver o menu de ajuda:**
```bash
python Passgenerator.py -h
````

**Gerar senha padrão (Mistura de letras, números e símbolos):**
Substitua `<quantidade>` pelo número de caracteres desejado.

```bash
python Passgenerator.py -q <quantidade>
```

### Filtros de Caracteres

*Nota: Você só pode escolher um filtro por vez.*

**Senha sem caracteres especiais (apenas letras e números):**

```bash
python Passgenerator.py -q 12 -z
```

**Senha apenas com letras (Maiúsculas e Minúsculas):**

```bash
python Passgenerator.py -q 12 -l
```

**Senha apenas com números:**

```bash
python Passgenerator.py -q 12 -n
```

**Senha apenas com caracteres especiais:**

```bash
python Passgenerator.py -q 12 -e
```

##  Bibliotecas Utilizadas

O projeto utiliza apenas bibliotecas nativas do Python, não sendo necessária nenhuma instalação via pip.

  * `argparse`: Para capturar e organizar os argumentos da linha de comando.
  * `random`: Para a geração aleatória dos caracteres.
  * `sys`: Para manipulação de saídas do sistema e tratamento de erros.

##  Fluxo de Funcionamento

1.  **Entrada:** O script recebe a quantidade de caracteres desejada via argumento `-q`.
2.  **Validação:** Verifica se a quantidade informada é um número válido.
3.  **Verificação:** Checa se foi passado mais de um parâmetro de filtro conflitante (ex: pedir apenas números e apenas letras ao mesmo tempo).
4.  **Filtragem:** Com base na escolha do usuário (ou falta dela), o script ajusta a lista de caracteres disponíveis (removendo números, especiais ou letras conforme necessário).
5.  **Geração:** O sistema entra em um loop, selecionando aleatoriamente um tipo de caractere e, em seguida, um caractere específico desse tipo, até atingir o tamanho solicitado.
6.  **Saída:** A lista de caracteres é unida em uma única string e a senha final é exibida no terminal.

-----