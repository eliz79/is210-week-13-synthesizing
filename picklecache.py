#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""

import os
import pickle

class PickleCache(object):

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Docstring."""
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.__file_object = None
        
    def __setitem__(self, key, value):
        """Docstring."""
        self.__data[key] = value
        if self.autosync is not False:
            self.flush()
                   
    def __len__(self):
        """Docstring."""
        return len(self.__data)
    
    def __getitem__(self,key):
        try:
            return self.__data[key]
        except TypeError or KeyError:
            raise KeyError
        
