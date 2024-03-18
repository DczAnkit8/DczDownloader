from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class DownloadApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # App title
        app_title = Label(text="DCZ Ankit Downloader", font_name="Roboto", size_hint_y=0.1,
                          color=(0, 0, 1, 1), font_size=24)
        
        # Link input field
        link_input = TextInput(hint_text="Enter Link Here", multiline=False, size_hint_y=0.1)
        
        # Quality selection dropdown
        quality_options = ["Select Quality", "240p", "360p", "480p", "720p", "1080p", "4K"]
        quality_dropdown = DropDown()
        for option in quality_options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: quality_dropdown.select(btn.text))
            quality_dropdown.add_widget(btn)
        quality_button = Button(text="Select Quality", size_hint=(None, None), size=(150, 40), pos_hint={'center_x': 0.5})
        quality_button.bind(on_release=quality_dropdown.open)
        quality_dropdown.bind(on_select=lambda instance, x: setattr(quality_button, 'text', x))
        
        # Download button
        download_button = Button(text="Download", size_hint_y=0.1, background_color=(0, 1, 0, 1))
        download_button.bind(on_press=self.start_download)
        
        # Add elements to layout
        layout.add_widget(app_title)
        layout.add_widget(link_input)
        layout.add_widget(quality_button)
        layout.add_widget(download_button)
        
        # Set background color
        layout.canvas.before_paint.append(self.draw_background)
        return layout

    def draw_background(self, canvas):
        canvas.draw_rectangle((0, 0), App.get_running_app().root.width, App.get_running_app().root.height,
                              color=(0.95, 0.95, 0.95, 1))

    def start_download(self, instance):
        link = self.root.children[0].children[1].text
        quality = self.root.children[0].children[2].text
        print(f"Download Link: {link}, Quality: {quality}")

if __name__ == "__main__":
    DownloadApp().run()
