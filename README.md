# MediCode System Design

MediCode is a recording keeping service for health care sector.

## Requirements of the System

- A patient can sign up to the system using USSD.
- A health institution can sign up to to the service from the website and recieve a unique ID.
- A doctor can view a patient's records from the system, using the patient's unique ID.

- A patient recieves message reminders about their prescriptions and appointments.

## Database Schema
### Patient Model 
- ID, Name, PhoneNumber

### Institution Name
- Name, UID

### Health Record
- patientID, institutionID, date, prescription, diagnosis

## Frontend Dashboard

- Institution signup/signin. Authentication
- Access patient's records
    - Input the patient's ID
    - Fetch records
- Display patient's records
- Add a record
