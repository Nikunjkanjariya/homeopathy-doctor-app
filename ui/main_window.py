import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from config.database import init_database
from models.patient import Patient
from ui.patient_dialog import PatientDialog
from ui.consultation_dialog import ConsultationDialog
from ui.prescription_dialog import PrescriptionDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homeopathy Doctor Management System")
        self.setGeometry(100, 100, 1200, 700)
        
        # Initialize database
        init_database()
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Homeopathy Practice Management")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        header_layout.addWidget(title)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)
        
        # Tab Widget
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Tab 1: Patient Management
        self.setup_patient_tab()
        
        # Tab 2: Consultations
        self.setup_consultation_tab()
        
        # Tab 3: Prescriptions
        self.setup_prescription_tab()
        
        self.show()
    
    def setup_patient_tab(self):
        """Setup patient management tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Search section
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search Patient:"))
        self.patient_search = QLineEdit()
        self.patient_search.setPlaceholderText("Enter name or phone...")
        self.patient_search.textChanged.connect(self.search_patients)
        search_layout.addWidget(self.patient_search)
        
        add_patient_btn = QPushButton("Add New Patient")
        add_patient_btn.clicked.connect(self.add_patient)
        search_layout.addWidget(add_patient_btn)
        layout.addLayout(search_layout)
        
        # Patient table
        self.patient_table = QTableWidget()
        self.patient_table.setColumnCount(6)
        self.patient_table.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Email", "Gender", "Actions"])
        self.patient_table.itemSelectionChanged.connect(self.on_patient_selected)
        layout.addWidget(self.patient_table)
        
        # Action buttons
        action_layout = QHBoxLayout()
        edit_btn = QPushButton("Edit Patient")
        edit_btn.clicked.connect(self.edit_patient)
        action_layout.addWidget(edit_btn)
        
        delete_btn = QPushButton("Delete Patient")
        delete_btn.clicked.connect(self.delete_patient)
        action_layout.addWidget(delete_btn)
        
        view_history_btn = QPushButton("View Medical History")
        view_history_btn.clicked.connect(self.view_patient_history)
        action_layout.addWidget(view_history_btn)
        
        layout.addLayout(action_layout)
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Patients")
        
        # Load initial data
        self.load_patients()
    
    def setup_consultation_tab(self):
        """Setup consultation tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Buttons
        button_layout = QHBoxLayout()
        new_consultation_btn = QPushButton("New Consultation")
        new_consultation_btn.clicked.connect(self.new_consultation)
        button_layout.addWidget(new_consultation_btn)
        
        layout.addLayout(button_layout)
        
        # Consultation table
        self.consultation_table = QTableWidget()
        self.consultation_table.setColumnCount(5)
        self.consultation_table.setHorizontalHeaderLabels(["ID", "Patient", "Date", "Symptoms", "Actions"])
        layout.addWidget(self.consultation_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Consultations")
    
    def setup_prescription_tab(self):
        """Setup prescription tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Buttons
        button_layout = QHBoxLayout()
        new_prescription_btn = QPushButton("New Prescription")
        new_prescription_btn.clicked.connect(self.new_prescription)
        button_layout.addWidget(new_prescription_btn)
        
        layout.addLayout(button_layout)
        
        # Prescription table
        self.prescription_table = QTableWidget()
        self.prescription_table.setColumnCount(6)
        self.prescription_table.setHorizontalHeaderLabels(["ID", "Patient", "Medicine", "Potency", "Dosage", "Actions"])
        layout.addWidget(self.prescription_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Prescriptions")
    
    def load_patients(self):
        """Load all patients into table"""
        patients = Patient.get_all()
        self.patient_table.setRowCount(len(patients))
        
        for row, patient in enumerate(patients):
            self.patient_table.setItem(row, 0, QTableWidgetItem(str(patient.id)))
            self.patient_table.setItem(row, 1, QTableWidgetItem(patient.full_name()))
            self.patient_table.setItem(row, 2, QTableWidgetItem(patient.phone))
            self.patient_table.setItem(row, 3, QTableWidgetItem(patient.email or ""))
            self.patient_table.setItem(row, 4, QTableWidgetItem(patient.gender or ""))
    
    def search_patients(self):
        """Search patients"""
        search_term = self.patient_search.text()
        if search_term:
            patients = Patient.search(search_term)
        else:
            patients = Patient.get_all()
        
        self.patient_table.setRowCount(len(patients))
        for row, patient in enumerate(patients):
            self.patient_table.setItem(row, 0, QTableWidgetItem(str(patient.id)))
            self.patient_table.setItem(row, 1, QTableWidgetItem(patient.full_name()))
            self.patient_table.setItem(row, 2, QTableWidgetItem(patient.phone))
            self.patient_table.setItem(row, 3, QTableWidgetItem(patient.email or ""))
            self.patient_table.setItem(row, 4, QTableWidgetItem(patient.gender or ""))
    
    def add_patient(self):
        """Add new patient"""
        dialog = PatientDialog(self)
        if dialog.exec():
            self.load_patients()
            QMessageBox.information(self, "Success", "Patient added successfully!")
    
    def edit_patient(self):
        """Edit selected patient"""
        current_row = self.patient_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a patient to edit.")
            return
        
        patient_id = int(self.patient_table.item(current_row, 0).text())
        patient = Patient.get_by_id(patient_id)
        
        dialog = PatientDialog(self, patient)
        if dialog.exec():
            self.load_patients()
            QMessageBox.information(self, "Success", "Patient updated successfully!")
    
    def delete_patient(self):
        """Delete selected patient"""
        current_row = self.patient_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a patient to delete.")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", 
                                      "Are you sure you want to delete this patient?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            patient_id = int(self.patient_table.item(current_row, 0).text())
            patient = Patient.get_by_id(patient_id)
            patient.delete()
            self.load_patients()
            QMessageBox.information(self, "Success", "Patient deleted successfully!")
    
    def on_patient_selected(self):
        """Handle patient selection"""
        pass
    
    def view_patient_history(self):
        """View patient medical history"""
        current_row = self.patient_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a patient.")
            return
        
        QMessageBox.information(self, "Medical History", "Medical history details coming soon...")
    
    def new_consultation(self):
        """Create new consultation"""
        dialog = ConsultationDialog(self)
        if dialog.exec():
            QMessageBox.information(self, "Success", "Consultation recorded successfully!")
    
    def new_prescription(self):
        """Create new prescription"""
        dialog = PrescriptionDialog(self)
        if dialog.exec():
            QMessageBox.information(self, "Success", "Prescription created successfully!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
