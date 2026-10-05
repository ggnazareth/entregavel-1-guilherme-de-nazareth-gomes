HARPIA - Processo Seletivo: Entregável 1

NOME PARTICIPANTE: 
GUILHERME DE NAZARETH GOMES

OBJETIVO: 
O projeto tem como objetivo verificar se um robô tem bateria suficiente para realizar uma missão.

FUNCIONAMENTO DO PROJETO: 
Menu - Pequena função com "prints" de explicação pro usuário.

Entradas do Usuário - O programa solicita ao usuário os dados de bateria, duração da missão e consumo por minuto. O código trata as entradas do usuário para garantir bom funcionamento, e conversão em float (Cada uma das entradas do usuário tem uma respectiva função). São criadas variáveis e a elas são atribuídas os valores dessas funções iniciais para não ter de chamar a função constantemente. 

Verificação de Valores Válidos - Para garantir que o código não rode com valores falsos, existe uma condicional if para checar valores inválidos.

Cálculo e Saídas do Programa - São calculados valores como consumo total e bateria restante, e com base na condicional é printada na tela a resposta da pergunta "A missão pode acontecer?" e outros valores.

Função main - Criação da main para evitar variáveis globais e reorganizar o código, para que a parte mais relevante dele fique nas primeiras linhas (Facilitando entendimento do código)

COMANDO DE EXECUÇÃO:
Para executar o programa, abra o terminal e certifique-se de estar na pasta principal do repositório. Então, escreva o seguinte comando no terminal:
python3 src/missao.py
E dê "Enter"

EXEMPLO:
Entradas ==> Bateria atual = 90.0 (%); Duração da missão = 10.0 (minutos); Consumo por minuto = 3.0 (%)

A saída no terminal ==> A missão pode ser concluída!
O consumo total foi de: 30.0%
A bateria restante será de: 60.0%

