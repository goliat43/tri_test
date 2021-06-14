from flask import Blueprint, request, jsonify, make_response
from werkzeug.exceptions import abort
from datetime import datetime as dt
from tri_test.db import db, Message
from distutils.util import strtobool

bp = Blueprint('message', __name__, url_prefix='/message')


@bp.route('/', methods=('GET', 'POST', 'DELETE'))
def message_query():
    if request.method == 'POST':
        if not request.is_json:
            return 'Invalid input', 400

        req = request.get_json()
        msg = Message(dt.now(), req['sender'], req['receiver'], req['content'])
        db.session.add(msg)
        db.session.commit()

        return make_response(jsonify(msg), 201)

    elif request.method == 'GET':
        if not request.args or not request.args['from_index'] or not request.args['to_index']:
            abort(400)

        get_all_messages = bool(strtobool(request.args.get('include_read_messages', 'False')))

        res = Message.query.filter(((Message.id >= request.args['from_index']) &
                                   (Message.id <= request.args['to_index'])) &
                                   (get_all_messages or (Message.is_read == db.false())))\
                           .all()

        return make_response(jsonify(res), 200)

    elif request.method == 'DELETE':
        if request.args and request.args['from_index'] and request.args['to_index']:
            Message.query.filter((Message.id >= request.args['from_index']) &
                                 (Message.id <= request.args['to_index']))\
                         .delete(synchronize_session=False)
            db.session.commit()
            return '', 204

        abort(400)


def get_msg_with_fail(msg_id):
    msg = Message.query.filter_by(id=msg_id).one_or_none()

    if msg is None:
        abort(404, f"Message id {msg_id} doesn't exist.")

    return msg


@bp.route('/<int:id>/read', methods=['POST'])
def message_set_read(id):
    msg = get_msg_with_fail(id)
    msg.is_read = True

    db.session.add(msg)
    db.session.commit()

    return '', 204


@bp.route('/<int:id>', methods=('GET', 'DELETE'))
def message(id):
    msg = get_msg_with_fail(id)

    if request.method == 'DELETE':
        db.session.delete(msg)
        db.session.commit()

        return '', 204

    return make_response(jsonify(msg), 200)

