from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit,
    QPushButton, QMessageBox
)
from models.patient import Patient
from models.medical_history import MedicalHistory

class MedicalHistoryDialog(QDialog):
    def __init__(self, parent=None, patient_id=None, medical_history=None):
        super().__init__(parent)
        self.patient_id = patient_id
        self.medical_history = medical_history
        self.setWindowTitle("Medical History")
        self.setGeometry(100, 100, 700, 800)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Patient Info
        if self.patient_id:
            layout.addWidget(QLabel(f"Patient ID: {self.patient_id}"))
        
        # Chief Complaint
        layout.addWidget(QLabel("Chief Complaint:"))
        self.chief_complaint_input = QTextEdit()
        self.chief_complaint_input.setPlaceholderText("Main reason for visit...")
        if self.medical_history:
            self.chief_complaint_input.setText(self.medical_history.chief_complaint or "")
        layout.addWidget(self.chief_complaint_input)
        
        # Past Medical History
        layout.addWidget(QLabel("Past Medical History:"))
        self.past_medical_input = QTextEdit()
        self.past_medical_input.setPlaceholderText("Previous illnesses, surgeries, treatments...")
        if self.medical_history:
            self.past_medical_input.setText(self.medical_history.past_medical_history or "")
        layout.addWidget(self.past_medical_input)
        
        # Family History
        layout.addWidget(QLabel("Family History:"))
        self.family_history_input = QTextEdit()
        self.family_history_input.setPlaceholderText("Genetic conditions, hereditary diseases...")
        if self.medical_history:
            self.family_history_input.setText(self.medical_history.family_history or "")
        layout.addWidget(self.family_history_input)
        
        # Allergies
        layout.addWidget(QLabel("Allergies & Sensitivities:"))
        self.allergies_input = QTextEdit()
        self.allergies_input.setPlaceholderText("Drug allergies, food allergies, environmental allergies...")
        if self.medical_history:
            self.allergies_input.setText(self.medical_history.allergies or "")
        layout.addWidget(self.allergies_input)
        
        # Lifestyle & Habits
        layout.addWidget(QLabel("Lifestyle & Habits:"))
        self.lifestyle_input = QTextEdit()
        self.lifestyle_input.setPlaceholderText("Diet, exercise, sleep, smoking, alcohol use...")
        if self.medical_history:
            self.lifestyle_input.setText(self.medical_history.lifestyle_habits or "")
        layout.addWidget(self.lifestyle_input)
        
        # Vaccination History
        layout.addWidget(QLabel("Vaccination History:"))
        self.vaccination_input = QTextEdit()
        self.vaccination_input.setPlaceholderText("Vaccinations received...")
        if self.medical_history:
            self.vaccination_input.setText(self.medical_history.vaccination_history or "")
        layout.addWidget(self.vaccination_input)
        
        # Current Medications
        layout.addWidget(QLabel("Current Medications:"))
        self.current_meds_input = QTextEdit()
        self.current_meds_input.setPlaceholderText("Current medications being taken...")
        if self.medical_history:
            self.current_meds_input.setText(self.medical_history.current_medications or "")
        layout.addWidget(self.current_meds_input)
        
        # Mental State
        layout.addWidget(QLabel("Mental State:"))
        self.mental_state_input = QTextEdit()
        self.mental_state_input.setPlaceholderText("Emotional state, stress levels, depression, anxiety...")
        if self.medical_history:
            self.mental_state_input.setText(self.medical_history.mental_state or "")
        layout.addWidget(self.mental_state_input)
        
        # Physical Constitution
        layout.addWidget(QLabel("Physical Constitution:"))
        self.constitution_input = QTextEdit()
        self.constitution_input.setPlaceholderText("Body type, weight, height, physical condition...")
        if self.medical_history:
            self.constitution_input.setText(self.medical_history.physical_constitution or "")
        layout.addWidget(self.constitution_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save History")
        save_btn.clicked.connect(self.save_history)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_history(self):
        if self.medical_history:
            self.medical_history.chief_complaint = self.chief_complaint_input.toPlainText()
            self.medical_history.past_medical_history = self.past_medical_input.toPlainText()
            self.medical_history.family_history = self.family_history_input.toPlainText()
            self.medical_history.allergies = self.allergies_input.toPlainText()
            self.medical_history.lifestyle_habits = self.lifestyle_input.toPlainText()
            self.medical_history.vaccination_history = self.vaccination_input.toPlainText()
            self.medical_history.current_medications = self.current_meds_input.toPlainText()
            self.medical_history.mental_state = self.mental_state_input.toPlainText()
            self.medical_history.physical_constitution = self.constitution_input.toPlainText()
            self.medical_history.update()
        else:
            medical_history = MedicalHistory(
                patient_id=self.patient_id,
                chief_complaint=self.chief_complaint_input.toPlainText(),
                past_medical_history=self.past_medical_input.toPlainText(),
                family_history=self.family_history_input.toPlainText(),
                allergies=self.allergies_input.toPlainText(),
                lifestyle_habits=self.lifestyle_input.toPlainText(),
                vaccination_history=self.vaccination_input.toPlainText(),
                current_medications=self.current_meds_input.toPlainText(),
                mental_state=self.mental_state_input.toPlainText(),
                physical_constitution=self.constitution_input.toPlainText()
            )
            medical_history.save()
        
        self.accept()
