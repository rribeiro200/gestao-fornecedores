def valida_edicao_fornecedor(fornecedor, dados_edicao):
    mapeamento_campos = {
        'nomeFornecedor': 'nome',
        'cidadeFornecedor': 'cidade',
        'estadoFornecedor': 'estado',
        'cepFornecedor': 'cep',
        'contatoFornecedor': 'contato',
        'emailFornecedor': 'email',
        'tipoFornecedor': 'tipo'
    }

    for campo, valor_post in dados_edicao.items():
        if campo in mapeamento_campos:
            campo_modelo = mapeamento_campos[campo]
            valor_atual = getattr(fornecedor, campo_modelo)

            if valor_post != valor_atual:
                setattr(fornecedor, campo_modelo, valor_post)

                fornecedor.save()