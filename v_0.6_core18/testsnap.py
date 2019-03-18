# -*- coding: utf-8 -*-

import wx
from wx.html2 import WebView


class MyTestFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, wx.ID_ANY, title, size=(1200, 700))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self._browser = WebView.New(self)
        bSizer9.Add(self._browser, 1, wx.ALL | wx.EXPAND, 5)  # widget, proportion, flags, border

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        for i in range(5):
            btn = wx.Button(self, wx.ID_OK, f"Btn{i}", wx.DefaultPosition, wx.DefaultSize, 0)
            bSizer8.Add(btn, 0, wx.ALL | wx.EXPAND, 5)
            self.Bind(wx.EVT_BUTTON, self.OnButtonClick, btn)
        bSizer9.Add(bSizer8, 0)

        self.SetSizer(bSizer9)
        self.Layout()

        # self._browser.LoadURL('http://pynsource.com')
        self._browser.LoadURL('http://google.com')

        self.Show()

    def OnButtonClick(self, event):
        button = event.GetEventObject()  # get the button that was clicked
        wx.MessageBox(f"Hi from a button click {button.GetLabel()}")


if __name__ == '__main__':
    app = wx.App()
    frame = MyTestFrame(None, 'Test')
    app.MainLoop()
