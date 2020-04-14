import os

from broker.broker_settings import BrokerSettings


class RabbitSettings(BrokerSettings):
    def __init__(self, host=None, user=None, password=None, port=None):
        if host is None:
            self.host = os.environ.get("RBMQ_HOST")
        if user is None:
            self.user = os.environ.get("RBMQ_USER")
        if password is None:
            self.password = os.environ.get("RBMQ_PASS")
        if port is None:
            self.port = os.environ.get("RBMQ_PORT")
        self._validate_host()
        self._validate_user()
        self._validate_pass()
        self._validate_port()

    def get_host(self):
        return self.host

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_port(self):
        return self.port

    def _validate_host(self):
        if self.host is None:
            raise ValueError("RBMQ_HOST should not be empty")

    def _validate_user(self):
        if self.user is None:
            raise ValueError("RBMQ_USER should not be empty")

    def _validate_pass(self):
        if self.password is None:
            raise ValueError("RBMQ_PASS should not be empty")

    def _validate_port(self):
        if self.port is None:
            raise ValueError("RBMQ_PORT should not be empty")
