import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QGroupBox, QFormLayout, QSpacerItem, QSizePolicy

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 600, 700)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")

        # Mengatur layout utama
        main_layout = QVBoxLayout()

        # Membuat layout bagian identitas
        identitas_group = QGroupBox("Identitas")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama  : Ida Ayu Dewi Purnama Anjani"))
        identitas_layout.addWidget(QLabel("NIM   : F1D022050"))
        identitas_layout.addWidget(QLabel("Kelas : D"))
        identitas_group.setLayout(identitas_layout)
        main_layout.addWidget(identitas_group)

        # Bagian navigasi
        navigation_group = QGroupBox("Navigasi")
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(QPushButton("Home"))
        navigation_layout.addWidget(QPushButton("About"))
        navigation_layout.addWidget(QPushButton("Contact"))
        navigation_group.setLayout(navigation_layout)
        main_layout.addWidget(navigation_group)

        # Bagian User Registration
        registration_group = QGroupBox("User Registration")
        registration_layout = QFormLayout()

        # Full Name
        registration_layout.addRow(QLabel("Full Name:"), QLineEdit())

        # Email
        registration_layout.addRow(QLabel("Email:"), QLineEdit())

        # Phone
        registration_layout.addRow(QLabel("Phone:"), QLineEdit())

        # Gender
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))
        registration_layout.addRow(QLabel("Gender:"), gender_layout)

        # Country
        country_combo = QComboBox()
        country_combo.addItems(["Select Country", "Indonesia", "Thailand", "Singapore"])
        registration_layout.addRow(QLabel("Country:"), country_combo)

        registration_group.setLayout(registration_layout)
        main_layout.addWidget(registration_group)

        # Bagian Actions
        actions_group = QGroupBox("Actions")
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton("Submit"))
        actions_layout.addWidget(QPushButton("Cancel"))
        actions_group.setLayout(actions_layout)
        main_layout.addWidget(actions_group)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())