from Dependencies import *

imgSizeX = 0.25
imgSizeY = 0.25


def resizeframe(frame):
    return cv2.resize(frame, (0, 0), fx=imgSizeX, fy=imgSizeY)


def getdistance(frameh, framew, recth, rectw):
    ratio1 = float(recth)/float(frameh)
    ratio2 = float(rectw)/float(framew)
    print ratio1, ratio2
    if ratio1 < 0.2 and ratio1 < 0.2:
        return 1
    elif 0.6 > ratio1 > 0.2 and ratio2 < 0.6 and ratio2 > 0.2:
        return 2
    else:
        return 3


def videowriter(frame, codec, dest, fps):
    height, width, depth = frame.shape
    return cv2.VideoWriter(dest, codec, fps, (width, height), 1)


def clear(event, x, y, flags, pathFrame):
    global firstFrame, gray
    if event is cv2.EVENT_LBUTTONDOWN:
        pathFrame[:] = (255, 255, 255)
        firstFrame = gray


def isclose(cnt1,cnt2):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in xrange(row1):
        for j in xrange(row2):
            dist = np.linalg.norm(cnt1[i]- cnt2[j])
            if abs(dist) < 50 :
                return True
            elif i==row1-1 and j==row2-1:
                return False

