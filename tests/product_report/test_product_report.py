from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = {
        "id": 1,
        "nome_do_produto": "carne",
        "nome_da_empresa": "FreeBeef",
        "data_de_fabricacao": "2023-01-20",
        "data_de_validade": "2023-06-20",
        "numero_de_serie": "33345456",
        "instrucoes_de_armazenamento": "armazenar em freezer",
    }
    product = Product(**new_product)
    assert product.__dict__ == new_product
