import enum

BASE_URL = "https://p.grabtaxi.com"
MAX_RETRIES = 5
BACK_OFF = 0.5

LAT = 1.2791398397204945
LNG = 103.83517246501242

# maximum concurrent network requests at a time
LIMIT = 10

class ENDPOINT(enum):
    RESTAURANTS = "/api/passenger/v3/grabfood/category?latlng={lat}%2C{lng}&categoryShortcutID={category_id}&offset={offset}&poiID=IT.264BA9AKW4BGF"
    RESTAURANT = "/api/passenger/v4/grabfood/merchants/{restaurant_id}?latlng={lat}%2C{lng}&poiID=IT.264BA9AKW4BGF"

class CATEGORY(enum):
    NEARBY = "5047"
    BESTSELLER = "4171"

HEADERS = {
    "x-mts-ssid": "eyJhbGciOiJSUzI1NiIsImtpZCI6Il9kZWZhdWx0IiwidHlwIjoiSldUIn0.eyJhdWQiOiJQQVNTRU5HRVIiLCJlc2kiOiJDaW94bmVJdFVOK3FTSkhMSjNtZFV3MkdOZDFyRitpWjl2RlUxRjJDZEo5UTBvRkZjUT09IiwiZXhwIjo0ODI3MDIwODE3LCJpYXQiOjE2NzM0MjA4MTQsImp0aSI6IjYxNGIzNzU4LTdkNGEtNGRjZS05OTdjLWRhYjg3ZTg0M2EzOSIsImxtZSI6IlBIT05FTlVNQkVSIiwibmFtZSI6IiIsInN1YiI6ImMzNDRjZjNjLTc5ZTktNDE3OC04YjE3LWZhYjk0MThmMDM2NiJ9.EdhxqJNLs5n71kh96FqZyov4-T6rRfe2bcfGTiiuT2vy-BqQA8sdf5b17X1tHp1Yd5hIW06_bOn0-6DhnZYuNEWnDHUotjoTLPU0HWGEh_I8HS92Qsk9PY-uctGA6TfI1eF03cKlbTpxl76AunFV8JpBD_M2yCXJ9rjiYSrvr-nVROdJkqEwoTv3owy_K8vCWshrRqodlm8Sjt480MbQ7Ax7QRqSnxNidXuwfhYacdFkWAdxix3P9wRkt8LJgxSEsET7zy4VwvF3k-E_Gi4YA8j-JVlHOX6BARAJ6yI0L0r_nmSkyafKNG7jp7OBF_H-GsqO-gcd1pUkKGqqcyyp6dRNJrYRbDCL-bvLuyNgpMKjv-kkgYoB2KFweR3mA28GmqxH3yQdopYnMTX1IAsARgPIzBg5pieI-CUcDwzyaJkEHq1goxR4IJQQbR9jxeTsGMpJv2hMeuKkDYr9m13M8TVPAR5D-tjahlNdaqRH2D1sdUlwO_7YgeZYvGVpQaNOQS-JDPLT2gAjkfPuWMr5n7uBCdioiny-pFatMBDscsW9Jy376zhqjqTGxwaFm-thd2OWMhG4RDu0a432QyO9zyVimrIasnp2--EP3EjsKPAfj6nS0ZZ9ngtVTMG9cnPFXVXgc3AXcP9xVQW5IRfzMNy8HK7q53EHHPVh-4COeSk",
    "user-agent": "Grab/5.233.2 (Android 10; Build 42174715)"
}