# Импорт библиотек
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from randomizer.chooser import start


class Interface(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        def on_start_press(instance):
            text = self.ids.members_count_field.text
            members_count = int(text) if text else 0
            if members_count:
                self.ids.start_button.unbind(on_press=on_start_press)
            start(self.ids.start_button, self.ids.start_button_text, members_count)

        self.ids.start_button.bind(on_press=on_start_press)


class ChemistryImposterApp(MDApp):
    def build(self):
        return Interface()


if __name__ == '__main__':
    ChemistryImposterApp().run()
