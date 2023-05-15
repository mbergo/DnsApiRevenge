import subprocess


class BINDService:
    def __init__(self):
        self.rndc_path = '/path/to/rndc'

    def execute_rndc_command(self, command):
        cmd = [self.rndc_path, '-c', '/path/to/named.conf'] + command
        subprocess.run(cmd)

    def create_domain(self, domain_name):
        self.execute_rndc_command(
            ['addzone', domain_name, '{ type master; file "/path/to/zone.db"; };'])

    def update_domain(self, domain_name):
        self.execute_rndc_command(['modzone', domain_name, 'refresh'])

    def delete_domain(self, domain_name):
        self.execute_rndc_command(['delzone', domain_name])

    def create_record(self, domain_name, record_name, record_value):
        self.execute_rndc_command(
            ['add', domain_name, 'IN', 'A', record_value])

    def update_record(self, domain_name, record_name, record_value):
        self.execute_rndc_command(
            ['mod', domain_name, 'IN', 'A', record_value])

    def delete_record(self, domain_name, record_name):
        self.execute_rndc_command(['del', domain_name, 'IN', 'A', record_name])
