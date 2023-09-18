from menu import products


def calculate_tab(lista: list):
    soma = 0
    for consumed_product in lista:
        for product in products:
            if product.get('_id') == consumed_product.get('_id'):
                soma += product.get('price') * consumed_product.get('amount')
    subtotal = {'subtotal': f'${round(soma, 2)}'}
    return subtotal
