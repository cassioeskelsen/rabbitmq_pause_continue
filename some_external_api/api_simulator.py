#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from utils.logger import logger
app = Flask(__name__)

"""
    Imagine that this is a vital service API for your application and in case of a fall your internal queue must be stopped.
    Simulate service interruption by interrupting the execution of this .py
"""


@app.route("/api/whatever/<message>")
def whatever(message):
    logger.info(f"Incoming message: {message}")
    resp = jsonify(my_result=42)
    return resp


@app.route("/api/healthcheck")
def healthcheck():
    resp = jsonify(health=True)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
