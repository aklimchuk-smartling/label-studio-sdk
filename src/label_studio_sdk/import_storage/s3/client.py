# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...types.s3import_storage import S3ImportStorage
from .types.s3create_response import S3CreateResponse
from .types.s3update_response import S3UpdateResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class S3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[S3ImportStorage]:
        """
        Get a list of all S3 import storage connections.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[S3ImportStorage]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/s3/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[S3ImportStorage], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        project: typing.Optional[int] = OMIT,
        bucket: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        aws_access_key_id: typing.Optional[str] = OMIT,
        aws_secret_access_key: typing.Optional[str] = OMIT,
        aws_session_token: typing.Optional[str] = OMIT,
        aws_sse_kms_key_id: typing.Optional[str] = OMIT,
        region_name: typing.Optional[str] = OMIT,
        s3endpoint: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        recursive_scan: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> S3CreateResponse:
        """
        Create new S3 import storage

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        bucket : typing.Optional[str]
            S3 bucket name

        prefix : typing.Optional[str]
            S3 bucket prefix

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        aws_access_key_id : typing.Optional[str]
            AWS_ACCESS_KEY_ID

        aws_secret_access_key : typing.Optional[str]
            AWS_SECRET_ACCESS_KEY

        aws_session_token : typing.Optional[str]
            AWS_SESSION_TOKEN

        aws_sse_kms_key_id : typing.Optional[str]
            AWS SSE KMS Key ID

        region_name : typing.Optional[str]
            AWS Region

        s3endpoint : typing.Optional[str]
            S3 Endpoint

        presign : typing.Optional[bool]
            Presign URLs for download

        presign_ttl : typing.Optional[int]
            Presign TTL in seconds

        recursive_scan : typing.Optional[bool]
            Scan recursively

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3CreateResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/s3/",
            method="POST",
            json={
                "project": project,
                "bucket": bucket,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "aws_access_key_id": aws_access_key_id,
                "aws_secret_access_key": aws_secret_access_key,
                "aws_session_token": aws_session_token,
                "aws_sse_kms_key_id": aws_sse_kms_key_id,
                "region_name": region_name,
                "s3_endpoint": s3endpoint,
                "presign": presign,
                "presign_ttl": presign_ttl,
                "recursive_scan": recursive_scan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3CreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate(self, *, request_options: typing.Optional[RequestOptions] = None) -> S3ImportStorage:
        """
        Validate a specific S3 import storage connection.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3ImportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.validate()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/s3/validate", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3ImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> S3ImportStorage:
        """
        Get a specific S3 import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this s3 import storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3ImportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3ImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific S3 import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this s3 import storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        project: typing.Optional[int] = OMIT,
        bucket: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        aws_access_key_id: typing.Optional[str] = OMIT,
        aws_secret_access_key: typing.Optional[str] = OMIT,
        aws_session_token: typing.Optional[str] = OMIT,
        aws_sse_kms_key_id: typing.Optional[str] = OMIT,
        region_name: typing.Optional[str] = OMIT,
        s3endpoint: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        recursive_scan: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> S3UpdateResponse:
        """
        Update a specific S3 import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this s3 import storage.

        project : typing.Optional[int]
            Project ID

        bucket : typing.Optional[str]
            S3 bucket name

        prefix : typing.Optional[str]
            S3 bucket prefix

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        aws_access_key_id : typing.Optional[str]
            AWS_ACCESS_KEY_ID

        aws_secret_access_key : typing.Optional[str]
            AWS_SECRET_ACCESS_KEY

        aws_session_token : typing.Optional[str]
            AWS_SESSION_TOKEN

        aws_sse_kms_key_id : typing.Optional[str]
            AWS SSE KMS Key ID

        region_name : typing.Optional[str]
            AWS Region

        s3endpoint : typing.Optional[str]
            S3 Endpoint

        presign : typing.Optional[bool]
            Presign URLs for download

        presign_ttl : typing.Optional[int]
            Presign TTL in seconds

        recursive_scan : typing.Optional[bool]
            Scan recursively

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3UpdateResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project": project,
                "bucket": bucket,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "aws_access_key_id": aws_access_key_id,
                "aws_secret_access_key": aws_secret_access_key,
                "aws_session_token": aws_session_token,
                "aws_sse_kms_key_id": aws_sse_kms_key_id,
                "region_name": region_name,
                "s3_endpoint": s3endpoint,
                "presign": presign,
                "presign_ttl": presign_ttl,
                "recursive_scan": recursive_scan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3UpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def sync(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> S3ImportStorage:
        """
        Sync tasks from an S3 import storage connection.

        Parameters
        ----------
        id : int
            Storage ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3ImportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.s3.sync(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}/sync", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3ImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncS3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[S3ImportStorage]:
        """
        Get a list of all S3 import storage connections.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[S3ImportStorage]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/s3/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[S3ImportStorage], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        project: typing.Optional[int] = OMIT,
        bucket: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        aws_access_key_id: typing.Optional[str] = OMIT,
        aws_secret_access_key: typing.Optional[str] = OMIT,
        aws_session_token: typing.Optional[str] = OMIT,
        aws_sse_kms_key_id: typing.Optional[str] = OMIT,
        region_name: typing.Optional[str] = OMIT,
        s3endpoint: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        recursive_scan: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> S3CreateResponse:
        """
        Create new S3 import storage

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        bucket : typing.Optional[str]
            S3 bucket name

        prefix : typing.Optional[str]
            S3 bucket prefix

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        aws_access_key_id : typing.Optional[str]
            AWS_ACCESS_KEY_ID

        aws_secret_access_key : typing.Optional[str]
            AWS_SECRET_ACCESS_KEY

        aws_session_token : typing.Optional[str]
            AWS_SESSION_TOKEN

        aws_sse_kms_key_id : typing.Optional[str]
            AWS SSE KMS Key ID

        region_name : typing.Optional[str]
            AWS Region

        s3endpoint : typing.Optional[str]
            S3 Endpoint

        presign : typing.Optional[bool]
            Presign URLs for download

        presign_ttl : typing.Optional[int]
            Presign TTL in seconds

        recursive_scan : typing.Optional[bool]
            Scan recursively

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3CreateResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/s3/",
            method="POST",
            json={
                "project": project,
                "bucket": bucket,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "aws_access_key_id": aws_access_key_id,
                "aws_secret_access_key": aws_secret_access_key,
                "aws_session_token": aws_session_token,
                "aws_sse_kms_key_id": aws_sse_kms_key_id,
                "region_name": region_name,
                "s3_endpoint": s3endpoint,
                "presign": presign,
                "presign_ttl": presign_ttl,
                "recursive_scan": recursive_scan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3CreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate(self, *, request_options: typing.Optional[RequestOptions] = None) -> S3ImportStorage:
        """
        Validate a specific S3 import storage connection.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3ImportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.validate()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/s3/validate", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3ImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> S3ImportStorage:
        """
        Get a specific S3 import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this s3 import storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3ImportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3ImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific S3 import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this s3 import storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: int,
        *,
        project: typing.Optional[int] = OMIT,
        bucket: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        aws_access_key_id: typing.Optional[str] = OMIT,
        aws_secret_access_key: typing.Optional[str] = OMIT,
        aws_session_token: typing.Optional[str] = OMIT,
        aws_sse_kms_key_id: typing.Optional[str] = OMIT,
        region_name: typing.Optional[str] = OMIT,
        s3endpoint: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        recursive_scan: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> S3UpdateResponse:
        """
        Update a specific S3 import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this s3 import storage.

        project : typing.Optional[int]
            Project ID

        bucket : typing.Optional[str]
            S3 bucket name

        prefix : typing.Optional[str]
            S3 bucket prefix

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        aws_access_key_id : typing.Optional[str]
            AWS_ACCESS_KEY_ID

        aws_secret_access_key : typing.Optional[str]
            AWS_SECRET_ACCESS_KEY

        aws_session_token : typing.Optional[str]
            AWS_SESSION_TOKEN

        aws_sse_kms_key_id : typing.Optional[str]
            AWS SSE KMS Key ID

        region_name : typing.Optional[str]
            AWS Region

        s3endpoint : typing.Optional[str]
            S3 Endpoint

        presign : typing.Optional[bool]
            Presign URLs for download

        presign_ttl : typing.Optional[int]
            Presign TTL in seconds

        recursive_scan : typing.Optional[bool]
            Scan recursively

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3UpdateResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.update(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project": project,
                "bucket": bucket,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "aws_access_key_id": aws_access_key_id,
                "aws_secret_access_key": aws_secret_access_key,
                "aws_session_token": aws_session_token,
                "aws_sse_kms_key_id": aws_sse_kms_key_id,
                "region_name": region_name,
                "s3_endpoint": s3endpoint,
                "presign": presign,
                "presign_ttl": presign_ttl,
                "recursive_scan": recursive_scan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3UpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def sync(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> S3ImportStorage:
        """
        Sync tasks from an S3 import storage connection.

        Parameters
        ----------
        id : int
            Storage ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        S3ImportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.s3.sync(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/s3/{jsonable_encoder(id)}/sync", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(S3ImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
