# -*- coding: utf-8 -*-

import wx
from wx.html2 import WebView


class MyTestFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, wx.ID_ANY, title, size=(600, 500))
        self._browser = WebView.New(self)
        self._browser.LoadURL('https://jenyay.net')

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyTestFrame(None, 'Test')
    app.MainLoop()
