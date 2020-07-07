from crontab import CronTab

cron = CronTab(user="benjamin")
job = cron.new(
    command='cd /home/benjamin/Documents/projects/unscrap && /home/benjamin/Documents/projects/unscrap/env/bin/python /home/benjamin/Documents/projects/unscrap/main.py')
job.minute.every(1)

cron.write()


class Cron():

    def __init__(self):
