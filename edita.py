import wx
 
 
def click_save_button(event):  # 保存ボタンをクリック時の動作
    save_file = open('wxtest.txt', 'w')  # テキストファイルを開く
    save_file.write(text.GetValue())  # 入力されたテキストを取得し、ファイルへ書き込み
    save_file.close()
 
 
if __name__ == '__main__':
    window = wx.App()  # wxPythonのGUI Appインスタンスを生成 (= GUI Appを初期化)
    frame = wx.Frame(None, -1, 'テキスト入力＆保存', size=(500, 250))  # フレーム作成
 
    panel = wx.Panel(frame, -1)  # ボタンやテキストボックスを配置するためのパネルを作成
    save_button = wx.Button(panel, -1, pos=(10, 10), label='保存')  # 保存ボタンの作成
 
    text = wx.TextCtrl(panel, -1, pos=(10, 50), size=(465, 150), style=wx.TE_MULTILINE)  # テキストボックスの作成
    save_button.Bind(wx.EVT_BUTTON, click_save_button)  # 保存ボタンとボタン押下時の動作をまとめた関数をひもづける
    frame.Show()  # フレーム表示
    window.MainLoop()  # イベント待機