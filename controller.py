import sys
import time
import flet as ft
import model as md


class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view
        self._selected_language = None
        self._selected_modality = None

    def handle_lang_dd_change(self, e):
        # Map dropdown value to language code
        language_map = {
            "Italian": "italian",
            "English": "english",
            "Spanish": "spanish"
        }

        # Update the controller's state with the selected language
        if e.control.value in language_map:
            self._selected_language = language_map[e.control.value]
            print(f"Language changed to: {self._selected_language}")
            # You could update some UI elements here if needed
            self._view.update()

    def handle_modality_dd_change(self, e):
        # Map dropdown value to search mode
        modality_map = {
            "Contains": "Default",
            "Linear": "Linear",
            "Dichotomic": "Dichotomic"
        }

        # Update the controller's state with the selected modality
        if e.control.value in modality_map:
            self._selected_modality = modality_map[e.control.value]
            print(f"Search modality changed to: {self._selected_modality}")
            # You could update some UI elements here if needed
            self._view.update()

    def handleSentence(self, e):
        # Extract the text from the text field
        txtIn = self._view.get_text_input()

        # Check if language and modality are selected
        if not self._selected_language:
            self._view.show_error("Please select a language first")
            return

        if not self._selected_modality:
            self._view.show_error("Please select a search modality first")
            return

        # Process the text
        if not txtIn:
            self._view.show_error("Please enter some text to check")
            return

        # Clean the text and split into words
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()

        if not words:
            self._view.show_error("No valid words to check")
            return

        # Call the appropriate method based on the selected modality
        paroleErrate, execution_time = self.handleSentence_internal(
            words, self._selected_language, self._selected_modality)

        # Update the UI with results
        self._view.display_results(paroleErrate, execution_time)


    def handleSentence_internal(self, words, language, modality):
        # We're now expecting 'words' to be a list of strings
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + ", "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + ", "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + ", "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return "Invalid modality", 0

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleExit(self,e):
        """Exit the application"""
        self._view.page.window.close()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text