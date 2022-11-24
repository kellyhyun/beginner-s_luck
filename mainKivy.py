from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas as pd
from kivy.core.window import Window 
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import finalSort

global dictionaryPreferences
dictionaryPreferences = {"valid": False,"maxtime": "", "mintime": "", "genres":[], "minyear": "", "maxyear": "", "maxrating": "", "minrating": ""}
global preferencesImportance
preferencesImportance = {1:"", 2:"", 3:"", "valid":False}

Window.maximize()

class MainWindow(Screen):
    def setBack (self, s):
        global screenName
        screenName = s
        return screenName

class SecondWindow(Screen):
    genrecontainer = ObjectProperty()
    choiceList = []
    errorList = []
    global dictionaryPreferences
    
    def popup(self):
        global dictionaryPreferences
        layout = GridLayout(cols = 1, padding = 10)
        if len(self.errorList) == 0:
            dictionaryPreferences["valid"] = True
            string = "All user inputs have been saved."
        else:
            dictionaryPreferences = {"valid": False,"maxtime": "", "mintime":"", "genres":[], "minyear":"", "maxyear": "", "maxrating":"", "minrating":""}
            string = "Please fix all of the following and save again:\n"
            for i in self.errorList:
                string = string + ("   -   {}\n".format(i))
            # string = string + ("\n{}".format(dictionaryPreferences))
            
        popupLabel = Label(text = string)
        closeButton = Button(text = "Close")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)  
        # Instantiate the modal popup and display
        popup = Popup(title ='Errors Found', content = layout)  
        popup.open()   
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)
        self.errorList = []
        
        
    def saveTimes(self):
        maxtext = self.ids.maxruntime.text
        mintext = self.ids.minruntime.text
        maxnum = 0
        minnum = 1
        try: 
            testmaxnum = float(maxtext)
            assert (45 <= testmaxnum <= 467)
            maxnum = float(maxtext)
        except:
            self.errorList.append("Enter a valid maximum runtime.")
            
        try:
            testminnum = float(mintext)
            assert (45 <= testminnum <= 467)
            minnum = float(mintext)
        except:
            self.errorList.append("Enter a valid minimum runtime.")
        
        if (type(maxnum) == float) and (type(minnum) == float):
            try: 
                assert(maxnum>=minnum)
                dictionaryPreferences["maxtime"] = maxnum
                dictionaryPreferences["mintime"] = minnum
            except:
                self.errorList.append("The maximum runtime should be larger or equal to the minimum runtime.")

    def saveGenre(self):
        self.choiceList = []
        for child in reversed(self.ids.genrecontainer.children):
            if isinstance(child, ToggleButton):
                if child.state == "down":
                    self.choiceList.append(child.text)
        if (len(self.choiceList) == 0) or (len(self.choiceList) > 3):
            self.errorList.append("Choose 1-3 genres.")
        else:
            dictionaryPreferences["genres"] = self.choiceList
    
    def saveYear(self):
        maxtext = self.ids.maxyear.text
        mintext = self.ids.minyear.text
        maxnum = 0.0
        minnum = 1.0
        try: 
            testmaxnum = float(maxtext)
            assert(1915 <= testmaxnum <= 2022)
            maxnum = int(maxtext)
        except:
            self.errorList.append("Enter a valid maximum year.")
            
        try:
            testminnum = float(mintext)
            assert(1915 <= testminnum <= 2022)
            minnum = int(mintext)
            
        except:
            self.errorList.append("Enter a valid minimum year.")
        
        if (type(maxnum) == int) and (type(minnum) == int):
            try: 
                assert(maxnum>=minnum)
                dictionaryPreferences["maxyear"] = maxnum
                dictionaryPreferences["minyear"] = minnum
            except:
                self.errorList.append("The maximum year should be larger or equal to the minimum year.")
                
    def saveRatings(self):
        maxtext = self.ids.maxrating.text
        mintext = self.ids.minrating.text
        maxnum = 0
        minnum = 1
        try: 
            testmaxnum = float(maxtext)
            assert(1 <= testmaxnum <= 9.7)
            maxnum = float(maxtext)
        except:
            self.errorList.append("Enter a valid maximum rating.")
            
        try:
            testminnum = float(mintext)
            assert(1 <= testminnum <= 9.7)
            minnum = float(mintext)
        except:
            self.errorList.append("Enter a valid minimum rating.")
        
        if (type(maxnum) == float) and (type(minnum) == float):
            try: 
                assert(maxnum>=minnum)
                dictionaryPreferences["maxrating"] = maxnum
                dictionaryPreferences["minrating"] = minnum
            except:
                self.errorList.append("The maximum rating should be larger or equal to the minimum rating.")
        
    def setBack (self, s):
        global screenName
        screenName = s
        return screenName  
    
    def returnBack(self):
        global screenName
        return screenName
    
    def returnBoolPref(self):
        global dictionaryPreferences
        return dictionaryPreferences["valid"]

    def returnBoolImport(self):
        global preferencesImportance
        return preferencesImportance["valid"]
    
    def popup2(self):
        layout = GridLayout(cols = 1, padding = 10)
        popupLabel = Label(text = "Check and save user inputs before continuing.")
        closeButton = Button(text = "Close")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)  
        # Instantiate the modal popup and display
        popup = Popup(title ='Errors Found', content = layout)  
        popup.open()   
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)
        self.errorList = []
    
