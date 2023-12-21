from requests import request as http_request
from time import sleep
from getcourse_export_api.exceptions import GetcourseApiError


class Getcourse:
    def __init__(self, account_name: str, secret_key: str):
        self.account_name = account_name
        self.__secret_key = secret_key
        self._api_base_url = f'https://{account_name}.getcourse.ru/pl/api'
        self._critical_api_error_codes = (
            903,  # Слишком много запросов
        )

    def _make_request(self, url, filters=None, delay=10):
        if filters:
            params = {
                'key': self.__secret_key,
                **filters
            }
        else:
            params = {
                'key': self.__secret_key
            }

        while True:
            response = http_request('GET', url=url, params=params)

            if response.status_code == 200:
                response_json = response.json()
                success = response_json.get('success', False)
                error = response_json.get('error', False)
                error_code = response_json.get('error_code', None)

                if success:
                    return response_json
                elif error and error_code in self._critical_api_error_codes:
                    raise GetcourseApiError(response_json)
                else:
                    # TODO: реализовать логику увеличения времени задержки при большем количестве попыток запроса
                    sleep(delay)
            else:
                GetcourseApiError(response.text)

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

    def export(self, action: str, filters: dict):
        base_url = '/'.join([self._api_base_url, 'account'])
        action_url = '/'.join([base_url, action])

        # Запуск задачи на сбор данных
        action_response = self._make_request(action_url, filters)
        export_id = str(action_response.get('info', {}).get('export_id', 0))
        export_url = '/'.join([base_url, 'exports', export_id])

        # Запрос на экспорт данных
        export_response = self._make_request(export_url)
        return export_response
