# -*- coding: utf-8 -*-

import wx


class MyTestFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, wx.ID_ANY, title, size=(400, 150))
        self._listCtrl = wx.ListCtrl(self, style=wx.LC_LIST)

        for n in range(20):
            self._listCtrl.InsertItem(0, 'bla-bla-bla-bla-bla')

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyTestFrame(None, 'Test')
    app.MainLoop()
