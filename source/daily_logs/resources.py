from flask_restful import Resource
from flask import request

from source.daily_logs.crud import (add_daily_log, retrieve_daily_logs, retrieve_daily_log, update_daily_log,
                                    delete_daily_log)


class DailyLogListResource(Resource):
    def get(self):
        return retrieve_daily_logs()

    def post(self):
        data = request.json
        return add_daily_log(data)


class DailyLogResource(Resource):
    def get(self, daily_log_id):
        return retrieve_daily_log(daily_log_id)

    def put(self, daily_log_id):
        data = request.json
        return update_daily_log(daily_log_id, data)

    def delete(self, daily_log_id):
        return delete_daily_log(daily_log_id)
