# GNOSES
👨‍💻GNOSES É UM APP DE CHATBOT DE CALCULOS QUE RODA NO CONSOLE DA IDE.

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA)
[![GitHub Repo stars](https://img.shields.io/badge/MEUS-CURSOS-03A9F4?logo=github)](https://github.com/VILHALVA?tab=repositories&q=CURSO&type=public&language=&sort=)

<img src="https://cdn.icon-icons.com/icons2/325/PNG/256/Letter-G-icon_34759.png" align="center" width="280"> <br>

## DESCRIÇÃO:
O aplicativo é um programa em Python que oferece uma variedade de funcionalidades interativas em um menu. Para acessar o menu, o usuário precisa fornecer uma senha correta. Uma vez dentro, o usuário pode escolher entre diferentes opções numeradas (de 1 a 20) para realizar várias tarefas, como entrevistas de emprego simuladas, cálculos matemáticos, conversões, etc. Cada opção representa uma funcionalidade específica e executa uma tarefa diferente. O programa utiliza recursos visuais, como cores e estilos de texto, para tornar a interação mais interessante. Além disso, inclui mensagens de espera e contagens regressivas para criar uma experiência mais envolvente. 

## ATUALIZAÇÕES:
### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%202.2%20--%2020%2F12%2F2023-blueviolet)
* ✅Depois de muito tempo, temos o prazer de anunciar o lançamento desse maravilhoso app para Windows X64. Se trata de um arquivo executável. Basta apenas baixar e executar.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%202.1%20--%2005%2F04%2F2022-blueviolet)
* ✅Além de criar uma função, mudamos o tempo de espera em relação a senha:
    - 🔸Se errar 3 vezes = 60 sgs.
    - 🔸Se errar 6 vezes = 300 sgs.
    - 🔸Se errar +10 vezes = 9999999 sgs.
* 🈯️Refatoramos novamente o código em:
    - 🔸Reduzindo o número de linhas do "print("_" *35)" sendo que criamos uma def para as linhas do relatório e o resultado de todas as funções.
    - 🔸Criamos uma def personalizavel para "⌛️I.PF..." para todas as funções do sistema. Além de deixá-lo mais rápido. Agora o alfa numérico (0%, 25%, 50%, 75%, 100%) será exibido para todos os módulos;
    - 🔸Criamos outra def para a finalização universal de cada função com "⌛️Inderisando...";
* ✅Agora, o programa aceita vírgula no lugar de ponto nos valores reais;
* ✅Imprementamos a validação de dados e tratamento de excessões em todas as funções. O programa não irá processeguir até que o usuário tenha digitado os dados corretamente (int ou float).
* ✅Correções de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%202.0%20--%2023%2F02%2F2022-blueviolet)
* 🈯️Refatoramos todo o script em relação:
  - 🔸"str" foi eliminado de todas as strings; Porém, "int" e "float" continuam para evitar cocatenação;
  - 🔸Através da atualização recente do PYTHON 3.7+; A formatação de todas as strings foram trocadas de: "...{}....format(obj))" para: f"...{obj}..."; 
* ❇️Foi adicionado a senha de autenticação ao inicar. O usuário só poderá usar o script se acertar a senha ("SAMUEL"); Caso erre 3 vezes terá que esperar 10 segundos, se 6, irá esperar 30 seg, se errar +10 vezes terá que esperar 1 minuto para digitar. O script também exibe o tempo de espera em contagem regressiva;
* 🈯️Em relação a animação de "⏳ICF...(00%, 25%, 50%, 75%, 100%)"; Substituímos as 12 linhas (flood) por apenas 3; Utilizando o laço "for" somente:
  - 🔸Ao Iniciar;
  - 🔸Antes do "menu principal";
  - 🔸Depois do "menu principal";
  - 🔸Ao finalizar o programa.
* ✅Em relação a entrevista copt [ 1 ] fizemos grandes melhorias:
  - 🔸Eliminamos a possibilidade das condições darem erro quando o usuario deixa espaços na resposta (".strip()") e/ou em maiusculo ou minusculo(".upper()"); 
  - 🔸Refatoramos a função. Agora as condicionais estão bem estruturas com "in", "or" e "and" para responder palavras chaves de qualquer frase. 
  - 🔸Foi inclementado "else" em todas as condicionais. O script sempre irá responder, independente do que usuário digitou.
  - 🔸Foi adicionado nova pergunta referente ao sexo [M/F]; Caso o usuário erre ao responder ocorrerá loop até acertar;
  - 🔸Adicionamos novamente o "resultado" no "relatório final".  Se o usuário responder na meta e experiência profissional: "Advogado, doutor, juiz e político" ele será aprovado.
