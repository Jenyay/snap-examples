# -*- coding: utf-8 -*-

import wx
from wx.html2 import WebView


HTML = '''<!DOCTYPE html>
<html>
<head>
    <meta http-equiv='X-UA-Compatible' content='IE=edge' />
    <meta http-equiv='content-type' content='text/html; charset=utf-8'/>
    <title>Версия WebKit</title>
</head>

<body>
<p id="info"></p>

<script>
    document.getElementById("info").innerHTML = navigator.userAgent;
</script>
</body>
</html>
'''


class MyTestFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, wx.ID_ANY, title, size=(600, 500))
        self._browser = WebView.New(self)
        self._browser.SetPage(HTML, '.')

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyTestFrame(None, 'Test')
    app.MainLoop()
