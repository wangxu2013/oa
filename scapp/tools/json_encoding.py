import json
import datetime
import decimal

class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)

class DateDecimalEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, decimal.Decimal):
            return float(obj)


