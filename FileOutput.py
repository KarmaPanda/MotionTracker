from Dependencies import *
from Extensions import videowriter

class FileOutput(object):
    codec = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
    destinationVid = 'Videos/'
    destinationPic = "ScreenShots/"
    facetracker = None
    fileCountVid = 0
    fileCountPic = 0
    filenameVid = 'vid_'
    filenamePic = 'pic_'
    output = None
    record = False

    def __init__(self, facetracker):
        cv2.setUseOptimized(True)
        filesindirp = os.listdir(self.destinationPic)
        self.fileCountPic = 0
        for fileName in filesindirp:
            if fileName.__contains__(self.filenamePic):
                self.fileCountPic += 1

        filesindirv = os.listdir(self.destinationVid)
        self.fileCountVid = 0
        for fileName in filesindirv:
            if fileName.__contains__(self.filenameVid):
                self.fileCountVid += 1

        if self.record:
            self.output = self.setuprecording()

        self.facetracker = facetracker

    def takescreenshot(self, frame):
        ret = cv2.imwrite("{0}{1}{2}.jpg".format(self.destinationPic, self.filenamePic, str(self.fileCountPic)), frame)
        self.fileCountPic += 1
        return ret

    def setuprecording(self, frame=None):
        if frame is None:
            frame = self.facetracker.detectface
        fps = self.facetracker.getaveragefps
        output = videowriter(frame, self.codec, self.destinationVid + self.filenameVid + str(self.fileCountVid), fps)
        return output