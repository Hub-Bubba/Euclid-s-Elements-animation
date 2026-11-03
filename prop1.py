from manimlib import *

class ConstructionScene(Scene):
    def construct(self):
        # Set frame height (default is usually 8.0)
        self.camera.frame.set_height(30)
        
        # Set frame width
        self.camera.frame.set_width(20)
        
        # Move the frame center to a specific location
        self.camera.frame.move_to([0, 0, 0])
        self.wait(2)
        #text1 
        intro = Text("Euclid's Elements is one of if not", font_size=50, font = "Times New Roman")
        intro2 = Text("the most influential work in the history of mathematics.", font_size=50, font = "Times New Roman")
        intro2.move_to([0, -1, 0])
        self.play(Write(intro), Write(intro2), run_time=3)
        self.wait(3)
        self.play(FadeOut(intro), FadeOut(intro2), run_time=3)

        #text2
        intro3 = Text("This is Euclid's first proposition.", font_size=50, font = "Times New Roman")
        self.play(Write(intro3), run_time=3)
        self.wait(3)
        self.play(FadeOut(intro3), run_time=3)

        # 1. Setup points and connecting line
        dotA = Dot([-2, 0, 0])
        letterA = Text("A", font="Times New Roman", font_size=30)
        letterA.move_to([-2.5, 0, 0])
        dotB = Dot([2, 0, 0])
        letterB = Text("B", font="Times New Roman", font_size=30)
        letterB.move_to([2.5, 0, 0])
        line = Line(dotA.get_center(), dotB.get_center())
        line.set_stroke(WHITE, width=4)

        # 2. First circle animation (dotB rotates counter-clockwise around dotA)
        circle_path = TracedPath(
            dotB.get_center, 
            stroke_width=4
        )

        circle = Circle(radius=4, arc_center=dotA.get_center())
        circle.set_stroke(ORANGE, width=4)

        self.add(circle_path)
        self.play(ShowCreation(dotA), ShowCreation(dotB))
        self.wait(0.5)
        self.play(Write(letterA), Write(letterB))
        self.wait(0.5)
        self.play(ShowCreation(line))
        
        # Group line and dotB to rotate around dotA
        rotating_group = VGroup(line, dotB)
        self.play(
            ShowCreation(circle),
            Rotate(
                rotating_group,
                angle=2 * PI,
                about_point=dotA.get_center(),
                rate_func=smooth
            ),
            run_time=3
        )
        self.wait(1)

        # 3. Second circle animation (dotA rotates clockwise around dotB)
        circle_path2 = TracedPath(
            dotA.get_center, 
            stroke_color=BLUE,
            stroke_width=4
        )

        circle2 = Arc(radius=4, start_angle=0, angle=PI, arc_center=dotB.get_center())
        circle3 = Arc(radius=4, start_angle=PI, angle=(2 * PI), arc_center=dotB.get_center())
        circle2.set_stroke(BLUE, width=4)
        circle3.set_stroke(BLUE, width=4)

        circle2.reverse_points()
        circle3.reverse_points()
        self.add(circle_path2)
        
        # Group line and dotA to rotate around dotB
        rotating_group2 = VGroup(line, dotA)
        self.play(
            ShowCreation(circle2, run_time=3),
            Rotate(
                rotating_group2,
                angle=-2 * PI,
                about_point=dotB.get_center(),
                rate_func=smooth,
                run_time=3
            ),
            ShowCreation(circle3, run_time=3)
        )
        self.add(dotA, dotB, line)
        self.wait(1)
        
        # 4. Equilateral triangle construction
        dotC = Dot([0, 3.464, 0])
        dotD = Dot([0, -3.464, 0])
        letterC = Text("C", font="Times New Roman", font_size=30)
        letterC.move_to([0, 3, 0])
        letterCneg = Text("-C", font="Times New Roman", font_size=30)
        letterCneg.move_to([0, -3, 0])
        self.play(FadeIn(dotC), FadeIn(dotD))
        self.play(Write(letterC), Write(letterCneg))

        # rotate group 1
        dotA2 = Dot([-2, 0, 0])
        dotB2 = Dot([2, 0, 0])
        line2 = Line(dotA2.get_center(), dotB2.get_center())
        line2.set_stroke(WHITE, width=4)
        self.add(dotA2, dotB2, line2)
        rotating_group2 = VGroup(line2, dotB2)

        # rotate group 2
        dotA3 = Dot([-2, 0, 0])
        dotB3 = Dot([2, 0, 0])
        line3 = Line(dotA3.get_center(), dotB3.get_center())
        line3.set_stroke(WHITE, width=4)
        self.add(dotA3, dotB3, line3)
        rotating_group3 = VGroup(line3, dotA3)
        self.play(
            Rotate(
                rotating_group3,
                angle= -0.333 * PI,
                about_point=dotB3.get_center(),
                rate_func=smooth
            ),
            Rotate(
                rotating_group2,
                angle=0.333 * PI,
                about_point=dotA2.get_center(),
                rate_func=smooth
            ),
            run_time=3
        )
        self.wait(2)

        start_point = [0, 4.7, 0]
        end_point = [0, 3.5, 0]
        
        arrow = Arrow(start_point, end_point)
        arrow.set_stroke(WHITE, width=2)
        triangle1 = Polygon(dotA.get_center(), dotB.get_center(), dotC.get_center())
        triangle1.set_stroke(RED, width=4)
        
        self.wait(1)
        text = Text("Equilateral", font_size=50, font = "Times New Roman")
        text.move_to([0, 5, 0])
        self.play(Write(text), ShowCreation(arrow), FadeIn(triangle1), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(triangle1))
        self.wait(3)