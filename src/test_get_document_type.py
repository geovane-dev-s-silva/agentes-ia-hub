"""
Módulo: test_get_document_type.py
Responsável: Geovane Silva
Função: Testes unitários para get_document_type()

Casos de Teste Adicionais:
- Testes de priorização (múltiplas palavras-chave)
- Cenários de conflito entre tipos
"""

import unittest
from get_document_type import get_document_type

class TestGetDocumentType(unittest.TestCase):

    def test_nota_fiscal_positive(self):
        self.assertEqual(get_document_type("NF_12345.pdf"), "nota_fiscal")
        self.assertEqual(get_document_type("NFE_67890.xml"), "nota_fiscal")
        self.assertEqual(get_document_type("nota_fiscal_servico.pdf"), "nota_fiscal")
        self.assertEqual(get_document_type("NOTA_FISCAL_PRODUTO.PDF"), "nota_fiscal")
        self.assertEqual(get_document_type("invoice_123.pdf"), "nota_fiscal")

    def test_boleto_positive(self):
        self.assertEqual(get_document_type("Boleto_XPTO.jpg"), "boleto")
        self.assertEqual(get_document_type("BLT_ABC.png"), "boleto")
        self.assertEqual(get_document_type("pagamento_conta.pdf"), "boleto")

    def test_desconhecido_negative(self):
        self.assertEqual(get_document_type("Documento.pdf"), "desconhecido")
        self.assertEqual(get_document_type("relatorio_mensal.docx"), "desconhecido")
        self.assertEqual(get_document_type("imagem.jpeg"), "desconhecido")
        self.assertEqual(get_document_type("arquivo_sem_extensao"), "desconhecido")
        self.assertEqual(get_document_type("outro_documento_qualquer.txt"), "desconhecido")

    def test_case_insensitivity(self):
        self.assertEqual(get_document_type("nf_MAIUSCULA.pdf"), "nota_fiscal")
        self.assertEqual(get_document_type("BOLETO_minuscula.pdf"), "boleto")
        self.assertEqual(get_document_type("NoTaFiScAl.pdf"), "nota_fiscal")

    def test_special_characters(self):
        self.assertEqual(get_document_type("NF-123_abc.pdf"), "nota_fiscal")
        self.assertEqual(get_document_type("Boleto (01-2023).pdf"), "boleto")
        self.assertEqual(get_document_type("nota fiscal com espaco.pdf"), "nota_fiscal")

    def test_recibo_positive(self):
        self.assertEqual(get_document_type("Recibo_2023.pdf"), "recibo")
        self.assertEqual(get_document_type("RCB_001.jpg"), "recibo")
        self.assertEqual(get_document_type("comprovante_pagamento.png"), "recibo")

    def test_cte_positive(self):
        self.assertEqual(get_document_type("CTE_123456.xml"), "cte")
        self.assertEqual(get_document_type("conhecimento_transporte.pdf"), "cte")
        self.assertEqual(get_document_type("CT-e_7890.pdf"), "cte")

    def test_priority_rules(self):
        # Nota Fiscal tem prioridade sobre recibo
        self.assertEqual(get_document_type("recibo_nf_123.pdf"), "nota_fiscal")
        
        # Boleto tem prioridade sobre CTE
        self.assertEqual(get_document_type("boleto_cte_456.pdf"), "boleto")
        
        # Recibo tem prioridade sobre CTE
        self.assertEqual(get_document_type("recibo_transporte.pdf"), "recibo")

    def test_new_types_negative(self):
        self.assertEqual(get_document_type("documento_genérico.pdf"), "desconhecido")
        self.assertEqual(get_document_type("fatura_energia.pdf"), "desconhecido")

if __name__ == '__main__':
    unittest.main()