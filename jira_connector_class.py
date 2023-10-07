import requests
import typing
import pydantic
import traceback





class UserValidateResult(typing.NamedTuple):
    """Global User configuation, NameTupple"""

    success: bool
    container: dict
    error: pydantic.ValidationError
    trace: None



class JiraConnector:
    def __init__(self, **kwargs):
        self.hostname = kwargs.get('hostname')
        self.api_token = kwargs.get('api_token')
        self.admin_email = kwargs.get('admin_email')


    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        'Accept-Charset': 'UTF-8'
    }



    def get_last_id(self):
        try:
            url = f'https://{self.hostname}/rest/backup/1/export/lastTaskId'

            resp = requests.get(
                url, 
                auth=(self.admin_email, self.api_token),
                headers=self.headers
            )

            if resp.status_code == 200:
                return UserValidateResult(True, container=resp, error=None, trace=None)
            else:
                print(f'Response code = {resp.status_code}')
                print(f'Response text = {resp.text}')
                return UserValidateResult(False, container=resp, error=resp.text, trace=None)
        except Exception as e:
            return UserValidateResult(False, container=None, error=None, trace=e)



    def get_process(self, task_id):

        print(f'Last task_id = {task_id}')
        url = f'https://{hostname}/rest/backup/1/export/getProgress?taskId={task_id}'

        resp = requests.get(
            url, 
            auth=(admin_email, api_token2),
            headers=headers
        )

        return resp 


    def download_file(self, filename_to_download):
        print(f'Now download file: {filename_to_download}')


        resp = requests.get(
            filename_to_download,        
            auth=(admin_email, api_token2),
            headers=headers,
            stream=True)

        # with open(backup_filename, 'wb') as f:
        #     for chunk in resp:
        #         f.write(chunk)

        pbar = tqdm(
                desc=backup_filename, 
                total=int(resp.headers.get('content-length', 0)),
                unit='B', 
                unit_scale=True, 
                unit_divisor=1024
                )

        with open(backup_filename, 'wb') as f:
            for data in resp.iter_content(chunk_size=1024):
                f.write(data)
                pbar.update(len(data))

        pbar.close()
    
