from manim import *
from math import sin , pi , sqrt , erf


text1 = Text("Let's do a simple Experiment:" , font = "Noto Sans")
text2 = Text("Throwing a Ball" , font = "Nunito" , stroke_color = BLUE , color=BLUE)

text3 = Text("With Physics" , font = "Nunito" , stroke_color = WHITE , color=WHITE , t2c={'Physics' : YELLOW})
text3[5:].set_stroke(color = YELLOW)

text4 = Text("we can understand rules of the Universe" , font="Nunito" , stroke_color=WHITE , color=WHITE)

text5 = Text("• Force of gravity varies directly with" , font = "Nunito" , t2c={"gravity" : GREEN})
text6 = Text("  the product of masses and inversely " , font = "Nunito")
text7 = Text("  with the square of the distance." , font = "Nunito")

text8 = Text("• Acceleration of an object varies" , font = "Nunito" , t2c={"Acceleration" : GREEN})
text9 = Text("  in proportion to the applied force" , font = "Nunito")
text10 = Text("  and inversely with the mass." , font = "Nunito")

text11 = Text("With Math" , font = "Nunito" , stroke_color = WHITE , color=WHITE , t2c={'Math' : YELLOW})
text11[5:].set_stroke(color = YELLOW)

text12 = Text("we can write the rules Precisely" , font="Nunito" , stroke_color=WHITE , color=WHITE)

text13 = MathTex(r"\bullet \; F = \frac{GMm}{r^2}")

text14 = MathTex(r"\bullet \; a = \frac{F}{m}")

text15 = MathTex(r"\bullet \; a = \frac{d^2x}{dt^2}")

text16 = MathTex(r"m = 1.5")

text17 = MathTex(r"v = 4.657")

text18 = MathTex(r"\theta = 1.31")

braceEquation = MathTex(r"\frac{d^2x}{dt^2} = \frac{GMm}{mr^2}")
braceEquation2 = MathTex(r"x(t) = vt - \frac{1}{2}gt^2 + x_0")

text19 = Text("With Computer Science" , font = "Nunito" , stroke_color = WHITE , color=WHITE , t2c={'Computer Science' : YELLOW})
text19[5:].set_stroke(color = YELLOW)

text20 = Text("we can Simulate" , font="Nunito" , stroke_color=WHITE , color=WHITE)

