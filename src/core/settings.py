"""
全局配置文件
"""

import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# 全局时区
TIME_ZONE = "Asia/Shanghai"

# 全局密钥
SECRET = "ae98601a29e89b43bd17541a0beedc463c2d03b1b4c4f57adfa597ecf68f7b1e"

# jwt过期时间（单位秒）
JWT_LIFETIME_SECONDS = 60 * 60 * 24 * 7

# postgresql
POSTGRESQL_HOST = "127.0.0.1"
POSTGRESQL_USER = "postgres"
POSTGRESQL_PASSWORD = "123456"
POSTGRESQL_NAME = "fastapi-project"
IS_PRINT_SQL = True

# redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = "6379"
REDIS_PASSWORD = ""

# celery
CELERY_BROKER_DB = 15
CELERY_RESULT_DB = 14
CELERY_RESULT_EXPIRES = 60 * 60 * 24 * 7

# 其他媒体文件存放根路由
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
