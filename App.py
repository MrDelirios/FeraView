from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsLineItem, QGraphicsItem, QWidget, QGraphicsView, QGridLayout, QMenu, QGraphicsPixmapItem, QFileDialog
from PySide6.QtCore import Qt, QRectF, QEvent
from PySide6.QtGui import QPen, QAction, QPixmap
from IDE import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #variaveis de controle de widget
        self.current_widget = self.ui.tabWidget.currentWidget()
        
        # Variáveis para a ferramenta de desenho
        self.last_point = None
        self.pen = QPen(Qt.black, 5)
        self.eraser_radius = 30
        self.active_tool = None, False

        # Configuração inicial
        self.setup_connections()

    def setup_scene(self, widget):
        """Configura a cena e o QGraphicsView."""
        print(widget.objectName())
        if widget:
            graphicsView = widget.findChild(QGraphicsView)
            self.scene = QGraphicsScene()
            graphicsView.setScene(self.scene)
            graphicsView.setMouseTracking(True)
            graphicsView.viewport().installEventFilter(self)

    def setup_connections(self):
        """Conecta os sinais aos métodos."""
        self.ui.actionNew_2.triggered.connect(lambda : self.newTab((self.ui.tabWidget.count() + 1)))
        self.ui.actionCaneta.toggled.connect(lambda checked: self.activate_tool("caneta", checked))
        self.ui.actionBorracha.toggled.connect(lambda checked: self.activate_tool("borracha", checked))
        self.ui.actionInsert.triggered.connect(self.insert_image)

    def insert_image(self):
        """Permite ao usuário inserir uma imagem na cena ativa."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Inserir Imagem", "", "Imagens (*.png *.jpg *.jpeg *.bmp);;Todos os Arquivos (*)")

        if file_path:
            pixmap = QPixmap(file_path)
            if pixmap.isNull():
                print("Falha ao carregar a imagem.")
                return

            pixmap_item = QGraphicsPixmapItem(pixmap)
            pixmap_item.setFlag(QGraphicsItem.ItemIsMovable)
            pixmap_item.setFlag(QGraphicsItem.ItemIsSelectable)

            if self.ui.tabWidget.count() == 0:
                self.newTab(1)
            self.scene.addItem(pixmap_item)


    def newTab(self, num):
        new = QWidget()
        new.setObjectName(f"Page_{num}")
        
        gridLayout = QGridLayout(new)
        gridLayout.setObjectName(f"gridLayout{num}")

        graphicsView = QGraphicsView(new)
        graphicsView.setObjectName(f"graphicsView{num}")
        graphicsView.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        
        self.setup_scene(new)
        
        gridLayout.addWidget(graphicsView, 0, 0, 1, 1)
        
        self.ui.tabWidget.addTab(new, f"Page_{num}")

    def activate_tool(self, tool_name, checked):
        """Ativa uma ferramenta específica."""
        self.active_tool = tool_name, checked
        current_widget = self.ui.tabWidget.currentWidget()

        if current_widget:
            graphicsView = current_widget.findChild(QGraphicsView)
            self.scene = graphicsView.scene()

    def add_circle(self):
        """Adiciona um círculo à cena."""
        self.scene.addEllipse(50, 50, 100, 100)

    def add_square(self):
        """Adiciona um quadrado à cena."""
        self.scene.addRect(200, 50, 100, 100)

    def clear_scene(self):
        """Limpa todos os itens da cena."""
        self.scene.clear()

    def eventFilter(self, source, event):
        """Filtro de eventos para ferramentas de desenho."""
        graphics_view = self.ui.tabWidget.currentWidget().findChild(QGraphicsView)
        if source is graphics_view.viewport():
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:
                self.show_context_menu_Graph(event.globalPos())
            elif self.active_tool == ("caneta", True):
                self.handle_pen_tool(event)
            elif self.active_tool == ("borracha", True):
                self.handle_eraser_tool(event)
        return super().eventFilter(source, event)

    def show_context_menu_Graph(self, global_pos):
        """Exibe o menu de contexto na posição especificada."""
        context_menu = QMenu(self)
        
        # Adiciona ações ao menu
        action_add_circle = QAction("Adicionar Círculo", self)
        action_add_square = QAction("Adicionar Quadrado", self)
        action_clear_scene = QAction("Limpar Cena", self)

        # Conecta as ações aos métodos
        action_add_circle.triggered.connect(self.add_circle)
        action_add_square.triggered.connect(self.add_square)
        action_clear_scene.triggered.connect(self.clear_scene)

        # Adiciona as ações ao menu
        context_menu.addAction(action_add_circle)
        context_menu.addAction(action_add_square)
        context_menu.addSeparator()  # Linha separadora
        context_menu.addAction(action_clear_scene)

        # Exibe o menu na posição do clique
        context_menu.exec(global_pos)

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
        return self.ui.tabWidget.currentWidget().findChild(QGraphicsView).mapToScene(event.pos())

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
