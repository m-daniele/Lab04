import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.__dd_lang = None
        self.__dd_modality = None
        self.__txt_input = None
        self.__button = None
        self.__results_text = None
        self.__time_text = None
        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.CENTER)
        )

        # row 1 only select language
        self.__dd_lang = ft.Dropdown(
            label="Select language",
            options=[
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Spanish"),
            ],
            width=750,
            on_change=self.__controller.handle_lang_dd_change,
        )
        self.page.add(ft.Row(spacing=30,
                             controls=[self.__dd_lang],
                             alignment=ft.MainAxisAlignment.CENTER)
                      )

        # row 2  select modality + text input + button
        self.__dd_modality = ft.Dropdown(
            label="Select Modality",
            options=[
                ft.dropdown.Option("Contains"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic"),
            ],
            width=200,
            on_change=self.__controller.handle_modality_dd_change,
        )
        self.__txt_input = ft.TextField(
            label="add your sentence here",
            width=400,
            multiline=True,
        )
        self.__button = ft.ElevatedButton(
            text="Spell Check",
            on_click=self.__controller.handleSentence,
        )
        row2 = ft.Row(
            spacing=30,
            controls=[self.__dd_modality, self.__txt_input, self.__button],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page.add(row2)

        # Row 3: Results display
        self.__results_text = ft.Text("Results will appear here", size=16)
        self.__time_text = ft.Text("", size=14)
        row3 = ft.Row(
            spacing=30,
            controls=[self.__results_text],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        row4 = ft.Row(
            spacing=30,
            controls=[self.__time_text],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # Row 5: Exit Button
        self.__exitButton = ft.ElevatedButton(
            text="Exit",
            on_click=self.__controller.handleExit,
        )
        row5 = ft.Row(
            spacing=30,
            controls=[self.__exitButton],
            alignment=ft.MainAxisAlignment.END
        )

        self.page.add(row3)
        self.page.add(row4)
        self.page.add(row5)
        self.page.update()

    def get_text_input(self):
        """Returns the text from the input field"""
        return self.__txt_input.value if self.__txt_input.value else ""

    def show_error(self, message):
        """Displays an error message to the user"""
        self.__results_text.value = f"Error: {message}"
        self.__results_text.color = "red"
        self.page.update()

    def display_results(self, results, execution_time):
        """Displays the spell check results and execution time"""
        input_text = self.__txt_input.value
        self.__results_text.value = f"Original sentence: {input_text}\n\nIncorrect words: {results}"
        self.__time_text.value = f"Execution time: {execution_time:.6f} seconds"
        self.__txt_input.value = ""  # Clear the input field
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        self.page.update()

