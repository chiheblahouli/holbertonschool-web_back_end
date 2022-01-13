#!/usr/bin/env python3
""" flask app """
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def wlcm():
    """ welcome flask """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def registration():
    """ register new user app """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'])
def createsession():
    """ create session """
    email = request.form['email']
    password = request.form['password']
    logging = AUTH.valid_login(email, password)
    sessionId = AUTH.create_session(email)
    if not logging or not sessionId:
        abort(401)
    rwt = make_response(jsonify({"email": email, "message": "logged in"}))
    rwt.set_cookie("session_id", sessionId)
    return rwt


@app.route('/sessions', methods=['DELETE'])
def logout():
    """delete session"""
    session = request.cookies.get("session_id")
    Obj = AUTH.get_user_from_session_id(session)
    if not Obj:
        abort(403)
    else:
        AUTH.destroy_session(Obj.id)
        return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
