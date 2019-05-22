import datetime as dt

from currency_retrieve.backends import NbuBackend, PrivatBackend
from currency_retrieve.exceptions import InvalidBackendAlias, CurrencyRetrieveException


class CurrencyService:
    backends = {
        NbuBackend.alias: NbuBackend,
        PrivatBackend.alias: PrivatBackend,
    }

    def download(self, backend_alias, start_date, end_date, currencies=None):
        backend_cls = self.backends.get(backend_alias, None)
        if backend_cls is None:
            raise InvalidBackendAlias('Invalid backend alias: {}'.format(backend_alias))

        backend = backend_cls()
        result = backend.extract(start_date, end_date, currencies)

        return result


service = CurrencyService()

end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=3)

try:
    data = service.download('nbu', start_date, end_date)
    privat_data = service.download('privat', start_date, end_date)
except InvalidBackendAlias as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(data)
    print(privat_data)
finally:
    print('finally')