text21 = Text("float g = 1" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text22 = Text("float m = 1.5" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text23 = Text("float v = 4.56" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text24 = Text("float theta = 1.31" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text25 = Text("Ball ball = new Ball(m , g , v , theta)" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text26 = Text("ball.getAttracted()" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text27 = Text("ball.update()" , font="Fira Code" , stroke_color=WHITE , color=WHITE)
text28 = Text("ball.show()" , font="Fira Code" , stroke_color=WHITE , color=WHITE)

text29 = Text("and Predict" , font="Nunito" , stroke_color=WHITE , color=WHITE)

def x(t):
    return (1.2 * t)

def y(t):
    return (4.5 * t) - (1 * t * t)

ball_color = "#E1296FCC"
ball_radius = 0.3


base = Line(start=[-4,-2,0] , end=[4,-2,0] , stroke_width = 1.5 , color=WHITE , stroke_color = WHITE)



class ratio16_9(MovingCameraScene):
    def construct(self):
        config.pixel_width = 1920
        config.pixel_height = 1080

        # self.add(NumberPlane())


        text1.scale(1.2).shift(UP * 0.7)
        text2.next_to(text1 , DOWN , buff=0.5)
        underline = Line(start=text2.get_left() , end=text2.get_right() , buff=0.2 , color=BLUE).next_to(text2 , DOWN , buff=0.05)
        

        # -------------------------
        # PARAMETERS you provided/tweaked
        # -------------------------
        x_min, x_max, x_step = -2, 7, 1
        y_min, y_max, y_step = -2, 6, 1

        AXIS_STROKE = 1.5           # axis stroke width
        TICK_SIZE = 0.06            # tick mark length (units)
        NUM_FONT_SIZE = 20          # small integer label size
        TIP_WIDTH = 0.14            # tip arrow width
        TIP_HEIGHT = 0.14           # tip arrow height
        GRID_DASH_LEN = 0.12
        GRID_DASHED_RATIO = 0.45
        GRID_STROKE = 0.95
        GRID_OPACITY = 0.3

        # -------------------------
        # AXES (configured)
        # -------------------------
        ax = Axes(
            x_range=[x_min, x_max, x_step],
            y_range=[y_min, y_max, y_step],
            x_length=9,
            y_length=6,
            axis_config={
                "stroke_width": AXIS_STROKE,
                "color": WHITE,
                "tick_size": TICK_SIZE,
                "tip_width": TIP_WIDTH,
                "tip_height": TIP_HEIGHT,
            },
            x_axis_config={
                "include_numbers": True,
                "font_size": NUM_FONT_SIZE,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            y_axis_config={
                "include_numbers": True,
                "font_size": NUM_FONT_SIZE,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            tips=True,
        )
        ax.set_color(WHITE)

        # Tweak number labels
        for n in ax.x_axis.numbers:
            n.set_color(WHITE).scale(0.85)
        for n in ax.y_axis.numbers:
            n.set_color(WHITE).scale(0.85)

        # -------------------------
        # FULL-AXES GRID (covering both positive and negative)
        # -------------------------
        grid_group = VGroup()

        def make_full_grid():
            lines = []
            x_ticks = ax.x_axis.get_tick_range()
            y_ticks = ax.y_axis.get_tick_range()

            # vertical lines at each x tick
            for xv in x_ticks:
                start = ax.coords_to_point(xv, y_min)
                end = ax.coords_to_point(xv, y_max)
                lines.append(
                    DashedLine(
                        start, end,
                        dash_length=GRID_DASH_LEN,
                        dashed_ratio=GRID_DASHED_RATIO,
                        stroke_width=GRID_STROKE,
                        color=WHITE,
                        stroke_opacity=GRID_OPACITY,
                    )
                )

            # horizontal lines at each y tick
            for yv in y_ticks:
                start = ax.coords_to_point(x_min, yv)
                end = ax.coords_to_point(x_max, yv)
                lines.append(
                    DashedLine(
                        start, end,
                        dash_length=GRID_DASH_LEN,
                        dashed_ratio=GRID_DASHED_RATIO,
                        stroke_width=GRID_STROKE,
                        color=WHITE,
                        stroke_opacity=GRID_OPACITY,
                    )
                )

            return VGroup(*lines)

        def _grid_updater(mob):
            mob.become(make_full_grid())

        grid_group.add_updater(_grid_updater)
        grid_group.become(make_full_grid())
        grid_group.set_z_index(0)
        ax.set_z_index(1)






        ax.shift(-1 * ax.c2p(0,0))

        shift_amount = ax.c2p(5.4 , 0)[0]

        ax.shift(base.get_left() + [1,0,0])

        # self.add(grid_group , ax)

        t = ValueTracker(0)

        def give_ball():
            ball = Circle(radius=ball_radius, stroke_width = 2.4 , stroke_color = ball_color , fill_opacity = 1 , fill_color = BLACK)
            ball.move_to(ax.c2p(x(t.get_value()) , y(t.get_value())) + [0 , ball_radius , 0])

            return ball
        
        ball = always_redraw(give_ball)
    
        text3.move_to([7,2.8,0]).scale(0.95)
        text4.scale(0.8).next_to(text3 , DOWN , buff=0).align_to(text3 , LEFT)


        text5.scale(0.65).align_to(text3 , LEFT).shift(UP * 0.7)
        text6.scale(0.65).next_to(text5 , DOWN , buff=0).align_to(text5 , LEFT)
        text7.scale(0.65).next_to(text6 , DOWN , buff=0).align_to(text5 , LEFT)


        text8.scale(0.65).align_to(text3 , LEFT).shift(DOWN * 1)
        text9.scale(0.65).next_to(text8 , DOWN , buff=0).align_to(text5 , LEFT)
        text10.scale(0.65).next_to(text9 , DOWN , buff=0).align_to(text5 , LEFT)

        text11.scale(0.95).move_to(text3).align_to(text3 , LEFT)

        text12.scale(0.8).next_to(text3 , DOWN , buff=0).align_to(text3 , LEFT)

        text13.scale(0.9).align_to(text3 , LEFT).shift(UP * 0.7)
        text14.scale(0.9).next_to(text13 , DOWN , buff=0.8).align_to(text3 , LEFT)
        text15.scale(0.9).next_to(text14 , DOWN , buff=0.8).align_to(text3 , LEFT)

        text16.scale(0.85).move_to([-2 , -3 , 0])
        
        arr = Arrow(start = ball.get_center() , end = ball.get_center() + 0.24 * np.array([1.2 , 4.5 , 0]) , buff=0 , stroke_width=2 , color = GREEN , max_tip_length_to_length_ratio=0.19)

        text17.scale(0.7).next_to(arr.get_end() , UP , buff=0.15)

        text18.scale(0.85).next_to(text16 , RIGHT , buff=2)

        arc = Arc(radius = 0.5 , start_angle=0 , angle=1.31 , arc_center=ball.get_center() , stroke_width = 2)

        brace = Brace(VGroup(text13 , text14 , text15) , RIGHT , buff=1 , sharpness=1)

        braceEquation.scale(0.8).next_to(brace , RIGHT)
        braceEquation2.scale(0.8).next_to(brace , RIGHT)

        text19.scale(0.95).move_to(text3).align_to(text3 , LEFT)

        text20.scale(0.8).next_to(text3 , DOWN , buff=0).align_to(text3 , LEFT)

        text21.scale(0.4).move_to([-6 , 3 , 0])
        text22.scale(0.4).next_to(text21 , DOWN , buff=0.02).align_to(text21 , LEFT)
        text23.scale(0.4).next_to(text22 , DOWN , buff=0.02).align_to(text21 , LEFT)
        text24.scale(0.4).next_to(text23 , DOWN , buff=0.02).align_to(text21 , LEFT)
        text25.scale(0.4).next_to(text24 , DOWN , buff=0.3).align_to(text21 , LEFT)
        text26.scale(0.4).next_to(text25 , DOWN , buff=0.3).align_to(text21 , LEFT)
        text27.scale(0.4).next_to(text26 , DOWN , buff=0.02).align_to(text21 , LEFT)
        text28.scale(0.4).next_to(text27 , DOWN , buff=0.02).align_to(text21 , LEFT)

        text29.scale(0.8).next_to(text20 , DOWN , buff=0.1).align_to(text3 , LEFT)


        

        trajectory = always_redraw(lambda : 
            ParametricFunction(lambda t: ax.c2p(x(t) , y(t) + ball_radius) , t_range=[0 , t.get_value()] , color=WHITE , stroke_width = 2)
        )


        self.play(Write(text1))
        self.wait(0.5)
        self.play(Write(text2) , Create(underline))
        self.wait(0.5)

        self.play(FadeOut(text1 , run_time = 0.3) , VGroup(text2 , underline).animate.to_edge(UP))

        self.play(Create(base) , Create(ball))
        # self.add(ax)

        self.wait(0.5)


        self.play(t.animate.set_value(4.5) , rate_func = linear , run_time = 2)


        self.camera.frame.save_state()

        self.wait(0.5)
        self.play(Write(text3 , run_time = 1.5) , t.animate.set_value(0) , ball.animate.shift(LEFT * shift_amount) , self.camera.frame.animate(run_time = 1).scale(1.4).move_to([5, 0, 0]))
        self.play(Write(text4))

        self.wait(0.7)
        self.play(Write(VGroup(text5 , text6 , text7)))
        self.play(Write(VGroup(text8 , text9 , text10)))

        self.wait(1)
        self.play(Unwrite(VGroup(text8 , text9 , text10)) , Unwrite(VGroup(text5 , text6 , text7)) , Unwrite(text4))
        self.play(ReplacementTransform(text3[4:] , text11[4:]))

        self.wait(0.5)
        self.play(Write(text12))
        
        self.wait(0.5)
        self.play(Write(text13))
        self.play(Write(text14))
        self.play(Write(text15))

        self.play(Write(text16))

        self.play(GrowArrow(arr) , FadeIn(text17 , shift=arr.get_end() - arr.get_start()) , run_time = 0.7)

        self.play(Write(text18) , Create(arc))

        self.play(GrowFromCenter(brace))
        self.play(FadeIn(braceEquation))
        self.play(TransformMatchingShapes(braceEquation , braceEquation2))

        self.wait()
        self.play(
            Unwrite(text12),
            Unwrite(text13),
            Unwrite(text14),
            Unwrite(text15),
            Unwrite(text16),
            Unwrite(text17),
            Unwrite(text18),
            Unwrite(braceEquation2),
            FadeOut(brace),
            Uncreate(arc),
            FadeOut(arr)
        )

        # self.play(text11[4:].animate.shift(UP))

        self.play(ReplacementTransform(text11[4:] , text19[4:]))

        self.play(Write(text20))

        self.wait(0.5)
        self.play(Restore(self.camera.frame), run_time=1)

        cursor = Line(color=WHITE , start=[0 , 0.3 , 0] , end=ORIGIN , stroke_width = 2).move_to(text21[0])
        self.play(TypeWithCursor(text21 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text22[0])
        self.play(TypeWithCursor(text22 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text23[0])
        self.play(TypeWithCursor(text23 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text24[0])
        self.play(TypeWithCursor(text24 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text25[0])
        self.play(TypeWithCursor(text25 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text26[0])
        self.play(TypeWithCursor(text26 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text27[0])
        self.play(TypeWithCursor(text27 , time_per_char=0.003 , cursor=cursor))
        cursor.move_to(text28[0])
        self.play(TypeWithCursor(text28 , time_per_char=0.003 , cursor=cursor))

        self.wait(0.5)
        self.play(t.animate(rate_func = linear , run_time = 1.7).set_value(4.5))


        self.wait(0.5)
        self.play(Unwrite(VGroup(text21 , text22 , text23 , text24 , text25 , text26 , text27 , text28) , run_time = 1) , self.camera.frame.animate(run_time = 1).scale(1.4).move_to([5, 0, 0]) , FadeOut(cursor , run_time = 0.2))

        self.play(Write(text29))


        self.wait(0.5)
        self.play(t.animate(run_time = 1).set_value(0) , ball.animate(run_time = 1).shift(LEFT * shift_amount) , FadeIn(grid_group , ax , run_time = 2) , Restore(self.camera.frame , run_time = 1))

        self.add(trajectory)


        

        self.play(t.animate(rate_func = ease_out_sine , run_time = 2).set_value(3.285))


        predicted_trajectory = always_redraw(lambda : 
            ParametricFunction(lambda t: ax.c2p(x(t) , y(t) + ball_radius) , t_range=[t.get_value() , 4.5] , color=RED , stroke_width = 1.2)
        )

        blinker_dot = Dot(ax.c2p(x(4.5) , y(4.5)) , 0.06 , color=RED_D)


        self.play(Create(predicted_trajectory))
        self.add(blinker_dot)
        self.play(Blink(blinker_dot , 0.2 , 0.2 , 2 , False))

        self.play(t.animate.set_value(4.5))




        self.wait()
