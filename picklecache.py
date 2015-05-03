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
    
    def __getitem__(self, key):
        try:
            if self.__data[key]:
                return self.__data[key]
        except KeyError, TypeError:
            raise KeyError

    def __delitem__(self, key):
        """Docstring."""
        if key in self.__data:
            del self.__data[key]
            if self.autosync is not False:
                self.flush()

    def load(self):
        """Docstring."""
        self.__file_path = load
        if os.path.exists(load) is True and os.path.getsize(load) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
    
        
        
    
