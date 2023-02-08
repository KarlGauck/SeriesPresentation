from manim import *
from manim_fonts import *
import math


class Achill(Scene):
    def construct(self):
        raceGroup = Group()

        numberline = NumberLine(x_range=[0, 13], length=10).add_numbers()
        meter = Text("m").next_to(numberline, RIGHT)
        raceGroup.add(numberline, meter)

        self.play(Write(VGroup(numberline, meter)))

        turtle = Group(ImageMobject("resources/Schildkrote.png").shift(1.3 * UP + LEFT * 5), Dot(color=GREEN).shift(.3 * UP + 5 * LEFT))
        achill = Group(ImageMobject("resources/achill.png").scale(.3).shift(1.3 * DOWN + LEFT * 5), Dot(color=RED).shift(.6 * DOWN + 5 * LEFT))
        raceGroup.add(turtle, achill)

        self.play(FadeIn(Group(turtle, achill)))

        velocityTurtle = MathTex(r'\vec{v}_{schild} = 0,1\frac{m}{s}').scale(.8).next_to(meter, UP).shift(.5 * UP)
        velocityAchill = MathTex(r'\vec{v}_{achill} = 1\frac{m}{s}').scale(.8).next_to(meter, DOWN).shift(.5 * DOWN).align_to(velocityTurtle, LEFT)
        raceGroup.add(velocityAchill, velocityTurtle)

        self.play(Write(velocityTurtle))
        self.play(Write(velocityAchill))

        self.play(turtle.animate(run_time=2).shift(10 * (10 / 13) * RIGHT))

        clocktimeSeconds = ValueTracker(0.0)

        def createClock():
            with RegisterFont("Orbitron") as fonts:
                string1 = str(math.floor(clocktimeSeconds.get_value()))
                if len(string1) == 1:
                    string1 = "0" + string1
                string2 = str(int((round(clocktimeSeconds.get_value(), 2) - math.floor(clocktimeSeconds.get_value())) * 100))
                if len(string2) == 1:
                    string2 = "0" + string2
                return Text(string1 + ":" + string2, font=fonts[0]).align_on_border(UP + LEFT)

        clock = always_redraw(createClock)
        raceGroup.add(clock)
        self.play(Write(clock))

        self.play(FadeIn(Text("3", color=GREEN).scale(5), scale=1 / 5, rate_func=rate_functions.there_and_back_with_pause))
        self.play(FadeIn(Text("2", color=ORANGE).scale(5), scale=1 / 5, rate_func=rate_functions.there_and_back_with_pause))
        self.play(FadeIn(Text("1", color=RED).scale(5), scale=1 / 5, rate_func=rate_functions.there_and_back_with_pause))

        self.play(FadeIn(Text("GO").scale(5), scale=1 / 5, rate_func=rate_functions.there_and_back), clocktimeSeconds.animate(run_time=13, rate_func=rate_functions.linear).set_value(13),
                  achill.animate(run_time=13, rate_func=rate_functions.linear).shift(10 * RIGHT), turtle.animate(run_time=13, rate_func=rate_functions.linear).shift(RIGHT))

        coordsGroup = VGroup()
        axes = Axes(x_range=[0, 13], y_range=[0, 13]).add_coordinates()
        x_label = axes.get_x_axis_label("Zeit / s")
        y_label = axes.get_y_axis_label("Distanz / m")
        system = VGroup(axes, x_label, y_label)
        coordsGroup.add(system)

        self.play(raceGroup.animate(rate_func=rate_functions.ease_in_sine).shift(20 * LEFT), FadeIn(system, shift=20 * LEFT), FadeOut(clock))

        turtleGraph = axes.plot(lambda x: (1 / 10) * x + 10, color=GREEN)
        achillGraph = axes.plot(lambda x: x, color=RED)
        coordsGroup.add(achillGraph, turtleGraph)

        turtleFunc = MathTex(r'y = \frac{1}{10}x + 10', color=GREEN).move_to(turtleGraph).shift(UP + .2 * LEFT)
        achillFunc = MathTex(r'y = x', color=RED).move_to(achillGraph).shift(DOWN + RIGHT)
        coordsGroup.add(turtleFunc, achillFunc)

        self.play(Write(VGroup(turtleFunc, turtleGraph)))
        self.play(Write(VGroup(achillFunc, achillGraph)))

        dot = Dot(axes.c2p(11.1, 11.1), color=YELLOW)
        coords = MathTex(r'(11,1\ s | 11,1\ m)', color=YELLOW).scale(.6).next_to(dot, RIGHT + DOWN)
        coordsGroup.add(dot, coords)
        self.play(Write(VGroup(dot, coords)))

        raceGroup.set_z_index(2)
        turtle.shift(LEFT)
        achill.shift(10 * LEFT)
        clocktimeSeconds.set_value(0)
        raceGroup.remove(velocityTurtle, velocityAchill)
        self.remove(velocityTurtle, velocityAchill)
        raceGroupYShift = 1.5
        raceGroup.shift(raceGroupYShift * UP)

        self.play(raceGroup.animate.shift(20 * RIGHT), coordsGroup.animate.shift(20 * RIGHT))
        self.play(FadeIn(clock, run_time=.25))

        table1Text1 = Text("Strecke").scale(.5)
        table1Text2 = Text("Zeit").scale(.5).next_to(table1Text1, RIGHT)

        table2Text1 = Text("Zeit").scale(.5)
        table2Text2 = Text("Strecke").scale(.5).next_to(table2Text1, RIGHT)
        table1 = VGroup(
            table1Text1,
            table1Text2,
            Line(start=2 * RIGHT, end=2 * LEFT).next_to(VGroup(table1Text1, table1Text2), DOWN).shift(0.3 * RIGHT),
            Line(start=UP, end=DOWN).next_to(VGroup(table1Text1, table1Text2), DOWN).shift(0.3 * RIGHT),
            Text("Achilles").scale(.5).next_to(VGroup(table1Text1, table1Text2), UP).shift(0.3 * RIGHT)
        ).center().shift(2.2 * DOWN + 3 * LEFT).set_z_index(2)

        table2 = VGroup(
            table2Text1,
            table2Text2,
            Line(start=2 * RIGHT, end=2 * LEFT).next_to(VGroup(table2Text1, table2Text2), DOWN).shift(0.3 * LEFT),
            Line(start=UP, end=DOWN).next_to(VGroup(table2Text1, table2Text2), DOWN).shift(0.3 * LEFT),
            Text("Schildkröte").scale(.5).next_to(VGroup(table2Text1, table2Text2), UP).shift(0.3 * LEFT)
        ).center().shift(2.2 * DOWN + 3 * RIGHT).set_z_index(2)

        self.play(Write(table1))

        steps = 3
        turtlepositions = []
        currentxoffset = -5.0 + 10 * (10 / 13)

        values = []

        for step in range(steps):
            time = (10 / pow(10, step))
            realdist = (10 / pow(10, step))

            if step != 0:
                timeLabel = Text(str(10 / pow(10, step - 1)) + " s").scale(.4).next_to(table1.submobjects[3], RIGHT).align_to(table1.submobjects[2], UP).shift(0.3 * (step - 1) * DOWN + 0.2 * DOWN)
                values.append(timeLabel)

                self.play(Write(timeLabel))

                if step == 1:
                    self.play(Write(table2))

                turtleTimeLabel = Text(str(10 / pow(10, step - 1)) + " s").scale(.4).next_to(table2.submobjects[3], LEFT).align_to(table2.submobjects[2], UP).shift(0.3 * (step - 1) * DOWN + 0.2 * DOWN)
                turtleDistLabel = Text(str(realdist) + " m").scale(.4).next_to(table2.submobjects[3], RIGHT).align_to(table2.submobjects[2], UP).shift(0.3 * (step - 1) * DOWN + 0.2 * DOWN)
                values.append(turtleTimeLabel)
                values.append(turtleDistLabel)

                self.play(Write(turtleTimeLabel))
                self.play(Write(turtleDistLabel))

            distLabel = Text(str(realdist) + " m").scale(.4).next_to(table1.submobjects[3], LEFT).align_to(table1.submobjects[2], UP).shift(0.3 * step * DOWN + 0.2 * DOWN)
            values.append(distLabel)

            turtlePosition = Line(start=(.5 + raceGroupYShift) * UP + currentxoffset * RIGHT, end=(.5 - raceGroupYShift) * DOWN + currentxoffset * RIGHT, color=GREEN)
            turtlepositions.append(turtlePosition)

            self.play(Write(turtlePosition))
            self.play(Write(distLabel))

            dist = realdist * (10 / 13)
            currentxoffset += dist / 10
            print(currentxoffset)
            self.play(clocktimeSeconds.animate(run_time=time, rate_func=rate_functions.linear).set_value(clocktimeSeconds.get_value() + time), achill.animate(run_time=time, rate_func=rate_functions.linear).shift(dist * RIGHT),
                      turtle.animate(run_time=time, rate_func=rate_functions.linear).shift((dist / 10) * RIGHT))

        upperbackgroundrect = Rectangle(width=14, height=8, color=BLACK, fill_color=BLACK, fill_opacity=1).align_to(table2.submobjects[2], DOWN).set_z_index(1)
        lowerbackgroundrect = Rectangle(width=14, height=8, color=BLACK, fill_color=BLACK, fill_opacity=1).align_to(table2.submobjects[3], UP).shift(2 * DOWN).set_z_index(1)

        self.play(Unwrite(clock))
        self.add(upperbackgroundrect, lowerbackgroundrect)

        newvalues = []
        newstepsize = 30
        for s in range(newstepsize):
            step = s + 3
            shiftstep = step

            if 10 < s < 20:
                step += (step+15)*(step+15)
            elif s > 10:
                step += 7946

            realdist = (10 / pow(10, step))

            timeString = str(10 / pow(10, step - 1)) + " s"
            distString = str(realdist) + " m"

            if (step > 10):
                timeString = "1e-" + str(step - 1) + " s"
                distString = "1e-" + str(step) + " m"

            timeLabel = Text(timeString).scale(.4).next_to(table1.submobjects[3], RIGHT).align_to(table1.submobjects[2], UP).shift(0.3 * (shiftstep - 1) * DOWN + 0.2 * DOWN)
            newvalues.append(timeLabel)
            turtleTimeLabel = Text(timeString).scale(.4).next_to(table2.submobjects[3], LEFT).align_to(table2.submobjects[2], UP).shift(0.3 * (shiftstep - 1) * DOWN + 0.2 * DOWN)
            turtleDistLabel = Text(distString).scale(.4).next_to(table2.submobjects[3], RIGHT).align_to(table2.submobjects[2], UP).shift(0.3 * (shiftstep - 1) * DOWN + 0.2 * DOWN)
            newvalues.append(turtleTimeLabel)
            newvalues.append(turtleDistLabel)
            distLabel = Text(distString).scale(.4).next_to(table1.submobjects[3], LEFT).align_to(table1.submobjects[2], UP).shift(0.3 * shiftstep * DOWN + 0.2 * DOWN)
            newvalues.append(distLabel)

        for v in newvalues:
            values.append(v)

        self.play(Write(VGroup(*newvalues)))

        self.play(VGroup(*values).animate.shift(7.5 * UP))
