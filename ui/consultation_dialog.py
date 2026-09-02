from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QTextEdit, QDateEdit, QMessageBox
)
from PyQt6.QtCore import QDate
from models.patient import Patient
from models.consultation import Consultation

class ConsultationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Consultation")
        self.setGeometry(150, 150, 600, 700)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Patient Selection
        layout.addWidget(QLabel("Select Patient:"))
        self.patient_combo = QComboBox()
        patients = Patient.get_all()
        for patient in patients:
            self.patient_combo.addItem(patient.full_name(), patient.id)
        layout.addWidget(self.patient_combo)
        
        # Consultation Date
        layout.addWidget(QLabel("Consultation Date:"))
        self.consultation_date = QDateEdit()
        self.consultation_date.setCalendarPopup(True)
        self.consultation_date.setDate(QDate.currentDate())
        layout.addWidget(self.consultation_date)
        
        # Symptoms
        layout.addWidget(QLabel("Symptoms:"))
        self.symptoms_input = QTextEdit()
        self.symptoms_input.setPlaceholderText("Enter patient symptoms...")
        layout.addWidget(self.symptoms_input)
        
        # Physical Findings
        layout.addWidget(QLabel("Physical Findings:"))
        self.findings_input = QTextEdit()
        self.findings_input.setPlaceholderText("Enter physical examination findings...")
        layout.addWidget(self.findings_input)
        
        # Vital Signs
        layout.addWidget(QLabel("Vital Signs (BP, Temp, etc.):"))
        self.vital_signs_input = QLineEdit()
        self.vital_signs_input.setPlaceholderText("e.g., BP: 120/80, Temp: 98.6F")
        layout.addWidget(self.vital_signs_input)
        
        # Diagnosis
        layout.addWidget(QLabel("Diagnosis:"))
        self.diagnosis_input = QTextEdit()
        self.diagnosis_input.setPlaceholderText("Enter diagnosis...")
        layout.addWidget(self.diagnosis_input)
        
        # Clinical Observation
        layout.addWidget(QLabel("Clinical Observation:"))
        self.observation_input = QTextEdit()
        self.observation_input.setPlaceholderText("Enter clinical observations...")
        layout.addWidget(self.observation_input)
        
        # Consultation Notes
        layout.addWidget(QLabel("Consultation Notes:"))
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Enter additional notes...")
        layout.addWidget(self.notes_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save Consultation")
        save_btn.clicked.connect(self.save_consultation)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_consultation(self):
        if self.patient_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validation", "Please select a patient.")
            return
        
        patient_id = self.patient_combo.currentData()
        consultation = Consultation(
            patient_id=patient_id,
            consultation_date=self.consultation_date.date().toString("yyyy-MM-dd"),
            symptoms=self.symptoms_input.toPlainText(),
            findings=self.findings_input.toPlainText(),
            vital_signs=self.vital_signs_input.text(),
            diagnosis=self.diagnosis_input.toPlainText(),
            clinical_observation=self.observation_input.toPlainText(),
            consultation_notes=self.notes_input.toPlainText()
        )
        consultation.save()
        self.accept()
