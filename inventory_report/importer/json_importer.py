import json
from inventory_report.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        try:
            with open(path) as file:
                data = file.read()
                return json.loads(data)
        except ValueError:
            raise ValueError("Arquivo inválido")
