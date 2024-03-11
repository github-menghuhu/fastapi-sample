from uuid import uuid4, UUID


def get_random_uuid() -> UUID:
    """
    获取随机uuid
    :return:
    """
    return uuid4()
