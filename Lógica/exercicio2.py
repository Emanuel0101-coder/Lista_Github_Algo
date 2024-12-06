"""
Três jesuítas e três canibais precisam atravessar um rio. No entanto dispõem apenas de um barco com capacidade para duas pessoas. 
Por medida de segurança não se permite que em alguma das margens do rio a quantidade de jesuítas seja inferior 
à quantidade de canibais. 
Qual a sequência de viagens necessárias para a travessia do rio com segurança para os jesuítas?
"""

#Resposta
"""
1 -Primeira viagem: Dois canibais atravessam o rio.
Margem Inicial: 3 jesuítas e 1 canibal.
Margem Final: 2 canibais.

2 -Segunda viagem: Um canibal retorna com o barco.
Margem Inicial: 3 jesuítas e 2 canibais.
Margem Final: 1 canibal.

3 -Terceira viagem: Dois canibais atravessam novamente.
Margem Inicial: 3 jesuítas.
Margem Final: 3 canibais.

4 -Quarta viagem: Um canibal retorna com o barco.
Margem Inicial: 3 jesuítas e 1 canibal.
Margem Final: 2 canibais.

5 -Quinta viagem: Dois jesuítas atravessam o rio.
Margem Inicial: 1 jesuíta e 1 canibal.
Margem Final: 2 jesuítas e 2 canibais.

6 -Sexta viagem: Um jesuíta e um canibal retornam.
Margem Inicial: 2 jesuítas e 2 canibais.
Margem Final: 1 jesuíta e 1 canibal.

7 -Sétima viagem: Dois jesuítas atravessam novamente.
Margem Inicial: 1 canibal.
Margem Final: 3 jesuítas e 2 canibais.

8 -Oitava viagem: Um canibal retorna com o barco.
Margem Inicial: 1 canibal.
Margem Final: 3 jesuítas e 1 canibal.

9 -Nona viagem: Os dois canibais restantes atravessam o rio.
Margem Inicial: 0.
Margem Final: 3 jesuítas e 3 canibais.
"""

