Database Scheme
===============
 
tbQuestoes
  id:integer
  questao:string
  numresp:integer

tbOpcoes
  id:integer
  questao_id: integer
  opcoes:string

tbGrupos
  id:integer
  tipo: integer/enum ("regiao", "curso", "cursocampus")
  codigo: string/int?
  nome: string
  fase: integer

tbTotais
  grupo_id: integer
  questao_id: integer
  total: integer

tbRespostas
  id:integer
  grupo_id: integer
  questao_id: integer
  opcao_id: integer
  quantidade: integer