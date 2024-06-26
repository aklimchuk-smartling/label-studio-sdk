# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class Prediction(pydantic_v1.BaseModel):
    id: typing.Optional[int] = None
    result: typing.List[typing.Dict[str, typing.Any]] = pydantic_v1.Field()
    """
    List of prediction results for the task
    """

    model_version: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Model version - tag for predictions that can be used to filter tasks in Data Manager, as well as select specific model version for showing preannotations in the labeling interface
    """

    created_ago: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Delta time from creation time
    """

    score: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Prediction score
    """

    cluster: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Cluster for the current prediction
    """

    neighbors: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Array of task IDs of the closest neighbors
    """

    mislabeling: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    Related task mislabeling score
    """

    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    model: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    An ML Backend instance that created the prediction.
    """

    model_run: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    A run of a ModelVersion that created the prediction.
    """

    task: int
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
