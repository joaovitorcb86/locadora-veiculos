"""DONO: P4 - Grupo 2 (Domínio)
TODO: um teste por fórmula + o exemplo numérico completo (R$ 690,00).
Use django.test.SimpleTestCase (sem banco). Cubra: frações de 24 h, tolerância
exata de 60 min, arredondamento HALF_UP, combustível sem crédito.
Rodar: python manage.py test locacao.tests.test_services
"""
from datetime import datetime

from django.test import SimpleTestCase

from locacao import services  # noqa: F401

class DiariasContratadasTests(SimpleTestCase):
    def test_tres_dias_exatos(self):
        retirada = datetime(2026, 10, 10, 9, 0)
        prevista = datetime(2026, 10, 13, 9, 0)
        self.assertEqual(services.diarias_contratadas(retirada, prevista), 3)

    def test_uma_hora_a_mais_conta_outra_diaria(self):
        retirada = datetime(2026, 10, 10, 9, 0)
        prevista = datetime(2026, 10, 13, 10, 0)
        self.assertEqual(services.diarias_contratadas(retirada, prevista), 4)

    def test_minimo_de_uma_diaria(self):
        retirada = datetime(2026, 10, 10, 9, 0)
        prevista = datetime(2026, 10, 10, 11, 0)
        self.assertEqual(services.diarias_contratadas(retirada, prevista), 1)

class FormulasTests(SimpleTestCase):
    def test_exemplo_numerico_690(self):
        self.skipTest("TODO P4")

class ValorPrevistoTests(SimpleTestCase):
    def test_tres_diarias_de_120(self):
        resultado = services.valor_previsto(3, Decimal("120.00"))
        self.assertEqual(resultado, Decimal("360.00"))

    def test_uma_diaria(self):
        resultado = services.valor_previsto(1, Decimal("99.90"))
        self.assertEqual(resultado, Decimal("99.90"))

from datetime import datetime
from decimal import Decimal

from django.test import SimpleTestCase

class DiariasDeAtrasoTests(SimpleTestCase):
    def setUp(self):
        self.prevista = datetime(2026, 10, 13, 9, 0)

    def test_dentro_da_tolerancia(self):
        real = datetime(2026, 10, 13, 9, 30)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 0)

    def test_exatamente_60_minutos_nao_tem_atraso(self):
        real = datetime(2026, 10, 13, 10, 0)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 0)

    def test_um_minuto_alem_da_tolerancia(self):
        real = datetime(2026, 10, 13, 10, 1)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 1)

    def test_exemplo_do_projeto_5_horas(self):
        real = datetime(2026, 10, 13, 14, 0)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 1)

    def test_devolveu_antes_do_prazo(self):
        real = datetime(2026, 10, 12, 9, 0)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 0)

    def test_24h_mais_tolerancia_ainda_e_uma_diaria(self):
        real = datetime(2026, 10, 14, 10, 0)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 1)

    def test_um_minuto_depois_vira_duas_diarias(self):
        real = datetime(2026, 10, 14, 10, 1)
        self.assertEqual(services.diarias_de_atraso(self.prevista, real), 2)