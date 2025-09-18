# EduBud: AI-Based Drop-Out Prediction and Counseling System

## Overview

**EduBud** is a consolidated digital dashboard designed to help educational institutes identify and support students at risk of dropping out. The system automatically ingests data from multiple sources (attendance, assessment scores, fee payments, etc.), applies rule-based and machine learning approaches to flag at-risk students, and provides timely notifications and intuitive visualizations for proactive intervention by mentors and guardians.

---

## Problem Statement

By the time term-end marks reveal failures, many struggling students have already disengaged. Early, data-driven intervention is crucial. However, data silos (attendance, test results, fee payment) hinder a unified view of student risk. Commercial analytics platforms are costly and complex.

**EduBud** offers a simple, transparent, and cost-effective solution:
- Merge existing spreadsheets and databases.
- Apply clear logic and machine learning to color-code risk.
- Notify mentors and guardians on a predictable schedule.
- Empower educators by providing actionable insights, not replacing their judgment.

---

## Key Features

- **Automated Data Ingestion**: Seamlessly combine attendance, grades, and other data from various spreadsheets or data sources.
- **Risk Identification**: Use configurable, rule-based thresholds and machine learning models to flag students at risk based on:
  - Falling attendance
  - Repeated subject failures
  - Declining test scores
  - Fee payment irregularities
- **Visual Dashboard**: Intuitive interface with color-coded risk indicators for each student.
- **Notifications System**: Automated alerts to mentors and guardians via email or preferred channels.
- **Configurable and Easy to Use**: Minimal training required; simple setup for non-technical users.
- **Transparent Logic**: Clear, auditable rules and ML models—no black boxes.
- **Privacy Respecting**: Designed for secure, local deployment in public institutions.

---

## How It Works

1. **Data Collection**
    - Upload or connect spreadsheets (attendance, grades, fees, etc.) via the dashboard.
2. **Data Fusion**
    - The system merges data using unique student identifiers.
3. **Risk Analysis**
    - Rule-based logic and ML models analyze trends and thresholds to compute risk scores.
4. **Visualization**
    - Dashboard displays students flagged as "At Risk" with clear, color-coded cues.
5. **Notification**
    - Mentors/guardians receive regular, actionable notifications.

---

## Technology Stack

- **Backend**: Python (Polars)
- **Frontend**: Streamlit for quick prototyping
- **Database**: Streamlit cloud
- **Notification**: Email (SMTP) or SMS integration

---

## Getting Started

### Prerequisites

- Python 3.8+ 
- pip (for Python dependencies)

---

## Usage

1. **Upload Data**: Go to the 'Data Upload' section and upload all relevant spreadsheets (attendance, grades, fees).
2. **Configure Thresholds**: Set risk thresholds in the 'Settings' panel (e.g., attendance below 75%, failing 2+ subjects, score decline >15%).
3. **View Dashboard**: Navigate to the 'Dashboard' to see risk visualizations.
4. **Check Notifications**: Mentors/guardians receive emails/SMS on scheduled intervals for identified at-risk students.

---

## Example Risk Rules

- **Attendance** < 75%
- **Score Drop**: Decrease by >15% over two assessments
- **Fee Default**: Delayed payment beyond 30 days
- **Subject Attempts**: More than 2 attempts in the same subject

---

## Customization

- **Edit risk rules** in the config file or via the dashboard.
- **Integrate new data sources** by adding connectors (see `data_ingestion/`).
- **Change notification channel** in settings.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- Built for the AI Hackathon 2025
- Inspired by the need for accessible, impactful EdTech solutions in public institutions

---

## Contact

For questions, support, or demo requests, please open an issue or contact [Dakshx-Gupta](https://github.com/Dakshx-Gupta).
