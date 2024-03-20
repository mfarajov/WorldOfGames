from flask import Flask
from Utils import SCORES_FILE_NAME
from MainGame import main


app = Flask(__name__)


@app.route("/")
def score_server():

    try:
        with open(SCORES_FILE_NAME, 'r') as score_file:
            score = score_file.read()
    except Exception as e:
        return f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1><div id="score" style="color:red">Error: {e}</div></h1>
                    </body>
                </html>
                """

    return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{score}</div></h1>
                </body>
            </html>
            """


if __name__ == "__main__":
    main()
    app.run(debug=False, host="0.0.0.0", port=8777)


