#!/bin/python
# Create your views here.
# -*- coding: utf-8 -*-

# Copyright (C) 2012, Diego Rabatone, bamorim
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

class tbQuestoes:

    #id: integer
    #questao: string
    #numresp: integer

class tbOpcoes:
    #id: integer
    #questao_id: integer
    #opcoes: string

class tbGrupos:
    #id: integer
    #tipo: integer/enum ("regiao", "curso", "cursocampus")
    #codigo: string/int?
    #nome: string
    #fase: integer

class tbTotais:
    #grupo_id: integer
    #questao_id: integer
    #total: integer

class tbRespostas:
    #id: integer
    #grupo_id: integer
    #questao_id: integer
    #opcao_id: integer
    #quantidade: integer
