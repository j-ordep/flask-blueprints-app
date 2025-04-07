from flask import Blueprint, render_template
from database.client import CLIENTS


client_route = Blueprint('client', __name__)

@client_route.route('/', methods=['GET'])
def list_clients():
    return render_template('list_clients.html', clients=CLIENTS)


@client_route.route('/', methods=['POST'])
def add_client():
    pass


@client_route.route('/new', methods=['GET'])
def form_client():
    return render_template('form_client.html')


@client_route.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    return render_template('get_client.html')


@client_route.route('/<int:client_id>/edit', methods=['GET'])
def form_edit_client():
    return render_template('form_edit_client.html')
    

@client_route.route('/<client_id>/update', methods=['PUT'])
def update_client(client_id):
    pass


@client_route.route('/<client_id>/update', methods=['DELETE'])
def delete_client(client_id):
    pass