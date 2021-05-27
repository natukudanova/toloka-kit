from datetime import datetime
from enum import Enum
from toloka.client.owner import Owner
from toloka.client.primitives.base import BaseTolokaObject
from typing import (
    Dict,
    Optional,
    Any
)


class Attachment(BaseTolokaObject):
    """Attachment

    Files uploaded by users are saved in Toloka.
    Attributes:
        id: File ID.
        name: File name.
        details: Infomation about the pool, the task, and the user who uploaded the file.
        created: Date the file was uploaded to Toloka.
        media_type: MIME data type.
        owner: Owner
    """

    ASSIGNMENT_ATTACHMENT = ...

    class Details(BaseTolokaObject):
        """Information about the pool, task, and user from which the file was received.

        Attributes:
            user_id: ID of the user from whom the file was received.
            assignment_id: ID for issuing a set of tasks to the user.
            pool_id: Pool ID.
        """

        def __init__(self, *, user_id: Optional[str] = None, assignment_id: Optional[str] = None, pool_id: Optional[str] = None) -> None:
            """Method generated by attrs for class Attachment.Details.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        user_id: Optional[str]
        assignment_id: Optional[str]
        pool_id: Optional[str]



    class Type(Enum):
        """An enumeration.
        """

        ASSIGNMENT_ATTACHMENT = 'ASSIGNMENT_ATTACHMENT'



    def __init__(self, *, id: Optional[str] = None, name: Optional[str] = None, details: Optional[Details] = None, created: Optional[datetime] = None, media_type: Optional[str] = None, owner: Optional[Owner] = None) -> None:
        """Method generated by attrs for class Attachment.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    id: Optional[str]
    name: Optional[str]
    details: Optional[Details]
    created: Optional[datetime]
    media_type: Optional[str]
    owner: Optional[Owner]

class AssignmentAttachment(Attachment):
    """Assignment Attachment.
    """

    def __init__(self, *, id: Optional[str] = None, name: Optional[str] = None, details: Optional[Attachment.Details] = None, created: Optional[datetime] = None, media_type: Optional[str] = None, owner: Optional[Owner] = None) -> None:
        """Method generated by attrs for class AssignmentAttachment.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    id: Optional[str]
    name: Optional[str]
    details: Optional[Attachment.Details]
    created: Optional[datetime]
    media_type: Optional[str]
    owner: Optional[Owner]

