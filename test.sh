#!/bin/bash
echo "Hello! Welcome to your first shell script."
source /d/Max_Spacer/Documents/My_web_projects/prod_parting_project/.venv/Scripts/activate
#cd /d/Max_Spacer/Documents/My_web_projects/prod_parting_project
python /d/Max_Spacer/Documents/My_web_projects/prod_parting_project/manage.py db_worker --reload