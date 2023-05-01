from datetime import date, datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):
        earliest_date = list(
            map(
                lambda fab_date: fab_date["data_de_fabricacao"],
                products,
            )
        )

        current_date = date.today()

        valid_dates = [
            valid_date["data_de_validade"]
            for valid_date in products
            if datetime.fromisoformat(valid_date["data_de_validade"]).date()
            >= current_date
        ]
        closest_date = (
            min(
                valid_dates,
                key=lambda x: abs(
                    datetime.fromisoformat(x).date() - current_date
                ),
            )
            if valid_dates
            else None
        )

        companies = Counter(company["nome_da_empresa"] for company in products)

        return (
            f"Data de fabricação mais antiga: {min(earliest_date)}"
            f"Data de validade mais próxima: {closest_date}"
            f"Empresa com mais produtos: {companies.most_common(1)[0][0]}"
        )
