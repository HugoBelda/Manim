from manim import *


class WordsScene(Scene):
    def construct(self):
        # Crear la "T" más grande
        e = Text("T", font_size=160)
        e.set_color(BLUE)

        # Crear el resto de las letras más pequeñas
        olos = Text("est", font_size=100)
        olos.next_to(e, RIGHT, buff=0.1)

        word = VGroup(e, olos)
        word.move_to(ORIGIN)  # centra el grupo en la escena

        # Animaciones
        self.play(Write(e))
        self.wait(0.5)
        self.play(Write(olos))
        self.wait(1)
