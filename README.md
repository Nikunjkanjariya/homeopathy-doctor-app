# Homeopathy Doctor Management App

> A professional desktop application for homeopathy doctors to manage patients, consultations, prescriptions, and medical records.

## 🎯 Key Features

### Patient Management
- **Complete Patient Database**: Add, edit, search, and manage patient profiles
- **Medical History Tracking**: Record comprehensive patient history including:
  - Chief complaints
  - Past medical history
  - Family history
  - Allergies and sensitivities
  - Lifestyle and habits
  - Current medications

### Consultation System
- **Detailed Consultations**: Record symptoms, findings, and observations
- **Vital Signs Tracking**: Document blood pressure, temperature, pulse
- **Clinical Notes**: Add comprehensive consultation notes
- **Diagnosis Documentation**: Store diagnosis and clinical observations

### Prescription Management
- **Homeopathic Prescriptions**: Create detailed prescriptions with:
  - Medicine selection
  - Potency levels (6C to CM)
  - Dosage specifications
  - Frequency settings
  - Duration tracking
  - Manufacturer information
  - Pricing details
- **Special Instructions**: Add notes for patients (e.g., "Take on empty stomach")

### Recommendations & Follow-up
- **Dietary Recommendations**: Provide diet guidelines
- **Lifestyle Advice**: Suggest lifestyle modifications
- **Precautions**: Document important precautions
- **Follow-up Scheduling**: Set follow-up appointments

### Reports & Documentation
- **PDF Generation**: Generate professional prescription PDFs
- **Patient Reports**: Create comprehensive medical records
- **Print-ready Formats**: Professional formatting for printing

## 🚀 Quick Start

### System Requirements
- Python 3.8 or higher
- Windows, macOS, or Linux
- 100MB disk space

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nikunjkanjariya/homeopathy-doctor-app.git
   cd homeopathy-doctor-app
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## 📖 Usage Guide

### Adding a Patient
1. Go to **Patients** tab
2. Click **Add New Patient**
3. Fill in patient details
4. Click **Save**

### Recording a Consultation
1. Go to **Consultations** tab
2. Click **New Consultation**
3. Select patient
4. Enter symptoms, findings, and diagnosis
5. Click **Save Consultation**

### Creating a Prescription
1. Go to **Prescriptions** tab
2. Click **New Prescription**
3. Select patient and consultation
4. Choose medicine, potency, and dosage
5. Add special instructions if needed
6. Click **Save Prescription**

## 📁 Project Structure

```
homeopathy-doctor-app/
├── main.py                      # Application entry point
├── requirements.txt             # Dependencies
├── config/
│   └── database.py             # Database setup
├── models/
│   ├── patient.py              # Patient model
│   ├── consultation.py         # Consultation model
│   └── prescription.py         # Prescription model
├── ui/
│   ├── main_window.py          # Main window
│   ├── patient_dialog.py       # Patient dialog
│   ├── consultation_dialog.py  # Consultation dialog
│   └── prescription_dialog.py  # Prescription dialog
├── utils/
│   ├── validators.py           # Input validation
│   └── pdf_generator.py        # PDF reports
├── README.md                   # This file
└── GETTING_STARTED.md          # Detailed guide
```

## 💊 Supported Homeopathic Potencies

- **6C, 6X** - Low potency (acute)
- **12C, 12X** - Medium potency
- **30C, 30X** - High potency (chronic)
- **200C, 200X** - Very high potency
- **1M, 10M, CM** - Ultra-high potency

## 🔧 Technology Stack

- **Framework**: PyQt6 (Desktop GUI)
- **Database**: SQLite3
- **Language**: Python 3.8+
- **Reporting**: ReportLab (PDF generation)
- **Data Handling**: Pandas

## 🎨 Features by Tab

### Patients Tab
- Search patients by name or phone
- Add new patient records
- Edit existing patient information
- Delete patient records
- View complete medical history
- Quick access to all patient data

### Consultations Tab
- Record new consultations
- Document symptoms and findings
- Store vital signs
- Add diagnosis and observations
- Maintain consultation history
- Link to patient records

### Prescriptions Tab
- Create prescriptions
- Track medication history
- Generate PDF prescriptions
- Manage dosage and frequency
- Store manufacturer details
- Track medicine pricing

## 📊 Database

SQLite database location:
- **Windows**: `C:\Users\<username>\.homeopathy_app\homeopathy.db`
- **macOS/Linux**: `~/.homeopathy_app/homeopathy.db`

Database includes tables for:
- Patients
- Medical History
- Consultations
- Prescriptions
- Recommendations
- Medicines Master

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed
- Verify all dependencies: `pip install -r requirements.txt`
- Check write permissions in home directory

### Database errors
- Application creates database automatically
- If corrupted, delete `~/.homeopathy_app/homeopathy.db`
- Application will recreate on next start

### PyQt6 issues
- Try: `pip install --upgrade PyQt6`
- On Linux: `sudo apt-get install python3-pyqt6`

## 🚀 Future Enhancements

- [ ] Cloud backup system
- [ ] Mobile app
- [ ] Multi-user login
- [ ] Appointment reminders
- [ ] Billing system
- [ ] Advanced analytics
- [ ] Telemedicine integration
- [ ] SMS/Email notifications
- [ ] Lab integration
- [ ] Medicine inventory management

## 📄 License

MIT License - See LICENSE file for details

## 👨‍💻 Author

**Nikunj Kanjariya**
- GitHub: [@Nikunjkanjariya](https://github.com/Nikunjkanjariya)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/Nikunjkanjariya/homeopathy-doctor-app/issues)
- Check [GETTING_STARTED.md](GETTING_STARTED.md) for detailed guide
- Review existing documentation

---

**Made with ❤️ for homeopathy practitioners**
