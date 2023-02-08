import math
import random
from math import *

from manim import *


def lerp(a, b, t):
    return a + (b - a) * t


def createMandelbrot(w, h, z, dx, dy, colored=False):
    palette = [[255, 109, 0],
               [255, 121, 0],
               [36, 0, 70],
               [36, 0, 70],
               [255, 158, 0],
               [36, 0, 70],
               [60, 9, 108],
               [36, 0, 70],
               [123, 44, 191],
               [157, 78, 221]]

    WIDTH = w
    HEIGHT = h
    ZOOM = (WIDTH / 2) * z
    image = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * (0, 255, 0)
    maxIteration = 100
    for x in range(WIDTH):
        for y in range(HEIGHT):
            c = complex((x - WIDTH / 2) / ZOOM - dx, (y - HEIGHT / 2) / ZOOM - dy)
            z = 0 + 0j
            finalStep = 0
            for step in range(maxIteration):
                z = z ** 2 + c
                if abs(z) > 2:
                    finalStep = step
                    break

            H = len(palette)
            color = [0, 0, 0]
            if finalStep != 0 or abs(c) >= 2:
                if colored:
                    k = abs(z)
                    if k <= 0:
                        k = 0.0000000001
                    m = log(k)
                    if m <= 0:
                        m = 0.0000000001
                    nsmooth = finalStep + 1 - log(m) / log(2)

                    color1 = palette[floor(nsmooth) % H]
                    color2 = palette[(floor(nsmooth) + 1) % H]
                    alpha = nsmooth % 1
                    color = [lerp(color1[0], color2[0], alpha), lerp(color1[1], color2[1], alpha),
                             lerp(color1[2], color2[2], alpha)]
                else:
                    color = [255, 255, 255]

            image[y][x] = color

    return image


