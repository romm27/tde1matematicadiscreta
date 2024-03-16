## Projeto de Faculdade - Matemática Discreta

O programa é capaz de realizar operações de União, Interseção, Diferença e Produto Cartesiano entre quaisquer conjuntos, numéricos ou textuais.

Estas operações e seus conjuntos podem ser carregados de qualquer arquivo .txt no diretório do programa, contanto que este siga as regras de formatação, basta indicá-lo pelo nome no primeiro prompt do programa.

## Criação de arquivos de operação
Segue aqui uma breve descrição de como se montar um arquivo de operações válido.
Desça até o fim do README para um exemplo de arquivo.


1 - No topo do arquivo se define a quantidade de operações para se executar.<br><br>
2 - Em uma nova linha, Para se declarar uma operação, primeiro o operador é escolhido, este consiste das possíveis letras:
<br> - U para União
<br> - I para interseção
<br> - D para Diferença
<br> - C para Produto Cartesiano
<br><br>3 - Na linha seguinte é definido o primeiro conjunto, seus elementos devem ser separados com ','.<br>
<br>4 - O mesmo processo se repete na linha seguinte para gerar o segundo conjunto.
## Exemplo de um arquivo de operações válido

4<br>
U<br>
3, 5, 67, 7<br>
1, 2, 3, 4<br>
I<br>
2, 6, 10, 14, 18<br>
1, 2, 3, 4, 5<br>
D<br>
1, 2, 3, 34<br>
2, 3, 4, 23<br>
C<br>
A, 1, B, 2, C, 2, E<br>
A, B, C, D, E<br>
