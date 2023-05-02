from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

REPORTS = {
    "simples": SimpleReport.generate,
    "completo": CompleteReport.generate,
}


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        data = self.importer.import_data(path)
        for item in data:
            self.data.append(item)
        if type in REPORTS:
            return f"{REPORTS[type](data)}"

    def __iter__(self):
        return InventoryIterator(self.data)
