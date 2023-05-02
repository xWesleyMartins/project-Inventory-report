import xmltodict
from inventory_report.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        try:
            with open(path) as file:
                data = file.read()
                return [
                    row for row in xmltodict.parse(data)["dataset"]["record"]
                ]
        except ValueError:
            raise ValueError("Arquivo inválido")
