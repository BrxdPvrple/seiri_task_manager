from application import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc') # Access via https connection to provide a secure encryption for entering passwords