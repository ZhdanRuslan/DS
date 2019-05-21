import datetime as dt

from currency_retrieve.backends import NbuBackend
from currency_retrieve.backends.exceptions import InvalidBackendAlias

class CurrencyService:
    backends = {
        NbuBackend.alias: NbuBackend,
    }

    def downloaad(self, backend_alias, start_date, end_date, currencies = None):
        backend_cls = self.backends.get(backend_alias, None)
        if backend_cls is None:
            raise InvalidBackendAlias('Invalid backend alias: {}'.format(backend_alias))




service = CurrencyService()
end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=3)
data = service.downloaad('nbu_test', start_date, end_date)