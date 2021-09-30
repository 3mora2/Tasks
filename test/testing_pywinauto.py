from pywinauto.application import Application
from pywinauto import Desktop

app = Application(backend="uia").start('notepad.exe')
app = Application(backend="uia").start('C:\Users\3mora\AppData\Local\Programs\Python\Python39\pythonw.exe')

app.UntitledNotepad.exists()
app.untitlednotepad.exists()
app.Untitled.exists()
app['Untitled - Notepad'].exists()
app['Untitled'].exists()
app.UntitledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
########################################################################
title = 'Program Files'
app = Application(backend="uia").connect(title=title)
app[title].set_focus()
# common_files = app.ProgramFiles.ItemsView.get_item(row=2)
# or
common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
common_files.right_click_input()
# or
# common_files.click_input(button='right')
app.ContextMenu.Properties.invoke()
# this dialog is open in another process (Desktop object doesn't rely on any process id)
Properties = Desktop(backend='uia').Common_Files_Properties
Properties.print_control_identifiers()
Properties.Cancel.click()
# make sure the dialog is closed
Properties.wait_not('visible')





app = Desktop().window(title='Open')
app['FileName'].texts()
app['FileName:Edit'].texts()
app['FileName:Edit'].set_text("file.txt")

# هيروح يضغط عليها بالماوس
app['Open'].click_input()
# هيضغط عليها من غير مايحرك الماوس
app['Open'].click()






#By title (window text, name):
app.Properties.OK.click()

# By title and control type:
app.Properties.OKButton.click()

# By control type and number:
app.Properties.Button3.click()
# (Note: Button0 and Button1 match the same button, Button2 is the next etc.)

# By top-left label and control type:
app.OpenDialog.FileNameEdit.set_text("")

# By control type and item text:
app.Properties.TabControlSharing.select("General")


app[u'File &name:ComboBox1'].Edit.print_control_identifiers()
# child_window(title="file.txt", class_name="Edit")
app.Properties.child_window(title="Contains:", auto_id="13087", control_type="Edit")




app = Application(backend="uia").start(r'C:\Users\3mora\AppData\Local\Programs\Python\Python39\pythonw.exe "C:\Users\3mora\AppData\Local\Programs\Python\Python39\Lib\idlelib\idle.pyw"')
app = Application(backend="uia").connect(title='IDLE Shell 3.9.1')
app.Dialog.menu_select("File -> 0").click()
new_window = app.window(title='untitled')


