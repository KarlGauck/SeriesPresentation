from manim import *


class Start(Scene):
    def construct(self):
        konvergenzText = Text('Konvergenz / Divergenz').scale(1.2)
        beschränktheitsText = Text(r'Beschränktheit').scale(1.2).align_to(konvergenzText, LEFT)
        monotonieText = Text('Monotonie').next_to(beschränktheitsText, 3.5 * UP).scale(1.2).align_to(beschränktheitsText, LEFT)
        konvergenzText.next_to(beschränktheitsText, 3.5 * DOWN).align_to(beschränktheitsText, LEFT)

        self.play(Write(monotonieText))
        self.play(Write(beschränktheitsText))
        self.play(Write(konvergenzText))

        self.play(Indicate(monotonieText))
        self.play(Indicate(beschränktheitsText))
        self.play(Indicate(konvergenzText))

        summaryLine1 = Text(r'Eine Folge ist streng monoton wachsend, wenn gilt:').scale(0.8).shift(1.5 * UP)
        summaryLine2 = MathTex(r'a_{n+1} - a_n > 0', color=RED).next_to(summaryLine1, DOWN)
        summaryLine3 = Text('oder').scale(0.8).next_to(summaryLine2, DOWN)
        summaryLine4 = MathTex(r'\frac{a_{n+1}}{a_n} > 1', color=BLUE).next_to(summaryLine3, DOWN)

        summaryGroup = VGroup(summaryLine1, summaryLine2, summaryLine3, summaryLine4)

        self.play(FadeIn(summaryGroup, shift=20 * LEFT), VGroup(beschränktheitsText, monotonieText, konvergenzText).animate.shift(20 * LEFT))

        axesgroup = VGroup()
        axes = Axes(x_range=[0, 8], y_range=[0, 1.2], x_length=8, y_length=5 * 1.2).shift(2 * RIGHT).add_coordinates()
        axesgroup.add(axes)
        series = lambda n: n / (n + 1)
        dotgroup = VGroup()
        axesgroup.add(dotgroup)
        nmax = 8
        for val in range(nmax):
            n = val
            an = series(n)
            dot = Dot(color=YELLOW).shift((n * RIGHT + an * UP * 5) + 2 * LEFT + 3 * DOWN)
            dotgroup.add(dot)
        upperbound = Line(color=BLUE, start=2 * LEFT, end=RIGHT * 7, stroke_width=5).shift(2 * UP)
        lowerbound = Line(color=BLUE, start=2 * LEFT, end=RIGHT * 7, stroke_width=5).shift(3 * DOWN)
        uppertext1 = Text("nach oben", color=BLUE).scale(.8)
        uppertext2 = Text("beschränkt", color=BLUE).scale(.8).next_to(uppertext1, DOWN).align_to(uppertext1, LEFT)
        upperlabel = VGroup(uppertext1, uppertext2).move_to(upperbound).align_on_border(LEFT).shift((RIGHT + DOWN) * .5)
        und = Text("&", color=RED).scale(.8).next_to(upperlabel, DOWN)
        lowertext1 = Text("nach unten", color=BLUE).scale(.8)
        lowertext2 = Text("beschränkt", color=BLUE).scale(.8).next_to(lowertext1, DOWN).align_to(lowertext1, LEFT)
        lowerlabel = VGroup(lowertext1, lowertext2).move_to(lowerbound).align_on_border(LEFT).shift((RIGHT + UP) * .5).next_to(und, DOWN)
        gleich = Text("=", color=RED).scale(.8).next_to(lowerlabel, DOWN)
        beschränkttext = Text("beschränkt", color=BLUE).scale(.8).next_to(gleich, DOWN)

        self.add(axesgroup, upperbound, lowerbound, upperlabel, lowerlabel, und, gleich, beschränkttext)
        self.play(FadeIn(VGroup(axesgroup, upperbound, lowerbound, upperlabel, lowerlabel, und, gleich, beschränkttext), shift=20 * LEFT), summaryGroup.animate.shift(20 * LEFT))

        convergesif = MathTex(r'Die\ Folge\ (a_n)\ konvergiert,\ wenn\ gilt:').align_on_border(UP)
        prooflabel = MathTex(r'\forall {{\epsilon > 0}}: \exists N_{\epsilon} \in \mathbb{N}}: {{\forall n \ge N_{\epsilon}:}} | a_{n} - g| {{<}} \epsilon').next_to(convergesif, DOWN)
        proofl2 = MathTex(r'\textrm{der Abstand zwischen dem Folgenglied und der Grenze g}')
        proofl1 = MathTex(r'\textrm{für alle }\epsilon \textrm{ größer als 0 gibt es ein } N_{\epsilon} \textrm{, sodass }').next_to(proofl2, UP)
        proofl3 = MathTex(r'\textrm{ für jedes Folgenglied nach } a_{N_{\epsilon}} \textrm{ kleiner ist als } \epsilon').next_to(proofl2, DOWN)
        divergesif = MathTex(r'Die\ Folge\ (a_n)\ divergiert,\ wenn\ sie\ nicht\ konvergiert').align_on_border(DOWN).shift(UP * .5)

        self.play(FadeIn(VGroup(proofl1, proofl2, proofl3, convergesif, divergesif, prooflabel), shift=20 * LEFT), FadeOut(VGroup(axesgroup, upperbound, lowerbound, upperlabel, lowerlabel, und, gleich, beschränkttext), shift=20 * LEFT))


