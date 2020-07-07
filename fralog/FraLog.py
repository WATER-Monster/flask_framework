# coding:utf-8

import logging
import logging.config
import datetime
import json
import os


# 第一步，创建一个logger
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = './fralog/mainlog.log'
if not os.path.exists(os.path.abspath(logfile)):
    os.mkdir("./fralog")
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
fmt = logging.Formatter("%(asctime)s - %(name)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(fmt)
ch.setFormatter(fmt)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)


def get_datetimes():
    dates = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return dates


def getConsoleLog():
    return Fralog().getFileLog()


def getFileLog():
    return Fralog().getFileLog()


class Fralog(object):
    _client_sys = None  # 系统日志
    _client_app = None  # app业务日志
    _app = ''

    def __init__(self):
        super(Fralog, self).__init__()

        """取消InfluxDB"""
        # self._client_app = InfluxDBClient(
        #     host=LOG_SERVER_IP, port=LOG_SERVER_PORT,
        #     username=LOG_SERVER_USER, password=LOG_SERVER_PWD,
        #     database='fra'
        # )
        # self._client_app.create_database(dbname='fra')
        #
        # self._client_sys = InfluxDBClient(
        #     host=LOG_SERVER_IP, port=LOG_SERVER_PORT,
        #     username=LOG_SERVER_USER, password=LOG_SERVER_PWD,
        #     database='syslog'
        # )
        # self._client_sys.create_database(dbname='syslog')

    def set_app(self, app=''):
        """设置app名称"""
        self._app = app
        return self

    def get_app(self, **args):
        """如果用户特别指定app名称，则使用用户指定的名称;
        否则，使用默认名称
        """
        if args.get('product_id') is not None:
            return args.get('product_id')
        else:
            return self._app

    def build_log(self, **args):
        """
        
        :param product_id: 
        :param args: 
        :return: 
        """
        ret = {
            "measurement": "log",
            "tags": {
            },
            "fields": {
            }
        }
        if args.get('msg') is not None:
            msg = args.get('msg')
            if isinstance(msg, dict):
                msg = json.dumps(msg)
            elif isinstance(msg, str):
                pass
            args['msg'] = msg

        keys = ['level', 'product_id', 'event']
        for key in keys:
            if args.get(key) is not None:
                level = args.get(key)
                ret['tags'][key] = level
                args.pop(key)

        for k in args:
            ret['fields'][k] = args[k]
        return ret

    def debug(self, msg, **args):
        logger.debug(msg)
        app = self.get_app(**args)

    def warn(self, msg, **args):
        logger.warning(msg)
        app = self.get_app(**args)

    def warning(self, msg, **args):
        logger.warning(msg)
        app = self.get_app(**args)

    def error(self, msg, **args):
        logger.error(msg)
        app = self.get_app(**args)

    def info(self, msg, **args):
        logger.info(msg)
        app = self.get_app(**args)

    def write_log(self, msg='', event='', product_id='', **args):
        pass

    def getFileLog(self):
        return self

    def getConsoleLog(self):
        return self
