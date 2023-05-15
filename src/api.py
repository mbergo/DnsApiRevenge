from flask import Flask, jsonify, request
from database import Database
from models import Domain, Record

app = Flask(__name__)
db = Database()  # Initialize the database (can use SQLite or any other database)


@app.route('/domains', methods=['GET'])
def get_domains():
    domains = db.get_domains()
    return jsonify(domains)


@app.route('/domains', methods=['POST'])
def create_domain():
    data = request.get_json()
    domain_name = data.get('domain_name')
    domain = Domain(domain_name)
    db.add_domain(domain)
    return jsonify({'message': 'Domain created successfully'}), 201


@app.route('/domains/<int:domain_id>', methods=['GET'])
def get_domain(domain_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    return jsonify(domain)


@app.route('/domains/<int:domain_id>', methods=['PUT'])
def update_domain(domain_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    data = request.get_json()
    domain.domain_name = data.get('domain_name')
    db.update_domain(domain)
    return jsonify({'message': 'Domain updated successfully'})


@app.route('/domains/<int:domain_id>', methods=['DELETE'])
def delete_domain(domain_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    db.delete_domain(domain)
    return jsonify({'message': 'Domain deleted successfully'})


@app.route('/domains/<int:domain_id>/records', methods=['GET'])
def get_records(domain_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    return jsonify(domain.records)


@app.route('/domains/<int:domain_id>/records', methods=['POST'])
def create_record(domain_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    data = request.get_json()
    record = Record(data.get('name'), data.get('value'))
    domain.add_record(record)
    db.update_domain(domain)
    return jsonify({'message': 'Record created successfully'}), 201


@app.route('/domains/<int:domain_id>/records/<int:record_id>', methods=['PUT'])
def update_record(domain_id, record_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    record = domain.get_record(record_id)
    if record is None:
        return jsonify({'message': 'Record not found'}), 404
    data = request.get_json()
    record.name = data.get('name')
    record.value = data.get('value')
    db.update_domain(domain)
    return jsonify({'message': 'Record updated successfully'})


@app.route('/domains/<int:domain_id>/records/<int:record_id>', methods=['DELETE'])
def delete_record(domain_id, record_id):
    domain = db.get_domain(domain_id)
    if domain is None:
        return jsonify({'message': 'Domain not found'}), 404
    record = domain.get_record(record_id)
    if record is None:
        return jsonify({'message': 'Record not found'}), 404
    domain.delete_record(record)
    db.update_domain(domain)
    return jsonify({'message': 'Record deleted successfully'})


if __name__ == '__main__':
    app.run()