* ❇️Novas funções foram adicionados:
  - 🔸[ 11 ] RADAR ELETRÔNICO
  - 🔸[ 12 ] CUSTO DA VIAJEM
  - 🔸[ 13 ] ANO BISSEXTO
  - 🔸[ 14 ] APROVANDO EMPRÉSTIMO
  - 🔸[ 15 ] CONVERSOR NUMÉRICO
  - 🔸[ 16 ] ALISTAMENTO MILITAR
  - 🔸[ 17 ] ANALISADOR TRIÂNGULO
  - 🔸[ 18 ] DETECTOR PALINDROMO
  - 🔸[ 19 ] JOGO ADIVINHAÇÃO
  - 🔸[ 20 ] PROGRESSÃO ARITMÉTICA
* ✅Correções de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.9%20--%2021%2F01%2F2022-blueviolet)
* 🈯️Substituímos as aspas simples (') por aspas duplas (") em todo o código (print/input); 
* ✅Melhoramos o Design do resultado final de todas as funções. Não exibe apenas o resultado, mas também os dados que o usuário digitou;
* ✅O "menu principal"  passou por algumas melhorias:
    - 🔸Melhor Enquadramento;
    - 🔸Melhor Espaçamento;
    - 🔸Fonte em Capital;
    - 🔸Eliminação de Artigos;
    - 🔸Acréscimo de Emojis.
* ❇️Foi adicionado o aviso de "SIMULAÇÃO" ao iniciar a "entrevista copt" ( [ 1 ] );
* ❎Em relação a "entrevista copt" o "resultado final" foi removido do "relatório final";
* ✅Na função [ 2 ], "CALCULAR MÉDIA"; O aluno poderá calcular suas 4 notas da prova (Ao invés de 2 de antigamente);
* ✅Reduzimos o modo lento na transição entre as funções;
* ✅Para dar tempo do usuário analisar os dados (Após o término da função), colocamos o modo lento antes do retorno automático para o "menu principal";
* ❇️Foi incrementado a animação de "⏳ICF...(00%, 25%, 50%, 75%, 100%)" somente:
  - 🔸Ao Iniciar;
  - 🔸Antes do "menu principal";
  - 🔸Depois do "menu principal";
  - 🔸Ao finalizar o programa.
* ❇️Foi adicionado o recado: "⛔️THE END" no fim da execução de cada função;
* ❇️Foi adicionado os devidos créditos na execução do "⛔️FIM DO PROGRAMA"( [ 0 ] );
* ❇️Foram lançados cinco novas funções:
  - 🔸[ 6 ] C.V. TEMPERATURA
  - 🔸[ 7 ] CALCULAR HIPOTENUSA
  - 🔸[ 8 ] CALCULAR SCT
  - 🔸[ 9 ]  PINTAR PAREDE
  - 🔸[ 10 ]  ALUGUEL CARRO
* ✅Correções de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.8%20--%2013%2F01%2F2022-blueviolet)
* ❇️Decidimos colorir o ambiente. Atualmente: A letra está em negrito, o texto em vermelho e o fundo azul. Devido a limitação do nosso dispositivo, o script inteiro está nesse formato; 
* ❇️Implementamos emojis de "reações" no início de todas as mensagens (As do final foram removidas);
* ❇️Adicionamos o símbolo "seta terminal" na próxima linha ("\n>>>") em cada pergunta, para que usuário não se confunda ao responder;
* ❇️Ao iniciar o programa, a primeira mensagem será: "⏳Inicializando..."; E "⏳Carregando..." Após digitar o seu nome;
* ✅Foi lançado auto destruição da mensagem "(⏳I.P.C)"; Após o envio da proxima string (,end="\r");
* ❇️No encerramento do script será enviado o aviso da "Finalização do programa" [0];
* ❇️Foram lançados duas novas funções:
      - 🔸[4] Calcular o Desconto (%)
      - 🔸[5] Calcular o Aumento (%)
* 🈯️Correções de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.7%20--%2008%2F01%2F2022-blueviolet)
* ❇️Foi adicionado o menu de opções com loop (while); Dando a liberdade para o usuário escolher qual o módulo disponível deseja usar; Basta digitar o número que representa a função:
   - 🔸[0] Sair do programa;
   - 🔸[1] Entrevista;
   - 🔸[2] Cálculo da Média;
   - 🔸[3] Calcular o IMC.
* ❇️Agora é obrigatório o usuário digitar o seu nome para usar o script;
* ✅A saudação inicial está mais completa com formatação (nome) antes do menu de opções;
* ✅Reduzimos o tempo de espera do modo lento para 5 segundos;
* ✅O resultado da "entrevista de emprego" foi movido para o "relatório final";
* ❎Algumas coisas precisaram ser removidas:
   - 🔸O termo: "FIM" com fonte Blue (🇫 🇮 🇲);
   - 🔸A formatação de ("-" *30) de "⏳Processando...";
