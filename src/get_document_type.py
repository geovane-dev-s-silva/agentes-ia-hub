"""
Módulo: get_document_type.py
Responsável: Geovane Silva
Função: Inferir tipo de documento fiscal baseado no nome do arquivo

Índice de Nomenclaturas:
----------------------------
file_name    : Nome do arquivo fornecido pelo módulo de upload
file_lower   : Versão em minúsculas para case-insensitivity
kw           : Palavra-chave usada na análise do nome do arquivo
nota_fiscal  : Tipo para documentos fiscais (NF-e, NFS-e, etc)
boleto       : Tipo para documentos bancários (boletos)
recibo       : Tipo para recibos diversos
cte          : Tipo para Conhecimento de Transporte Eletrônico
desconhecido : Retorno padrão para tipos não identificados

Lógica de Priorização:
----------------------------
1. Nota Fiscal (maior prioridade)
2. Boleto
3. Recibo
4. CTE
5. Desconhecido (padrão)

Implementacoes:
- Hierarquia de tipos para evitar conflitos
- Novos tipos de documentos (recibo, cte)
- Sistema extensível para novos tipos
"""

def get_document_type(file_name: str) -> str:
    """
    Infer o tipo de documento fiscal com base no nome do arquivo.

    Args:
        file_name (str): O nome do arquivo a ser analisado.

    Returns:
        str: Tipo inferido ('nota_fiscal', 'boleto', 'recibo', 'cte' ou 'desconhecido')
    
    Comportamento esperado:
    - Prioriza tipos na ordem definida (ex: se contém 'nf' e 'recibo', retorna 'nota_fiscal')
    - Case-insensitive
    - Palavras-chave:
        nota_fiscal: ['nf', 'nfe', 'nota', 'fiscal', 'invoice']
        boleto: ['blt', 'boleto', 'pagamento']
        recibo: ['recibo', 'rcb', 'comprovante']
        cte: ['cte', 'conhecimento', 'transporte']
    """
    file_lower = file_name.lower()
    
    # Sistema hierárquico de priorização
    if any(kw in file_lower for kw in ["nf", "nfe", "nota", "fiscal", "invoice"]):
        return "nota_fiscal"
    elif any(kw in file_lower for kw in ["blt", "boleto", "pagamento"]):
        return "boleto"
    elif any(kw in file_lower for kw in ["recibo", "rcb", "comprovante"]):
        return "recibo"
    elif any(kw in file_lower for kw in ["cte", "conhecimento", "transporte"]):
        return "cte"
    else:
        return "desconhecido"