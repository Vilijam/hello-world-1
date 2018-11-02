from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
# Importerer kivyelementer som der bruges i programmet

import fornærmelsesmaskinen
# Importerer funktionerne fra det originale program, som skal bruges i kivyprogrammet

start = Builder.load_file("InsultApp.kv")
# Uploader kivyfilen som bruges til at opbygge layoutet i programmet

class MenuLayout(Screen):
	insulttxt = StringProperty("Welcome to the Monty Python Insult Generator 9001")	
	pass
# Opretter det første layout der loades i programmet, det er bygget op som beskrevet i kivyfilen
# Opretter variablen insulttxt, og definerer den til den tekst som programmet først skal vise

class PersonalizedLayout(Screen):
# Opretter det andet layout der kan loades i programmet, det er bygget op som beskrevet i kivyfilen
	def togglenew(self):
		# Opretter en funktion som kan udskrive en personlig fornærmelse
		adj = self.ids.mitInput1.text
		jobone = self.ids.mitInput2.text
		act = self.ids.mitInput3.text
		famone = self.ids.mitInput4.text
		jobtwo = self.ids.mitInput5.text
		famtwo = self.ids.mitInput6.text
		thing = self.ids.mitInput7.text
		# Laver variable som indeholder textinputenes tekst
		sm.get_screen('menu').insulttxt = "I don't want to talk to you no more you "+adj+" "+jobone+"!... I "+act+" in your general direction!\nYour "+famone+" was a "+jobtwo+" and your "+famtwo+" smelt of "+thing+"!"
		# Finder teksten på startsiden og ændrer den til fornærmelsen, med brugerens input
	pass

sm = ScreenManager()
# Opretter screen manager
sm.add_widget(MenuLayout(name='menu'))
# Tilføjer det første layout til screen manager under navnet 'menu'
sm.add_widget(PersonalizedLayout(name='input'))
# Tilføjer det andet layout til screen manager under navnet 'input'

class BasicInsultApp(App):
# Opretter kivy-appen som skal vises
	def build(self):
		# Bygger appen
		return sm
		# Returnerer screen manageren, så den vil være appens vindue
		
	def toggle(self): 
		sm.get_screen('menu').insulttxt = fornærmelsesmaskinen.makeInsult()
		# Henter funktionen som tilfældigt genererer fornærmelser fra det originale program, og laver en ny funktion til den, som knapper kan calle


if __name__ == "__main__":
	BasicInsultApp().run()
# Sætter kivy-appen i gang
