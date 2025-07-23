# Code2Exe

**Code2Exe** is a user-friendly Python GUI application that lets you convert Python `.py` files into standalone Windows `.exe` executables using [PyInstaller](https://www.pyinstaller.org/). The application is built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter) and supports real-time logging, multiple build options, and a clean interface.

---

## 🚀 Features

- ✅ Convert `.py` scripts to `.exe` with a click
- ✅ Supports PyInstaller options:
  - `--onefile`: Single bundled executable
  - `--console`: Show terminal output
  - `--windowed`: GUI apps without console
- ✅ Live build logs in GUI
- ✅ Output stored in a custom folder
- ✅ Easy browsing for input/output files



## 📂 Project Structure

```
Code2Exe/
├──converter.py                 # GUI application code
├── assets/                 # Example Python files to convert
│   └── example_script.py
├── output/                 # Output EXE folder (ignored in version control)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HassanNetSec/ExeBuilder.git
cd ExeBuilder
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python src/app.py
```

---

## 🧪 Example Script

Use the included `assets/example_script.py` or browse any other `.py` file you want to convert via the GUI.

---

## 📦 Dependencies

- `customtkinter`
- `pyinstaller`
- `tkinter` (standard in Python)

> If you encounter missing modules, install them using:
> ```bash
> pip install customtkinter pyinstaller
> ```

---

## 🧰 Advanced Users

You can edit or extend `src/app.py` to:
- Support icon files (`--icon`)
- Modify default themes/colors
- Add output log export

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Contributions, suggestions, and pull requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## 📬 Contact

Have questions or feedback?  
Feel free to open an [issue](https://github.com/HassanNetSec/Code2Exe/issues).

---

**Built with Python ♥ by [@HassanNetSec](https://github.com/HassanNetSec)**
