from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DataTable
import requests
from models.session import Session


class ManageplayTUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield DataTable()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
        
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Name","Description")
        
        sessions = Session.all()

        for session in sessions:
            table.add_row(session.name, session.description)

if __name__ == "__main__":
    app = ManageplayTUI()
    app.run()
    
