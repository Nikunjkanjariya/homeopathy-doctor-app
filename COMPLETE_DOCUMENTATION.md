# Homeopathy Doctor Management App - Complete Feature Documentation

## 📋 Table of Contents
1. [System Overview](#system-overview)
2. [Complete Features](#complete-features)
3. [Installation & Setup](#installation--setup)
4. [Usage Guide](#usage-guide)
5. [Database Schema](#database-schema)
6. [API Reference](#api-reference)
7. [Troubleshooting](#troubleshooting)

---

## System Overview

A professional, enterprise-grade desktop application designed for homeopathy medical practitioners to manage their complete practice including:
- Patient records and medical history
- Appointment scheduling
- Consultation documentation
- Prescription management
- Billing and invoicing
- Advanced analytics and reporting

### Key Benefits
- **Complete Digitization**: Eliminate paper-based records
- **Time Saving**: Automated workflows and quick access to patient data
- **Better Patient Care**: Comprehensive medical history tracking
- **Financial Management**: Built-in billing and revenue tracking
- **Professional Reports**: Generate analytics and business reports
- **Data Security**: Local SQLite database with automatic backups

---

## Complete Features

### 1️⃣ Patient Management

#### Features:
- **Add Patients**: Complete patient profile with personal information
- **Search & Filter**: Quick patient lookup by name or phone
- **Edit Records**: Update patient information anytime
- **Delete Records**: Remove patient records (with confirmation)
- **Medical History**: Comprehensive medical history tracking

#### Patient Profile Fields:
```
Personal Information:
- First Name & Last Name (required)
- Date of Birth
- Gender
- Phone (required)
- Email
- Address
- City, State, Pincode
- Occupation
- Marital Status
```

#### Medical History Fields:
```
- Chief Complaint
- Past Medical History
- Family History
- Allergies & Sensitivities
- Lifestyle & Habits
- Vaccination History
- Current Medications
- Mental State
- Physical Constitution
```

### 2️⃣ Consultation System

#### Features:
- **Record Consultations**: Document complete consultation details
- **Symptom Documentation**: Detailed symptom recording
- **Physical Examination**: Record findings and observations
- **Vital Signs**: BP, Temperature, Pulse tracking
- **Diagnosis**: Store medical diagnosis
- **Notes**: Comprehensive consultation notes

#### Consultation Fields:
```
- Patient Selection
- Consultation Date
- Symptoms (detailed)
- Physical Findings
- Vital Signs (BP, Temp, Pulse, etc.)
- Diagnosis
- Clinical Observations
- Consultation Notes
```

### 3️⃣ Prescription Management

#### Features:
- **Prescription Creation**: Create detailed prescriptions
- **Medicine Selection**: Pre-defined homeopathic medicines
- **Potency Selection**: Multiple potency levels (6C to CM)
- **Dosage Specification**: Custom dosage instructions
- **Frequency Settings**: Various frequency options
- **Special Instructions**: Add patient-specific notes
- **PDF Generation**: Print-ready prescriptions

#### Potency Levels Supported:
```
Low Potency:    6C, 6X
Medium:         12C, 12X
High:           30C, 30X
Very High:      200C, 200X
Ultra-High:     1M, 10M, CM
```

#### Prescription Fields:
```
- Patient Selection
- Medicine Name
- Potency Level
- Dosage (tablets/drops)
- Frequency (Once daily, Twice daily, etc.)
- Duration (days/weeks/months)
- Quantity
- Manufacturer
- Price
- Additional Notes (empty stomach, avoid coffee, etc.)
```

### 4️⃣ Appointment Scheduling

#### Features:
- **Schedule Appointments**: Book patient appointments
- **Time Management**: Set specific appointment times
- **Status Tracking**: Track appointment status (Scheduled, Completed, Cancelled, Rescheduled)
- **Today's View**: Quick view of today's appointments
- **Upcoming List**: View all upcoming appointments
- **Notes**: Add doctor notes for follow-ups

#### Appointment Fields:
```
- Patient Selection
- Appointment Date (with calendar)
- Appointment Time
- Reason for Visit
- Status (Scheduled, Completed, Cancelled, Rescheduled)
- Doctor Notes
```

### 5️⃣ Billing & Invoicing

#### Features:
- **Invoice Creation**: Generate professional invoices
- **Payment Tracking**: Track payment status
- **Multiple Payment Methods**: Cash, Card, Online, Cheque
- **Pending Payments**: View outstanding payments
- **Invoice History**: Complete billing history
- **Revenue Analytics**: Track income and expenses

#### Billing Fields:
```
- Patient Selection
- Invoice Number (auto-generated)
- Amount
- Description/Services
- Payment Method (Cash, Card, Online, Cheque)
- Payment Status (Pending, Paid, Partially Paid, Cancelled)
- Notes
```

### 6️⃣ Analytics & Reports

#### Dashboard Metrics:
- **Total Patients**: Overall patient count
- **Total Consultations**: Consultation count
- **Total Prescriptions**: Prescriptions issued
- **Total Revenue**: Revenue from paid invoices
- **Pending Payments**: Outstanding payment amount
- **This Month Stats**: Current month consultations and revenue
- **Today's Appointments**: Count of today's appointments

#### Available Reports:

**Analytics Report** includes:
- Key Performance Indicators (KPIs)
- Top 10 prescribed medicines
- Patient visit frequency analysis
- Patient engagement statistics

**Billing Report** includes:
- Total revenue summary
- Pending payments
- Monthly revenue breakdown
- Payment status analysis

### 7️⃣ Report Generation

#### PDF Reports:
- **Prescription PDFs**: Professional prescription documents
- **Patient Reports**: Complete medical records
- **Analytics Reports**: Business analytics and insights
- **Billing Reports**: Revenue and payment reports

---

## Installation & Setup

### System Requirements
- **OS**: Windows 7+, macOS 10.13+, Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum
- **Disk Space**: 500MB
- **Internet**: Not required (offline operation)

### Step-by-Step Installation

#### 1. Install Python
```bash
# Download from python.org and install
# Verify installation
python --version  # Should show 3.8+
```

#### 2. Clone Repository
```bash
git clone https://github.com/Nikunjkanjariya/homeopathy-doctor-app.git
cd homeopathy-doctor-app
```

#### 3. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Run Application
```bash
python main.py
```

### Database Setup
- Database automatically initializes on first run
- Location: `~/.homeopathy_app/homeopathy.db`
- No manual setup required

---

## Usage Guide

### Dashboard
The dashboard displays key metrics at application startup:
- Total patients in system
- Consultation statistics
- Revenue information
- Pending payments
- Today's appointment count

### Patient Management Tab

#### Adding a New Patient:
1. Click "Patients" tab
2. Click "Add New Patient"
3. Fill in required fields (Name, Phone)
4. Add optional information (Email, Address, etc.)
5. Click "Save"

#### Searching Patients:
1. Use search box to find patients by name or phone
2. Results update in real-time
3. Click to select patient

#### Editing Patient Info:
1. Select patient from table
2. Click "Edit Patient"
3. Update information
4. Click "Save"

#### Viewing Medical History:
1. Select patient from table
2. Click "Medical History"
3. Fill in comprehensive history
4. Click "Save History"

### Consultation Tab

#### Recording Consultation:
1. Click "Consultations" tab
2. Click "New Consultation"
3. Select patient
4. Enter consultation date
5. Document symptoms and findings
6. Record vital signs
7. Add diagnosis and notes
8. Click "Save Consultation"

### Prescription Tab

#### Creating Prescription:
1. Click "Prescriptions" tab
2. Click "New Prescription"
3. Select patient
4. Optionally link to consultation
5. Enter medicine details:
   - Medicine name (e.g., Arnica Montana)
   - Potency (e.g., 30C)
   - Dosage (e.g., 2-3 tablets)
   - Frequency (e.g., Twice daily)
   - Duration (e.g., 30 days)
6. Add special instructions if needed
7. Click "Save Prescription"

### Appointment Tab

#### Scheduling Appointment:
1. Click "Appointments" tab
2. Click "Schedule Appointment"
3. Select patient
4. Choose appointment date
5. Set appointment time
6. Enter reason for visit
7. Set status (Scheduled, Completed, etc.)
8. Add doctor notes
9. Click "Save Appointment"

#### Viewing Today's Appointments:
1. Click "Appointments" tab
2. Click "View Today's Appointments"
3. See all appointments for today

### Billing Tab

#### Creating Invoice:
1. Click "Billing" tab
2. Click "Create Invoice"
3. Select patient
4. Invoice number auto-generates
5. Enter amount and description
6. Select payment method
7. Set payment status
8. Add notes if needed
9. Click "Save Invoice"

#### Viewing Pending Payments:
1. Click "Billing" tab
2. Click "View Pending Payments"
3. See all unpaid/partially paid invoices
4. Update status when paid

### Reports Tab

#### Generating Reports:
1. Click "Reports" tab
2. Choose report type:
   - **Analytics Report**: Business metrics and KPIs
   - **Billing Report**: Revenue and payment analysis
3. Click to generate
4. PDF saves to current directory
5. Use to print or email

---

## Database Schema

### Patients Table
```sql
CREATE TABLE patients (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth TEXT,
    gender TEXT,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    pincode TEXT,
    occupation TEXT,
    marital_status TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
)
```

### Consultations Table
```sql
CREATE TABLE consultations (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    consultation_date TEXT NOT NULL,
    symptoms TEXT,
    findings TEXT,
    vital_signs TEXT,
    diagnosis TEXT,
    clinical_observation TEXT,
    consultation_notes TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
```

### Prescriptions Table
```sql
CREATE TABLE prescriptions (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    consultation_id INTEGER,
    medicine_name TEXT NOT NULL,
    potency TEXT NOT NULL,
    dosage TEXT NOT NULL,
    frequency TEXT NOT NULL,
    duration TEXT,
    quantity INTEGER,
    manufacturer TEXT,
    price REAL,
    notes TEXT,
    prescribed_date TEXT NOT NULL,
    created_at TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
```

### Appointments Table
```sql
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    appointment_date TEXT NOT NULL,
    appointment_time TEXT NOT NULL,
    reason TEXT,
    status TEXT DEFAULT 'Scheduled',
    doctor_notes TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
```

### Billing Table
```sql
CREATE TABLE billing (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    invoice_number TEXT NOT NULL UNIQUE,
    amount REAL NOT NULL,
    description TEXT,
    payment_method TEXT,
    status TEXT DEFAULT 'Pending',
    notes TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
```

### Medical History Table
```sql
CREATE TABLE medical_history (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    chief_complaint TEXT,
    past_medical_history TEXT,
    family_history TEXT,
    allergies TEXT,
    lifestyle_habits TEXT,
    vaccination_history TEXT,
    current_medications TEXT,
    mental_state TEXT,
    physical_constitution TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
```

---

## API Reference

### Patient Model
```python
from models.patient import Patient

# Create patient
patient = Patient(
    first_name="John",
    last_name="Doe",
    phone="9876543210"
)
patient.save()  # Returns patient ID

# Get patient
patient = Patient.get_by_id(1)

# Get all patients
patients = Patient.get_all()

# Search patients
patients = Patient.search("John")

# Update patient
patient.first_name = "Jane"
patient.update()

# Delete patient
patient.delete()
```

### Consultation Model
```python
from models.consultation import Consultation

# Create consultation
consultation = Consultation(
    patient_id=1,
    consultation_date="2024-01-15",
    symptoms="Headache"
)
consultation.save()

# Get consultations by patient
consultations = Consultation.get_by_patient(1)
```

### Appointment Model
```python
from models.appointment import Appointment

# Schedule appointment
appointment = Appointment(
    patient_id=1,
    appointment_date="2024-01-20",
    appointment_time="10:30:00"
)
appointment.save()

# Get upcoming appointments
upcoming = Appointment.get_upcoming()

# Get today's appointments
today = Appointment.get_today_appointments()
```

### Billing Model
```python
from models.billing import Billing

# Create invoice
billing = Billing(
    patient_id=1,
    invoice_number="INV-001",
    amount=500.00
)
billing.save()

# Get pending payments
pending = Billing.get_pending_payments()

# Update status
billing.status = "Paid"
billing.update()
```

### Analytics
```python
from utils.analytics import Analytics

# Get metrics
Analytics.get_total_patients()
Analytics.get_total_revenue()
Analytics.get_this_month_consultations()
Analytics.get_top_medicines()
Analytics.get_patient_visit_frequency()
```

---

## Troubleshooting

### Application Won't Start

**Issue**: Import errors or module not found

**Solution**:
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

### Database Issues

**Issue**: Database locked or corrupted

**Solution**:
```bash
# Delete corrupted database
rm ~/.homeopathy_app/homeopathy.db

# Application will recreate on next start
python main.py
```

### PyQt6 Issues

**Issue**: PyQt6 not installing

**Solution**:
```bash
# Linux
sudo apt-get install python3-pyqt6

# macOS
brew install pyqt6

# Windows (or all platforms)
pip install --upgrade PyQt6
```

### PDF Generation Issues

**Issue**: Reports not generating

**Solution**:
```bash
# Ensure reportlab is installed
pip install --upgrade reportlab

# Check write permissions in current directory
ls -la .  # Should show write permissions
```

### Performance Issues

**Issue**: Application running slowly

**Solution**:
- Close other applications
- Ensure database file is not corrupt
- Check disk space availability
- Consider archiving old records

### Data Backup

**Regular Backups**:
```bash
# Copy database file
cp ~/.homeopathy_app/homeopathy.db ~/homeopathy_backup_$(date +%Y%m%d).db

# Or use cloud storage
cp ~/.homeopathy_app/homeopathy.db /path/to/cloud/drive/
```

---

## Common Homeopathic Medicines

### Frequently Used Medicines

| Medicine | Uses | Potency |
|----------|------|----------|
| Arnica Montana | Trauma, bruises, pain | 30C, 200C |
| Belladonna | Fever, acute inflammation | 30C |
| Bryonia | Headaches, joint pain | 30C, 200C |
| Calcarea Carbonica | Weakness, slow growth | 200C, 1M |
| Lycopodium | Digestive issues | 30C, 200C |
| Nux Vomica | Stress, constipation | 30C, 200C |
| Phosphorus | Respiratory issues | 30C, 200C |
| Pulsatilla | Emotional sensitivity | 30C |
| Sulphur | Skin conditions | 30C, 200C |
| Thuja | Warts, immunological | 30C, 200C |

---

## License & Support

**License**: MIT License

**Support**: For issues or feature requests, open an issue on GitHub

**Repository**: https://github.com/Nikunjkanjariya/homeopathy-doctor-app

---

**Made with ❤️ for homeopathy practitioners**