class Monotonie(Scene):
    def construct(self):
        seriesLabel = MathTex(r'(a_n) =  \frac{n}{n+1}').scale(3)
        self.play(Write(seriesLabel))

        axesgroup = VGroup()
        axes = Axes(x_range=[0, 8], y_range=[0, 1.2], x_length=8, y_length=5 * 1.2).shift(2 * RIGHT).add_coordinates()
        axesgroup.add(axes)
        self.play(seriesLabel.animate.scale(1 / 3).align_on_border(UP + LEFT), Write(axes))

        series = lambda n: n / (n + 1)

        dotgroup = VGroup()
        axesgroup.add(dotgroup)
        labelgroup = VGroup()
        nmax = 8
        for val in range(nmax):
            n = val
            an = series(n)

            rate = 1 if n < 3 else .3

            labelscale = 0.9
            yoffset = ((n % 4) * 1.3 + 1.5) * DOWN
            xoffset = int(n / 4) * 2 * RIGHT
            color = WHITE

            nlabel = MathTex(r'a_' + str(n) + r' = \frac{n}{n+1}', color=color).scale(labelscale).align_on_border(UP + LEFT).shift(yoffset + xoffset)
            self.play(Write(nlabel, run_time=rate))

            nlabel1 = MathTex(r'a_' + str(n) + r' = \frac{' + str(n) + '}{' + str(n) + '+1}', color=color).scale(labelscale).align_on_border(UP + LEFT).shift(yoffset + xoffset)
            self.play(Transform(nlabel, nlabel1, run_time=rate))

            nlabel2 = MathTex(r'a_' + str(n) + r' = \frac{' + str(n) + '}{' + str(n + 1) + '}', color=color).scale(labelscale).align_on_border(UP + LEFT).shift(yoffset + xoffset)
            self.play(Transform(nlabel, nlabel2, run_time=rate))

            dot = Dot(color=YELLOW).shift((n * RIGHT + an * UP * 5) + 2 * LEFT + 3 * DOWN)
            dotgroup.add(dot)
            labelgroup.add(nlabel)
            self.play(Write(dot, run_time=rate))

        list = [3, 4]
        for i in list:
            dot1 = dotgroup.submobjects[i]
            dot2 = dotgroup.submobjects[i + 1]

            anl = MathTex(r'a_n', color=ORANGE).next_to(dot1, DOWN)
            an1l = MathTex(r'a_{n+1}', color=ORANGE).next_to(dot2, DOWN)

            self.play(Write(anl), Circumscribe(dot1, color=ORANGE))
            self.play(Write(an1l), Circumscribe(dot2, color=ORANGE))

            line = Line(start=dot1, end=dot2, color=GREEN)
            linelabel = MathTex(r'\Delta a > 0', color=GREEN).next_to(line, RIGHT)

            self.play(Write(VGroup(line, linelabel)))

            self.play(Unwrite(anl), Unwrite(an1l), Unwrite(line), Unwrite(linelabel))

        self.play(Unwrite(axesgroup), Unwrite(seriesLabel), Unwrite(labelgroup))

        method1L = MathTex(r'\Delta a = a_{n+1} - a_n', color=RED).scale(2).align_on_border(2 * LEFT)
        method2L = MathTex(r'\frac{a_{n+1}}{a_n}', color=BLUE).scale(2).align_on_border(2 * RIGHT)

        self.play(Write(method1L))
        self.play(Write(method2L))

        self.play(method1L.animate.center().scale(.5).set_color(WHITE), FadeOut(method2L, shift=5 * RIGHT))

        eq1 = MathTex(r'{n+1 \over n+1+1} - {n \over n+1}')
        self.play(method1L.animate.shift(UP * 2), Write(eq1))

        eq2 = MathTex(r'{(n+1)^2 \over (n+1)(n+2)} - {n(n+2) \over (n+1)(n+2)}').shift(2 * DOWN)
        self.play(Write(eq2))

        eq3 = MathTex(r'{n^2 + 2n + 1 \over (n+1)(n+2)} - {n^2 + 2n \over (n+1)(n+2)}').shift(2 * DOWN)
        self.play(FadeOut(method1L, shift=2 * UP), eq1.animate.shift(UP * 2), eq2.animate.shift(UP * 2), FadeIn(eq3, shift=UP * 2))

        eq4 = MathTex(r'{n^2 + 2n + 1 n^2 - 2n \over n^2 + 3n + 2}').shift(2 * DOWN)
        self.play(FadeOut(eq1, shift=2 * UP), eq2.animate.shift(UP * 2), eq3.animate.shift(UP * 2), FadeIn(eq4, shift=UP * 2))

        eq5 = MathTex(r'{1 \over n^2 + 3n + 2}').shift(2 * DOWN)
        self.play(FadeOut(eq2, shift=2 * UP), eq3.animate.shift(UP * 2), eq4.animate.shift(UP * 2), FadeIn(eq5, shift=UP * 2))

        self.play(FadeOut(eq3, shift=2 * UP), FadeOut(eq4, shift=2 * UP), eq5.animate.center().shift(UP))

        brace = Brace(eq5, color=YELLOW)
        label = MathTex(r'{{>}} 0').next_to(brace, DOWN)

        self.play(Write(VGroup(brace, label)))

        implies = MathTex(r'\implies \textrm{streng monoton steigend }', color=RED).next_to(label, DOWN)
        self.play(Write(implies))

        self.play(label.submobjects[0].animate.rotate(PI).set_color(RED))
        self.play(Transform(implies, MathTex(r'\implies \textrm{streng monoton fallend }', color=RED).next_to(label, DOWN)))

        method2L.center()
        self.play(FadeOut(VGroup(eq5, label, brace, implies), shift=10 * LEFT), FadeIn(method2L, shift=10 * LEFT))

        eq1 = MathTex(r'{\frac{n+1}{n+2}} \over {\frac{n}{n+1}}').scale(2)
        self.play(ReplacementTransform(method2L, eq1))

        eq2 = MathTex(r'{\frac{n+1}{n+2}} * {\frac{n+1}{n}}').scale(2)
        self.play(ReplacementTransform(eq1, eq2))

        eq3 = MathTex(r'\frac{n^2 + 2n + 1}{n^2 + 2n}').scale(2)
        self.play(ReplacementTransform(eq2, eq3))

        self.play(eq3.animate.shift(UP))

        brace = Brace(eq3, color=YELLOW)
        label = MathTex(r'{{ > }} 1').next_to(brace, DOWN)

        self.play(Write(VGroup(brace, label)))

        implies = MathTex(r'\implies \textrm{streng monoton wachsend}', color=RED).next_to(label, DOWN)
        self.play(Write(implies))

        self.play(label.submobjects[0].animate.set_color(RED).rotate(PI))
        self.play(Transform(implies, MathTex(r'\implies \textrm{streng monoton fallend}', color=RED).next_to(label, DOWN)))

        but = MathTex(r'\textrm{Nur wenn } a_n  > 0 \land a_{n+1} > 0').next_to(implies, DOWN)
        self.play(Write(but))

        self.play(Unwrite(VGroup(eq3, brace, label, implies, but)))

        summaryLine1 = Text(r'Eine Folge ist streng monoton wachsend, wenn gilt:').scale(0.8).shift(1.5 * UP)
        summaryLine2 = MathTex(r'a_{n+1} - a_n > 0', color=RED).next_to(summaryLine1, DOWN)
        summaryLine3 = Text('oder').scale(0.8).next_to(summaryLine2, DOWN)
        summaryLine4 = MathTex(r'\frac{a_{n+1}}{a_n} > 1', color=BLUE).next_to(summaryLine3, DOWN)

        summaryGroup = VGroup(summaryLine1, summaryLine2, summaryLine3, summaryLine4)
        self.play(Write(summaryGroup))


