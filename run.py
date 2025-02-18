if __name__ == "__main__":
    from src.main.server import app

    app.run(host="0.0.0.0", port=3000, debug=True)
