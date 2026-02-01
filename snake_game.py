#│-----------------------------------------------------------│
#│  Link: t.me/FrontendVSCode                 │ 
#│  Author: Frontend & LED (𝙰𝚕𝚒𝚊 𝙴𝚝𝚑𝚎𝚛 𖤍) 🌷 │ 
#│  lang: python                              │
#│  [VS-HASH-01] ΞΩ77Λβ99PPHD8A71             │ 
#│  build:3.10.15                             │ 
#│-----------------------------------------------------------│


import curses
import random

SNAKE_CHAR = '■'
FOOD_CHAR = '🍎'
DELAY = 0.15
MAX_APPLES = 100

COLOR_SNAKE = 1
COLOR_FOOD = 2


def _game(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(COLOR_SNAKE, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(COLOR_FOOD, curses.COLOR_RED, curses.COLOR_BLACK)

    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(True)
    win.timeout(int(DELAY * 1000))

    snk_x, snk_y = sw // 4, sh // 2
    snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
    score = 0

    def new_food():
        empty = [
            [y, x]
            for y in range(1, sh - 1)
            for x in range(1, sw - 1)
            if [y, x] not in snake
        ]
        return random.choice(empty) if empty else None

    food = new_food()
    key = curses.KEY_RIGHT

    while True:
        win.clear()
        win.border()
        win.addstr(0, 2, f"Score: {score}/{MAX_APPLES}")

        if food:
            win.addch(food[0], food[1], FOOD_CHAR, curses.color_pair(COLOR_FOOD))

        for y, x in snake:
            win.addch(y, x, SNAKE_CHAR, curses.color_pair(COLOR_SNAKE) | curses.A_BOLD)

        next_key = win.getch()
        if next_key != -1:
            if (next_key == curses.KEY_UP and key != curses.KEY_DOWN) or \
               (next_key == curses.KEY_DOWN and key != curses.KEY_UP) or \
               (next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT) or \
               (next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT):
                key = next_key

        head = snake[0][:]
        if key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1

        if head in snake or head[0] in [0, sh - 1] or head[1] in [0, sw - 1]:
            break

        snake.insert(0, head)

        if head == food:
            score += 1
            if score >= MAX_APPLES:
                break
            food = new_food()
        else:
            snake.pop()

    win.clear()
    msg = f'🌸 {"Победа!" if score >= MAX_APPLES else "Game Over"} Score: {score} 🥰'
    win.addstr(sh // 2, sw // 2 - len(msg) // 2, msg, curses.A_BOLD)
    win.refresh()
    win.getch()


def main():
    curses.wrapper(_game)


if __name__ == "__main__":
    main()