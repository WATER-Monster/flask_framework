from datetime import timedelta

DEFAULT_SERVICE_NAME = "test"

#  跨域相关
CORS_HEADERS = ",".join([
    "Accept",
    "Accept-Language",
    "Content-Language",
    "Remote-Mac-Address",
    "Remote-Ip",
    "Content-Type",
    "Authorization",
    "Content-MD5",
    "Range",
    "x-dn-signature-method",
    "x-dn-api-version",
    "x-dn-download-size",
    "x-dn-body-raw-size",
    "x-dn-compress-type",
    "x-dn-date",
    "x-sgi-security-token"
])
CORS_RESOURCES = "*"
CORS_MAX_AGE = timedelta(minutes=30)

#  密钥
SECRET_KEY = b"32rd5.329j$#j3f"

#  token相关
TOKEN_NAME = "token"
TOKEN_EXPIRE_TIME = 20*60*60
TOKEN_ALGORITHM = "HS256"
TOKEN_ENCODE_TYPE = "utf-8"
TOKEN_HEADERS = {
    "alg": "HS256",
    "typ": "JWT"
}
PAYLOAD_PARAM = "name"

# mysql 相关
MAXCONNECTIONS = 20,  # 连接池允许的最大连接数，0和None表示不限制连接数
MINCACHED = 2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
MAXCACHED = 5,  # 链接池中最多闲置的链接，0和None不限制
MAXSHARED = 3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
BLOCKING = True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
MAXUSAGE = None,  # 一个链接最多被重复使用的次数，None表示无限制
SETSESSION = [],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
PING = 1,  # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
MYSQL_HOST = '127.0.0.1',
MYSQL_PORT = 3306,
MYSQL_USER = 'root',
MYSQL_PASSWORD = 'root',
MYSQL_DATABASE = 'test',
MYSQL_CHARSET = 'utf8'
