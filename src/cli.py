import keyboard
import curses
import main


def input_int(message: str, max_=-1, min_=-1) -> int:
    try:
        if min_ >= 0:
            if max_ > 0:
                message += f' ({min_}-{max_})'
            else:
                message += f' (Minimum: {min_})'
        elif max_ >= 0:
            message += f'(Maximum: {max_})'

        raw = input(message)
        answer = int(raw)

        if max_ != -1 and answer > max_:
            raise IndexError

        if max_ != -1 and answer < min_:
            raise IndexError

        return answer
    except ValueError:
        print('Please enter number.')
        return input_int(message)
    except IndexError:
        print('Number is out of range.')
        return input_int(message)


class CLIMenu:
    message: str
    chooses: list
    is_multiple: bool
    is_done = False
    index = 0
    selected = list()

    win = None

    def __init__(self, message: str, chooses: list, is_multiple: bool):
        self.chooses = chooses
        self.is_multiple = is_multiple
        self.message = message

    def clear(self):
        for _ in self.chooses:
            self.win.clear()

    def draw(self):
        self.win.addstr(self.message + '\n')
        self.win.addstr(('[SPACE - Select | Enter - Next]' if self.is_multiple else '[SPACE - Select]') + '\n')

        for i in range(len(self.chooses)):
            self.win.addstr('> ' if i == self.index else '  ')

            if self.is_multiple:
                self.win.addstr(('x' if i in self.selected else 'o') + ' ')

            self.win.addstr(self.chooses[i]+'\n')
        self.win.refresh()

    def update(self):
        self.clear()
        self.draw()

    def move_up(self):
        if self.index > 0:
            self.index = self.index - 1
            self.update()

    def move_down(self):
        if self.index < len(self.chooses) - 1:
            self.index = self.index + 1
            self.update()

    def select(self):
        if self.is_multiple:
            if self.index in self.selected:
                self.selected.remove(self.index)
            else:
                self.selected.append(self.index)
            self.update()
        else:
            self.selected.append(self.index)
            self.is_done = True

    def done(self):
        if self.is_multiple:
            self.is_done = True

    def open(self):
        self.win = curses.initscr()
        curses.noecho()
        curses.cbreak()

        keyboard.add_hotkey('up', self.move_up)
        keyboard.add_hotkey('down', self.move_down)
        keyboard.add_hotkey('space', self.select)
        keyboard.add_hotkey('enter', self.done)

        self.draw()
        while not self.is_done:
            pass

        keyboard.remove_all_hotkeys()

        curses.endwin()
        curses.echo()
        curses.nocbreak()

        if self.is_multiple:
            output = list()
            for i in self.selected:
                output.append(self.chooses[i])
            return output
        else:
            return self.chooses[self.selected[0]]
