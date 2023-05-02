import csv

from inventory_report.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        try:
            with open(path, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                return data
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
