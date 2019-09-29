from pyautogui import *
from imagesearch import *

precision = 0.7
fail_in_a_row_threshold = 3


def main():
    log('Staring...')
    ranks_gained = 0
    total_failed = 0
    total_failed_in_a_row = 0
    last_failed = 0
    failed = 0
    cnt = 0
    while 1:
        if go_and_long_click_polite('quest-lv-70-button.png'):
            last_failed = failed
            failed = 0

            if last_failed == 0:
                total_failed_in_a_row = 0
            else:
                total_failed_in_a_row = total_failed_in_a_row + 1

            if total_failed_in_a_row >= fail_in_a_row_threshold:
                exit(1)

            cnt = cnt + 1
            log('Iteration [{}], failed [{}], failed in a row [{}], ranks gained [{}]'.format(cnt, total_failed,
                                                                                              total_failed_in_a_row,
                                                                                              ranks_gained))

        go_and_long_click_polite('begin-button.png')
        go_and_long_click_polite('begin-button2.png')
        go_and_long_click_polite('next-button.png')
        if go_and_long_click_polite('confirm-button.png'):
            ranks_gained = ranks_gained + 1

        if exists_image('receive-support.png'):
            go_and_long_click_polite('rank.png')

        if exists_image('give-up.png'):
            go_and_long_click_polite('yes.png')
            failed = 1

        if exists_image('spend-100.png'):
            go_and_long_click_polite('no.png')


def log(message):
    print(str(datetime.datetime.now().isoformat(timespec='seconds')) + ': ' + message)


def exists_image(image):
    return imagesearch(image, precision)[0] != -1


def go_and_long_click_polite(image):
    pos = imagesearch(image, precision)
    if pos[0] == -1:
        return 0
    moveTo(pos[0], pos[1])
    long_click_here()
    return 1


def long_click_here():
    mouseDown()
    time.sleep(0.5)
    mouseUp()


if __name__ == "__main__":
    main()