class Beschränktheit(Scene):
    def construct(self):
        axesgroup = VGroup()
        axes = Axes(x_range=[0, 8], y_range=[0, 1.2], x_length=8, y_length=5 * 1.2).shift(2 * RIGHT).add_coordinates()
        axesgroup.add(axes)

        series = lambda n: n / (n + 1)

        dotgroup = VGroup()
        axesgroup.add(dotgroup)
        nmax = 8
        for val in range(nmax):
            n = val
            an = series(n)

            dot = Dot(color=YELLOW).shift((n * RIGHT + an * UP * 5) + 2 * LEFT + 3 * DOWN)
            dotgroup.add(dot)

        self.add((axesgroup))

        upperbound = Line(color=BLUE, start=2 * LEFT, end=RIGHT * 7, stroke_width=5).shift(2 * UP)
        lowerbound = Line(color=BLUE, start=2 * LEFT, end=RIGHT * 7, stroke_width=5).shift(3 * DOWN)

        uppertext1 = Text("nach oben", color=BLUE).scale(.8)
        uppertext2 = Text("beschränkt", color=BLUE).scale(.8).next_to(uppertext1, DOWN).align_to(uppertext1, LEFT)
        upperlabel = VGroup(uppertext1, uppertext2).move_to(upperbound).align_on_border(LEFT).shift((RIGHT + DOWN) * .5)

        lowertext1 = Text("nach unten", color=BLUE).scale(.8)
        lowertext2 = Text("beschränkt", color=BLUE).scale(.8).next_to(lowertext1, DOWN).align_to(lowertext1, LEFT)
        lowerlabel = VGroup(lowertext1, lowertext2).move_to(lowerbound).align_on_border(LEFT).shift((RIGHT + UP) * .5)

        self.play(Write(VGroup(upperbound, lowerbound)))
        self.play(Circumscribe(upperbound))
        self.play(Write(upperlabel))
        self.play(Circumscribe(lowerbound))
        self.play(Write(lowerlabel))

        und = Text("&", color=RED).scale(.8).next_to(upperlabel, DOWN)
        gleich = Text("=", color=RED).scale(.8)

        self.play(Write(und), lowerlabel.animate.next_to(und, DOWN))
        gleich.next_to(lowerlabel, DOWN)

        beschränkttext = Text("beschränkt", color=BLUE).scale(.8).next_to(gleich, DOWN)
        self.play(Write(VGroup(gleich, beschränkttext)))

        self.play(Unwrite(beschränkttext), Unwrite(upperlabel), Unwrite(gleich), Unwrite(und))
        self.play(Circumscribe(dotgroup.submobjects[0], color=GREEN))

        an0 = MathTex(r'a_0 = 0', color=GREEN).scale(.8).next_to(dotgroup.submobjects[0], DOWN).align_on_border(LEFT)
        self.play(Write(an0), VGroup(axesgroup, upperbound, lowerbound).animate.shift(.5 * UP))

        monotonie = MathTex(r'\textrm{+ streng monoton wachsend}', color=GREEN).scale(.8).next_to(an0, RIGHT)
        implies = MathTex(r'\implies \textrm{ nach unten beschränkt}', color=GREEN).scale(.8).next_to(monotonie, RIGHT)
        self.play(Write(VGroup(monotonie, implies)))

        questionmark = Text("?", color=RED).scale(3).move_to(axesgroup)
        self.play(Circumscribe(upperbound, color=RED), upperbound.animate.set_color(RED))
        self.play(FadeIn(questionmark, scale=1 / 4, run_time=.5))


