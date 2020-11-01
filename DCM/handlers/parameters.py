import json
from json import JSONDecodeError
from typing import Dict, List

from PyQt5.QtWidgets import QMessageBox, QTableWidget

PARAMETERS_FILE_PATH = "parameters.json"


# This class handles the parameters for the DCM
class ParametersHandler:
    table: QTableWidget
    params_per_mode: Dict[str, List[str]]
    default_params_store: Dict[str, str]
    units: Dict[str, str]
    params_store: Dict[str, str]

    def __init__(self, table: QTableWidget):
        print("Parameters handler init")
        self.table = table

        # Create dictionary of parameters per pacing mode
        self.params_per_mode = {
            'AOO': ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width"],
            'AAI': ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width", "ARP"],
            'VOO': ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width"],
            'VVI': ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width", "VRP"]}

        # Keys are the parameter name, values are the param value or param units respectively
        self.default_params_store = {}
        self.units = {}

        # Get GUI default param values from table, so that we're not hard-coding values multiple times. Param values
        # in column 0, units in column 1.
        for row in range(table.rowCount()):
            key = table.verticalHeaderItem(row).text()
            self.default_params_store[key] = table.item(row, 0).text()
            self.units[key] = table.item(row, 1).text()

        # Try and optionally load existing parameters from file and update GUI with those saved values
        try:
            with open(PARAMETERS_FILE_PATH, mode='r') as f:
                self.params_store = json.load(f)
                self.update_params_gui()
        except (FileNotFoundError, JSONDecodeError):
            self.params_store = self.default_params_store

    # When confirm is clicked, update param store and write the values to file
    def confirm(self) -> None:
        self.params_store = {self.table.verticalHeaderItem(row).text(): self.table.item(row, 0).text() for row in
                             range(self.table.rowCount())}
        self.update_params_file()

    # When reset is clicked, prompt user if they're sure, and optionally load GUI defaults and update file and GUI
    def reset(self) -> None:
        qm = QMessageBox()
        response = QMessageBox.question(qm, "Parameters", "Are you sure you want to reset all the values?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            self.params_store = self.default_params_store
            self.update_params_file()
            self.update_params_gui()

    # Write params store to file, creating a new one if it doesn't exist
    def update_params_file(self) -> None:
        with open(PARAMETERS_FILE_PATH, mode='w+') as f:
            json.dump(self.params_store, f)

    # Update the parameters GUI table with the values from the params store
    def update_params_gui(self) -> None:
        for row in range(self.table.rowCount()):
            self.table.item(row, 0).setText(self.params_store[self.table.verticalHeaderItem(row).text()])

    # Return a list of parameters with the names, values and units for the specified pacing mode
    def filter_params(self, pacing_mode: str) -> Dict[str, str]:
        mode_params = {key: f"{self.params_store[key]}{self.units[key]}" for key in self.params_per_mode[pacing_mode]}
        mode_params["Pacing Mode"] = pacing_mode
        return mode_params
