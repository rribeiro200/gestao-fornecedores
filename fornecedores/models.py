from django.db import models

# Constantes
ESTADOS = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

TIPO_CONTATO = (
    ('CPF', 'CPF'),
    ('CNPJ', 'CNPJ'),
)

class Fornecedor(models.Model):
    id_fornecedor = models.BigAutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=ESTADOS) # type:ignore
    cep = models.CharField(max_length=9)
    contato = models.CharField(max_length=20, null=True, blank=True)  # Alterado para CharField e permitido nulo
    email = models.EmailField(null=True, blank=True)  # Permitido nulo
    tipo = models.CharField(max_length=4, choices=TIPO_CONTATO, null=True, blank=True)

    def __str__(self):
        return self.nome