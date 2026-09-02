from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QSpinBox, QDoubleSpinBox, QTextEdit, QDateEdit, QMessageBox
)
from PyQt6.QtCore import QDate
from models.patient import Patient
from models.consultation import Consultation
from models.prescription import Prescription

class PrescriptionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Prescription")
        self.setGeometry(150, 150, 600, 800)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Patient Selection
        layout.addWidget(QLabel("Select Patient:"))
        self.patient_combo = QComboBox()
        patients = Patient.get_all()
        for patient in patients:
            self.patient_combo.addItem(patient.full_name(), patient.id)
        self.patient_combo.currentIndexChanged.connect(self.on_patient_selected)
        layout.addWidget(self.patient_combo)
        
        # Consultation Selection
        layout.addWidget(QLabel("Select Consultation (Optional):"))
        self.consultation_combo = QComboBox()
        self.consultation_combo.addItem("None", None)
        layout.addWidget(self.consultation_combo)
        
        # Medicine Name
        layout.addWidget(QLabel("Medicine Name:"))
        self.medicine_input = QLineEdit()
        self.medicine_input.setPlaceholderText("e.g., Arnica Montana, Belladonna...")
        layout.addWidget(self.medicine_input)
        
        # Potency
        layout.addWidget(QLabel("Potency:"))
        self.potency_combo = QComboBox()
        self.potency_combo.addItems([
            "6C", "6X", "12C", "12X", "30C", "30X", 
            "200C", "200X", "1M", "10M", "CM"
        ])
        layout.addWidget(self.potency_combo)
        
        # Dosage
        layout.addWidget(QLabel("Dosage (e.g., 2-3 tablets):"))
        self.dosage_input = QLineEdit()
        self.dosage_input.setPlaceholderText("e.g., 2-3 tablets")
        layout.addWidget(self.dosage_input)
        
        # Frequency
        layout.addWidget(QLabel("Frequency:"))
        self.frequency_combo = QComboBox()
        self.frequency_combo.addItems([
            "Once daily", "Twice daily", "Three times daily",
            "Every 4 hours", "Every 6 hours", "Every 8 hours",
            "Once weekly", "As needed"
        ])
        layout.addWidget(self.frequency_combo)
        
        # Duration
        layout.addWidget(QLabel("Duration:"))
        self.duration_input = QLineEdit()
        self.duration_input.setPlaceholderText("e.g., 30 days, 2 months")
        layout.addWidget(self.duration_input)
        
        # Quantity
        layout.addWidget(QLabel("Quantity:"))
        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(1)
        self.quantity_input.setValue(1)
        layout.addWidget(self.quantity_input)
        
        # Manufacturer
        layout.addWidget(QLabel("Manufacturer:"))
        self.manufacturer_input = QLineEdit()
        self.manufacturer_input.setPlaceholderText("e.g., SBL, Schwabe...")
        layout.addWidget(self.manufacturer_input)
        
        # Price
        layout.addWidget(QLabel("Price:"))
        self.price_input = QDoubleSpinBox()
        self.price_input.setMinimum(0)
        self.price_input.setValue(0)
        layout.addWidget(self.price_input)
        
        # Notes
        layout.addWidget(QLabel("Additional Notes:"))
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("e.g., Take on empty stomach, avoid coffee...")
        layout.addWidget(self.notes_input)
        
        # Prescribed Date
        layout.addWidget(QLabel("Prescribed Date:"))
        self.prescribed_date = QDateEdit()
        self.prescribed_date.setCalendarPopup(True)
        self.prescribed_date.setDate(QDate.currentDate())
        layout.addWidget(self.prescribed_date)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save Prescription")
        save_btn.clicked.connect(self.save_prescription)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def on_patient_selected(self):
        """Load consultations for selected patient"""
        patient_id = self.patient_combo.currentData()
        self.consultation_combo.clear()
        self.consultation_combo.addItem("None", None)
        
        if patient_id:
            consultations = Consultation.get_by_patient(patient_id)
            for consultation in consultations:
                self.consultation_combo.addItem(
                    f"{consultation.consultation_date} - {consultation.diagnosis or 'No diagnosis'}",
                    consultation.id
                )
    
    def save_prescription(self):
        if self.patient_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validation", "Please select a patient.")
            return
        
        if not self.medicine_input.text():
            QMessageBox.warning(self, "Validation", "Medicine name is required.")
            return
        
        if not self.dosage_input.text():
            QMessageBox.warning(self, "Validation", "Dosage is required.")
            return
        
        patient_id = self.patient_combo.currentData()
        consultation_id = self.consultation_combo.currentData()
        
        prescription = Prescription(
            patient_id=patient_id,
            medicine_name=self.medicine_input.text(),
            potency=self.potency_combo.currentText(),
            dosage=self.dosage_input.text(),
            frequency=self.frequency_combo.currentText(),
            prescribed_date=self.prescribed_date.date().toString("yyyy-MM-dd"),
            consultation_id=consultation_id,
            duration=self.duration_input.text(),
            quantity=self.quantity_input.value(),
            manufacturer=self.manufacturer_input.text(),
            price=self.price_input.value(),
            notes=self.notes_input.toPlainText()
        )
        prescription.save()
        self.accept()