class Mandelbrot(Scene):
    def construct(self):
        # ==============================================================================================================
        # ----------------------------------------------- Fraktale -----------------------------------------------------
        # ==============================================================================================================

        fractalTitel = Text("Fraktale")
        self.play(Write(fractalTitel))
        self.play(Unwrite(fractalTitel))

        axes = Axes()
        circle = Circle(color=RED_D, radius=2)
        shapeGroup = VGroup(axes, circle)

        self.play(Write(circle), Write(axes))
        shapeGroup.save_state()
        self.play(shapeGroup.animate.scale(5).shift(5 * (UP + RIGHT)))
        self.play(Restore(shapeGroup))

        square = Square(color=BLUE_D, side_length=2)
        self.play(ReplacementTransform(circle, square))
        shapeGroup.add(square)
        shapeGroup.save_state()
        self.play(shapeGroup.animate.scale(5).shift(5 * (UP + RIGHT)))
        self.play(Restore(shapeGroup))
        self.play(Unwrite(square), Unwrite(circle))

        # ============================================ eine Funktion ===================================================

        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t) + (1 / 7 * np.cos(50 * t)) + (
                    1 / 40) * np.sin(100 * t),
            color=RED,
            x_range=[-6, 6]
        )
        funGroup = VGroup(axes, cos_func)

        self.play(Write(cos_func))
        funGroup.save_state()
        self.play(funGroup.animate.shift(15 * DOWN + 15 * LEFT).scale(20))
        self.play(Restore(funGroup))
        self.play(Unwrite(funGroup))

        # ========================================== das erste Mandelbrotset ===========================================

        uncoloredSet = ImageMobject(createMandelbrot(1080, 1080, 0.6, 0.6, 0.0, False))
        uncoloredSet.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        uncoloredSet.scale(0.8)
        self.play(FadeIn(uncoloredSet))

        coloredSet = ImageMobject(createMandelbrot(1080, 1080, 0.6, 0.6, 0.0, True))
        coloredSet.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        coloredSet.scale(0.8)
        self.play(FadeIn(coloredSet))
        self.remove(uncoloredSet)

        self.play(coloredSet.animate.scale(1.5).align_on_border(LEFT).shift(LEFT))

        # ==============================================================================================================
        # -------------------------------------------------- i ---------------------------------------------------------
        # ==============================================================================================================

        scaling = 1
        rightshift = 10

        i = MathTex(r'i').scale(scaling).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)
        iequals = MathTex(r'i = \sqrt{-1}').scale(scaling).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)

        self.play(Write(i))
        self.play(TransformMatchingShapes(i, iequals))

        # ==============================================================================================================
        # -------------------------------------------------- sqrt -4 ---------------------------------------------------
        # ==============================================================================================================

        fdist = 2
        upshift = UP * fdist

        papasgleichung = MathTex(r'x^2 -4x + 5 = 0').scale(scaling).align_to(coloredSet,
                                                                            LEFT).shift(RIGHT * rightshift)
        self.play(Write(papasgleichung), iequals.animate.shift(upshift))

        sqrtnegfour = MathTex(r'x_{1,2} = { 4 \pm {{\sqrt{-4}}} \over 2 }').scale(scaling).align_to(coloredSet,
                                                                                                    LEFT).shift(
            RIGHT * rightshift)
        self.play(TransformMatchingShapes(papasgleichung, sqrtnegfour))
        self.play(Circumscribe(sqrtnegfour.submobjects[1]))

        sqrtnegonefour = MathTex(r'x_{1,2} = { 4 \pm {{ \sqrt{-1 * 4} }} \over {2} }').scale(scaling).shift(
            fdist * DOWN).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)
        self.play(FadeIn(sqrtnegonefour, shift=upshift))
        self.play(Circumscribe(sqrtnegonefour.submobjects[1]))

        twosqrt = MathTex(r'x_{1,2} = { 4 \pm \sqrt{-1} * {{ \sqrt{4} }} \over 2 }').scale(scaling).shift(
            fdist * DOWN).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)
        self.play(FadeOut(iequals, shift=upshift), sqrtnegfour.animate.shift(upshift),
                  sqrtnegonefour.animate.shift(upshift), FadeIn(twosqrt, shift=upshift))
        self.play(Circumscribe(twosqrt.submobjects[1]))

        foursqrtresolved = MathTex(r'x_{1,2} = { 4 \pm {{ \sqrt{-1} }} * 2 \over 2 }').scale(scaling).shift(
            fdist * DOWN).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)
        self.play(FadeOut(sqrtnegfour, shift=upshift), sqrtnegonefour.animate.shift(upshift),
                  twosqrt.animate.shift(upshift), FadeIn(foursqrtresolved, shift=upshift))
        self.play(Circumscribe(foursqrtresolved.submobjects[1]))

        isqrtresolved = MathTex(r'x_{1,2} = { 4 {{ \pm }} i * 2 \over 2 }').scale(scaling).shift(fdist * DOWN).align_to(
            coloredSet, LEFT).shift(RIGHT * rightshift)
        self.play(FadeOut(sqrtnegonefour, shift=upshift), twosqrt.animate.shift(upshift),
                  foursqrtresolved.animate.shift(upshift), FadeIn(isqrtresolved, shift=upshift))
        self.play(Indicate(isqrtresolved.submobjects[1]))

        res1q = MathTex(r'x_1 =').scale(scaling).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)
        res2q = MathTex(r'x_2 =').scale(scaling).shift(fdist * DOWN).align_to(coloredSet, LEFT).shift(
            RIGHT * rightshift)

        self.play(FadeOut(twosqrt, shift=2 * upshift), FadeOut(foursqrtresolved, shift=2 * upshift),
                  isqrtresolved.animate.shift(2 * upshift), FadeIn(res1q, shift=upshift), FadeIn(res2q, shift=upshift))

        res1 = MathTex(r'x_1 = {{ 2 }} + {{ i }}').scale(scaling).align_to(coloredSet, LEFT).shift(RIGHT * rightshift)
        res2 = MathTex(r'x_2 = 2 - i').scale(scaling).shift(fdist * DOWN).align_to(coloredSet, LEFT).shift(
            RIGHT * rightshift)

        self.play(TransformMatchingShapes(res1q, res1))
        self.play(TransformMatchingShapes(res2q, res2))

        # ==============================================================================================================
        # --------------------------------------- Komplexe Zahl und Ebene ----------------------------------------------
        # ==============================================================================================================

        self.play(Unwrite(res2), Unwrite(isqrtresolved), FadeOut(coloredSet), res1.animate.center().scale(3))
        self.play(res1.submobjects[1].animate.set_color(GREEN_C))
        self.play(res1.submobjects[3].animate.set_color(RED_C))

        complexNum = Text("Komplexe Zahl").scale(1.4).shift(UP * 2)
        self.play(Write(complexNum))

        realPart = Text("Realteil", color=GREEN_C).shift(DOWN * 2 + LEFT * 2)
        self.play(Write(realPart))

        imagPart = Text("Imaginärteil", color=RED_C).shift(DOWN * 2 + RIGHT * 2)
        self.play(Write(imagPart))

        complexplane = ComplexPlane(
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()
        complexplane.stroke_width = 0.1

        # res1.z_index = 1
        realPart.z_index = 1
        imagPart.z_index = 1

        self.play(Unwrite(complexNum), realPart.animate.center().scale(0.4).align_on_border(RIGHT).shift(UP * .5),
                  imagPart.animate.center().scale(0.4).align_on_border(UP).shift(RIGHT) , Unwrite(res1))
        realPart.add_background_rectangle(opacity=0.5)
        imagPart.add_background_rectangle(opacity=0.5)

        z = Dot(color=BLUE_C, fill_color=YELLOW_C).set_z_index(2)
        z.z_index = 1

        stroke_width = 5

        def x_line():
            return Line([0.0, 0.0, 0.0], [z.get_x(), 0.0, 0.0], color=GREEN_C, stroke_width=stroke_width, z_index=1)

        def x_label():
            dec = DecimalNumber(z.get_x(), color=GREEN_C, z_index=1).scale(0.6).move_to(x_line().get_center()).shift(
                DOWN * .5)
            dec.add_background_rectangle(opacity=0.6)
            return dec

        x_lineMob = always_redraw(x_line)
        x_labelMob = always_redraw(x_label)

        def y_line():
            return Line([z.get_x(), 0.0, 0.0], [z.get_x(), z.get_y(), 0.0], color=RED_C, stroke_width=stroke_width,
                        z_index=1)

        def y_label():
            dec = DecimalNumber(z.get_y(), color=RED_C, z_index=1).scale(0.6).move_to(y_line().get_center()).shift(
                0.5 * RIGHT)
            dec.add_background_rectangle(opacity=0.6)
            return dec

        y_lineMob = always_redraw(y_line)
        y_labelMob = always_redraw(y_label)

        self.add(x_lineMob, x_labelMob, y_lineMob, y_labelMob)
        self.play(Write(complexplane), Write(z))

        self.play(z.animate.shift(RIGHT * 2))
        self.play(z.animate.shift(UP))

        self.play(z.animate.shift(DOWN * 4.3234 + 3 * LEFT))
        self.play(z.animate.shift(UP * 7.1101 + LEFT * (3 + e)))

        # ==============================================================================================================
        # --------------------------------------------  zn = zn-1² + c -------------------------------------------------
        # ==============================================================================================================

        mandelbrotSeries = MathTex(r'z_n = z_{n-1}^2 + {{ c }}', z_index=3).scale(3).set_z_index(3)
        mandelbrotSeries.add_background_rectangle(opacity=1)
        self.play(Write(mandelbrotSeries))
        self.play(Indicate(mandelbrotSeries.submobjects[2]), reversed=True)

        xOff = 2.5
        xshift = xOff * LEFT

        def x_line():
            return Line([-xOff, 0.0, 0.0], [z.get_x(), 0.0, 0.0], color=GREEN_C, stroke_width=stroke_width, z_index=1)

        def x_label():
            dec = DecimalNumber(z.get_x() + xOff, color=GREEN_C, z_index=1).scale(0.6).move_to(x_line().get_center()).shift(
                DOWN * .5)
            dec.add_background_rectangle(opacity=0.6)
            return dec

        self.remove(x_lineMob, x_labelMob)
        x_lineMob = always_redraw(x_line)
        x_labelMob = always_redraw(x_label)

        globalGroup = VGroup(complexplane, z, x_lineMob, x_labelMob, y_lineMob, y_labelMob, realPart, imagPart)
        equationBackground = Rectangle(width=5, height=12, fill_color=BLACK, fill_opacity=1,
                                       z_index=2).shift(RIGHT * 5).set_z_index(2)

        self.play(FadeIn(equationBackground), mandelbrotSeries.animate.scale(1 / 3).align_to(equationBackground, LEFT).shift(RIGHT).align_on_border(UP))
        self.play(globalGroup.animate.shift(xshift))

        rf = 3
        x_len = 14.0 + (2 / 9)
        y_len = 8.0
        grid = NumberPlane(
            x_length=x_len,
            y_length=y_len,
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            },
            x_range=[-x_len * rf / 2, x_len * rf / 2],
            y_range=[-y_len * rf / 2, y_len * rf / 2]
        ).shift(xshift)
        globalGroup.add(grid)

        self.play(FadeIn(grid))

        pixels = Group()
        pixelWidth = 10
        pixelHeight = 8
        for dx in range(pixelWidth * rf):
            for dy in range(pixelHeight * rf):

                x = (pixelWidth / 2 - (1 / (2 * rf))) - (1 / rf) * dx
                y = (pixelHeight / 2 - (1 / (2 * rf))) - (1 / rf) * dy

                pixel = Rectangle(width=1 / rf, height=1 / rf, fill_opacity=0.3, stroke_opacity=0.3).shift(xshift + y * UP + x * RIGHT).set_z_index(10)
                if (dx + dy) % 2 == 0:
                    pixel.set_color(BLUE_B)
                else:
                    pixel.set_color(BLUE_C)
                pixels.add(pixel)
        self.play(ShowIncreasingSubsets(pixels, rate_func=there_and_back_with_pause, run_time=3))

        doesItConverge = MathTex("Konvergiert \\ (z_n) ?").align_to(mandelbrotSeries, LEFT + DOWN).shift(3 * DOWN + .8 * LEFT).set_z_index(3)
        yes = MathTex("konvergiert \\rightarrow ").align_to(mandelbrotSeries, LEFT + DOWN).shift(4 * DOWN + .8 * LEFT).set_z_index(3)
        blackSquare = Square(side_length=0.5, fill_color=BLUE, fill_opacity=1).align_to(mandelbrotSeries, LEFT + DOWN).shift(4 * DOWN + 2.8 * RIGHT).set_z_index(3)
        no = MathTex("divergiert \\rightarrow ").align_to(mandelbrotSeries, LEFT + DOWN).shift(5 * DOWN + .8 * LEFT).set_z_index(3)
        whiteSquare = Square(side_length=0.5, fill_color=WHITE, fill_opacity=1).align_to(mandelbrotSeries, LEFT + DOWN).shift(5 * DOWN + 2.8 * RIGHT).set_z_index(3)

        maxIteration = 15
        lineGroup = VGroup()

        values = [[15, 10], [17, 9]]
        x = (pixelWidth / 2 - (1 / (2 * rf))) - (1 / rf) * values[0][0]
        y = (pixelHeight / 2 - (1 / (2 * rf))) - (1 / rf) * values[0][1]
        cdot = Dot(color=GREEN).shift(xshift + x * RIGHT + y * UP).set_z_index(2)
        c = ComplexValueTracker(complex(x, y))
        for vI in range(len(values)):
            v = values[vI]
            x = (pixelWidth / 2 - (1 / (2 * rf))) - (1 / rf) * v[0]
            y = (pixelHeight / 2 - (1 / (2 * rf))) - (1 / rf) * v[1]
            pixel = Rectangle(width=1 / rf, height=1 / rf, color=ORANGE, fill_opacity=0.3, stroke_opacity=0.3).shift(xshift + y * UP + x * RIGHT)
            self.play(FadeIn(pixel))

            c.set_value(complex(x, y))
            text = MathTex(r'c = ' + str(round(c.get_value().real, 2)) + ' + ' + str(round(c.get_value().imag, 2)) + 'i').align_to(mandelbrotSeries, LEFT + DOWN).shift(DOWN + .8*LEFT).set_z_index(3)
            cdot = Dot(color=GREEN).shift(xshift + x * RIGHT + y * UP).set_z_index(2)
            self.play(Write(text), Write(cdot))

            if vI == 0:
                self.play(Write(doesItConverge))
                self.play(Write(yes), Write(blackSquare))
                self.play(Write(no), Write(whiteSquare))

            self.play(z.animate.center().shift(xshift))
            zn = 0 + 0j
            for step in range(maxIteration):
                znp1 = zn ** 2 + c.get_value()
                dx = (znp1.real - zn.real)
                dy = (znp1.imag - zn.imag)
                line = Line((zn.real - xOff) * RIGHT + zn.imag * UP, (znp1.real - xOff) * RIGHT + znp1.imag * UP, color=BLUE)
                self.play(z.animate.shift(dx * RIGHT + dy * UP), Write(line))
                lineGroup.add(line)
                zn = znp1
                if abs(zn) > 4:
                    break

            color = WHITE
            if vI == 0:
                color = BLUE
                self.play(Unwrite(lineGroup), pixel.animate.set_color(color), Unwrite(text), Unwrite(cdot))
            else:
                self.play(Unwrite(lineGroup), pixel.animate.set_color(color), Unwrite(text))

        circle = Circle(color=RED, radius=2).shift(xshift)
        self.play(Write(circle), z.animate.center().shift(xshift))

        def getLineGroup():
            newLineGroup = VGroup()
            zn = 0 + 0j
            for step in range(maxIteration):
                znp1 = zn ** 2 + c.get_value()
                line = Line((zn.real - xOff) * RIGHT + zn.imag * UP, (znp1.real - xOff) * RIGHT + znp1.imag * UP, color=BLUE)
                newLineGroup.add(line)
                zn = znp1
                if abs(zn) > 4:
                    break
            return newLineGroup

        def getCDot():
            return Dot(color=GREEN).shift(xshift + c.get_value().real * RIGHT + c.get_value().imag * UP).set_z_index(2)

        self.remove(lineGroup)
        lineGroup = always_redraw(getLineGroup)
        self.add(lineGroup)
        self.remove(cdot)
        cdot = always_redraw(getCDot)
        self.add(cdot)

        self.play(c.animate.set_value(5 + 3j))

        pixels = []
        width = 6
        height = 4
        for dx in range(width * rf):
            x = (width / 2 - (1 / (2 * rf))) - (1 / rf) * dx
            for dy in range(height * rf):
                y = (height / 2 - (1 / (2 * rf))) - (1 / rf) * dy

                pixels.append([x, y])

        pixelGroup = VGroup()
        a = 0
        random.seed = 1
        while len(pixels) != 0:
            a += 1
            rate = 1
            if a > 5:
                rate = 0.3
            if a > 10:
                rate = 0.1
            if a > 20:
                rate = 0.03
            pixel = random.choice(pixels)
            pixels.remove(pixel)
            x = pixel[0]
            y = pixel[1]

            self.play(c.animate(run_time=rate).set_value(complex(x, y)))
            pixel = Rectangle(width=1 / rf, height=1 / rf, fill_opacity=0.3, color=BLUE, stroke_opacity=0.3).shift(xshift + y * UP + x * RIGHT)
            if len(getLineGroup().submobjects) < 15:
                pixel.set_color(WHITE)

            self.play(FadeIn(pixel, run_time=rate))
            pixelGroup.add(pixel)

        self.play(Unwrite(cdot), Unwrite(lineGroup), Unwrite(x_lineMob), Unwrite(x_labelMob), Unwrite(y_lineMob), Unwrite(y_labelMob), Unwrite(z))

        for resstep in range(3):
            rf *= 2
            self.remove(grid)
            self.remove(pixelGroup)
            grid = NumberPlane(
                x_length=x_len,
                y_length=y_len,
                background_line_style={
                    "stroke_color": GRAY,
                    "stroke_width": 1,
                    "stroke_opacity": 0.6
                },
                x_range=[-x_len * rf / 2, x_len * rf / 2],
                y_range=[-y_len * rf / 2, y_len * rf / 2]
            ).shift(xshift)
            self.add(grid)

            pixels = []
            width = 6
            height = 4
            for dx in range(width * rf):
                x = (width / 2 - (1 / (2 * rf))) - (1 / rf) * dx
                for dy in range(height * rf):
                    y = (height / 2 - (1 / (2 * rf))) - (1 / rf) * dy
                    pixels.append([x, y])

            pixelGroup = VGroup()
            while len(pixels) != 0:
                pixel = random.choice(pixels)
                pixels.remove(pixel)
                x = pixel[0]
                y = pixel[1]
                c.set_value(complex(x, y))
                pixel = Rectangle(width=1 / rf, height=1 / rf, fill_opacity=0.3, color=BLUE, stroke_opacity=0.3).shift(xshift + y * UP + x * RIGHT)
                if len(getLineGroup().submobjects) < 15:
                    pixel.set_color(WHITE)
                self.add(pixel)
                pixelGroup.add(pixel)

            self.wait()