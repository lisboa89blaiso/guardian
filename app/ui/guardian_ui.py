from app.ui.main_window import MainWindow
from app.ui.panel_window import PanelWindow
from app.ui.tray_controller import TrayController
from app.ui.window_manager import WindowManager
from app.ui.window_mode import WindowMode
from app.controllers.status_controller import StatusController
from app.controllers.session_controller import SessionController
from app.controllers.action_controller import ActionController


class GuardianUI:

    def __init__(self, webcam, mode=WindowMode.DEVELOPMENT):

        self.mode = mode

        self.status = StatusController()

        self.session = SessionController()

        self.actions = ActionController(
            self.status,
            self.session
        )

        self.windows = WindowManager()

        #
        # Main Window
        #

        main = MainWindow(webcam, self.actions)

        self.windows.register(
            "main",
            main
        )

        #
        # Professional Panel
        #

        panel = PanelWindow(
            main.root,
            webcam,
            self.actions
        )
        
        self.status.bind_panel(panel)

        self.windows.register(
            "panel",
            panel
        )

        #
        # Tray
        #

        self.tray = TrayController(main)

    def bind_guardian(self, guardian):

        self.actions.bind_guardian(guardian)

        self.windows.get("main").bind_guardian(
            guardian
        )

    def update_preview(self, path):

        self.windows.get("main").update_preview(path)

    def run(self):

        self.tray.start()
        

        #
        # Modo de inicialização
        #

        if self.mode == WindowMode.DEVELOPMENT:

            self.windows.get("main").root.deiconify()

        elif self.mode == WindowMode.PROFESSIONAL:

            self.windows.get("main").root.withdraw()

            self.windows.get("panel").show()

        elif self.mode == WindowMode.HEADLESS:

            self.windows.get("main").root.withdraw()

        try:

            self.windows.get("main").root.mainloop()

        finally:

            self.tray.stop()

    @property
    def root(self):

        return self.windows.get("main").root

    @property
    def sidebar(self):

        return self.windows.get("main").sidebar

    @property
    def status_panel(self):

        return self.windows.get("main").status_panel

    @property
    def panel(self):

        return self.windows.get("panel")


    def toggle_panel(self):

        panel = self.panel

        try:

            visible = panel.winfo_viewable()

        except Exception:

            visible = False

        if not visible:

            panel.show()
            return

        #
        # Se estiver minimizado
        #

        if panel.state() == "iconic":

            panel.deiconify()

            panel.lift()

            panel.focus_force()

            return

        #
        # Se já estiver aberto e ativo
        #

        if panel.focus_displayof() is not None:

            panel.hide()

            return

        #
        # Apenas trazer para frente
        #

        panel.lift()

        panel.focus_force()

    def toggle_main_window(self):

        main = self.windows.get("main").root

        if main.state() == "withdrawn":

            main.deiconify()
            main.lift()
            main.focus_force()

        else:

            main.withdraw()