import requests
import json

from python.src.bandopenapi import models


class BandOpenApi:
    def __init__(self):
        print('init')
        self.access_token = '...'

    def check_env(self):
        print('check_env')

        print('http call test')
        result = requests.get('https://naver.com')
        print(result)

    def call(self):
        self.check_env()
        self.get_profile()

    def get_profile(self) -> models.Profile:
        # 사용자 정보 조회
        # https://developers.band.us/develop/guide/api/get_user_information

        api_call_result = requests.get('https://openapi.band.us/v2/profile',
                     {'access_token' : self.access_token})
        if not api_call_result.ok:
            print(f'[get_person_info] api call fail. api call result : {api_call_result}')
            return None

        api_call_result_json = json.loads(api_call_result.text)
        if 'result_code' not in api_call_result_json or 'result_data' not in api_call_result_json:
            print(f'[get_person_info] api call result structure malformed. api call result json : {api_call_result_json}')
            return None

        api_call_result_json_result_data = api_call_result_json['result_data']
        profile = models.Profile(**api_call_result_json_result_data)
        print(f'[get_person_info] profile : {profile}')
        return profile

    def get_bands(self):
        pass

