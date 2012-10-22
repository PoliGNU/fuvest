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
from __future__ import unicode_literals
import sqlite
import sys
import re
import os

"""Classes:
    tbQuestoes - questões do questionário sócio econômico
    tbOpcoes - respostas para as questões do questionário
    tbGrupos - Grupos de respostas: 'Região',  'curso' e 'cursocampus'
    tbTotais - totais de respostas por pergunta para cada grupo
    tbRespostas - total de respostas para cada pergunta em cada grupo
    """

"""Classe tbQuestoes
        Classe que mapeia as questões do questionário sócio econômico. Possui os seguintes atributos:
            id: integer
            questao: string
            numresp: integer
    """
class tbQuestoes:
    
    def __init__(self, questao='', numresp=0):
        self.questao = questao
        sefl.numresp = numresp
    #id: integer
    #questao: string
    #numresp: integer

"""Classe tbOpcoes:
        Classe que mapeia as possíveis respostas para cada uma das questões. Possui os seguintes atributos:
            id: integer
            questao_id: integer
            opcoes: string
    """
class tbOpcoes:
    #id: integer
    #questao_id: integer
    #opcoes: string

"""Classe tbGrupos:
        Classe que define as formas de agrupamento das respostas. Por "Região" de inscrição,
            por "Curso", por "Campus" ao qual o curso está atrelado, etc.
    """
class tbGrupos:
    #id: integer
    #tipo: integer/enum ("regiao", "curso", "cursocampus")
    #codigo: string/int?
    #nome: string
    #fase: integer

"""Classe tbTotais:
        Classe que define o total de respostas que uma determinada pergunta obteve em cada
            um dos grupos existentes.
    """
class tbTotais:
    #grupo_id: integer
    #questao_id: integer
    #total: integer

"""Classe tbRespostas:
        Classe que define o total de respostas que uma determinada alternativa (opção) 
            oteve em cada um dos grupos existentes.
    """
class tbRespostas:
    #id: integer
    #grupo_id: integer
    #questao_id: integer
    #opcao_id: integer
    #quantidade: integer
