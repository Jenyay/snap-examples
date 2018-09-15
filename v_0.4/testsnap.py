# -*- coding: utf-8 -*-

import wx


class MyTestFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, wx.ID_ANY, title, size=(600, 500))
        self._editor = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self._menuBar = wx.MenuBar()
        self._menuOpen = wx.Menu()
        self._menuOpen.Append(wx.ID_OPEN, 'Open file...\tCTRL+O')
        self._menuOpen.Append(wx.ID_SAVEAS, 'Save file as...\tCTRL+S')
        self._menuBar.Append(self._menuOpen, 'File')

        self.Bind(wx.EVT_MENU, id=wx.ID_OPEN, handler=self._onOpen)
        self.Bind(wx.EVT_MENU, id=wx.ID_SAVEAS, handler=self._onSaveAs)
        self.SetMenuBar(self._menuBar)
        self.Show()

    def _onOpen(self, event):
        with wx.FileDialog(self,
                           'Open file',
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                with open(dlg.GetPath(), 'r', encoding="utf-8") as fp:
                    text = fp.read()
                self._editor.SetValue(text)

    def _onSaveAs(self, event):
        with wx.FileDialog(self,
                           'Save file as',
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                with open(dlg.GetPath(), 'w', encoding="utf-8") as fp:
                    fp.write(self._editor.GetValue())


if __name__ == '__main__':
    app = wx.App()
    frame = MyTestFrame(None, 'Test')
    app.MainLoop()
