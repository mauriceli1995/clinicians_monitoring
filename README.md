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

# Questions

1. If you had more time, what would you change or focus more on?
- Discover more edge cases and improve the system performance.
- Better UI design.

2. Which part of the solution consumed the most amount of time?
- Since it is my first time to develop application via Django, spent few days to learn it.
- I knew how to develop application with trandition way, so it takes time for me to "convert" old way to the Django method.
- Handling the "OneToOneField" is the most challenge on me, because we need to handle two situations of it, e.g. if the data is not in database or there is data already in the database.
  
3. What suggestions do you have for stakeholders in this context that they may not have thought of?
- There is no function about updating personal information, like the email address and password. And in this user story, clinicians gain their account and password from the admin, and patients received their login information from clinicians, which is a security bug.
- To create auth countdown after the user login success. For example, if the user does not do any operation after login, around 15 min, then the system should logout the user automatically.

