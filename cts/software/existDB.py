#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..db import DB
from .. import shell
import os


class ExistDB(DB):
    """Implementation of DB for ExistDB"""
    def __init__(self, software, version, source, path, target="./", user=None):
        super(ExistDB, self).__init__(software=software, version=version, source=source, path=path, target=target, user=user)

    def setup(self):
        """ Returns a string to do a cmd """
        return [
            shell.Separator(),
            shell.Helper("java -jar {0} -console".format(self.file.path)),
            shell.Request("Select target path [{0}]".format(os.path.abspath(__file__))),
            shell.Parameter("{0}".format(self.file.directory + "/conf")),
            shell.Request("Data dir:  [webapp/WEB-INF/data]"),
            shell.Parameter("{0}".format(self.file.directory + "/data")),
            shell.Request("Enter password: []"),
            shell.Parameter("Secured password or simply [password]"),
            shell.Request("Enter password: []"),
            shell.Parameter("Password entered previously"),
            shell.Warning("Remind the password you are gonna enter !"),
            shell.Request("Maximum memory in mb: [1024]"),
            shell.Parameter("1024"),
            shell.Request("Cache memory in mb: [128]"),
            shell.Parameter("128")
        ]

    def start(self):
        return [shell.Helper("/home/thibault/dev/CTS-API/build/build_dir//db/conf/bin/startup.sh")]

    def stop(self):
        print (self.user)
        if self.user.password:
            return [shell.Command("/home/thibault/dev/CTS-API/build/build_dir//db/conf/bin/shutdown.sh -p {0}".format(self.user.password))]
        else:
            return [shell.Command("/home/thibault/dev/CTS-API/build/build_dir//db/conf/bin/shutdown.sh")]