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
        self.__dd_menu = None
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

        # Add your stuff here
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
        self.page.update()

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
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
