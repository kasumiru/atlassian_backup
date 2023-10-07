#!/usr/bin/python3 


import requests
import json
from pygments import highlight, lexers, formatters
import time 
from tqdm.auto import tqdm
from jira_connector_class import JiraConnector
from my_logger_class import MyLogger




with open('creds.json', 'r') as f:
    creds = json.load(f)



from dataclasses import dataclass
@dataclass
class class_parameters_collector:
    hostname: str = "NoUserNNAMME"
    admin_email: str = "NoUserEMMMAIL"
    api_token: str = "NOSCOPPE"


user_data = class_parameters_collector()



user_data.hostname = creds.get('domain')
user_data.admin_email = creds.get('admin_email')
user_data.api_token = creds.get('api_token')
user_data.today = time.strftime("%Y.%m.%d.%H.%M.%S")
user_data.backup_filename = f'JIRA-backup-{user_data.today}.zip'

log = MyLogger()


jc = JiraConnector(
    api_token=user_data.api_token, 
    admin_email=user_data.admin_email,
    hostname=user_data.hostname
)

log.print_resp(jc.get_last_id())





exit()











def start_backup():
    url = f'https://{hostname}/rest/backup/1/export/runbackup'
    data = { 
        "cbAttachments": "true", 
        "exportToCloud": "true"
    }

    resp = requests.post(
        url, 
        data=json.dumps(data), 
        auth=(admin_email, api_token2),
        headers=headers
    )

    return resp











def main():
    print(f'Start backup. response of start task: ')
    resp = start_backup()
    print_resp(resp)

    if resp.status_code != 200:
        print(f'Have error. see above')
            
        try:
            inp = input(f'Do You continue download OLD last backup filene from atlassian cloud server? \n')
            if inp != 'yes':
                print('exit now')
                exit(0)
        except (KeyboardInterrupt, SystemExit):
            print(f'\nExit: Ctrl+c pressed')
            exit()
        except Exception as e:
            print(f'exit with error: {e}')
            exit(1)



    last_id = get_last_id()

    if last_id:
        resp = get_process(last_id)
        print_resp(resp)

    if not resp.json().get('result', None):
        print(f'File not found, exit 1')
        exit(1)
    else:
        filename_to_download = resp.json().get('result')

    # print(f'Do You want download this backup file: "{filename_to_download}" ?')

    try:
        inp = input(f'Do You want download this backup file: "{filename_to_download}" ? yes/no\n')
        if inp != 'yes':
            print('exit now')
            exit(0)
    except (KeyboardInterrupt, SystemExit):
        print(f'\nExit: Ctrl+c pressed')
        exit()
    except Exception as e:
        print(f'exit with error: {e}')
        exit(1)

        
    url_file = "export/download/?fileId=658df623-2c73-4987-9251-b8b6666bb0fe"
    file_url_to_download = f'https://{hostname}/plugins/servlet/{url_file}'
    download_file(file_url_to_download)
    print(f'Download done, filename: {backup_filename}')


main()
