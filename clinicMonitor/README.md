# Clinicians Monitoring
## Setup
1) Install Django: `python -m pip install Django` or `python3 -m pip install Django`
2) Download & Install PostgreSQL (for Mac) from: https://postgresapp.com/downloads.html
3) Initialize your psql database
4) Head over to **clinicMonitor/settings.py** and find the **# Database** section, then update the content of `NAME`, `USER`, `PORT` according to your running psql database. (Refer: https://medium.com/cloud-tidbits/setup-django-with-postgres-app-on-macos-for-django-tutorials-22ed4dabfaf4)

## Demo flow
- Setup PostgreSQL as database
- Run `python manage.py runserver` or `python3 manage.py runserver` in "clinicians_monitoring/clinicMonitor/" dictionary.
- Login administrator (http://localhost:8000/admin/), and register new Clinician into the system. (for demo the email alert function, recommand to use real email address in clinician registration.)
- Login clinicians (http://localhost:8000/users/clinicianLoginPage/)
- Click button "Register New Patient" to register new patient into the system.
- Once compleled the form and click button "Register", thresholds setting page will be fetched.
- After completed the thresholds setting for new patient, the patient's measurement detail page will be fetched.
- Click button "Back" to homepage of Clinician to see all the patients' latest reading, who assigned under the clinician.
- If there are any abnormal reading detect, the alert will be shown in the homepage (http://localhost:8000/measurements/clinicianViewMeasurements/<int:clinician_id>/) of the clinician

## Administrators
- Administrators web page: http://localhost:8000/admin/
- Administrators user name: admin
- Administrators password: Aa100200300
- <ins>The administrator can register new clinician accounts into the system</ins>
- (for demo the email alert function, recommand to use real email address in clinician registration.)

## Clinicians
- <ins>Clinicians can register new patient accounts into the system</ins> by using `/users/registerPatientPage/<int:clinician_id>/`
- <ins>Clinicians can see a table of patients, who they registered, with their latest measurements</ins> and <ins>Abnormal readings will generate an alert for clinicians to review</ins> by using `/measurements/clinicianViewMeasurements/<int:clinician_id>/`
- <ins>Clinicians can view a patient dashboard showing history of patient measurements and alerts</ins> by using `/measurements/clinicianViewPatientDetail/<int:clinician_id>/<int:patient_id>/`
- <ins>Clinicians can set thresholds to detect abnormal measurements for each patient</ins> by using `/thresholds/setThresholdsPage/<int:patient_id>/`
- 

## Patients
- <ins>Patients can submit measurements via API</ins> by using `/measurements/fillInMeasurementPage/<int:patient_id>/`
- <ins>Patients can view historical measurements via API</ins> by using `/measurements/patientViewMeasurement/<int:patient_id>/`
- <ins>Clinicians will be notified via email when an alert is generated</ins> after the patient submitted the measurements, the system will automatically check whether the measurements are abnormal or not. If abnormal found, an alert email will be sent to corresponding clinician's email.
