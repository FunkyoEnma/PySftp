import os
from socket import socket
from typing import Optional, Dict, Iterable, Union, Text

from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
from paramiko.common import o777
from paramiko.config import SSH_PORT
from paramiko.pkey import PKey
from paramiko.sftp_client import SFTPClient


class Connect(SSHClient, SFTPClient):
    def __init__(self,
                 hostname=None,
                 port=SSH_PORT,
                 username=None,
                 password=None,
                 pkey=None,
                 key_filename=None,
                 timeout=None,
                 allow_agent=True,
                 look_for_keys=True,
                 compress=False,
                 sock=None,
                 gss_auth=False,
                 gss_kex=False,
                 gss_deleg_creds=True,
                 gss_host=None,
                 banner_timeout=None,
                 auth_timeout=None,
                 gss_trust_dns=True,
                 passphrase=None,
                 disabled_algorithms=None, ):
        super(Connect, self).__init__()

        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        self.__pkey = pkey
        self.__key_filename = key_filename
        self.__timeout = timeout
        self.__allow_agent = allow_agent
        self.__look_for_keys = look_for_keys
        self.__compress = compress
        self.__sock = sock
        self.__gss_auth = gss_auth
        self.__gss_kex = gss_kex
        self.__gss_deleg_creds = gss_deleg_creds
        self.__gss_host = gss_host
        self.__banner_timeout = banner_timeout
        self.__auth_timeout = auth_timeout
        self.__gss_trust_dns = gss_trust_dns
        self.__passphrase = passphrase
        self.__disabled_algorithms = disabled_algorithms

        self.__open = None

    def start(self):
        self.connect(self.__hostname,
                     self.__port,
                     self.__username,
                     self.__password,
                     self.__pkey,
                     self.__key_filename,
                     self.__timeout,
                     self.__allow_agent,
                     self.__look_for_keys,
                     self.__compress,
                     self.__sock,
                     self.__gss_auth,
                     self.__gss_kex,
                     self.__gss_deleg_creds,
                     self.__gss_host,
                     self.__banner_timeout,
                     self.__auth_timeout,
                     self.__gss_trust_dns,
                     self.__passphrase,
                     self.__disabled_algorithms)

        self.__open = self.open_sftp()

        return self.__open

    def exist(self, path: str):
        __open = self.__open
        try:
            __open.stat(path)
            return True
        except FileNotFoundError:
            return False

    def makedir(self, path: Union[bytes, Text]) -> None:
        print(path.split(self.getcwd()))

    def getcwd(self) -> Optional[Text]:
        return self.__open.getcwd()


sftp = Connect("192.168.10.15", username="root", password="eseusdi*1&")
sftp.set_missing_host_key_policy(AutoAddPolicy())
sftp.load_system_host_keys()
sftp.start()
sftp.makedir("/home/datos/backup/usuarios/Funkyo/test/multiples/folders/one/inside/the/other")
print(sftp.getcwd())
sftp.close()