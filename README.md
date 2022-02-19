# clinicians_monitoring
The clinicians will be remotely monitoring the patients from a portal. This portal needs to be able to showcase patients' daily measurements (e.g., heart rate / blood pressure / weight). Measurements will be manually entered via a mobile app and then sent to our server APIs. If an abnormal reading is detected, clinicians will be able to see what happened via the web portal.

:heavy_check_mark:  Clinicians can register new patient accounts into the system

:heavy_check_mark: Administrators can register new clinician accounts into the system

:heavy_check_mark: Patients can submit measurements via API

:heavy_check_mark: Patients can view historical measurements via API

:heavy_check_mark: Clinicians can see a table of all patients with their latest measurements

:heavy_check_mark: Clinicians can view a patient dashboard showing history of patient measurements and alerts

:heavy_check_mark: Clinicians can set thresholds to detect abnormal measurements for each patient

:heavy_check_mark: Abnormal readings will generate an alert for clinicians to review

:heavy_check_mark: Clinicians will be notified via email when an alert is generated

:heavy_check_mark: Clinicians can only see patients that they registered themselves or are otherwise assigned to them

:heavy_check_mark: User management should be managed in a separate Django app

:heavy_check_mark: Measurements/Thresholds/Alerts should be managed in another separate Django app
