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

    def _make_request(self, url, filters=None):
        # Параметры для регулирования скорости выполнения запросов на экспорт
        retry_count = 0
        base_delay = 10

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
                    # Увеличение задержки с каждой неудачной попыткой
                    retry_count += 1
                    sleep(base_delay * retry_count)
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

        # Для получения пользователей по группе можно передать ID группы в фильтре (кастомное решение для этого метода)
        group_id = filters.pop('group_id', None)
        if group_id is not None:
            action_url = '/'.join([action_url, group_id, 'users'])

        # Запуск задачи на сбор данных
        action_response = self._make_request(action_url, filters)
        # API отдаёт сразу список всех групп, делать exports не нужно
        if action == 'groups' and group_id is None:
            return action_response
        export_id = str(action_response.get('info', {}).get('export_id', 0))
        export_url = '/'.join([base_url, 'exports', export_id])

        # Запрос на экспорт данных
        sleep(15)  # Даём время на формирование файла
        export_response = self._make_request(export_url)
        return export_response
