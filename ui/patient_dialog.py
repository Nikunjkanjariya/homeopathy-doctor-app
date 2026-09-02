from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QDateEdit, QMessageBox
)
from PyQt6.QtCore import QDate
from models.patient import Patient
from utils.validators import validate_phone, validate_email

class PatientDialog(QDialog):
    def __init__(self, parent=None, patient=None):
        super().__init__(parent)
        self.patient = patient
        self.setWindowTitle("Add Patient" if not patient else "Edit Patient")
        self.setGeometry(150, 150, 500, 600)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # First Name
        layout.addWidget(QLabel("First Name:"))
        self.first_name_input = QLineEdit()
        if self.patient:
            self.first_name_input.setText(self.patient.first_name)
        layout.addWidget(self.first_name_input)
        
        # Last Name
        layout.addWidget(QLabel("Last Name:"))
        self.last_name_input = QLineEdit()
        if self.patient:
            self.last_name_input.setText(self.patient.last_name)
        layout.addWidget(self.last_name_input)
        
        # Phone
        layout.addWidget(QLabel("Phone:"))
        self.phone_input = QLineEdit()
        if self.patient:
            self.phone_input.setText(self.patient.phone)
        layout.addWidget(self.phone_input)
        
        # Email
        layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        if self.patient:
            self.email_input.setText(self.patient.email or "")
        layout.addWidget(self.email_input)
        
        # Date of Birth
        layout.addWidget(QLabel("Date of Birth:"))
        self.dob_input = QDateEdit()
        self.dob_input.setCalendarPopup(True)
        if self.patient and self.patient.date_of_birth:
            self.dob_input.setDate(QDate.fromString(self.patient.date_of_birth, "yyyy-MM-dd"))
        layout.addWidget(self.dob_input)
        
        # Gender
        layout.addWidget(QLabel("Gender:"))
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female", "Other"])
        if self.patient:
            index = self.gender_combo.findText(self.patient.gender or "")
            if index >= 0:
                self.gender_combo.setCurrentIndex(index)
        layout.addWidget(self.gender_combo)
        
        # Address
        layout.addWidget(QLabel("Address:"))
        self.address_input = QLineEdit()
        if self.patient:
            self.address_input.setText(self.patient.address or "")
        layout.addWidget(self.address_input)
        
        # City
        layout.addWidget(QLabel("City:"))
        self.city_input = QLineEdit()
        if self.patient:
            self.city_input.setText(self.patient.city or "")
        layout.addWidget(self.city_input)
        
        # State
        layout.addWidget(QLabel("State:"))
        self.state_input = QLineEdit()
        if self.patient:
            self.state_input.setText(self.patient.state or "")
        layout.addWidget(self.state_input)
        
        # Pincode
        layout.addWidget(QLabel("Pincode:"))
        self.pincode_input = QLineEdit()
        if self.patient:
            self.pincode_input.setText(self.patient.pincode or "")
        layout.addWidget(self.pincode_input)
        
        # Occupation
        layout.addWidget(QLabel("Occupation:"))
        self.occupation_input = QLineEdit()
        if self.patient:
            self.occupation_input.setText(self.patient.occupation or "")
        layout.addWidget(self.occupation_input)
        
        # Marital Status
        layout.addWidget(QLabel("Marital Status:"))
        self.marital_combo = QComboBox()
        self.marital_combo.addItems(["Single", "Married", "Divorced", "Widowed"])
        if self.patient:
            index = self.marital_combo.findText(self.patient.marital_status or "")
            if index >= 0:
                self.marital_combo.setCurrentIndex(index)
        layout.addWidget(self.marital_combo)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_patient)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_patient(self):
        # Validate inputs
        if not self.first_name_input.text():
            QMessageBox.warning(self, "Validation", "First name is required.")
            return
        
        if not self.last_name_input.text():
            QMessageBox.warning(self, "Validation", "Last name is required.")
            return
        
        if not validate_phone(self.phone_input.text()):
            QMessageBox.warning(self, "Validation", "Invalid phone number.")
            return
        
        if self.email_input.text() and not validate_email(self.email_input.text()):
            QMessageBox.warning(self, "Validation", "Invalid email address.")
            return
        
        if self.patient:
            # Update existing patient
            self.patient.first_name = self.first_name_input.text()
            self.patient.last_name = self.last_name_input.text()
            self.patient.phone = self.phone_input.text()
            self.patient.email = self.email_input.text()
            self.patient.date_of_birth = self.dob_input.date().toString("yyyy-MM-dd")
            self.patient.gender = self.gender_combo.currentText()
            self.patient.address = self.address_input.text()
            self.patient.city = self.city_input.text()
            self.patient.state = self.state_input.text()
            self.patient.pincode = self.pincode_input.text()
            self.patient.occupation = self.occupation_input.text()
            self.patient.marital_status = self.marital_combo.currentText()
            self.patient.update()
        else:
            # Create new patient
            patient = Patient(
                first_name=self.first_name_input.text(),
                last_name=self.last_name_input.text(),
                phone=self.phone_input.text(),
                email=self.email_input.text(),
                date_of_birth=self.dob_input.date().toString("yyyy-MM-dd"),
                gender=self.gender_combo.currentText(),
                address=self.address_input.text(),
                city=self.city_input.text(),
                state=self.state_input.text(),
                pincode=self.pincode_input.text(),
                occupation=self.occupation_input.text(),
                marital_status=self.marital_combo.currentText()
            )
            patient.save()
        
        self.accept()
