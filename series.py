from manim import *
import math
import random


class Series(Scene):
    def construct(self):
        title = Text("Folgen")
        self.play(Write(title))

        series = VGroup(*[Text(str(n)) for n in [7, 5, 1, 9, 10, 4, 1, 54, 1]]).arrange(RIGHT)
        self.play(FadeOut(title, run_time=.5), Write(series))

        brace = Brace(series.submobjects[0], color=YELLOW)
        text = Text("0. Glied", color=YELLOW).next_to(brace, DOWN)
        self.play(Write(VGroup(brace, text)))
        for i in range(len(series.submobjects) - 1):
            newbrace = Brace(series.submobjects[i + 1], color=YELLOW)
            self.play(Transform(brace, newbrace), Transform(text, Text(str(i + 1) + ". Glied", color=YELLOW).next_to(newbrace, DOWN)))

        finiteSeries = Text("endliche Folge").next_to(series, UP)
        self.play(Write(finiteSeries))

        seriesContinuation = VGroup(*[Text(str(random.randint(-10, 120))) for n in range(30)]).arrange(RIGHT).next_to(series, RIGHT)
        infiniteSereis = Text("unendliche Folge").move_to(finiteSeries)

        self.play(Write(seriesContinuation))
        self.play(TransformMatchingShapes(finiteSeries, infiniteSereis))

        self.play(Unwrite(brace), Unwrite(VGroup(series, seriesContinuation)), Unwrite(text), Unwrite(infiniteSereis))

        index = 0

        elementlabels = []
        lengthlabel = MathTex()
        brace = Brace(lengthlabel)

        def flockenanimation(startline):
            nonlocal index
            nonlocal lengthlabel
            nonlocal brace
            nonlocal elementlabels
            if index == 0:
                brace = Brace(startline)
                lengthlabel = MathTex(r'L_0').next_to(brace, DOWN)
                self.play(Write(VGroup(brace, lengthlabel)))
            else:
                text = MathTex(r'L_{' + str(index) + r'} = L_{' + str(index - 1) + r'} * {{ \frac{4}{3} }}').scale(.7).align_on_border(UP + LEFT).shift((index - 1) * DOWN)
                text.submobjects[1].color = RED
                elementlabels.append(text)
                self.play(Write(text))

            index += 1

        def flocke(line, depth, animation=False, removeAtEnd=True):
            global lines
            lines = [line]
            currentdepth = depth

            animationBorder = 3

            totalGroup = VGroup(Line(start=line[0][0] * RIGHT + line[0][1] * UP, end=line[1][0] * RIGHT + line[1][1] * UP))
            startline = totalGroup.submobjects[0]

            iterationLabel = Text("Iteration 1").shift(2 * UP)

            self.play(Write(iterationLabel))

            while currentdepth >= 0:
                animationIndex = depth - currentdepth
                newlines = []
                lineIndex = 0

                newTotalGroup = VGroup()

                if animation:
                    flockenanimation(startline)

                self.play(Transform(iterationLabel, Text("Iteration " + str(animationIndex + 1)).shift(2 * UP)))

                for line in lines:
                    print(animationIndex)
                    print("lineindex: " + str(lines.index(line)))
                    dy = line[1][1] - line[0][1]
                    dx = line[1][0] - line[0][0]
                    distance = math.sqrt(pow(dx, 2) + pow(dy, 2))
                    angle = math.asin(dy / distance)

                    if dy < 0 < dx:
                        angle = 2 * PI + angle
                    elif dx < 0 or dy < 0:
                        angle = PI - angle

                    segmentdist = distance / 3

                    p0 = line[0]
                    p1 = [line[0][0] + math.cos(angle) * segmentdist, line[0][1] + math.sin(angle) * segmentdist]
                    p2 = [p1[0] + math.cos(angle + (2 * PI * (60 / 360))) * segmentdist, p1[1] + math.sin(angle + (2 * PI * (60 / 360))) * segmentdist]
                    p3 = [line[1][0] - math.cos(angle) * segmentdist, line[1][1] - math.sin(angle) * segmentdist]
                    p4 = line[1]

                    stroke_width = 6 / (animationIndex + 1)
                    oldgroup = VGroup(
                        Line(start=p0[0] * RIGHT + p0[1] * UP, end=p1[0] * RIGHT + p1[1] * UP, stroke_width=stroke_width),
                        Line(start=p1[0] * RIGHT + p1[1] * UP, end=p3[0] * RIGHT + p3[1] * UP, stroke_width=stroke_width),
                        Line(start=p3[0] * RIGHT + p3[1] * UP, end=p4[0] * RIGHT + p4[1] * UP, stroke_width=stroke_width)
                    )
                    if currentdepth == depth:
                        self.play(Write(oldgroup))
                    else:
                        self.add(oldgroup)

                    line1 = Line(start=p1[0] * RIGHT + p1[1] * UP, end=p2[0] * RIGHT + p2[1] * UP, stroke_width=stroke_width)
                    line2 = Line(start=p2[0] * RIGHT + p2[1] * UP, end=p3[0] * RIGHT + p3[1] * UP, color=RED, stroke_width=stroke_width)

                    newTotalGroup.add(oldgroup.submobjects[0])
                    newTotalGroup.add(line1)
                    newTotalGroup.add(line2)
                    newTotalGroup.add(oldgroup.submobjects[2])

                    self.remove(totalGroup.submobjects[lineIndex])

                    animationNenner = pow(animationIndex + 1, 2)

                    if depth - currentdepth < animationBorder:
                        self.play(ReplacementTransform(oldgroup.submobjects[1], line1, run_time=1 / animationNenner))
                        self.play(Write(line2, run_time=1 / animationNenner))

                    if depth != 0:
                        newlines.append([p0, p1])
                        newlines.append([p1, p2])
                        newlines.append([p2, p3])
                        newlines.append([p3, p4])
                    self.remove(oldgroup)

                    lineIndex += 1

                if depth - currentdepth >= animationBorder:
                    self.add(newTotalGroup)

                totalGroup = newTotalGroup
                if animationIndex == depth:
                    totalGroup.add(iterationLabel)
                    return VGroup(*totalGroup)

                lines = newlines

                currentdepth -= 1

        print("flocke1 to begin")
        self.play(Unwrite(flocke([[-6, -2], [6, -2]], 3)))
        print("flocke1 done")
        flocke = flocke([[-6, -2], [6, -2]], 4, True)
        print("flocke2 done")

        recursiveSeries = MathTex(r'L_n = L_{n-1} * \frac{4}{3}').align_on_border(RIGHT + UP)
        recursiveLabel = Text("Rekursive Schreibweise").scale(.5).next_to(recursiveSeries, DOWN).align_on_border(RIGHT)
        self.play(Write(recursiveSeries))
        self.play(Write(recursiveLabel))

        newlabels = []
        for labelI in range(len(elementlabels)):
            newlabel = MathTex(r'=L_0 * \left(\frac{4}{3}\right)^' + str(labelI + 1)).scale(.7).next_to(elementlabels[labelI], RIGHT)
            self.play(Write(newlabel))
            newlabels.append(newlabel)

        explicitSeries = MathTex(r'L_n = L_0 * \left(\frac{4}{3}\right)^n').next_to(recursiveSeries, DOWN).shift(1.1 * DOWN)
        explicitLabel = Text("Explizite Schreibweise").scale(.5).next_to(explicitSeries, DOWN).align_on_border(RIGHT)
        self.play(Write(explicitSeries))
        self.play(Write(explicitLabel))
        print("unwrite")
        self.play(Unwrite(VGroup(flocke, brace, lengthlabel, recursiveSeries, recursiveLabel, explicitSeries, explicitLabel, VGroup(*newlabels), VGroup(*elementlabels))))
