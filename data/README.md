Data
====

Aqui será concentrado tudo relevante aos dados, seja os dados originais em JSON, seja os scripts de data mining ou até mesmo os bancos de dados sqlite já trablhados.

Neste arquivo está descrito a forma de obtenção de dados e as propostas para modelagem do banco de dados, assim como algumas observações importantes.

Data Range
----------

### Ano: 1995-2012
### Fase: 1..4
1. Inscritos
2. Convocados para a segunda fase
3. Matriculados na 1ª chamada
4. Matriculados após a última chamada

### Tipo: 1..3
1. Região
2. Carreira
3. Carreira por Campus(Só nas fases 3 e 4)

Data Sources
------------

**Questões**: http://www.fuvest.br/vest{ano}/js/qase_quest_{ano}.js

**Respostas**: http://www.fuvest.br/vest{ano}/js/qase_grupos_{fase}_{tipo}_{ano}.js

*Obs:* Os dados estão em formato Javascript, não JSON, na verdade é apenas um código JS que é carregado pelo cliente e executado, setando as variáveis necessárias para funcionamento, então, na prática, contêm um JSON.

No arquivo de questões essa variável é setada como:

    var aQst = [...

E no arquivo de respostas:

    var aGrp = [...

Database Scheme
---------------
 
tbQuestoes
* id:integer
* questao:string
* numresp:integer
* ano: integer/datetime

tbOpcoes
* id:integer
* questao_id: integer
* opcoes:string

tbGrupos
* id:integer
* tipo: integer
* codigo: string
* nome: string
* fase: integer

tbTotais
* grupo_id: integer
* questao_id: integer
* total: integer

tbRespostas
* id:integer
* grupo_id: integer
* questao_id: integer
* opcao_id: integer
* quantidade: integer