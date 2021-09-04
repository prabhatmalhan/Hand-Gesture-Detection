from EditJson import EditConfig
import cv2 as cv


def capture(ind=''):
    filePath = './Resources/'+ind
    x = EditConfig(filePath+'/info.json').readConfig()
    a = int(x['count'])
    i = 0
    video = cv.VideoCapture(0)
    mode = False
    sent = 'Press \'z\' when hand is in frame : '+x['name']
    success = False
    while(1):
        try:
            _, frame = video.read()
            frame = cv.flip(frame, 1)
            cropRegion = frame[50:350, 250:550]
            cv.rectangle(frame, (250, 50), (550, 350), (0, 255, 0), 2)
            k = cv.waitKey(5) & 0xFF
            if k == 27:
                break
            if k == 122:
                sent = 'Activated'
                mode = True

            cv.putText(frame, sent, (0, 470), cv.FONT_HERSHEY_COMPLEX_SMALL,
                       1, (0, 0, 255), 2, cv.LINE_8)

            sampleImg = cv.imread(filePath+'/sample.jpg')
            cv.imshow('sample', sampleImg)
            cv. moveWindow('sample', 40, 30)
            cv.imshow('frame', frame)
            cv. moveWindow('frame', 500, 150)
            cv.imshow('cropped', cropRegion)
            cv. moveWindow('cropped', 40, 400)
            if mode:
                cv.imwrite(filePath+'/'+str(a)+'.jpg', cropRegion)
                a += 1
                i += 1
                if(i == 240):
                    x['count'] = str(a)
                    EditConfig(filePath+'/info.json').writeConfig(x)
                    success = True
                    break
        except:
            print("Error Occured")
            break
    cv.destroyAllWindows()
    video.release()
    return success
