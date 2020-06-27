# -*- coding: utf-8 -*-
from telnetlib import Telnet
import json


class EnvStatus:

    def __init__(self):
        """检查测试机访问指定服务器的端口是否连通。

           包含：
            Jira:
            Testopia:
            Github:
            Jenkins:
            KnoxPortal:
        """
        self.ip = '8'
        self.jira_status = 0
        self.testopia_status = 0
        self.github_status = 0
        self.jenkins_status = 0
        self.knoxportal_status = 0

    def verify_status(self,url,port):
        try:
            tel = Telnet(url,port)
            tel.close()
            return 0
        except:
            return 1

e = EnvStatus()
print("++" + json.dumps(e.__dict__) + "++")