* ✅Correção de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.6%20--%2001%2F01%2F2022-blueviolet)
* 🈯️Foi adicionado o módulo "IMPORTANDO FUNÇÕES" para comandos que não estão disponíveis nativamente no python (Antes da entrevista);
* ❇️Inserimos o modo lento entre as perguntas e na transição dos módulos (time.sleep). Dando tempo para que o usuário leia as respostas do script (Sem Flood);
* ✅Na transição entre módulos temos os espaços (= e -) para uma boa compreensão e estética;
* ❇️Agora o usuário terá que esperar 10 segundos (time.sleep) para receber o resultado (relatório) de cada módulo que for interagir. Sendo assim, o string: "⏳ Processando dados..." sempre irá aparecer;
* ✅Em relação a função "cálculo da média", teve algumas melhorias: Agora o usuário saberá se está de recuperação, se foi reprovado ou aprovado em qualquer exame;
* ❇️Na finalização aparece o termo: "FIM"  com fonte Blue (🇫 🇮 🇲) após a despedida;
* ✅Correção de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.5%20--%2030%2F12%2F2021-blueviolet)
* ❇️Foi adicionado a saudação de abertura ao iniciar; Antes da "Entrevista de emprego";
* 🈯️Em relação ao "relatório final", o comando implícito personalizado (txt ('_')) mudou da nomeclatura: "título" para "relatorio";
* ❇️Foram lançados duas novas perguntas na "Entrevista de Emprego": "Você tem o ensino médio completo?" e "Qual é a sua experiência profissional?". Ambas estão nos conformes do Update API 1.5(Também estão nas variáveis, condições e "relatório final");
* ✅Correção de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.4%20--%2029%2F12%2F2021-blueviolet)
* ✳️Esse projeto passou a se chamar oficialmente: "GNOSES". E o arquivo é nomeado como "SCRIPTS(VERSÃO).PY" ("scripts" para o arquivo e "script" a  API);
* 🈯️Agora os strings das funções estão separadas em blocos, com base em seu módulo e temática;
* 🈯️Foi adicionado um comentário referente a função de cada bloco;
* ✅O "relatório final" foi movido para o 1° módulo (Entrevista de emprego); Antes da função: Média Aritmética;
* ✅Em relação ao "relatório final", foi adicionado linhas entre os dados ('_') e emoji em cada variável;
* ❇️Foi acrescentado a função do cálculo do IMC (Índice de massa corporal);
* ❇️Foi incrementado uma despedida calorosa no fim da execução do script;
* ✅Correção de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.3%20--%2028%2F12%2F2021-blueviolet)
* ❇️Foi acrescentado emojis na interassão com o usuário;
* 🈯️Foi corrigido o problema do excesso de linhas ao mencionar os dados no "relatório final" (+ '{}'format (nome da variável));
* ❇️Foi acrescentado as condicionais (if e else) junto as variáveis (nome, idade, local e emprego). Como em um vídeo game, a resposta do script irá variar conforme a resposta do usuário;
* ❇️Foi acrescentado o cálculo da média aritmética para a nota da prova de Matemática do entrevistado;
* ✅Correção de bugs e pequenas melhorias.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.2%20--%2024%2F12%2F2021-blueviolet)
* 🈯️O script está mais organizado e completo (Pula linha) para facilitar a leitura e as futuras atualizações;
* 🈯️Foi feito a junção de um diálogo (input) junto com as variáveis (=);
* ❇️Foi lançado o "relatório final" após a entrevista; Onde menciona os dados que salvou das variáveis; em conjunto com seus nomes na segunda linha;
* ❎As perguntas: peso e estado civil, foram removidas.
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.1%20--%2022%2F12%2F2021-blueviolet)
* ❇️Foi acrescentado mais perguntas, como: Nome, idade, endereço, peso e estado civil.
* 🈯️Input passa a funcionar com algumas variáveis (Alfa);
![](https://i.imgur.com/waxVImv.png)

### ![GitHub Repo stars](https://img.shields.io/badge/-VERS%C3%83O%201.0%20--%2022%2F12%2F2021-blueviolet)
* 👤Comecei a criar um script que interage com o usuário, como em uma entrevista de emprego. Não quero que esse projeto se limite apenas a isso, mas que alcance outras temáticas (ou até propósitos). Não sei qual o rumo que isso irá tomar; Se será um bot, um app, uma rede social ou um jogo. Por enquanto, esse código só funciona no compilador/interpretador. No futuro próximo, ele será liberado pra todos.
* 🆕Nesta versão o script interage com usuário apenas usando o comando print com as variáveis. Faz perguntas, após a resposta faz outra. Código pequeno, simples mais funcional.

