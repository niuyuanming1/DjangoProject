"""
结果管理
"""
class ResultManage:
    def __init__(self, status_code=0, content=object):
        self.status_code = status_code
        self.content = content