#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A pickle module used to operate files."""

import os
import pickle


class PickleCache(object):
    """A PickleCache custom class."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """A constructor for the PickleCache class.

        Args:
            file_path(str, optional): defaults to datastore.pkl
            autosync(bool, optional): defaults to False

        Returns: None

        Example:
            >>> cacher = PickleCache()
            >>> print cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.__file_object = None

    def __setitem__(self, key, value):
        """Method to make our cache act as a dictionary.
        Args:
            key(str, required): A required key input.
            value(str, required): A required value input.
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """To check the length of __data.

        Arg: None
        Return: None
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """To retrieve data from PickleCache objects.
        Args:
            key(str, required): A required key input.

        Return: None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        try:
            if self.__data[key]:
                return self.__data[key]
        except:
            raise KeyError

        if self.autosync is True:
            self.flush()

    def __delitem__(self, key):
        """To del unwanted objects.
        Args:
            key(str, required): A required key input.

        Return: None

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> len(pcache)
            0
        """
        if key in self.__data:
            del self.__data[key]
            if self.autosync is True:
                self.flush()

    def load(self):
        """To load existing file.
        Args: None
        Return: None
        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """
        my_load = self.__file_path
        if os.path.exists(my_load) and os.path.getsize(my_load) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """To save its stored data.
        Args: None
        Returns: None
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
