def load_style(app, file_path):
    try:
        with open(file_path, "r") as f:
            style = f.read()
            app.setStyleSheet(style)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")