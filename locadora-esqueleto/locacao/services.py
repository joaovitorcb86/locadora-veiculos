"""DONO: P4 - Grupo 2 (Domínio)
Fórmulas de cálculo: funções PURAS (sem banco). Dinheiro sempre Decimal com
quantize(Decimal("0.01"), ROUND_HALF_UP). Nunca float.

TODO: implementar as funções abaixo (escreva o teste primeiro, em tests/test_services.py).

  diarias_contratadas(retirada, devolucao_prevista)
        D = teto((devolucao_prevista - retirada) / 24h), mínimo 1
  valor_previsto(diarias, valor_diaria)                  -> D x diária
  diarias_de_atraso(devolucao_prevista, devolucao_real, tolerancia_min=60)
        Datraso = max(0, teto((real - prevista - 60 min) / 24h))
  valor_multa(diarias_atraso, valor_diaria)              -> Datraso x diária x 1,5
  taxa_combustivel(quartos_saida, quartos_retorno, valor_tanque_cheio)
        C = max(0, saída - retorno) x tanque_cheio / 4   (sem crédito se voltar com mais)
  valor_total(previsto, multa, combustivel)              -> soma (a caução é tratada à parte)
  multa_cancelamento(valor_estimado, retirada_prevista, agora)
        20% do valor estimado se faltar menos de 24 h (RN11), senão zero
  extrato_devolucao(...)   junta tudo para a tela de devolução (prévia)

Meta: o exemplo numérico da documentação dá exatamente R$ 690,00.
  diária 120, caução 500, tanque cheio 300
  retirada 10/10 09:00 (CHEIO) | prevista 13/10 09:00 | real 13/10 14:00 (METADE)
  3 diárias = 360 + multa 180 (1 diária extra x 120 x 1,5) + combustível 150 = 690
"""
from decimal import ROUND_HALF_UP, Decimal  # noqa: F401

import math

TOLERANCIA_ATRASO_MIN = 60
FATOR_MULTA_ATRASO = Decimal("1.5")
PERCENTUAL_MULTA_CANCELAMENTO = Decimal("0.20")


def diarias_contratadas(retirada, devolucao_prevista):
    horas = (devolucao_prevista - retirada).total_seconds() / 3600
    dias = math.ceil(horas / 24)
    return max(1, dias)

def valor_previsto(diarias, valor_diaria):
    total = diarias * valor_diaria
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def diarias_de_atraso(devolucao_prevista, devolucao_real, tolerancia_min=TOLERANCIA_ATRASO_MIN):
    minutos = (devolucao_real - devolucao_prevista).total_seconds() / 60
    minutos_alem_da_tolerancia = minutos - tolerancia_min
    dias = math.ceil(minutos_alem_da_tolerancia / (24 * 60))
    return max(0, dias)


def valor_multa(diarias_atraso, valor_diaria):
    raise NotImplementedError


def taxa_combustivel(quartos_saida, quartos_retorno, valor_tanque_cheio):
    raise NotImplementedError


def valor_total(previsto, multa, combustivel):
    raise NotImplementedError


def multa_cancelamento(valor_estimado, retirada_prevista, agora):
    raise NotImplementedError
