from Dependencies import *
from Extensions import resizeframe, getcolor, isclose

class ObjectTracker(object):
    isOccupied = False
    camera = None
    fgbg = cv2.createBackgroundSubtractorMOG2(history=500)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))

    def __init__(self, camera):
        self.camera = camera
        cv2.ocl.setUseOpenCL(False)

    def update(self):

        self.isOccupied = False
        ret, frame = self.camera.read()
        frame = resizeframe(frame)
        h, w, d = frame.shape
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            return None

        # fgmask = cv2.GaussianBlur(frame, (5, 5), 0)
        fgmask = self.fgbg.apply(frame)
        (height, width, depth) = frame.shape
        fgmask = cv2.GaussianBlur(fgmask, (21, 21), 0)
        thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]
        fgmask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel=self.kernel)
        q, contours, q1 = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow("Frame Differnce", fgmask)
        LENGTH = len(contours)
        status = np.zeros((LENGTH, 1))

        for i, cnt1 in enumerate(contours):
            x = i
            if cv2.contourArea(cnt1) > 500:
                if i != LENGTH - 1:
                    for j, cnt2 in enumerate(contours[i + 1:]):
                        if cv2.contourArea(cnt2) > 500:
                            x = x + 1
                            dist = isclose(cnt1, cnt2)
                            if dist == True:
                                val = min(status[i], status[x])
                                status[x] = status[i] = val
                            else:
                                if status[x] == status[i]:
                                    status[x] = i + 1

        if(len(status)  > 1):
            unified = []
            maximum = int(status.max()) + 1
            for i in xrange(maximum):
                pos = np.where(status == i)[0]
                if pos.size != 0:
                    cont = np.vstack(contours[i] for i in pos)
                    hull = cv2.convexHull(cont)
                    unified.append(hull)
            if unified is not None:
                color = getcolor(h*w, cv2.contourArea(unified[0]))
                cv2.drawContours(frame, unified, -1, color, 2)
                self.isOccupied = True

        return frame

    def printstamp(self, frame):
        text = "Occupied" if self.isOccupied else "Unoccupied"
        cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        return frame