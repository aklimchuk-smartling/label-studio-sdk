# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from label_studio_sdk.client import AsyncLabelStudio, LabelStudio


@pytest.fixture
def client() -> LabelStudio:
    return LabelStudio(api_key=os.getenv("ENV_API_KEY", "api_key"), base_url=os.getenv("TESTS_BASE_URL", "base_url"))


@pytest.fixture
def async_client() -> AsyncLabelStudio:
    return AsyncLabelStudio(
        api_key=os.getenv("ENV_API_KEY", "api_key"), base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
