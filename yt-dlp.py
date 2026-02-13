#will be used with subprocess and npyscreen to download playlist fast and efficiently.
#yt-dlp -x --audio-format mp3 --audio-quality 0 --cookies-from-browser firefox --embed-metadata --embed-thumbnail --add-metadata "https://music.youtube.com/playlist?list=PLJ77UmXjk2yHfiI8a_aN5tjf9ZyZP_HxB"
#if youre reading this, bare with me im learning npyscreen.

import npyscreen

class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.myName = self.add(npyscreen.TitleText, name='Name')
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True,
        max_height=3, name='Department', values = ['Amazon', 'Netflix', 'Google'])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed') 

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myEmployeeForm, name='New Employee')

if __name__ == '__main__':
    TestApp = MyApplication().run()
   