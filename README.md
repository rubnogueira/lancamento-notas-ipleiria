# Lançamento de notas IPLeiria

Script em Python que permite verificar se houve alterações na Unidade Curricular na plataforma eLearning do IPLeiria.

## Preparando o Script

Para correr o script necessita de um sistema com Python instalado.

### Pre requisitos

Necessita de um sistema com Python configurado. Testado em Python 2.7-3.5. Necessita do módulo requests instalado. Para configurar corra o seguinte comando.

```
python -m pip install requests
```

### Configurando os seus dados

Necessita de editar o script Python e alterar as variáveis com o seu username e password.

```
USERNAME = "2171234"
PASSWORD = "qwerty"
WAITING = 10
```

Ao alterar a variável **WAITING**, altera o intervalo de tempo de verificação à plataforma.

### Configurar as suas Unidades Curriculares

Para alterar quais as UCS deseja verificar, basta alterar a variável **UCS** e adicionar uma linha por UC, em que *uc* corresponde ao nome da cadeira e *url* ao link da UC na plataforma eLearning.

```
UCS = [
        {'uc':'SO','url':'https://ead.ipleiria.pt/2017-18/course/view.php?id=3659'},
        {'uc':'P2','url':'https://ead.ipleiria.pt/2017-18/course/view.php?id=3711'},
      ]
```

## Autores

* **Ruben Nogueira** - [rubnogueira](https://github.com/rubnogueira)