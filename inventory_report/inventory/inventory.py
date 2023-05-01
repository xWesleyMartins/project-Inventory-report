from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import csv
import json
import xmltodict


def read_csv(path):
    try:
        with open(path) as file:
            data = csv.DictReader(file)
            return [row for row in data]
    except FileNotFoundError:
        print(f"{path} Not Found")


def read_json(path):
    try:
        with open(path) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"{path} Not Found")


def read_xml(path):
    try:
        with open(path) as file:
            data = xmltodict.parse(file.read())["dataset"]["record"]
            return data
    except FileNotFoundError:
        print(f"{path} Not Found")


def read_file(path):
    if path.endswith(".csv"):
        return read_csv(path)
    elif path.endswith(".json"):
        return read_json(path)
    elif path.endswith(".xml"):
        return read_xml(path)


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        data = read_file(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
