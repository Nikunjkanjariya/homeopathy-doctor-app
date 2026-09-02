import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTabWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox,
    QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QColor
from config.database import init_database
from models.patient import Patient
from models.appointment import Appointment
from models.billing import Billing
from models.medical_history import MedicalHistory
from ui.patient_dialog import PatientDialog
from ui.consultation_dialog import ConsultationDialog
from ui.prescription_dialog import PrescriptionDialog
from ui.appointment_dialog import AppointmentDialog
from ui.billing_dialog import BillingDialog
from ui.medical_history_dialog import MedicalHistoryDialog
from utils.analytics import Analytics
from utils.invoice_generator import generate_analytics_report, generate_billing_report
from utils.pdf_generator import generate_prescription_pdf, generate_patient_report_pdf

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homeopathy Doctor Management System")
        self.setGeometry(100, 100, 1400, 800)
        
        # Initialize database
        init_database()
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel("Homeopathy Practice Management System")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        header_layout.addWidget(title)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)
        
        # Dashboard Row
        self.setup_dashboard(main_layout)
        
        # Tab Widget
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Tab 1: Patient Management
        self.setup_patient_tab()
        
        # Tab 2: Consultations
        self.setup_consultation_tab()
        
        # Tab 3: Prescriptions
        self.setup_prescription_tab()
        
        # Tab 4: Appointments
        self.setup_appointment_tab()
        
        # Tab 5: Billing
        self.setup_billing_tab()
        
        # Tab 6: Reports
        self.setup_reports_tab()
        
        self.show()
    
    def setup_dashboard(self, main_layout):
        """Setup dashboard with key metrics"""
        dashboard_layout = QGridLayout()
        
        # Total Patients
        patients_label = QLabel("Total Patients")
        patients_label.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        patients_value = QLabel(str(Analytics.get_total_patients()))
        patients_value.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        patients_value.setStyleSheet("color: #1f4788;")
        dashboard_layout.addWidget(patients_label, 0, 0)
        dashboard_layout.addWidget(patients_value, 1, 0)
        
        # Total Consultations
        consult_label = QLabel("Total Consultations")
        consult_label.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        consult_value = QLabel(str(Analytics.get_total_consultations()))
        consult_value.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        consult_value.setStyleSheet("color: #28a745;")
        dashboard_layout.addWidget(consult_label, 0, 1)
        dashboard_layout.addWidget(consult_value, 1, 1)
        
        # Total Revenue
        revenue_label = QLabel("Total Revenue")
        revenue_label.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        revenue_value = QLabel(f"₹ {Analytics.get_total_revenue():,.0f}")
        revenue_value.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        revenue_value.setStyleSheet("color: #20c997;")
        dashboard_layout.addWidget(revenue_label, 0, 2)
        dashboard_layout.addWidget(revenue_value, 1, 2)
        
        # Pending Payments
        pending_label = QLabel("Pending Payments")
        pending_label.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        pending_value = QLabel(f"₹ {Analytics.get_pending_payments():,.0f}")
        pending_value.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        pending_value.setStyleSheet("color: #fd7e14;")
        dashboard_layout.addWidget(pending_label, 0, 3)
        dashboard_layout.addWidget(pending_value, 1, 3)
        
        # Today's Appointments
        today_label = QLabel("Today's Appointments")
        today_label.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        today_value = QLabel(str(Analytics.get_today_appointments_count()))
        today_value.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        today_value.setStyleSheet("color: #dc3545;")
        dashboard_layout.addWidget(today_label, 0, 4)
        dashboard_layout.addWidget(today_value, 1, 4)
        
        main_layout.addLayout(dashboard_layout)
    
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
        
        view_history_btn = QPushButton("Medical History")
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
    
    def setup_appointment_tab(self):
        """Setup appointment tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Buttons
        button_layout = QHBoxLayout()
        new_appointment_btn = QPushButton("Schedule Appointment")
        new_appointment_btn.clicked.connect(self.new_appointment)
        button_layout.addWidget(new_appointment_btn)
        
        view_today_btn = QPushButton("View Today's Appointments")
        view_today_btn.clicked.connect(self.view_today_appointments)
        button_layout.addWidget(view_today_btn)
        
        layout.addLayout(button_layout)
        
        # Appointment table
        self.appointment_table = QTableWidget()
        self.appointment_table.setColumnCount(6)
        self.appointment_table.setHorizontalHeaderLabels(["ID", "Patient", "Date", "Time", "Status", "Actions"])
        layout.addWidget(self.appointment_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Appointments")
        self.load_appointments()
    
    def setup_billing_tab(self):
        """Setup billing tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Buttons
        button_layout = QHBoxLayout()
        new_invoice_btn = QPushButton("Create Invoice")
        new_invoice_btn.clicked.connect(self.new_billing)
        button_layout.addWidget(new_invoice_btn)
        
        pending_btn = QPushButton("View Pending Payments")
        pending_btn.clicked.connect(self.view_pending_payments)
        button_layout.addWidget(pending_btn)
        
        layout.addLayout(button_layout)
        
        # Billing table
        self.billing_table = QTableWidget()
        self.billing_table.setColumnCount(6)
        self.billing_table.setHorizontalHeaderLabels(["Invoice", "Patient", "Amount", "Status", "Date", "Actions"])
        layout.addWidget(self.billing_table)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Billing")
        self.load_billing()
    
    def setup_reports_tab(self):
        """Setup reports tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Generate Reports"))
        
        # Report buttons
        button_layout = QVBoxLayout()
        
        analytics_btn = QPushButton("Generate Analytics Report")
        analytics_btn.clicked.connect(self.generate_analytics_report)
        button_layout.addWidget(analytics_btn)
        
        billing_report_btn = QPushButton("Generate Billing Report")
        billing_report_btn.clicked.connect(self.generate_billing_report)
        button_layout.addWidget(billing_report_btn)
        
        layout.addLayout(button_layout)
        layout.addStretch()
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "Reports")
    
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
    
    def load_appointments(self):
        """Load appointments into table"""
        appointments = Appointment.get_upcoming()
        self.appointment_table.setRowCount(len(appointments))
        
        for row, appointment in enumerate(appointments):
            patient = Patient.get_by_id(appointment.patient_id)
            self.appointment_table.setItem(row, 0, QTableWidgetItem(str(appointment.id)))
            self.appointment_table.setItem(row, 1, QTableWidgetItem(patient.full_name() if patient else "N/A"))
            self.appointment_table.setItem(row, 2, QTableWidgetItem(appointment.appointment_date))
            self.appointment_table.setItem(row, 3, QTableWidgetItem(appointment.appointment_time))
            self.appointment_table.setItem(row, 4, QTableWidgetItem(appointment.status))
    
    def load_billing(self):
        """Load billing records into table"""
        billings = Billing.get_all()
        self.billing_table.setRowCount(len(billings[:20]))  # Show latest 20
        
        for row, billing in enumerate(billings[:20]):
            patient = Patient.get_by_id(billing.patient_id)
            self.billing_table.setItem(row, 0, QTableWidgetItem(billing.invoice_number))
            self.billing_table.setItem(row, 1, QTableWidgetItem(patient.full_name() if patient else "N/A"))
            self.billing_table.setItem(row, 2, QTableWidgetItem(f"₹ {billing.amount:,.2f}"))
            self.billing_table.setItem(row, 3, QTableWidgetItem(billing.status))
            self.billing_table.setItem(row, 4, QTableWidgetItem(billing.created_at.split()[0] if billing.created_at else ""))
    
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
        
        patient_id = int(self.patient_table.item(current_row, 0).text())
        medical_history = MedicalHistory.get_by_patient(patient_id)
        
        dialog = MedicalHistoryDialog(self, patient_id, medical_history)
        if dialog.exec():
            QMessageBox.information(self, "Success", "Medical history saved!")
    
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
    
    def new_appointment(self):
        """Create new appointment"""
        dialog = AppointmentDialog(self)
        if dialog.exec():
            self.load_appointments()
            QMessageBox.information(self, "Success", "Appointment scheduled successfully!")
    
    def view_today_appointments(self):
        """View today's appointments"""
        appointments = Appointment.get_today_appointments()
        if not appointments:
            QMessageBox.information(self, "Today's Appointments", "No appointments scheduled for today.")
            return
        
        msg = "Today's Appointments:\n\n"
        for apt in appointments:
            patient = Patient.get_by_id(apt.patient_id)
            msg += f"{apt.appointment_time} - {patient.full_name()} ({apt.status})\n"
        
        QMessageBox.information(self, "Today's Appointments", msg)
    
    def new_billing(self):
        """Create new billing record"""
        dialog = BillingDialog(self)
        if dialog.exec():
            self.load_billing()
            QMessageBox.information(self, "Success", "Invoice created successfully!")
    
    def view_pending_payments(self):
        """View pending payments"""
        billings = Billing.get_pending_payments()
        self.billing_table.setRowCount(len(billings))
        
        for row, billing in enumerate(billings):
            patient = Patient.get_by_id(billing.patient_id)
            self.billing_table.setItem(row, 0, QTableWidgetItem(billing.invoice_number))
            self.billing_table.setItem(row, 1, QTableWidgetItem(patient.full_name() if patient else "N/A"))
            self.billing_table.setItem(row, 2, QTableWidgetItem(f"₹ {billing.amount:,.2f}"))
            self.billing_table.setItem(row, 3, QTableWidgetItem(billing.status))
            self.billing_table.setItem(row, 4, QTableWidgetItem(billing.created_at.split()[0] if billing.created_at else ""))
    
    def generate_analytics_report(self):
        """Generate analytics report"""
        try:
            filename = generate_analytics_report()
            QMessageBox.information(self, "Success", f"Analytics report generated: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate report: {str(e)}")
    
    def generate_billing_report(self):
        """Generate billing report"""
        try:
            filename = generate_billing_report()
            QMessageBox.information(self, "Success", f"Billing report generated: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate report: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
