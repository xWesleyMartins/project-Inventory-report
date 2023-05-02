from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path, "r", encoding="utf-8") as file:
                content = csv.DictReader(file)
                return list(content)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
