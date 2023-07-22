#!/usr/bin/env python3

from argparse import ArgumentParser
import os
import sys
import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler


def generate_expfmt(namespace):
    path = namespace.path

    if not path:
        return 
    if path.endswith("/"):
        path = path[:-1]
        
    for script in os.listdir(path=path):
        if not path.endswith(".prom"):
            command = f"{path}/{script}"
            print(f"script triggerd by side-car: {command}")
            execute = subprocess.run(command, shell=True, env=os.environ)
            if execute.returncode == 0:
                print(f"script run successed: {command}")
            else:
                print(f"script triggered fail {command}", file=sys.stderr)

if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument('--path', help='execute python directory', default="/app/collector")
    ap.add_argument('--destpath', help='output .prom directory', default="/run/prometheus")
    namespace = ap.parse_args()
    os.environ['PROM_DIRCTORY'] = namespace.destpath

    scheduler = BlockingScheduler()
    scheduler.add_job(generate_expfmt, 'interval', args=[namespace], seconds=15)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
         