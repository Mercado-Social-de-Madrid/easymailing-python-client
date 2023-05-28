from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.treatment_purpose_jsonld_treatment_purpose_read import TreatmentPurposeJsonldTreatmentPurposeRead
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/treatment_purposes/{uuid}".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TreatmentPurposeJsonldTreatmentPurposeRead.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Client,
) -> Response[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]:
    """Retrieves a TreatmentPurpose resource.

     Retrieves a TreatmentPurpose resource.

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Client,
) -> Optional[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]:
    """Retrieves a TreatmentPurpose resource.

     Retrieves a TreatmentPurpose resource.

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
) -> Response[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]:
    """Retrieves a TreatmentPurpose resource.

     Retrieves a TreatmentPurpose resource.

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
) -> Optional[Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]]:
    """Retrieves a TreatmentPurpose resource.

     Retrieves a TreatmentPurpose resource.

    Args:
        uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TreatmentPurposeJsonldTreatmentPurposeRead]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed