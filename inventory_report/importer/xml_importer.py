import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        try:
            with open(path, "r") as file:
                content = xmltodict.parse(file.read())["dataset"]["record"]
                return list(content)
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
