from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsLineItem, QGraphicsItem, QWidget, QGraphicsView, QGridLayout
from PySide6.QtCore import Qt, QRectF, QEvent
from PySide6.QtGui import QPen
from IDE import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Variáveis para a ferramenta de desenho
        self.last_point = None
        self.pen = QPen(Qt.black, 5)
        self.eraser_radius = 30
        self.active_tool = None, False

        # Configuração inicial
        self.setup_scene()
        self.setup_connections()

    def setup_scene(self):
        """Configura a cena e o QGraphicsView."""
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def setup_connections(self):
        """Conecta os sinais aos métodos."""
        self.ui.actionNew_2.triggered.connect(lambda : self.newTab((self.ui.tabWidget.count() + 1)))
        self.ui.actionCaneta.toggled.connect(lambda checked: self.activate_tool("caneta", checked))
        self.ui.actionBorracha.toggled.connect(lambda checked: self.activate_tool("borracha", checked))
        self.ui.tabWidget.currentChanged.connect(self.update_active_scene)

    def update_active_scene(self):
        """Atualiza a cena ativa conforme a aba selecionada."""
        current_widget = self.ui.tabWidget.currentWidget()
        if current_widget:
            self.scene = current_widget.findChild(QGraphicsView).scene()

    def newTab(self, num):
        new = QWidget()
        new.setObjectName(f"Page_{num}")
        
        gridLayout = QGridLayout(new)
        gridLayout.setObjectName(f"gridLayout{num}")
        
        scene = QGraphicsScene()

        graphicsView = QGraphicsView(new)
        graphicsView.setObjectName(f"graphicsView{num}")
        graphicsView.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        graphicsView.setScene(scene)
        
        gridLayout.addWidget(graphicsView, 0, 0, 1, 1)
        
        self.ui.tabWidget.addTab(new, f"Page_{num}")

    def activate_tool(self, tool_name, checked):
        """Ativa uma ferramenta específica."""
        self.active_tool = tool_name, checked
        self.ui.graphicsView.setMouseTracking(True)
        self.ui.graphicsView.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.ui.graphicsView.viewport():
            if self.active_tool == ("caneta", True):
                self.handle_pen_tool(event)
            elif self.active_tool == ("borracha", True):
                self.handle_eraser_tool(event)
        return super().eventFilter(source, event)

    def handle_pen_tool(self, event):
        """Lida com eventos da ferramenta caneta."""
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.last_point = self.get_scene_position(event)
        elif event.type() == QEvent.MouseMove and self.last_point:
            current_point = self.get_scene_position(event)
            line = QGraphicsLineItem(self.last_point.x(), self.last_point.y(), current_point.x(), current_point.y())
            line.setPen(self.pen)
            self.scene.addItem(line)
            self.last_point = current_point
        elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            self.last_point = None

    def handle_eraser_tool(self, event):
        """Lida com eventos da ferramenta borracha."""
        if event.type() == QEvent.MouseMove and event.buttons() & Qt.LeftButton:
            current_pos = self.get_scene_position(event)
            self.erase_items_at(current_pos)

    def get_scene_position(self, event):
        """Obtém a posição do evento na cena."""
        return self.ui.graphicsView.mapToScene(event.pos())

    def erase_items_at(self, pos):
        """Apaga os itens gráficos dentro de uma área ao redor da posição."""
        erase_area = QRectF(pos.x() - self.eraser_radius, pos.y() - self.eraser_radius,
                            2 * self.eraser_radius, 2 * self.eraser_radius)
        for item in self.scene.items():
            if item.sceneBoundingRect().intersects(erase_area):
                self.scene.removeItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
