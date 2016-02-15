import argparse
import bitmap
import plotHandling

def parse_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("bitmap_file", help="File to be parsed")
    args = parser.parse_args()
    return args


def swapColors():
    args = parse_config()
    bitmap_file = args.bitmap_file
    with open(bitmap_file, 'rb') as fh:
        bm = bitmap.Bitmap()
        bm.parse_file_header(fh)
        bm.parse_picture_header(fh)
    bm.data.swapColors()
    with open("../swap.bmp", 'wb') as fh:
        bm.write(fh)

def getBM(bitmap_file):
    with open(bitmap_file, 'rb') as fh:
        bm = bitmap.Bitmap()
        bm.parse_file_header(fh)
        bm.parse_picture_header(fh)
        bm.parse_picture_data(fh)
    return bm

def writeBM(bm):
    with open("../sizes.bmp", 'wb') as fh:
        bm.write(fh)

def printHeaders(bm):
    bm.print_header()
    bm.print_picture_header()

def printDistributions(bm):
    plotHandler = plotHandling.PlotHandler()
    plotHandler.addFigure()
    plotHandler.addHistogram(bm.data.red)
    plotHandler.saveFigure("distRed.png")
    plotHandler.addFigure()
    plotHandler.addHistogram(bm.data.green)
    plotHandler.saveFigure("distGreen.png")
    plotHandler.addFigure()
    plotHandler.addHistogram(bm.data.blue)
    plotHandler.saveFigure("distBlue.png")


def main():
    args = parse_config()
    bitmap_file = args.bitmap_file
    bm = getBM(bitmap_file)
    bm.picture.width *= 2
    bm.picture.height *= 2
    printHeaders(bm)
    writeBM(bm)






if __name__ == "__main__":
    main()

