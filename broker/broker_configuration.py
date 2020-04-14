from broker.rabbit.rabbit_provider import RabbitMQProvider
from broker.rabbit.rabbit_settings import RabbitSettings

# TODO: get this configuration from env variables or something like that
DEFAULT_BROKER_PROVIDER_CLASS = RabbitMQProvider
DEFAULT_BROKER_CONFIGURATION_CLASS = RabbitSettings