class Convergence(Scene):
    def construct(self):
        def distanceLine(pos1, pos2, tiplen, color):
            group = VGroup()
            group.add(Line(start=pos1, end=pos2, color=color))
            group.add(Line(start=pos1 + (tiplen / 2) * RIGHT, end=pos1 + (tiplen / 2) * LEFT, color=color, stroke_width=6))
            group.add(Line(start=pos2 + (tiplen / 2) * RIGHT, end=pos2 + (tiplen / 2) * LEFT, color=color, stroke_width=6))
            return group

        # ==============================================================================================================
        # ------------------------------------------ construct series --------------------------------------------------
        # ==============================================================================================================

        axesgroup = VGroup()
        axes = Axes(x_range=[0, 8], y_range=[0, 1.2], x_length=8, y_length=5 * 1.2).shift(2 * RIGHT).add_coordinates()
        axesgroup.add(axes)

        series = lambda n: n / (n + 1)

        dotgroup = VGroup()
        axesgroup.add(dotgroup)
        nmax = 8
        for val in range(nmax):
            n = val
            an = series(n)

            dot = Dot(color=YELLOW).shift((n * RIGHT + an * UP * 5) + 2 * LEFT + 3 * DOWN)
            dotgroup.add(dot)

        self.add((axesgroup))

        upperbound = Line(color=RED, start=2 * LEFT, end=RIGHT * 7, stroke_width=5).shift(2 * UP)
        upperboundlabel = MathTex(r'Obere Grenze?').scale(.8).next_to(upperbound, DOWN)
        axesgroup.add(upperboundlabel, upperbound)
        axesgroup.save_state()
        self.add(upperbound)
        self.play(Write(upperboundlabel))
        self.play(Indicate(upperbound))

        self.play(upperbound.animate.shift(.5 * UP))
        self.play(upperbound.animate.shift(DOWN))
        self.play(upperbound.animate.shift(.5 * UP))

        # ==============================================================================================================
        # -------------------------------------------- convergence -----------------------------------------------------
        # ==============================================================================================================

        limlabel = MathTex(r'\frac{n}{n+1} \ \ \ \underset{n \rightarrow \infty}{\rightarrow} \ \ \ g\ ?').scale(1.5).next_to(axesgroup, LEFT).shift(3.5 * RIGHT)
        limlabel1 = MathTex(r'\frac{n}{n+1} \ \ \ \underset{n \rightarrow \infty}{\rightarrow} \ \ \ \infty\ ?').scale(1.5).next_to(axesgroup, LEFT).shift(3.5 * RIGHT)
        limlabel2 = MathTex(r'\frac{n}{n+1} \ \ \ \underset{n \rightarrow \infty}{\rightarrow} \ \ \ -\infty\ ?').scale(1.5).next_to(axesgroup, LEFT).shift(3.5 * RIGHT)
        limlabel3 = MathTex(r'\frac{n}{n+1} \ \ \ \underset{n \rightarrow \infty}{\rightarrow} \ \ \ ?').scale(1.5).next_to(axesgroup, LEFT).shift(3.5 * RIGHT)
        self.play(axesgroup.animate.scale(0.5).align_on_border(RIGHT), Write(limlabel))
        self.play(TransformMatchingShapes(limlabel, limlabel1))
        self.play(TransformMatchingShapes(limlabel1, limlabel2))
        self.play(TransformMatchingShapes(limlabel2, limlabel3))

        term = MathTex(r'\frac{n}{n+1}').scale(3)
        self.play(TransformMatchingShapes(limlabel3, term), Unwrite(axesgroup))
        numbers = [10, 42, 404, 1337]

        for n in range(len(numbers)):
            number = numbers[n]
            nterm = MathTex(r'\frac{' + str(number) + r'}{' + str(number) + '+1}').scale(3)
            fterm = MathTex(r'\frac{' + str(number) + r'}{' + str(number + 1) + '}').scale(3)
            self.play(Transform(term, nterm))
            self.play(Transform(term, fterm))

            res = MathTex(r'= ' + str(round(number / (number + 1), 3))).scale(3).next_to(term, RIGHT)
            self.play(Write(res))
            self.play(Unwrite(res))

        limlabel = MathTex(r'\lim_{n \rightarrow \infty}{\frac{n}{n+1}} = \ 1').scale(3)
        self.play(FadeOut(term, shift=3 * UP), FadeIn(limlabel, shift=3 * UP))

        convergesif = MathTex(r'Die\ Folge\ (a_n)\ konvergiert,\ wenn\ gilt:').align_on_border(UP)
        prooflabel = MathTex(r'\forall {{\epsilon > 0}}: \exists N_{\epsilon} \in \mathbb{N}}: {{\forall n \ge N_{\epsilon}:}} | a_{n} - g| {{<}} \epsilon').next_to(convergesif, DOWN)

        self.play(Write(convergesif))
        self.play(Write(prooflabel))

        axesgroup.saved_state.center().shift(0.6 * DOWN + RIGHT)

        # start

        self.play(FadeOut(limlabel, shift=10*RIGHT))

        proofl2 = MathTex(r'\textrm{der Abstand zwischen dem Folgenglied und der Grenze g}')
        proofl1 = MathTex(r'\textrm{für alle }\epsilon \textrm{ größer als 0 gibt es ein } N_{\epsilon} \textrm{, sodass }').next_to(proofl2, UP)
        proofl3 = MathTex(r'\textrm{ für jedes Folgenglied nach } a_{N_{\epsilon}} \textrm{ kleiner ist als } \epsilon').next_to(proofl2, DOWN)
        self.play(Write(VGroup(proofl1, proofl2, proofl3)))

        # end

        axesgroup.saved_state.remove(upperboundlabel)
        self.play(Restore(axesgroup), Unwrite(VGroup(proofl1, proofl2, proofl3)), FadeOut(convergesif, shift=UP), prooflabel.animate.shift(UP))

        # EPSILON

        epsilongreaterzero = MathTex(r'\epsilon > 0', color=BLUE_C).next_to(prooflabel, DOWN).align_on_border(LEFT)
        self.play(TransformMatchingShapes(prooflabel.submobjects[1].copy(), epsilongreaterzero), Unwrite(upperboundlabel))

        axesoff = dotgroup[0].get_x() * RIGHT + dotgroup[0].get_y() * UP
        epsilon = ValueTracker(0.25)
        epsilonx = ValueTracker(0.7)

        epsilonequals = MathTex(r'\epsilon = ', color=BLUE_C).next_to(epsilongreaterzero, DOWN).align_to(epsilongreaterzero, LEFT)

        def epsilonNum():
            dec = DecimalNumber(epsilon.get_value(), color=BLUE_C).next_to(epsilonequals, RIGHT)
            return dec

        epsilonNum = always_redraw(epsilonNum)
        self.play(Write(VGroup(epsilonequals, epsilonNum)))

        def epsilonLine():
            pos1 = axesoff + 5 * UP + epsilonx.get_value() * RIGHT + 7.5 * RIGHT
            pos2 = axesoff + (5 - epsilon.get_value() * 5) * UP + epsilonx.get_value() * RIGHT + 7.5 * RIGHT
            tiplen = 0.2
            return distanceLine(pos1, pos2, tiplen, BLUE_C).set_z_index(1)

        epsilonline = always_redraw(epsilonLine)
        self.play(Write(epsilonline))

        self.play(prooflabel.submobjects[1].animate.set_color(BLUE_C))

        # DISTANCE

        distlabel = MathTex(r'| {{a_n}} - {{g}}|', color=GREEN_C).next_to(epsilonequals, DOWN).align_to(epsilonequals, LEFT).shift(DOWN * 0.3)
        self.play(ReplacementTransform(prooflabel.submobjects[4].copy(), distlabel))

        self.play(Circumscribe(distlabel.submobjects[1]))
        self.play(*[Flash(d) for d in dotgroup.submobjects])

        self.play(Circumscribe(distlabel.submobjects[3]))
        self.play(Indicate(upperbound))

        self.play(Circumscribe(distlabel.submobjects[0], color=GREEN_C), Circumscribe(distlabel.submobjects[4], color=GREEN_C), Circumscribe(distlabel.submobjects[2], color=GREEN_C))

        def distline(n):
            pos1 = axesoff + 5 * UP + n * RIGHT
            pos2 = axesoff + (5 - (5 - (n / (n + 1)) * 5)) * UP + n * RIGHT
            tiplen = 0.2
            return distanceLine(pos1, pos2, tiplen, GREEN_C)

        distlines = [distline(n) for n in range(nmax)]

        self.play(*[Write(l) for l in distlines])
        self.play(prooflabel.submobjects[4].animate.set_color(GREEN_C))

        # NE

        nelabel = MathTex(r'N_{\epsilon} = ', color=ORANGE).next_to(distlabel, DOWN).align_to(distlabel, LEFT).shift(.3 * DOWN)
        self.play(ReplacementTransform(prooflabel.submobjects[3].copy(), nelabel))

        nex = ValueTracker(2)
        nevalue = always_redraw(lambda: MathTex(str(int(nex.get_value() + .5)), color=ORANGE).next_to(nelabel, RIGHT))

        ne = DashedLine(start=0 * UP, end=6 * UP, color=ORANGE, stroke_width=6).set_z_index(2)
        neshift = axesoff + 3 * UP
        ne.add_updater(lambda ne: ne.center().shift(neshift + nex.get_value() * RIGHT))

        self.play(Write(ne), Write(nevalue))

        # FÜR ALLE LOGIK

        self.play(Circumscribe(VGroup(*prooflabel.submobjects[4:])))

        brace = Brace(VGroup(*prooflabel.submobjects[4:]), color=YELLOW)
        self.play(Write(brace), prooflabel.submobjects[6].animate.set_color(BLUE_C))

        echeckline = always_redraw(lambda: DashedLine(color=BLUE_C, start=3.25 * LEFT, end=RIGHT * 5, stroke_width=5).next_to(epsilonline, LEFT).align_to(epsilonline, DOWN).shift(RIGHT * .25))
        self.play(Write(echeckline))

        for l in distlines:
            l.add_updater(lambda l: l.set_color(GREEN_C if epsilon.get_value() > 1 - (distlines.index(l) / (distlines.index(l) + 1)) else GRAY))
            l.add_updater(lambda l: l.set_opacity(1.0 if epsilon.get_value() > 1 - (distlines.index(l) / (distlines.index(l) + 1)) else 0.4))

        values = [0.1, 0.8]
        for value in values:
            self.play(epsilon.animate(run_time=3).set_value(value))

        self.play(Transform(brace, Brace(VGroup(*prooflabel.submobjects[2:4]), color=YELLOW)), prooflabel.submobjects[2].animate.set_color(ORANGE))
        self.play(epsilon.animate.set_value(5 / 16))
        self.play(nex.animate.set_value(3))
        self.play(Circumscribe(VGroup(*distlines[3:])))

        self.play(epsilon.animate.set_value(5 / 32))
        self.play(nex.animate.set_value(6))
        self.play(Circumscribe(VGroup(*distlines[6:])))

        for l in distlines:
            l.updaters.clear()

        self.play(Unwrite(VGroup(axesgroup, epsilongreaterzero, epsilonequals, epsilonline, echeckline, ne, epsilonNum, distlabel, nelabel, nevalue, brace)), *[Unwrite(l) for l in distlines])

        # ==============================================================================================================
        # ----------------------------------------- Mathematical Proof -------------------------------------------------
        # ==============================================================================================================

        def align_by_tex(ob1, ob2, si1, si2, direction):
            origin = ob2.submobjects[si2]
            ob1.submobjects[si1].align_to(origin, direction)
            for s in ob1.submobjects[si1 + 1:]:
                index = ob1.submobjects.index(s) - 1
                s.next_to(ob1.submobjects[index], RIGHT)
            for s in ob1.submobjects[:si1][::-1]:
                index = ob1.submobjects.index(s) + 1
                s.next_to(ob1.submobjects[index], LEFT)

        equationL = MathTex(r'|\frac{n}{n+1} - g| < \epsilon')
        group = VGroup(*prooflabel.submobjects[4:])
        prooflabel.save_state()
        self.play(group.animate.center(), FadeOut(VGroup(*prooflabel.submobjects[:4]), run_time=0.5))

        SIGNCOLOR = YELLOW

        self.play(TransformMatchingShapes(group, equationL))
        ntex = MathTex(r'|\frac{n}{n+1} - 1| {{<}} \epsilon')
        ntex.submobjects[1].color = SIGNCOLOR
        self.play(TransformMatchingShapes(equationL, ntex))

        greaterzero = MathTex(r'{{Fall\ 1:}} \ |\frac{n}{n+1} - 1| \ge 0').align_on_border(UP + LEFT)
        greaterzero.submobjects[1].color = RED
        leftGroup = VGroup(greaterzero, ntex)

        splitLine = Line(start=4 * UP, end=4 * DOWN)

        smallerzero = MathTex(r'{{Fall\ 2:}}\ |\frac{n}{n+1} - 1| < 0').next_to(splitLine, RIGHT).shift(.3 * RIGHT).align_on_border(UP)
        smallerzero.submobjects[1].color = BLUE
        rightGroup = VGroup(smallerzero)

        self.play(AnimationGroup(Write(greaterzero), Write(smallerzero), lag_ratio=0.1))

        EQSCALE = .8
        DSHIFT = 1

        # ----------------------------------------------------------- FALL 1 --------------------------------------------------

        splitLine.shift(4 * RIGHT)
        self.play(FadeIn(splitLine, shift=4 * RIGHT), rightGroup.animate.shift(4 * RIGHT).set_opacity(0.3), ntex.animate.scale(EQSCALE).next_to(greaterzero, DOWN).align_on_border(LEFT).shift(0.3 * DOWN))

        e1L = MathTex(r'\frac{n}{n+1} - 1 {{<}} \epsilon').scale(EQSCALE).move_to(ntex).shift(DOWN * DSHIFT).align_to(ntex, LEFT)
        leftGroup.add(e1L)
        e1L.submobjects[1].color = SIGNCOLOR
        align_by_tex(e1L, ntex, 1, 1, LEFT)
        self.play(Write(e1L))

        u1L = MathTex(r'|\ +\ 1').scale(EQSCALE).next_to(e1L, RIGHT).shift(3 * RIGHT)
        leftGroup.add(u1L)
        self.play(Write(u1L))

        e2L = MathTex(r'\frac{n}{n+1} {{<}} \epsilon + 1').scale(EQSCALE).move_to(e1L).shift(DOWN * DSHIFT).align_to(e1L, LEFT)
        e2L.submobjects[1].color = SIGNCOLOR
        leftGroup.add(e2L)
        align_by_tex(e2L, e1L, 1, 1, LEFT)
        self.play(Write(e2L))

        u2L = MathTex(r'|\ *\ (n+1)\ \ \ (n+1 \ne 0)').scale(EQSCALE).move_to(e2L, RIGHT).align_to(u1L, LEFT)
        leftGroup.add(u2L)
        self.play(Write(u2L))

        e3L = MathTex(r'n {{<}} (\epsilon+1)(n+1)').scale(EQSCALE).move_to(e2L).shift(DOWN * DSHIFT).align_to(e2L, LEFT)
        e3L.submobjects[1].color = SIGNCOLOR
        leftGroup.add(e3L)
        align_by_tex(e3L, e2L, 1, 1, LEFT)
        self.play(Write(e3L))

        ntex = MathTex(r'n {{<}} \epsilon n + \epsilon + n + 1').scale(EQSCALE).move_to(e2L).shift(DOWN * DSHIFT).align_to(e2L, LEFT)
        ntex.submobjects[1].color = SIGNCOLOR
        align_by_tex(ntex, e2L, 1, 1, LEFT)
        self.play(Transform(e3L, ntex))

        u3L = MathTex(r'|\ -n - \epsilon - 1').scale(EQSCALE).next_to(e3L, RIGHT).align_to(u2L, LEFT)
        leftGroup.add(u3L)
        self.play(Write(u3L))

        e4L = MathTex(r'-\epsilon - 1 {{<}} \epsilon n').scale(EQSCALE).move_to(e3L).shift(DOWN * DSHIFT).align_to(e3L, LEFT)
        e4L.submobjects[1].color = SIGNCOLOR
        leftGroup.add(e4L)
        align_by_tex(e4L, e3L, 1, 1, LEFT)
        self.play(Write(e4L))

        u4L = MathTex(r'|\ * \frac{1}{\epsilon}').scale(EQSCALE).next_to(e4L, RIGHT).align_to(u3L, LEFT)
        leftGroup.add(u4L)
        self.play(Write(u4L))

        e5L = MathTex(r'- \frac{\epsilon + 1}{\epsilon} {{<}} n').scale(EQSCALE).move_to(e4L).shift(DOWN * DSHIFT).align_to(e4L, LEFT)
        e5L.submobjects[1].color = SIGNCOLOR
        leftGroup.add(e5L)
        align_by_tex(e5L, e4L, 1, 1, LEFT)
        self.play(Write(e5L))

        brace1L = Brace(e5L, LEFT, color=YELLOW).scale(EQSCALE).shift(RIGHT)
        leftGroup.add(brace1L)

        braceLabel1L = MathTex(r' 0 >').scale(EQSCALE).next_to(brace1L, LEFT)
        leftGroup.add(braceLabel1L)

        self.play(e5L.animate.shift(RIGHT))
        self.play(Write(brace1L), Circumscribe(e5L.submobjects[0]), Write(braceLabel1L))

        impliesL = MathTex(r'\implies \ Immer\ wahr \ (warum\ wohl?)', color=RED).scale(EQSCALE).next_to(e5L, RIGHT)
        leftGroup.add(impliesL)
        self.play(Write(impliesL))

        self.play(splitLine.animate.shift(8 * LEFT), leftGroup.animate.shift(8 * LEFT).set_opacity(0.3), rightGroup.animate.shift(8 * LEFT).set_opacity(1))

        # ------------------------------------------------------------ FALL 2 ----------------------------------------------------------
        e1R = MathTex(r'|\frac{n}{n+1} - 1| {{<}} \epsilon').scale(EQSCALE).next_to(smallerzero, DOWN).align_to(smallerzero, LEFT).shift(0.3 * DOWN).shift(RIGHT)
        e1R.submobjects[1].color = SIGNCOLOR
        rightGroup.add(e1R)
        self.play(Write(e1R))

        u1R = MathTex(r'|\ Betrag * -1').scale(EQSCALE).next_to(e1R, RIGHT).shift(2 * RIGHT)
        rightGroup.add(u1R)
        self.play(Write(u1R))

        e2R = MathTex(r'-1*(\frac{n}{n+1} - 1) {{<}} \epsilon').scale(EQSCALE).move_to(e1R).shift(DOWN * DSHIFT).align_to(e1R, LEFT)
        e2R.submobjects[1].color = SIGNCOLOR
        rightGroup.add(e2R)
        align_by_tex(e2R, e1R, 1, 1, LEFT)
        self.play(Write(e2R))

        ntex = MathTex(r'1 - \frac{n}{n+1}{{<}} \epsilon').scale(EQSCALE).move_to(e1R).shift(DOWN * DSHIFT).align_to(e1R, LEFT)
        ntex.submobjects[1].color = SIGNCOLOR
        align_by_tex(ntex, e2R, 1, 1, LEFT)
        self.play(Transform(e2R, ntex))

        u2R = MathTex(r'|\ + \frac{n}{n+1} - \epsilon').scale(EQSCALE).next_to(e2R, RIGHT).align_to(u1R, LEFT)
        rightGroup.add(u2R)
        self.play(Write(u2R))

        e3R = MathTex(r'1 - \epsilon {{<}} \frac{n}{n+1}').scale(EQSCALE).move_to(e2R).shift(DOWN * DSHIFT).align_to(e2R, LEFT)
        e3R.submobjects[1].color = SIGNCOLOR
        rightGroup.add(e3R)
        align_by_tex(e3R, e2R, 1, 1, LEFT)
        self.play(Write(e3R))

        u3R = MathTex(r'|\ *\ (n+1)\ \ \ (n+1 \ne 0)').scale(EQSCALE).next_to(e3R, RIGHT).align_to(u2R, LEFT)
        rightGroup.add(u3R)
        self.play(Write(u3R))

        e4R = MathTex(r'(1 - \epsilon)(n+1) {{<}} n').scale(EQSCALE).move_to(e3R).shift(DOWN * DSHIFT).align_to(e3R, LEFT)
        e4R.submobjects[1].color = SIGNCOLOR
        rightGroup.add(e4R)
        align_by_tex(e4R, e3R, 1, 1, LEFT)
        self.play(Write(e4R))

        ntex = MathTex(r'-\epsilon n + n - \epsilon + 1 {{<}} n').scale(EQSCALE).move_to(e3R).shift(DOWN * DSHIFT).align_to(e3R, LEFT)
        ntex.submobjects[1].color = SIGNCOLOR
        align_by_tex(ntex, e4R, 1, 1, LEFT)
        self.play(Transform(e4R, ntex))

        u4R = MathTex(r'|\ +\epsilon n - n').scale(EQSCALE).next_to(e4R, RIGHT).align_to(u3R, LEFT)
        rightGroup.add(u4R)
        self.play(Write(u4R))

        e5R = MathTex(r'- \epsilon + 1 {{<}} \epsilon n').scale(EQSCALE).move_to(e4R).shift(DOWN * DSHIFT).align_to(e4R, LEFT)
        e5R.submobjects[1].color = SIGNCOLOR
        rightGroup.add(e5R)
        align_by_tex(e5R, e4R, 1, 1, LEFT)
        self.play(Write(e5R))

        u5R = MathTex(r'|\ * \frac{1}{\epsilon}').scale(EQSCALE).next_to(e5R, RIGHT).align_to(u4R, LEFT)
        rightGroup.add(u5R)
        self.play(Write(u5R))

        e6R = MathTex(r'\frac{1 - \epsilon}{\epsilon} {{<}} n').scale(EQSCALE).move_to(e5R).shift(DOWN * DSHIFT).align_to(e5R, LEFT)
        e6R.submobjects[1].color = SIGNCOLOR
        rightGroup.add(e6R)
        align_by_tex(e6R, e5R, 1, 1, LEFT)
        self.play(Write(e6R))

        impliesRArrow = MathTex(r'\implies', color=BLUE).scale(EQSCALE).next_to(e6R, RIGHT)
        impliesR = MathTex(r'\forall \epsilon > 0\ ist\ N_{\epsilon}\ berechenbar', color=BLUE).scale(EQSCALE).next_to(impliesRArrow, RIGHT)
        rightGroup.add(impliesR, impliesRArrow)
        self.play(Write(VGroup(impliesRArrow, impliesR)))

        totalGroup = VGroup(rightGroup, leftGroup, splitLine)
        qed = Text("qed", color=GREEN_D).scale(5).rotate((25 / 360) * 2 * PI)
        self.play(totalGroup.animate.set_opacity(1).scale(0.6).center().shift(.5 * UP))

        prooflabel.saved_state.next_to(totalGroup, DOWN)
        self.play(Restore(prooflabel))
        totalGroup.add(prooflabel)

        always_true = Text("ist immer wahr", color=GREEN_D).next_to(prooflabel, DOWN)
        totalGroup.add(always_true)
        self.play(Write(always_true))

        self.play(FadeIn(qed, scale=3, run_time=.5), totalGroup.animate(run_time=.5).set_opacity(0.3))

        self.play(FadeOut(qed), Unwrite(VGroup(rightGroup, splitLine, leftGroup, prooflabel, always_true)))

        serieslabel = MathTex(r'a_n = (-1)^{n}').scale(3)
        self.play(Write(serieslabel))

        axesgroup = VGroup()
        axes = Axes(x_range=[0, 8], y_range=[-1.2, 1.2], x_length=8, y_length=6 * 1.2).add_coordinates()
        axesgroup.add(axes)

        series = lambda n: pow(-1, n)

        dotgroup = VGroup()
        axesgroup.add(dotgroup)
        nmax = 8
        for val in range(nmax):
            n = val
            an = series(n)
            dot = Dot(color=YELLOW).shift((n-4)*RIGHT + 3*an*UP)
            dotgroup.add(dot)
        self.add((axesgroup))

        self.play(FadeOut(serieslabel, run_time=0.5), Write(axesgroup))

        text = MathTex(r'\textrm{Die Folge } (a_n) \textrm{ konvergiert nicht}').shift(UP)
        text2 = MathTex(r'\implies\textrm{ sie } {{\textrm{divergiert} }}').shift(DOWN)
        text2.submobjects[1].set_color(RED)

        self.play(axesgroup.animate(run_time=.5).set_opacity(0.2), Write(text))
        self.play(Write(text2))
