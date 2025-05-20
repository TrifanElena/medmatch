@echo off                    
cd /d C:\Users\elena\medical-platform   
call venv\Scripts\activate               
python manage.py send_reminders >> send_reminders.log 2>&1   
