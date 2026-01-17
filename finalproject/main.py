# FinalProject - A file management application
# Copyright (C) 2024 Samantha Ann Erickson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from PyQt6.QtCore import Qt
from finalproject.actionControllerClass import ActionController
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QCheckBox, QComboBox, QMessageBox, QScrollArea, QToolButton)
from finalproject.fileManagerClass import extensions, categories

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        self.init_UI()
        self.controller = ActionController()
        self.selectedGroups = set()

    def init_UI(self):
        layout = QVBoxLayout()

        self.sourceLabel = QLabel("Source Directory:")
        self.sourceInput = QLineEdit()
        self.sourceBrowse = QPushButton("Browse")
        self.sourceBrowse.clicked.connect(self.select_source)
        
        srcLayout = QHBoxLayout()
        srcLayout.addWidget(self.sourceLabel)
        srcLayout.addWidget(self.sourceInput)
        srcLayout.addWidget(self.sourceBrowse)

        self.destLabel = QLabel("Destination Directory:")
        self.destInput = QLineEdit()
        self.destBrowse = QPushButton("Browse")
        self.destBrowse.clicked.connect(self.select_destination)
        
        destLayout = QHBoxLayout()
        destLayout.addWidget(self.destLabel)
        destLayout.addWidget(self.destInput)
        destLayout.addWidget(self.destBrowse)

        self.fileLabel = QLabel("New File Name Prefix:")
        self.fileInput = QLineEdit()
        self.folderLabel = QLabel("New Folder Name:")
        self.folderInput = QLineEdit()
        self.filetypeLabel = QLabel("Select File Types:")
        self.checkboxes = []

        scrollArea = QScrollArea()
        checkboxWidget = QWidget()
        checkboxLayout = QVBoxLayout()
        
        for ext in extensions.keys():
            checkbox = QCheckBox(ext)
            self.checkboxes.append(checkbox)
            checkboxLayout.addWidget(checkbox)
       
        checkboxWidget.setLayout(checkboxLayout)
        scrollArea.setWidget(checkboxWidget)
        scrollArea.setWidgetResizable(True)
        scrollArea.setFixedHeight(200)
        button_layout = QHBoxLayout()
        
        for category in categories.keys():
            button = QToolButton()
            button.setText(category)
            button.setCheckable(True)
            button.toggled.connect(lambda checked, c=category: self.toggle_category(checked, c))
            button_layout.addWidget(button)

        self.actionLabel = QLabel("Select Action:")
        self.actionDropdown = QComboBox()
        self.actionDropdown.addItems([
            "Copy Only", "Rename Only", "Sort Only", "Copy & Rename",
            "Copy & Sort", "Rename & Sort", "Copy & Rename & Sort"])
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_action)

        layout.addLayout(srcLayout)
        layout.addLayout(destLayout)
        layout.addWidget(self.fileLabel)
        layout.addWidget(self.fileInput)
        layout.addWidget(self.folderLabel)
        layout.addWidget(self.folderInput)
        layout.addWidget(self.filetypeLabel)
        layout.addWidget(scrollArea)
        layout.addLayout(button_layout)
        layout.addWidget(self.actionLabel)
        layout.addWidget(self.actionDropdown)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def select_source(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        if directory:
            self.sourceInput.setText(directory)

    def select_destination(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Destination Directory")
        if directory:
            self.destInput.setText(directory)

    def toggle_category(self, checked, category):
        if checked:
            self.selectedGroups.add(category)
            selectedExtensions = categories[category]
            
            for checkbox in self.checkboxes:
                if checkbox.text() in selectedExtensions:
                    checkbox.setChecked(True)
        else:
            self.selectedGroups.remove(category)
            selectedExtensions = categories[category]
            
            for checkbox in self.checkboxes:
                if checkbox.text() in selectedExtensions:
                    checkbox.setChecked(False)

    def run_action(self):
        source = self.sourceInput.text()
        destination = self.destInput.text()
        filePrefix = self.fileInput.text()
        newFolderName = self.folderInput.text().strip()
        selectedExtensions = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        action = self.actionDropdown.currentText()

        if not source or not destination:
            QMessageBox.warning(self, "Error", "Please select both source and destination directories.")
            return

        if not newFolderName:
            QMessageBox.warning(self, "Error", "Please provide a name for the new folder.")
            return

        self.controller.execute_action(action, source, destination, selectedExtensions, filePrefix, newFolderName)
        QMessageBox.information(self, "Success", f"Action '{action}' completed successfully.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
