import os
import logging
from config.config import ModelConfig


logger = logging.getLogger(__name__)


class Model:
    def __init__(self, config_model: ModelConfig):
        self.model_name = config_model.name
        self.base_url = config_model.base_url
        self.api_key = os.getenv("MODEL_API_KEY", "")
        self.model_type = config_model.model_type

    def __str__(self):
        return f"{self.model_name} ({self.base_url} {self.model_type} {self.api_key})"
