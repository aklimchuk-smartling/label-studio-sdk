# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_create_many_status(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "preannotated_from_fields": {"preannotated_from_fields": {"key": "value"}},
        "commit_to_project": True,
        "return_task_ids": True,
        "status": "created",
        "url": "url",
        "traceback": "traceback",
        "error": "error",
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "finished_at": "2024-01-15T09:30:00Z",
        "task_count": 1,
        "annotation_count": 1,
        "prediction_count": 1,
        "duration": 1,
        "file_upload_ids": {"file_upload_ids": {"key": "value"}},
        "could_be_tasks_list": True,
        "found_formats": {"found_formats": {"key": "value"}},
        "data_columns": {"data_columns": {"key": "value"}},
        "tasks": {"tasks": {"key": "value"}},
        "task_ids": {"task_ids": {"key": "value"}},
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "preannotated_from_fields": ("dict", {0: (None, None)}),
        "commit_to_project": None,
        "return_task_ids": None,
        "status": None,
        "url": None,
        "traceback": None,
        "error": None,
        "created_at": "datetime",
        "updated_at": "datetime",
        "finished_at": "datetime",
        "task_count": "integer",
        "annotation_count": "integer",
        "prediction_count": "integer",
        "duration": "integer",
        "file_upload_ids": ("dict", {0: (None, None)}),
        "could_be_tasks_list": None,
        "found_formats": ("dict", {0: (None, None)}),
        "data_columns": ("dict", {0: (None, None)}),
        "tasks": ("dict", {0: (None, None)}),
        "task_ids": ("dict", {0: (None, None)}),
        "project": "integer",
    }
    response = client.tasks.create_many_status(id=1, import_pk="import_pk")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.create_many_status(id=1, import_pk="import_pk")
    validate_response(async_response, expected_response, expected_types)


async def test_delete_all_tasks(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.tasks.delete_all_tasks(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.tasks.delete_all_tasks(id=1) is None  # type: ignore[func-returns-value]


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "data": {"image": "https://example.com/image.jpg", "text": "Hello, AI!"},
        "meta": {"meta": {"key": "value"}},
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_labeled": False,
        "overlap": 1,
        "inner_id": 1,
        "total_annotations": 0,
        "cancelled_annotations": 0,
        "total_predictions": 0,
        "comment_count": 0,
        "unresolved_comment_count": 0,
        "last_comment_updated_at": "2024-01-15T09:30:00Z",
        "project": 1,
        "updated_by": 1,
        "file_upload": 1,
        "comment_authors": [1],
    }
    expected_types: typing.Any = {
        "id": "integer",
        "data": ("dict", {0: (None, None), 1: (None, None)}),
        "meta": ("dict", {0: (None, None)}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_labeled": None,
        "overlap": "integer",
        "inner_id": "integer",
        "total_annotations": "integer",
        "cancelled_annotations": "integer",
        "total_predictions": "integer",
        "comment_count": "integer",
        "unresolved_comment_count": "integer",
        "last_comment_updated_at": "datetime",
        "project": "integer",
        "updated_by": "integer",
        "file_upload": "integer",
        "comment_authors": ("list", {0: "integer"}),
    }
    response = client.tasks.create(data={"image": "https://example.com/image.jpg", "text": "Hello, world!"}, project=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.create(
        data={"image": "https://example.com/image.jpg", "text": "Hello, world!"}, project=1
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "data": {"image": "https://example.com/image.jpg", "text": "Hello, AI!"},
        "meta": {"meta": {"key": "value"}},
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_labeled": False,
        "overlap": 1,
        "inner_id": 1,
        "total_annotations": 0,
        "cancelled_annotations": 0,
        "total_predictions": 0,
        "comment_count": 0,
        "unresolved_comment_count": 0,
        "last_comment_updated_at": "2024-01-15T09:30:00Z",
        "project": 1,
        "updated_by": 1,
        "file_upload": 1,
        "comment_authors": [1],
    }
    expected_types: typing.Any = {
        "id": "integer",
        "data": ("dict", {0: (None, None), 1: (None, None)}),
        "meta": ("dict", {0: (None, None)}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_labeled": None,
        "overlap": "integer",
        "inner_id": "integer",
        "total_annotations": "integer",
        "cancelled_annotations": "integer",
        "total_predictions": "integer",
        "comment_count": "integer",
        "unresolved_comment_count": "integer",
        "last_comment_updated_at": "datetime",
        "project": "integer",
        "updated_by": "integer",
        "file_upload": "integer",
        "comment_authors": ("list", {0: "integer"}),
    }
    response = client.tasks.get(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.get(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.tasks.delete(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.tasks.delete(id="id") is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "data": {"image": "https://example.com/image.jpg", "text": "Hello, AI!"},
        "meta": {"meta": {"key": "value"}},
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "is_labeled": False,
        "overlap": 1,
        "inner_id": 1,
        "total_annotations": 0,
        "cancelled_annotations": 0,
        "total_predictions": 0,
        "comment_count": 0,
        "unresolved_comment_count": 0,
        "last_comment_updated_at": "2024-01-15T09:30:00Z",
        "project": 1,
        "updated_by": 1,
        "file_upload": 1,
        "comment_authors": [1],
    }
    expected_types: typing.Any = {
        "id": "integer",
        "data": ("dict", {0: (None, None), 1: (None, None)}),
        "meta": ("dict", {0: (None, None)}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "is_labeled": None,
        "overlap": "integer",
        "inner_id": "integer",
        "total_annotations": "integer",
        "cancelled_annotations": "integer",
        "total_predictions": "integer",
        "comment_count": "integer",
        "unresolved_comment_count": "integer",
        "last_comment_updated_at": "datetime",
        "project": "integer",
        "updated_by": "integer",
        "file_upload": "integer",
        "comment_authors": ("list", {0: "integer"}),
    }
    response = client.tasks.update(
        id="id", data={"image": "https://example.com/image.jpg", "text": "Hello, world!"}, project=1
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.tasks.update(
        id="id", data={"image": "https://example.com/image.jpg", "text": "Hello, world!"}, project=1
    )
    validate_response(async_response, expected_response, expected_types)
