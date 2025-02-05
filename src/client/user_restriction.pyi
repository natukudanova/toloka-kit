__all__ = [
    'DurationUnit',
    'UserRestriction',
    'AllProjectsUserRestriction',
    'PoolUserRestriction',
    'ProjectUserRestriction',
    'SystemUserRestriction',
]
import datetime
import enum
import toloka.client.primitives.base
import toloka.util._extendable_enum
import typing


class DurationUnit(enum.Enum):
    """An enumeration.
    """

    MINUTES = 'MINUTES'
    HOURS = 'HOURS'
    DAYS = 'DAYS'
    PERMANENT = 'PERMANENT'


class UserRestriction(toloka.client.primitives.base.BaseTolokaObject):
    """Controls access to projects and pools.

    You can restrict access to any project for a Toloker. Then he can't do tasks in the project. You may set the duration of restriction or apply permanent restriction.
    To unlock access pass the restriction ID to the `delete_user_restriction`.

    Attributes:
        user_id: The ID of the Toloker.
        private_comment: A comment for you why access to this Toloker was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read-only field.
        created: Date and time when the fact of access restriction was created. Read-only field.

    Example:
        How you can lock access for one Toloker on one project.

        >>> new_restrict = toloka_client.set_user_restriction(
        >>>     ProjectUserRestriction(
        >>>         user_id='1',
        >>>         private_comment='I dont like you',
        >>>         project_id='5'
        >>>     )
        >>> )
        ...

        And how you can unlock it.

        >>> toloka_client.delete_user_restriction(new_restrict.id)
        ...
    """

    class Scope(toloka.util._extendable_enum.ExtendableStrEnum):
        """Restriction scope

        * ALL_PROJECTS - All the requester's projects.
        * PROJECT - A single project (specify the project_id).
        * POOL - A pool (specify the pool_id).
        """

        SYSTEM = 'SYSTEM'
        ALL_PROJECTS = 'ALL_PROJECTS'
        PROJECT = 'PROJECT'
        POOL = 'POOL'

    def __init__(
        self,
        *,
        user_id: typing.Optional[str] = None,
        private_comment: typing.Optional[str] = None,
        will_expire: typing.Optional[datetime.datetime] = None,
        id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class UserRestriction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    user_id: typing.Optional[str]
    private_comment: typing.Optional[str]
    will_expire: typing.Optional[datetime.datetime]
    id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]


class AllProjectsUserRestriction(UserRestriction):
    """Forbid the Toloker to complete tasks from all your projects

    Attributes:
        user_id: The ID of the Toloker.
        private_comment: A comment for you why access to this Toloker was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read-only field.
        created: Date and time when the fact of access restriction was created. Read-only field.
    """

    def __init__(
        self,
        *,
        user_id: typing.Optional[str] = None,
        private_comment: typing.Optional[str] = None,
        will_expire: typing.Optional[datetime.datetime] = None,
        id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class AllProjectsUserRestriction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    user_id: typing.Optional[str]
    private_comment: typing.Optional[str]
    will_expire: typing.Optional[datetime.datetime]
    id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]


class PoolUserRestriction(UserRestriction):
    """Forbid the Toloker to complete tasks from a specific pool

    Attributes:
        user_id: The ID of the Toloker.
        private_comment: A comment for you why access to this Toloker was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read-only field.
        created: Date and time when the fact of access restriction was created. Read-only field.
        pool_id: Pool identifier to which access will be denied.
    """

    def __init__(
        self,
        *,
        user_id: typing.Optional[str] = None,
        private_comment: typing.Optional[str] = None,
        will_expire: typing.Optional[datetime.datetime] = None,
        id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None,
        pool_id: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class PoolUserRestriction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    user_id: typing.Optional[str]
    private_comment: typing.Optional[str]
    will_expire: typing.Optional[datetime.datetime]
    id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    pool_id: typing.Optional[str]


class ProjectUserRestriction(UserRestriction):
    """Forbid the Toloker to complete tasks from a specific project

    Attributes:
        user_id: The ID of the Toloker.
        private_comment: A comment for you why access to this Toloker was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read-only field.
        created: Date and time when the fact of access restriction was created. Read-only field.
        project_id: Project identifier to which access will be denied.
    """

    def __init__(
        self,
        *,
        user_id: typing.Optional[str] = None,
        private_comment: typing.Optional[str] = None,
        will_expire: typing.Optional[datetime.datetime] = None,
        id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None,
        project_id: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class ProjectUserRestriction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    user_id: typing.Optional[str]
    private_comment: typing.Optional[str]
    will_expire: typing.Optional[datetime.datetime]
    id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    project_id: typing.Optional[str]


class SystemUserRestriction(UserRestriction):
    """DEPRECATED

    Attributes:
        user_id: The ID of the Toloker.
        private_comment: A comment for you why access to this Toloker was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read-only field.
        created: Date and time when the fact of access restriction was created. Read-only field.
    """

    def __init__(
        self,
        *,
        user_id: typing.Optional[str] = None,
        private_comment: typing.Optional[str] = None,
        will_expire: typing.Optional[datetime.datetime] = None,
        id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class SystemUserRestriction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    user_id: typing.Optional[str]
    private_comment: typing.Optional[str]
    will_expire: typing.Optional[datetime.datetime]
    id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
