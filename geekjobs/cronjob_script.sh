#!/usr/bin/env bash
# */10 * * * * bash /home/django/geekjobs.git/geekjobs/cronjob_script.sh
set -x

TIMESTAMP="$(date +%Y-%m-%d-%H:%M:%S)"
LOG=/tmp/geekjobs_job.log

print_command_output()
{
if [ $? -eq 0 ]; then
    echo "[GEEKJOBS ${TIMESTAMP}] OK" >> ${LOG}
else
    echo "[GEEKJOBS ${TIMESTAMP}] FAIL" >> ${LOG}
fi
}


echo "######### START RUNNING SCRIPT ${TIMESTAMP} ##########" >> ${LOG}
# set path
PATH=/home/frevilla/bin:/home/frevilla/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
export PATH
# execute command
source /home/django/geekjobs.git/geekjobs/settings/secrets.sh
python3 /home/django/geekjobs.git/manage.py parse_jobs
chown django:django /home/django/geekjobs.git/geekjobs/stackoverflow_jobs.json
# log output
print_command_output
echo "######### STOP RUNNING SCRIPT ${TIMESTAMP} ##########" >> ${LOG}
