import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        try:
            with open(path, encoding="utf-8") as file:
                content = json.load(file)
                return list(content)
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
