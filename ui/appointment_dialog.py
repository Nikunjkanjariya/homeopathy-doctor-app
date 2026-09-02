from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QDateEdit, QTimeEdit, QTextEdit, QMessageBox
)
from PyQt6.QtCore import QDate, QTime
from models.patient import Patient
from models.appointment import Appointment

class AppointmentDialog(QDialog):
    def __init__(self, parent=None, appointment=None):
        super().__init__(parent)
        self.appointment = appointment
        self.setWindowTitle("Schedule Appointment" if not appointment else "Edit Appointment")
        self.setGeometry(150, 150, 600, 500)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Patient Selection
        layout.addWidget(QLabel("Select Patient:"))
        self.patient_combo = QComboBox()
        patients = Patient.get_all()
        for patient in patients:
            self.patient_combo.addItem(patient.full_name(), patient.id)
        if self.appointment:
            index = self.patient_combo.findData(self.appointment.patient_id)
            if index >= 0:
                self.patient_combo.setCurrentIndex(index)
        layout.addWidget(self.patient_combo)
        
        # Appointment Date
        layout.addWidget(QLabel("Appointment Date:"))
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        if self.appointment:
            self.date_input.setDate(QDate.fromString(self.appointment.appointment_date, "yyyy-MM-dd"))
        layout.addWidget(self.date_input)
        
        # Appointment Time
        layout.addWidget(QLabel("Appointment Time:"))
        self.time_input = QTimeEdit()
        self.time_input.setTime(QTime.currentTime())
        if self.appointment:
            self.time_input.setTime(QTime.fromString(self.appointment.appointment_time, "hh:mm:ss"))
        layout.addWidget(self.time_input)
        
        # Reason for Visit
        layout.addWidget(QLabel("Reason for Visit:"))
        self.reason_input = QTextEdit()
        self.reason_input.setPlaceholderText("Enter reason for appointment...")
        if self.appointment:
            self.reason_input.setText(self.appointment.reason or "")
        layout.addWidget(self.reason_input)
        
        # Status
        layout.addWidget(QLabel("Status:"))
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Scheduled", "Completed", "Cancelled", "Rescheduled"])
        if self.appointment:
            index = self.status_combo.findText(self.appointment.status)
            if index >= 0:
                self.status_combo.setCurrentIndex(index)
        layout.addWidget(self.status_combo)
        
        # Doctor Notes
        layout.addWidget(QLabel("Doctor Notes:"))
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Enter doctor notes...")
        if self.appointment:
            self.notes_input.setText(self.appointment.doctor_notes or "")
        layout.addWidget(self.notes_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save Appointment")
        save_btn.clicked.connect(self.save_appointment)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_appointment(self):
        if self.patient_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validation", "Please select a patient.")
            return
        
        patient_id = self.patient_combo.currentData()
        
        if self.appointment:
            self.appointment.patient_id = patient_id
            self.appointment.appointment_date = self.date_input.date().toString("yyyy-MM-dd")
            self.appointment.appointment_time = self.time_input.time().toString("hh:mm:ss")
            self.appointment.reason = self.reason_input.toPlainText()
            self.appointment.status = self.status_combo.currentText()
            self.appointment.doctor_notes = self.notes_input.toPlainText()
            self.appointment.update()
        else:
            appointment = Appointment(
                patient_id=patient_id,
                appointment_date=self.date_input.date().toString("yyyy-MM-dd"),
                appointment_time=self.time_input.time().toString("hh:mm:ss"),
                reason=self.reason_input.toPlainText(),
                status=self.status_combo.currentText(),
                doctor_notes=self.notes_input.toPlainText()
            )
            appointment.save()
        
        self.accept()
