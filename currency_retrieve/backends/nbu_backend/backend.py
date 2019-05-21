import requests
import datetime as dt
# from ..base import BackendBase as CustomBaseBackend
from currency_retrieve.backends.base import BackendBase


class NbuBackend(BackendBase):
    alias = 'nbu'
    api_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json'

    def extract(self, start_date, end_date, currencies=None):
        assert isinstance(start_date, dt.date), '`start date` must be type `date`'
        assert isinstance(end_date, dt.date), '`end date` must be type `date`'

        min_date = min(start_date, end_date)
        max_date = max(start_date, end_date)


        next_date = min_date
        while True:
            self._download_data(next_date)
            next_date = next_date + dt.timedelta(days=1)
            if next_date > max_date:
                break

    def transform(self):
        pass

    def load(self):
        pass

    def _download_data(self, on_date):
        date_str = on_date.strftime('%Y%m%d')
        request_url = self.api_url.format(date=date_str)
        response = requests.get(request_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None