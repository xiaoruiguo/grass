# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:44:45 2012

@author: pietro
"""
import ctypes
import grass.lib.raster as libraster
import datetime


class History(object):
    """
    *Examples*

    ::
        >>> import grass.lib.gis as libgis
        >>> libgis.G_gisinit('')
        >>> hist = History('elevation')
        >>> hist.creator
        'helena'
        >>> hist.src1
        ''
        >>> hist.src2
        ''
        >>> hist.keyword
        'generated by r.proj'
        >>> hist.date
        datetime.datetime(2006, 11, 7, 1, 9, 51)
        >>> hist.mapset
        'PERMANENT'
        >>> hist.maptype
        'raster'
        >>> hist.title
        'elev_ned10m'

    ..
    """
    def __init__(self, name, mapset='', mtype='',
                 creator='', src1='', src2='', keyword='',
                 date='', title=''):
        self.c_hist = ctypes.pointer(libraster.History())
        #                'Tue Nov  7 01:11:23 2006'
        self.date_fmt = '%a %b  %d %H:%M:%S %Y'
        self.name = name
        self.mapset = mapset
        self.mtype = mtype
        self.creator = creator
        self.src1 = src1
        self.src2 = src2
        self.keyword = keyword
        self.date = date
        self.title = title

    def __repr__(self):
        attrs = ['name', 'mapset', 'mtype', 'creator', 'src1', 'src2',
                 'keyword', 'date', 'title']
        return "History(%s)" % ', '.join(["%s=%r" % (attr, getattr(self, attr))
                                          for attr in attrs])

    def __del__(self):
        """Rast_free_history"""
        pass

    def __len__(self):
        return self.length()

    #----------------------------------------------------------------------
    #libraster.HIST_CREATOR
    def _get_creator(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_CREATOR)

    def _set_creator(self, creator):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_CREATOR,
                                          ctypes.c_char_p(creator))

    creator = property(fget=_get_creator, fset=_set_creator,
                       doc="Set or obtain the creator of map")

    #----------------------------------------------------------------------
    #libraster.HIST_DATSRC_1
    def _get_src1(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_DATSRC_1)

    def _set_src1(self, src1):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_DATSRC_1,
                                          ctypes.c_char_p(src1))

    src1 = property(fget=_get_src1, fset=_set_src1,
                    doc="Set or obtain the first source of map")

    #----------------------------------------------------------------------
    #libraster.HIST_DATSRC_2
    def _get_src2(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_DATSRC_2)

    def _set_src2(self, src2):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_DATSRC_2,
                                          ctypes.c_char_p(src2))

    src2 = property(fget=_get_src2, fset=_set_src2,
                    doc="Set or obtain the second source of map")

    #----------------------------------------------------------------------
    #libraster.HIST_KEYWORD
    def _get_keyword(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_KEYWRD)

    def _set_keyword(self, keyword):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_KEYWRD,
                                          ctypes.c_char_p(keyword))

    keyword = property(fget=_get_keyword, fset=_set_keyword,
                       doc="Set or obtain the keywords of map")

    #----------------------------------------------------------------------
    #libraster.HIST_MAPID
    def _get_date(self):
        date_str = libraster.Rast_get_history(self.c_hist,
                                              libraster.HIST_MAPID)
        if date_str:
            return datetime.datetime.strptime(date_str, self.date_fmt)

    def _set_date(self, datetimeobj):
        if datetimeobj:
            date_str = datetimeobj.strftime(self.date_fmt)
            return libraster.Rast_set_history(self.c_hist,
                                              libraster.HIST_MAPID,
                                              ctypes.c_char_p(date_str))

    date = property(fget=_get_date, fset=_set_date,
                    doc="Set or obtain the date of map")

    #----------------------------------------------------------------------
    #libraster.HIST_MAPSET
    def _get_mapset(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_MAPSET)

    def _set_mapset(self, mapset):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_MAPSET,
                                          ctypes.c_char_p(mapset))

    mapset = property(fget=_get_mapset, fset=_set_mapset,
                      doc="Set or obtain the mapset of map")

    #----------------------------------------------------------------------
    #libraster.HIST_MAPTYPE
    def _get_maptype(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_MAPTYPE)

    def _set_maptype(self, maptype):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_MAPTYPE,
                                          ctypes.c_char_p(maptype))

    maptype = property(fget=_get_maptype, fset=_set_maptype,
                       doc="Set or obtain the type of map")

    #----------------------------------------------------------------------
    #libraster.HIST_NUM_FIELDS
    #
    # Never used in any raster modules
    #
    #    def _get_num_fields(self):
    #        return libraster.Rast_get_history(self.c_hist,
    #                                          libraster.HIST_NUM_FIELDS)
    #
    #    def _set_num_fields(self, num_fields):
    #        return libraster.Rast_set_history(self.c_hist,
    #                                          libraster.HIST_NUM_FIELDS,
    #                                          ctypes.c_char_p(num_fields))
    #
    #    num_fields = property(fget = _get_num_fields, fset = _set_num_fields)
    #----------------------------------------------------------------------
    #libraster.HIST_TITLE
    def _get_title(self):
        return libraster.Rast_get_history(self.c_hist,
                                          libraster.HIST_TITLE)

    def _set_title(self, title):
        return libraster.Rast_set_history(self.c_hist,
                                          libraster.HIST_TITLE,
                                          ctypes.c_char_p(title))

    title = property(fget=_get_title, fset=_set_title,
                     doc="Set or obtain the title of map")

    def append(self, obj):
        """Rast_append_history"""
        libraster.Rast_append_history(self.c_hist,
                                      ctypes.c_char_p(str(obj)))

    def append_fmt(self, fmt, *args):
        """Rast_append_format_history"""
        libraster.Rast_append_format_history(self.c_hist,
                                             ctypes.c_char_p(fmt),
                                             *args)

    def clear(self):
        """Rast_clear_history"""
        libraster.Rast_clear_history(self.c_hist)

    def command(self):
        """Rast_command_history"""
        libraster.Rast_command_history(self.c_hist)

    def format(self, field, fmt, *args):
        """Rast_format_history"""
        libraster.Rast_format_history(self.c_hist,
                                      ctypes.c_int(field),
                                      ctypes.c_char_p(fmt),
                                      *args)

    def length(self):
        """Rast_history_length"""
        return libraster.Rast_history_length(self.c_hist)

    def line(self, line):
        """Rast_history_line"""
        return libraster.Rast_history_line(self.c_hist,
                                           ctypes.c_int(line))

    def read(self):
        """Rast_read_history. ::

            >>> import grass.lib.gis as libgis
            >>> libgis.G_gisinit('')
            >>> import ctypes
            >>> import grass.lib.raster as libraster
            >>> hist = libraster.History()
            >>> libraster.Rast_read_history(ctypes.c_char_p('elevation'),
            ...                             ctypes.c_char_p(''),
            ...                             ctypes.byref(hist))
            0
            >>> libraster.Rast_get_history(ctypes.byref(hist),
            ...                            libraster.HIST_MAPID)
            'Tue Nov  7 01:09:51 2006'

        ..
        """
        libraster.Rast_read_history(self.name, self.mapset, self.c_hist)

    def write(self):
        """Rast_write_history"""
        libraster.Rast_write_history(self.name,
                                     self.c_hist)

    def short(self):
        """Rast_short_history"""
        libraster.Rast_short_history(self.name,
                                     'raster',
                                     self.c_hist)
