from manim import *

class BikeDrawing(Scene):
    def construct(self):
        # Bike parameters
        wheel_radius = 1
        wheel_distance = 3.5
        tire_thickness = 0.1
        frame_color = BLUE
        wheel_color = WHITE

        # Wheels
        back_wheel = Circle(radius=wheel_radius, color=wheel_color, stroke_width=4)
        front_wheel = Circle(radius=wheel_radius, color=wheel_color, stroke_width=4)
        front_wheel.shift(RIGHT * wheel_distance)
        
        # Spokes (simplified as lines)
        def create_spokes(wheel):
            spokes = VGroup()
            for i in range(8):
                angle = i * PI / 4
                spoke = Line(wheel.get_center(), wheel.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * wheel_radius, color=wheel_color)
                spokes.add(spoke)
            return spokes

        back_spokes = create_spokes(back_wheel)
        front_spokes = create_spokes(front_wheel)

        wheels = VGroup(back_wheel, front_wheel, back_spokes, front_spokes)
        
        # Center the wheels
        wheels.move_to(ORIGIN + DOWN * 1)

        # Frame points
        # Back wheel center is now at wheels[0].get_center()
        bw_center = back_wheel.get_center()
        fw_center = front_wheel.get_center()
        
        bottom_bracket = bw_center + RIGHT * 1.2 + UP * 0.5
        seat_post_top = bottom_bracket + UP * 1.8 + LEFT * 0.2
        handlebar_stem = fw_center + UP * 2.5 + LEFT * 0.5
        
        # Frame Lines
        # Chainstay: Back wheel to bottom bracket
        chainstay = Line(bw_center, bottom_bracket, color=frame_color, stroke_width=6)
        
        # Seat tube: Bottom bracket to seat post top
        seat_tube = Line(bottom_bracket, seat_post_top, color=frame_color, stroke_width=6)
        
        # Down tube: Bottom bracket to handlebar stem area (approximate head tube bottom)
        head_tube_bottom = handlebar_stem + DOWN * 0.8 + RIGHT * 0.1
        down_tube = Line(bottom_bracket, head_tube_bottom, color=frame_color, stroke_width=6)
        
        # Top tube: Seat post top to head tube top area
        top_tube = Line(seat_post_top + DOWN*0.2, head_tube_bottom + UP*0.2 + LEFT*0.1, color=frame_color, stroke_width=6)
        
        # Seat stays: Back wheel to seat post top
        seat_stay = Line(bw_center, seat_post_top + DOWN*0.2, color=frame_color, stroke_width=6)
        
        # Fork: Front wheel to handlebar stem
        fork = Line(fw_center, handlebar_stem, color=frame_color, stroke_width=6)
        
        frame = VGroup(chainstay, seat_tube, down_tube, top_tube, seat_stay, fork)

        # Handlebars
        handlebar = Line(handlebar_stem + LEFT * 0.3, handlebar_stem + RIGHT * 0.3, color=RED, stroke_width=8)
        handlebar_curve = ArcBetweenPoints(handlebar_stem + RIGHT * 0.3, handlebar_stem + RIGHT * 0.5 + DOWN * 0.3, color=RED, stroke_width=8)
        handlebars = VGroup(handlebar, handlebar_curve)

        # Seat
        seat = RoundedRectangle(corner_radius=0.1, height=0.2, width=0.8, color=RED, fill_opacity=1).move_to(seat_post_top + UP * 0.1)

        bike = VGroup(wheels, frame, handlebars, seat)

        # Animation
        self.play(DrawBorderThenFill(back_wheel), DrawBorderThenFill(front_wheel))
        self.play(Create(back_spokes), Create(front_spokes))
        self.play(Create(frame))
        self.play(Create(handlebars), FadeIn(seat))
        
        self.wait(1)
        
        # Move the bike
        self.play(bike.animate.shift(RIGHT * 2), run_time=2)
        self.wait(1)
