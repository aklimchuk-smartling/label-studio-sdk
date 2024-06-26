# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .project_import_status import ProjectImportStatus


class ProjectImport(pydantic_v1.BaseModel):
    id: typing.Optional[int] = None
    preannotated_from_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    commit_to_project: typing.Optional[bool] = None
    return_task_ids: typing.Optional[bool] = None
    status: typing.Optional[ProjectImportStatus] = None
    url: typing.Optional[str] = None
    traceback: typing.Optional[str] = None
    error: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Creation time
    """

    updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Updated time
    """

    finished_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Complete or fail time
    """

    task_count: typing.Optional[int] = None
    annotation_count: typing.Optional[int] = None
    prediction_count: typing.Optional[int] = None
    duration: typing.Optional[int] = None
    file_upload_ids: typing.Optional[typing.Dict[str, typing.Any]] = None
    could_be_tasks_list: typing.Optional[bool] = None
    found_formats: typing.Optional[typing.Dict[str, typing.Any]] = None
    data_columns: typing.Optional[typing.Dict[str, typing.Any]] = None
    tasks: typing.Optional[typing.Dict[str, typing.Any]] = None
    task_ids: typing.Optional[typing.Dict[str, typing.Any]] = None
    project: typing.Optional[int] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
