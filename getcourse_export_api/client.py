import requests
import time

from getcourse_export_api.exceptions import GetcourseApiError


BASE_URL = 'https://{account_name}.getcourse.ru/pl/api'


class Getcourse:
    def __init__(self, account_name: str, secret_key: str):
        self.account_name = account_name
        self._secret_key = secret_key
        self._api_base_url = BASE_URL.format(account_name=account_name)

    def _send_request(self, url, filters=None, delay=5, attempts=5):
        if filters:
            params = {
                'key': self._secret_key,
                **filters
            }
        else:
            params = {
                'key': self._secret_key
            }

        response = requests.request('GET', url=url, params=params)

        if response.status_code == 200:
            response_json = response.json()
            success = response_json.get('success', False)

            if success:
                return response_json
            elif attempts > 0:
                attempts = attempts - 1
                time.sleep(delay)

                return self._send_request(url, filters, delay, attempts)
            else:
                raise GetcourseApiError(response.content)
        else:
            attempts = attempts - 1
            time.sleep(delay)

            return self._send_request(url, filters, delay, attempts)

    @staticmethod
    def normalize_response(data):
        normalize_result = []

        info = data.get('info', {})
        column_headers = info.get('fields', [])
        rows = info.get('items', [])

        for row in rows:
            normalize_dict = {
                header: value for header, value in zip(column_headers, row)
            }

            normalize_result.append(normalize_dict)

        return normalize_result

    def export(self, action: str, filters: dict, delay: int = 30):
        base_url = '/'.join([self._api_base_url, 'account'])
        action_url = '/'.join([base_url, action])

        # Запуск задачи на сбор данных
        action_response = self._send_request(action_url, filters, attempts=1)
        export_id = str(action_response.get('info', {}).get('export_id', 0))
        export_url = '/'.join([base_url, 'exports', export_id])

        # Запрос на экспорт данных
        export_response = self._send_request(export_url, delay=delay)
        return export_response
