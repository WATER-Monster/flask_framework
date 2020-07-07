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
