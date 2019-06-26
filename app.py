from src import create_app

app = create_app(templates_path="./src/templates")

if __name__ == "__main__":
    app.run(port="5440")