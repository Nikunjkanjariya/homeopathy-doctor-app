from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QDoubleSpinBox, QTextEdit, QMessageBox
)
from models.patient import Patient
from models.billing import Billing
import uuid

class BillingDialog(QDialog):
    def __init__(self, parent=None, billing=None):
        super().__init__(parent)
        self.billing = billing
        self.setWindowTitle("Create Invoice" if not billing else "Edit Invoice")
        self.setGeometry(150, 150, 600, 600)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Patient Selection
        layout.addWidget(QLabel("Select Patient:"))
        self.patient_combo = QComboBox()
        patients = Patient.get_all()
        for patient in patients:
            self.patient_combo.addItem(patient.full_name(), patient.id)
        if self.billing:
            index = self.patient_combo.findData(self.billing.patient_id)
            if index >= 0:
                self.patient_combo.setCurrentIndex(index)
        layout.addWidget(self.patient_combo)
        
        # Invoice Number
        layout.addWidget(QLabel("Invoice Number:"))
        self.invoice_input = QLineEdit()
        self.invoice_input.setPlaceholderText("Auto-generated")
        if self.billing:
            self.invoice_input.setText(self.billing.invoice_number)
        else:
            self.invoice_input.setText(f"INV-{str(uuid.uuid4())[:8].upper()}")
        layout.addWidget(self.invoice_input)
        
        # Amount
        layout.addWidget(QLabel("Amount:"))
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setMinimum(0)
        self.amount_input.setValue(self.billing.amount if self.billing else 0)
        layout.addWidget(self.amount_input)
        
        # Description
        layout.addWidget(QLabel("Description/Services:"))
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("e.g., Consultation fee, Medicine cost, Lab tests...")
        if self.billing:
            self.description_input.setText(self.billing.description or "")
        layout.addWidget(self.description_input)
        
        # Payment Method
        layout.addWidget(QLabel("Payment Method:"))
        self.payment_method_combo = QComboBox()
        self.payment_method_combo.addItems(["Cash", "Card", "Online Transfer", "Cheque"])
        if self.billing:
            index = self.payment_method_combo.findText(self.billing.payment_method)
            if index >= 0:
                self.payment_method_combo.setCurrentIndex(index)
        layout.addWidget(self.payment_method_combo)
        
        # Status
        layout.addWidget(QLabel("Payment Status:"))
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Pending", "Paid", "Partially Paid", "Cancelled"])
        if self.billing:
            index = self.status_combo.findText(self.billing.status)
            if index >= 0:
                self.status_combo.setCurrentIndex(index)
        layout.addWidget(self.status_combo)
        
        # Notes
        layout.addWidget(QLabel("Notes:"))
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Additional notes...")
        if self.billing:
            self.notes_input.setText(self.billing.notes or "")
        layout.addWidget(self.notes_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save Invoice")
        save_btn.clicked.connect(self.save_billing)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_billing(self):
        if self.patient_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validation", "Please select a patient.")
            return
        
        if self.amount_input.value() <= 0:
            QMessageBox.warning(self, "Validation", "Amount must be greater than 0.")
            return
        
        patient_id = self.patient_combo.currentData()
        
        if self.billing:
            self.billing.patient_id = patient_id
            self.billing.invoice_number = self.invoice_input.text()
            self.billing.amount = self.amount_input.value()
            self.billing.description = self.description_input.toPlainText()
            self.billing.payment_method = self.payment_method_combo.currentText()
            self.billing.status = self.status_combo.currentText()
            self.billing.notes = self.notes_input.toPlainText()
            self.billing.update()
        else:
            billing = Billing(
                patient_id=patient_id,
                invoice_number=self.invoice_input.text(),
                amount=self.amount_input.value(),
                description=self.description_input.toPlainText(),
                payment_method=self.payment_method_combo.currentText(),
                status=self.status_combo.currentText(),
                notes=self.notes_input.toPlainText()
            )
            billing.save()
        
        self.accept()
