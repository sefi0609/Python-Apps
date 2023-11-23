import os
import cv2
from threading import Thread, Lock
import time
from send_email import send_email


def clean_folder():
    """ Instead of deleting files delete the directory
        and make a new one it's faster
    """
    file_paths = os.listdir('images')

    # wait for the email to be sent
    # or to write images to folder
    time.sleep(1)

    lock.acquire()

    for file in file_paths:
        os.remove(f'images/{file}')

    lock.release()


def write_images():
    global count, status

    lock.acquire()

    for contour in contours:
        # if the change (new object) is a smell one, skip it
        if cv2.contourArea(contour) < 5000:
            continue
        # else draw a rectangle around it
        else:
            status = 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # record images to send
            cv2.imwrite(f'images/{count}.png', frame)
            count += 1

    lock.release()


# activate the default camera of this computer
video = cv2.VideoCapture(0)
time.sleep(1)

frame1 = None
status_list = [0, 0]
count = 1
lock = Lock()

while True:
    status = 0

    # read a new frame
    check, frame = video.read()

    # make the frame easy to process
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gu = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # save the firs frame for reference
    if frame1 is None:
        frame1 = gray_frame_gu

    # get the delta between the first frame and the current frame
    delta_frame = cv2.absdiff(frame1, gray_frame_gu)

    # make the frame easy to process
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # make contours around the new objects in the frame (comparing it to the first one)
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # create images for an object that enter the frame
    write_images()

    # crate a status list to detect when the object left the frame
    # and save only the 2 last ones to save memory space
    status_list.append(status)
    status_list = status_list[-2:]

    # check if the object have left the frame, release thread
    if status_list[0] == 1 and status_list[1] == 0:

        # get the image with the object
        all_images = os.listdir('images')
        mid = int(len(all_images) / 2)
        file_path = f'images/{all_images[mid]}'

        # send it with a thread so the video will continue to run
        Thread(target=send_email, args=(file_path, )).start()

        # release clean folder thread
        Thread(target=clean_folder).start()

    # show thw frame
    cv2.imshow('My Video', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
