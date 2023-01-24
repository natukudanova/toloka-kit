__all__ = [
    'Owner',
]
import toloka.client.primitives.base
import typing


class Owner(toloka.client.primitives.base.BaseTolokaObject):
    """Parameters of the customer who created an object.

    Attributes:
        id: Customer ID.
        myself: An object accessory marker.
            Possible values:
                * `True` — An object is created by the customer whose OAuth token is used in the request.
                * `False` — An object does not belong to the customer whose OAuth token is used in the request.
        company_id: ID of the customer's company.
    """

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        myself: typing.Optional[bool] = None,
        company_id: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class Owner.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    id: typing.Optional[str]
    myself: typing.Optional[bool]
    company_id: typing.Optional[str]