class ThirdWindow(Screen):
    global preferencesImportance
    prefList = []
    errorString = ""
    
    def popup(self):
        global dictionaryPreferences
        layout = GridLayout(cols = 1, padding = 10)
        if self.errorString == "":
            string = "All user inputs have been saved."
            preferencesImportance["valid"] = True
        else:
            string = self.errorString
            preferencesImportance["valid"] = False
            
        popupLabel = Label(text = string)
        closeButton = Button(text = "Close")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)  
        # Instantiate the modal popup and display
        popup = Popup(title ='Errors Found', content = layout)  
        popup.open()   
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)
        self.errorList = []
    
    def determineImportance(self):
        global preferencesImportance
        self.prefList = []
        for child in reversed(self.ids.firstcontainer.children):
            if isinstance(child, ToggleButton):
                if child.state == "down":
                    self.prefList.append(child.text)
        for child in reversed(self.ids.secondcontainer.children):
            if isinstance(child, ToggleButton):
                if child.state == "down":
                    self.prefList.append(child.text)
        for child in reversed(self.ids.thirdcontainer.children):
            if isinstance(child, ToggleButton):
                if child.state == "down":
                    self.prefList.append(child.text)
        
        try:
            prefset = set(self.prefList)
            assert(len(prefset) == 3)
            preferencesImportance[1] = self.prefList[0]
            preferencesImportance[2] = self.prefList[1]
            preferencesImportance[3] = self.prefList[2]
            self.errorString = ""
        except AssertionError:
            preferencesImportance = {1:"", 2:"", 3:"", "valid": False}
            self.errorString = "Rank your preferences. No duplicates are allowed."
            
    def popup2(self):
        layout = GridLayout(cols = 1, padding = 10)
        global dictionaryPreferences
        pref = dictionaryPreferences["valid"]
        global preferencesImportance
        impor = preferencesImportance["valid"]
        if not impor:
            string = "Check importance of preferences and save before continuing."
        if not pref:
            string = "Check user preferences and save before continuing."
        if not impor and not pref:
            string = "Check both user preference and importance of preferences and save before continuing."
            
        popupLabel = Label(text = string)
        closeButton = Button(text = "Close")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)  
        # Instantiate the modal popup and display
        popup = Popup(title ='Errors Found', content = layout)  
        popup.open()   
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)
        self.errorList = []         
    
    def returnBoolPref(self):
        global dictionaryPreferences
        return dictionaryPreferences["valid"]
    
    def returnBoolImport(self):
        global preferencesImportance
        return preferencesImportance["valid"]
    
    def returnBack(self):
        global screenName
        return screenName
    
    def setBack (self, s):
        global screenName
        screenName = s
        return screenName
    
class FourthWindow(Screen): 
    global preferencesImportance
    global dictionaryPreferences 
    global refreshed
    global top
    global mList
    refreshed = pd.DataFrame()
    top = pd.DataFrame()
    mList = []
    
    def returnTopRefreshedMlist1(self):
        global preferencesImportance
        global dictionaryPreferences
        global refreshed
        global top
        global mList
        df = finalSort.initialize(dictionaryPreferences)
        top, refreshed, mList = finalSort.movieList(df, preferencesImportance, dictionaryPreferences)
    
    def returnTopRefreshedMlist(self):
        global preferencesImportance
        global dictionaryPreferences
        global refreshed
        global top
        global mList
        if refreshed == pd.DataFrame():
            print("nothing to refresh")
        else:
            top, refreshed, mList = finalSort.movieList(refreshed, preferencesImportance, dictionaryPreferences)
    
    def returnLabelText(self):
        global top
        print(top.to_string())
        self.ids.resultLabel.text = top.to_string()
        # labelText = ""
        # for i, r in top.iterrows():
        #     labelText.join(str(r))
        # return labelText
    
    
    
    def returnBack(self):
        global screenName
        return screenName
    

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
    Window.close()
    
