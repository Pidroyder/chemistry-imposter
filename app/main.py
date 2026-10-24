# Импорт библиотек
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from randomizer.chooser import start


class Interface(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_running = False

    def on_kv_post(self, base_widget):
        self.ids.start_button.bind(on_press=self.on_start_press)

    def on_start_press(self, instance):
        if self.game_running:
            return
        text = self.ids.members_count_field.text
        members_count = int(text) if text else 0
        if not members_count:
            self.ids.start_button_text.text = 'Введите корректное количиство игроков'
            return
        self.game_running = True
        start(self.ids.start_button, self.ids.start_button_text, members_count,
              on_finish=self.on_game_finish)

    def on_game_finish(self):
        self.game_running = False


class ChemistryImposterApp(MDApp):
    def build(self):
        return Interface()


if __name__ == '__main__':
    ChemistryImposterApp().run()
