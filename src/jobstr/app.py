from textual.app import ComposeResult
from textual.app import App as TextualApp
from textual.widgets import Footer, Header


class App(TextualApp):
    """
    Job tracking application in the terminal.
    """

    BINDINGS = [("ctrl+q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


def init():
    app = App()
    app.run()


if __name__ == "__main__":
    init()
