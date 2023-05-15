# RNDC API

This is a Python API that provides REST endpoints to interact with RNDC (Remote Name Daemon Control) on BIND servers. It allows you to perform CRUD operations on domains and their records.

## Prerequisites

- Python 3.x
- Flask framework
- BIND server with RNDC configured

## Installation

1. Clone this repository:

```
git clone https://github.com/mbergo/DnsApiRevenge.git
cd rndc-api
```

2. Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Set up the BIND server and configure RNDC. Ensure that you have the necessary permissions and access to the server.

## Configuration

1. Open the `bind_service.py` file and complete the methods inside the `BINDService` class.
2. Implement the necessary commands or methods to communicate with RNDC on your BIND server.
3. Customize the logic based on your specific setup and requirements.

## Usage

1. Start the API server:

```
python api.py
```

2. Use an HTTP client (e.g., cURL, Postman) to interact with the API endpoints.

### API Endpoints

- **GET /domains**: Retrieve a list of all domains.
- **POST /domains**: Create a new domain.
- **GET /domains/{domain_id}**: Retrieve details of a specific domain.
- **PUT /domains/{domain_id}**: Update the details of a specific domain.
- **DELETE /domains/{domain_id}**: Delete a specific domain.
- **GET /domains/{domain_id}/records**: Retrieve a list of records for a specific domain.
- **POST /domains/{domain_id}/records**: Create a new record for a specific domain.
- **PUT /domains/{domain_id}/records/{record_id}**: Update the details of a specific record.
- **DELETE /domains/{domain_id}/records/{record_id}**: Delete a specific record.
