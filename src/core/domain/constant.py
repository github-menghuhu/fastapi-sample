from dataclasses import dataclass


@dataclass(frozen=True)
class ResponseCode:
    """
    自定义响应码
    """
    request_success = 2000
    create_success = 2001
    update_success = 2002
    delete_success = 2003
    request_error = 4000

    pass


@dataclass(frozen=True)
class ResponseMessage:
    """
    自定义响应信息
    """
    request_success = '请求成功。'
    create_success = '创建成功。'
    update_success = '更新成功。'
    delete_success = '删除成功。'
    request_error = '请求异常。'

    pass
