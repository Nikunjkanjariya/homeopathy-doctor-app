from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from datetime import datetime
from utils.analytics import Analytics

def generate_analytics_report():
    """
    Generate comprehensive analytics and business report
    """
    filename = f"analytics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=30,
        alignment=1
    )
    
    # Header
    elements.append(Paragraph("PRACTICE ANALYTICS REPORT", title_style))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Key Metrics
    elements.append(Paragraph("Key Performance Indicators", styles['Heading2']))
    
    metrics_data = [
        ['Metric', 'Value'],
        ['Total Patients', str(Analytics.get_total_patients())],
        ['Total Consultations', str(Analytics.get_total_consultations())],
        ['Total Prescriptions', str(Analytics.get_total_prescriptions())],
        ['Total Revenue', f"₹ {Analytics.get_total_revenue():,.2f}"],
        ['Pending Payments', f"₹ {Analytics.get_pending_payments():,.2f}"],
        ['This Month Consultations', str(Analytics.get_this_month_consultations())],
        ['This Month Revenue', f"₹ {Analytics.get_this_month_revenue():,.2f}"],
        ['Upcoming Appointments', str(Analytics.get_upcoming_appointments_count())],
        ['Today Appointments', str(Analytics.get_today_appointments_count())]
    ]
    
    metrics_table = Table(metrics_data, colWidths=[3*inch, 2*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
    ]))
    
    elements.append(metrics_table)
    elements.append(Spacer(1, 0.4*inch))
    
    # Top Medicines
    elements.append(Paragraph("Top 10 Prescribed Medicines", styles['Heading2']))
    
    top_medicines = Analytics.get_top_medicines()
    medicines_data = [['Medicine Name', 'Prescription Count']]
    for medicine in top_medicines:
        medicines_data.append([medicine['medicine_name'], str(medicine['count'])])
    
    if len(medicines_data) > 1:
        medicines_table = Table(medicines_data, colWidths=[3*inch, 2*inch])
        medicines_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        elements.append(medicines_table)
    else:
        elements.append(Paragraph("No prescription data available.", styles['Normal']))
    
    elements.append(Spacer(1, 0.4*inch))
    elements.append(PageBreak())
    
    # Top Patients
    elements.append(Paragraph("Patient Visit Frequency (Top 20)", styles['Heading2']))
    
    patient_visits = Analytics.get_patient_visit_frequency()
    patient_data = [['Patient Name', 'Visit Count']]
    for patient in patient_visits:
        name = f"{patient['first_name']} {patient['last_name']}"
        patient_data.append([name, str(patient['visits'])])
    
    if len(patient_data) > 1:
        patient_table = Table(patient_data, colWidths=[3*inch, 2*inch])
        patient_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
        ]))
        elements.append(patient_table)
    else:
        elements.append(Paragraph("No patient data available.", styles['Normal']))
    
    # Build PDF
    doc.build(elements)
    return filename

def generate_billing_report(start_date=None, end_date=None):
    """
    Generate billing and revenue report
    """
    filename = f"billing_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=30,
        alignment=1
    )
    
    # Header
    elements.append(Paragraph("BILLING & REVENUE REPORT", title_style))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Summary
    elements.append(Paragraph("Financial Summary", styles['Heading2']))
    
    summary_data = [
        ['Metric', 'Amount'],
        ['Total Revenue (Paid)', f"₹ {Analytics.get_total_revenue():,.2f}"],
        ['Pending Payments', f"₹ {Analytics.get_pending_payments():,.2f}"],
        ['This Month Revenue', f"₹ {Analytics.get_this_month_revenue():,.2f}"]
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    
    elements.append(summary_table)
    
    # Build PDF
    doc.build(elements)
    return filename
