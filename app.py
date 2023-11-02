from flask import Flask, jsonify, request

from model.db_handler import match_exact, match_like

app = Flask(__name__)

ERROR_RESPONSE = {"status": "error"}
SUCCESS_RESPONSE = {"status": "success"}
PARTIAL_RESPONSE = {"status": "partial"}
WORD_NOT_FOUND_RESPONSE = {"data": "word not found"}


@app.get("/")
def index():

    response = {"usage": "/dict?=<word>"}

    return jsonify(response)

@app.get("/dict")
def dictionary():

    words = request.args.getlist("word")

    if not words:
        return ERROR_RESPONSE | {"word": words} | WORD_NOT_FOUND_RESPONSE

    responses = {"words": []}
    for word in words:
        definitions = match_exact(word)

        if definitions:
            responses["words"].append(SUCCESS_RESPONSE | {"word": word} | {"data": definitions})
            continue

        definitions = match_like(word)

        if definitions:
            responses["words"].append(PARTIAL_RESPONSE | {"word": word} | {"data": definitions})
            continue
        else:
            responses["words"].append(ERROR_RESPONSE | {"word": word} | WORD_NOT_FOUND_RESPONSE)
            continue

    return responses
