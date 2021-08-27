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
import toloka.client.util._extendable_enum
import typing


class DurationUnit(enum.Enum):
    """An enumeration.
    """

    MINUTES = 'MINUTES'
    HOURS = 'HOURS'
    DAYS = 'DAYS'
    PERMANENT = 'PERMANENT'


class UserRestriction(toloka.client.primitives.base.BaseTolokaObject):
    """Allows you to control the performer's access to your projects and pools

    You can close user access to one or more projects. This allows you to control which users will perform tasks.
    For example, you can select users with a skill value below N and block them from accessing tasks.
    You can also unlock access.

    Attributes:
        user_id: Which performer is denied access.
        private_comment: A comment for you why access to this performer was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read only.
        created: Date and time when the fact of access restriction was created. Read only.

    Example:
        How you can lock access for one user on one project.

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

    class Scope(toloka.client.util._extendable_enum.ExtendableStrEnum):
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
    """Forbid the performer from doing tasks from all your projects

    Attributes:
        user_id: Which performer is denied access.
        private_comment: A comment for you why access to this performer was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read only.
        created: Date and time when the fact of access restriction was created. Read only.
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
    """Forbid the performer from doing tasks from a specific pool

    Attributes:
        user_id: Which performer is denied access.
        private_comment: A comment for you why access to this performer was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read only.
        created: Date and time when the fact of access restriction was created. Read only.
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
    """Forbid the performer from doing tasks from a specific project

    Attributes:
        user_id: Which performer is denied access.
        private_comment: A comment for you why access to this performer was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read only.
        created: Date and time when the fact of access restriction was created. Read only.
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
        user_id: Which performer is denied access.
        private_comment: A comment for you why access to this performer was restricted.
        will_expire: When access is restored. If you do not set the parameter, then the access restriction is permanent.
        id: The identifier of a specific fact of access restriction. Read only.
        created: Date and time when the fact of access restriction was created. Read only.
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
