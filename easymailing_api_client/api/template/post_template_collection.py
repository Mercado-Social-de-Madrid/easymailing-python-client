from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.template_jsonld_template_read import TemplateJsonldTemplateRead
from ...models.template_jsonld_template_test import TemplateJsonldTemplateTest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: TemplateJsonldTemplateTest,
) -> Dict[str, Any]:
    url = "{}/templates".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, TemplateJsonldTemplateRead]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = TemplateJsonldTemplateRead.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, TemplateJsonldTemplateRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: TemplateJsonldTemplateTest,
) -> Response[Union[Any, TemplateJsonldTemplateRead]]:
    """Creates a Template resource.

     Creates a Template resource.

    Args:
        json_body (TemplateJsonldTemplateTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TemplateJsonldTemplateRead]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: TemplateJsonldTemplateTest,
) -> Optional[Union[Any, TemplateJsonldTemplateRead]]:
    """Creates a Template resource.

     Creates a Template resource.

    Args:
        json_body (TemplateJsonldTemplateTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TemplateJsonldTemplateRead]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: TemplateJsonldTemplateTest,
) -> Response[Union[Any, TemplateJsonldTemplateRead]]:
    """Creates a Template resource.

     Creates a Template resource.

    Args:
        json_body (TemplateJsonldTemplateTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TemplateJsonldTemplateRead]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: TemplateJsonldTemplateTest,
) -> Optional[Union[Any, TemplateJsonldTemplateRead]]:
    """Creates a Template resource.

     Creates a Template resource.

    Args:
        json_body (TemplateJsonldTemplateTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TemplateJsonldTemplateRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
