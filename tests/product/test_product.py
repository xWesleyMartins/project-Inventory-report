from inventory_report.inventory.product import Product


def test_cria_produto():
    newProduct = Product(
        541,
        "Void Pro",
        "corsair",
        "15/12/2022",
        "15/12/2032",
        "n2n23n3n54n5n1n1n",
        "em caixa lacrada a vacuo",
    )

    assert newProduct.id == 541

    assert newProduct.nome_do_produto == "Void Pro"
    assert newProduct.nome_da_empresa == "corsair"
    assert newProduct.data_de_fabricacao == "15/12/2022"
    assert newProduct.data_de_validade == "15/12/2032"
    assert newProduct.numero_de_serie == "n2n23n3n54n5n1n1n"
    assert newProduct.instrucoes_de_armazenamento == "em caixa lacrada a vacuo"
