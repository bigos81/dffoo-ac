from pyautogui import *
from imagesearch import *

def_wait_time = 2


def main():
    cnt = 0
    while 1:

        cnt = cnt + 1
        log("here we go again: " + str(cnt))
        log('looking for q70 button')
        go_and_long_click('quest-lv-70-button.png')
        log('looking for begin button')
        go_and_long_click('begin-button.png')
        time.sleep(get_wait_time())
        log('picking support')
        long_click_here()
        time.sleep(get_wait_time())
        log('clicking begin with support')
        long_click_here()
        log('waiting for battle to end')
        wait_and_long_click('next-button.png')
        time.sleep(get_wait_time() * 2)
        log('clicking ok after exp added')
        long_click_here()  # exp is added

        log('search loop for end of cycle')
        while 1:
            log('searching for lv 70 button')
            pos = imagesearch('quest-lv-70-button.png')
            if pos[0] != -1:
                log('  FOUND, ending cycle')
                break

            pos = imagesearch('yes.png')
            if pos[0] != -1:
                log('!!!!!LOST DETECTED!!!!')
                pos_fail = imagesearch('give-up.pgn')
                if pos_fail[0] != -1:
                    go_and_long_click('yes.png')
                    continue
                break

            log('searching for next button to click')
            go_and_long_click_polite('next-button.png')
            log('searching for confirm button')
            go_and_long_click_polite('confirm-button.png')
            log('next loop cycle')


def log(message):
    print(str(datetime.datetime.now()) + ': ' + message)


def get_wait_time():
    return def_wait_time + random.randint(2, 5) * 0.1


def wait_and_long_click(image):
    pos = imagesearch_loop(image, 5, precision=0.5)
    moveTo(pos[0], pos[1])
    long_click_here()


def go_and_long_click(image):
    pos = imagesearch_numLoop(image, 0.5, 10)
    if pos[0] == -1:
        exit(1)
    moveTo(pos[0], pos[1])
    long_click_here()


def go_and_long_click_polite(image):
    pos = imagesearch_numLoop(image, 0.5, 10)
    if pos[0] == -1:
        return
    moveTo(pos[0], pos[1])
    long_click_here()


def long_click_here():
    mouseDown()
    time.sleep(0.5)
    mouseUp()


if __name__ == "__main__":
    main()
