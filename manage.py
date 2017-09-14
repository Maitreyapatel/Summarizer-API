#!/usr/bin/env python3
import os
import sys


class MyDict(dict):
    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        return 0

if __name__ == "__main__":



    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

