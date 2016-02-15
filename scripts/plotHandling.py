import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class PlotHandler:
    def __init__(self):
        self.numFig = 0
        self.currSubPlot = 0

    # to call in addFigure
    def addRandomThemes(self):
        themes = ["darkgrid", "whitegrid", "dark", "white", "ticks"]
        contexts = ["paper", "notebook", "talk", "poster"]
        theme = self.numFig % 5
        context = theme % 4
        sns.set_style(themes[theme])
        sns.set_context(contexts[context])

    def addFigure(self):
        self.numFig += 1
        self.currSubPlot = 0
        plt.figure(self.numFig)

    def addAxes(self, xlabel, ylabel):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def addTitle(self, title):
        plt.title(title, y=1.08)

    def addMainTitle(self, title):
        plt.suptitle(title)

    def resetSubPlot(self):
        self.currSubPlot = 0

    def addSubPlot(self, numSubPlots):
        self.currSubPlot += 1
        plt.subplot(numSubPlots, 1, self.currSubPlot)

    def addCurve(self, x, y, label):
        def convert(x):
            return np.asarray(map(int, x))
        x = convert(x)
        y = convert(y)

        a, b, c, d, e = stats.linregress(convert(x), convert(y))
        a = int(a)
        b = int(b)
        equation = str(a) + " * x + " + str(b)

        sns.regplot(x=convert(x), y=convert(y), label=label + " : " + equation);
        for l in plt.gca().lines:
                l.set_alpha(.3)
                l.set_linewidth(1.0)
        ax = plt.gca()
        ax.set_ylim(bottom=0.)
        ax.set_xlim(left=0.)
        plt.legend(loc="upper left")
        #mng = plt.get_current_fig_manager()
        #mng.resize(*mng.window.maxsize())

    def addHistogram(self, x):
        sns.distplot(x, bins=256, kde=False, rug=False);

    def show(self):
        plt.show()

    def saveFigure(self, filename):
        #plt.savefig(filename, bbox_inches="tight")
        plt.savefig(filename, bbox_inches="tight", dpi=300)

