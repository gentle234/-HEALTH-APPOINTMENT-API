#
PROJECT TITLE: CyberMed Healthcare Appointment System

#
PROJECT OVERVIEW
CyberMed is a Django-based healthcare appointment system, that enable Scheduling, 
and Booking of appointments between Doctors and Patients. The system handles user authentication
with custom roles for Doctor and Patients. Doctors are able to schedule appointments with patients,
while patients are able to book appointments with doctors. The application is structured such that 
there is no conflicing scheduling and booking time between the patient and doctors. Upon Scheduling
or Booking an appointment, the application indicated the appointment status, whether it be pending,
confirmed,completed or cancled.

#
PROJECT FEATURES
* User Authentication:JWT-based authentication using Django-based Rest Framework(DRF) with role-based access (Doctor or Partient).
* Role-Specific Behaviour: Users can update their profiles based on their roles.
* Management/Validation: Patients can book appointments with available doctors. Doctors can schedule appointments, with their patients.
The application doesn't allow for double booking or scheduling from either patients or doctors.
* RESTful API: The entire system is built using RESTful APIs for easy integration with front-end systems or mobile applicaions.
* User-Friendly: Automatically assigns the authenticated user's role(patients or doctors) without requiring the manual input of their ID.

* Tech Stack Backend: Django 5.1, Django Rest Framework (DRF) 
* Authentication: JWT (via djangorestframework-simplejwt) 
* Database: SQLite (can be swapped with PostgreSQL/MySQL) 
* Other Dependencies: Pillow (for image handling), django-use-email-as-username (for handling on-boarding process)

#
API Endpoints Authentication 
* Register: POST /api/auth/register/ Register as a doctor or patient.
* Login: POST /api/auth/login/ Obtain a JWT token by providing your credentials (email and password).
* Token Refresh: POST /api/auth/login/refresh/ Refresh your JWT token.
* Doctors Doctor Profile Creation: POST /api/doctor-profile/ Create or update a doctor's profile (Requires authentication as a doctor). 
* Patients Patient Profile Creation: POST /api/patient-profile/ Create or update a patient’s profile (Requires authentication as a patient).
* Appointments List Appointments: GET /api/appointments/ List all appointments for the authenticated user (patients see their own appointments, doctors see theirs).
* Create Appointment: POST /api/appointments/ Book an appointment (patients) or schedule an appointment (doctors).

#
MODELS STRUCTURE
User Model (Custom) Fields: email, password, first_name, last_name, is_doctor, is_patient, gender 
* Description: Base user model that supports both doctors and patients.
Doctor Model Fields: user, specialty, phone_number, experience_years 
* Description: Links a user to a doctor profile, containing their specialty, phone number, and years of experience.
Patient Model Fields: user, date_of_birth, address, emergency_contact_name, emergency_contact_phone 
* Description: Links a user to a patient profile, containing personal and emergency contact details. 
Appointment Model Fields: doctor, patient, date, time, reason_for_visit, status 
* Description: Represents an appointment between a doctor and a patient, with automatic validation to prevent double booking.

#
Validation and Constraints 
* Doctor Scheduling: A doctor cannot schedule multiple appointments for the same date and time. 
* Patient Booking: A patient can only book with available doctors, and cannot book multiple appointments at the same time slot. 
* Status Choices: The Appointment model includes a status field with choices (pending, confirmed, completed, cancelled).
