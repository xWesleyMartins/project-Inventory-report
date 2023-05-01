from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        simple_report = SimpleReport.generate(products)

        companies = Counter(company["nome_da_empresa"] for company in products)

        products_by_company = "Produtos estocados por empresa:\n"

        for company, count in companies.items():
            products_by_company += f"- {company}: {count}\n"

        return f"{simple_report}\n{products_by_company}"
