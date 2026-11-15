from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.025, 0.04, 0.10, 1)

class QodirCyberLab(App):
    def build(self):
        main = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        main.add_widget(Label(
            text="[b]QODIR CYBER LAB[/b]",
            markup=True,
            font_size=30,
            color=(0.1, 0.65, 1, 1),
            size_hint_y=0.2
        ))

        main.add_widget(Label(
            text="YOUR DIGITAL SECURITY LAB",
            font_size=13,
            color=(0.6, 0.75, 0.9, 1)
        ))

        buttons = [
            "🔐  PASSWORD CHECKER",
            "#️⃣  SHA-256 GENERATOR",
            "🔗  LINK SAFETY",
            "🧠  PHISHING QUIZ",
            "🛡️  CYBER TIPS"
        ]

        for name in buttons:
            btn = Button(
                text=name,
                font_size=18,
                background_normal="",
                background_color=(0.04, 0.25, 0.48, 1),
                color=(1, 1, 1, 1),
                size_hint_y=0.14
            )
            main.add_widget(btn)

        main.add_widget(Label(
            text="Created with QODIR CYBER LAB",
            font_size=12,
            color=(0.4, 0.6, 0.8, 1),
            size_hint_y=0.12
        ))

        return main

if __name__ == "__main__":
    QodirCyberLab().run()

