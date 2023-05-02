import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    importer_dict = {
        ".csv": CsvImporter,
        ".json": JsonImporter,
        ".xml": XmlImporter,
    }

    file_path = sys.argv[1]
    file_extension = file_path[file_path.rfind("."):]

    if file_extension not in importer_dict:
        print(f"Extensão inválida: {file_extension}", file=sys.stderr)
        return

    importer_class = importer_dict[file_extension]
    report = InventoryRefactor(importer_class())

    result = report.import_data(file_path, sys.argv[2])
    sys.stdout.write(result)
