from source.daily_logs.resources import DailyLogListResource, DailyLogResource


def initialize_routes(api):
    api.add_resource(DailyLogListResource, "/daily-logs")
    api.add_resource(DailyLogResource, "/daily-logs/<string:daily_log_id>")
