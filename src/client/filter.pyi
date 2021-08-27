__all__ = [
    'FilterCondition',
    'FilterOr',
    'FilterAnd',
    'Condition',
    'Profile',
    'Computed',
    'Skill',
    'Gender',
    'Country',
    'Citizenship',
    'Education',
    'AdultAllowed',
    'DateOfBirth',
    'City',
    'Languages',
    'RegionByPhone',
    'RegionByIp',
    'DeviceCategory',
    'ClientType',
    'OSFamily',
    'OSVersion',
    'OSVersionMajor',
    'OSVersionMinor',
    'OSVersionBugfix',
    'UserAgentType',
    'UserAgentFamily',
    'UserAgentVersion',
    'UserAgentVersionMajor',
    'UserAgentVersionMinor',
    'UserAgentVersionBugfix',
    'Rating',
]
import toloka.client.primitives.base
import toloka.client.primitives.operators
import toloka.client.util._extendable_enum
import typing


class FilterCondition(toloka.client.primitives.base.BaseTolokaObject):
    """You can select users to access pool tasks.

    For example, you can select users by region, skill, or browser type (desktop or mobile).

    Example:
        How to setup filter for selecting users.

        >>> # you can combine filters using bitwise operators '|' and  '&'
        >>> filter = (
        >>>    (toloka.filter.Languages.in_('EN')) &
        >>>    (toloka.client.filter.DeviceCategory.in_(toloka.client.filter.DeviceCategory.SMARTPHONE))
        >>> )
        ...
    """

    @classmethod
    def structure(cls, data: dict): ...

    def __init__(self) -> None:
        """Method generated by attrs for class FilterCondition.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


class FilterOr(FilterCondition):
    """Use to combine multiple filters via "or" logic

    Attributes:
        or_: list of filters to combine
    """

    @classmethod
    def structure(cls, data): ...

    def __init__(self, or_: typing.List[FilterCondition]) -> None:
        """Method generated by attrs for class FilterOr.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    or_: typing.List[FilterCondition]


class FilterAnd(FilterCondition):
    """Use to combine multiple filters via "and" logic

    Attributes:
        and_: list of filters to combine
    """

    @classmethod
    def structure(cls, data): ...

    def __init__(self, and_: typing.List[FilterCondition]) -> None:
        """Method generated by attrs for class FilterAnd.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    and_: typing.List[FilterCondition]


class Condition(FilterCondition):
    """Condition to select users.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Attribute value from the field key. For example, the ID of the region specified in the profile,
            or the minimum skill value.
    """

    class Category(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """An enumeration.
        """

        PROFILE = 'profile'
        COMPUTED = 'computed'
        SKILL = 'skill'

    @classmethod
    def structure(cls, data): ...

    def __init__(
        self,
        *,
        operator: typing.Any,
        value: typing.Any
    ) -> None:
        """Method generated by attrs for class Condition.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operator: typing.Any
    value: typing.Any


class Profile(Condition):
    """Use to select users based on profile data.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Attribute value from the field key. For example, the ID of the region specified in the profile,
            or the minimum skill value.
    """

    class Key(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """Possible criteria for filtering users by profile.
        """

        GENDER = 'gender'
        COUNTRY = 'country'
        CITIZENSHIP = 'citizenship'
        EDUCATION = 'education'
        ADULT_ALLOWED = 'adult_allowed'
        DATE_OF_BIRTH = 'date_of_birth'
        CITY = 'city'
        LANGUAGES = 'languages'

    def __init__(
        self,
        *,
        operator: typing.Any,
        value: typing.Any
    ) -> None:
        """Method generated by attrs for class Profile.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operator: typing.Any
    value: typing.Any


class Computed(Condition):
    """Use to select users based on data received or calculated by Toloka.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Attribute value from the field key. For example, the ID of the region specified in the profile,
            or the minimum skill value.
    """

    class Key(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """Possible criteria for filtering users by computed data.
        """

        CLIENT_TYPE = 'client_type'
        REGION_BY_PHONE = 'region_by_phone'
        REGION_BY_IP = 'region_by_ip'
        RATING = 'rating'
        DEVICE_CATEGORY = 'device_category'
        OS_FAMILY = 'os_family'
        OS_VERSION = 'os_version'
        USER_AGENT_TYPE = 'user_agent_type'
        USER_AGENT_FAMILY = 'user_agent_family'
        USER_AGENT_VERSION = 'user_agent_version'
        OS_VERSION_MAJOR = 'os_version_major'
        OS_VERSION_MINOR = 'os_version_minor'
        OS_VERSION_BUGFIX = 'os_version_bugfix'
        USER_AGENT_VERSION_MAJOR = 'user_agent_version_major'
        USER_AGENT_VERSION_MINOR = 'user_agent_version_minor'
        USER_AGENT_VERSION_BUGFIX = 'user_agent_version_bugfix'

    def __init__(
        self,
        *,
        operator: typing.Any,
        value: typing.Any
    ) -> None:
        """Method generated by attrs for class Computed.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operator: typing.Any
    value: typing.Any


class Skill(toloka.client.primitives.operators.StatefulComparableConditionMixin, Condition):
    """Use to select users by skill value.

    To select users without a skill set the parameter value operator=CompareOperator.EQ and exclude the parameter value.
    Attributes:
        key: Skill ID.
        operator: Comparison operator in the condition.
        value: Attribute value from the field key.
    """

    def __init__(
        self,
        key: str,
        operator: toloka.client.primitives.operators.CompareOperator = toloka.client.primitives.operators.CompareOperator.EQ,
        value: typing.Optional[float] = None
    ) -> None:
        """Method generated by attrs for class Skill.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operator: toloka.client.primitives.operators.CompareOperator
    value: typing.Optional[float]
    key: str


class Gender(Profile, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by gender.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User gender.
    """

    class Gender(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """User gender.
        """

        MALE = 'MALE'
        FEMALE = 'FEMALE'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: Gender
    ) -> None:
        """Method generated by attrs for class Gender.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: Gender


class Country(Profile, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by country.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Country of the user (two-letter code of the standard ISO 3166-1 alpha-2).
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: str
    ) -> None:
        """Method generated by attrs for class Country.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: str


class Citizenship(Profile, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by citizenship.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User citizenship (two-letter country code) ISO 3166-1 alpha-2
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: str
    ) -> None:
        """Method generated by attrs for class Citizenship.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: str


class Education(Profile, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by education.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User education.
    """

    class Education(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """User education.
        """

        BASIC = 'BASIC'
        MIDDLE = 'MIDDLE'
        HIGH = 'HIGH'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: Education
    ) -> None:
        """Method generated by attrs for class Education.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: Education


class AdultAllowed(Profile, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by their agreement to perform tasks that contain adult content.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User agreement.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: bool
    ) -> None:
        """Method generated by attrs for class AdultAllowed.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: bool


class DateOfBirth(Profile, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by date of birth.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: The user's date of birth (UNIX time in seconds).
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class DateOfBirth.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class City(Profile, toloka.client.primitives.operators.InclusionConditionMixin):
    """Use to select users by city.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User city(ID of the region).
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.InclusionOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class City.
        """
        ...

    operator: toloka.client.primitives.operators.InclusionOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class Languages(Profile, toloka.client.primitives.operators.InclusionConditionMixin):
    """Use to select users by languages specified by the user in the profile.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Languages specified by the user in the profile (two-letter ISO code of the standard ISO 639-1 in upper case).
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.InclusionOperator,
        value: typing.Union[str, typing.List[str]]
    ) -> None:
        """Method generated by attrs for class Languages.
        """
        ...

    operator: toloka.client.primitives.operators.InclusionOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: typing.Union[str, typing.List[str]]


class RegionByPhone(Computed, toloka.client.primitives.operators.InclusionConditionMixin):
    """Use to select users by their region determined by the mobile phone number.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: The user's region.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.InclusionOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class RegionByPhone.
        """
        ...

    operator: toloka.client.primitives.operators.InclusionOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class RegionByIp(Computed, toloka.client.primitives.operators.InclusionConditionMixin):
    """Use to select users by their region determined by IP address.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: The user's region.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.InclusionOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class RegionByIp.
        """
        ...

    operator: toloka.client.primitives.operators.InclusionOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class DeviceCategory(Computed, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by their device category.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: The user's device category.
    """

    class DeviceCategory(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """Device сategory.
        """

        PERSONAL_COMPUTER = 'PERSONAL_COMPUTER'
        SMARTPHONE = 'SMARTPHONE'
        TABLET = 'TABLET'
        WEARABLE_COMPUTER = 'WEARABLE_COMPUTER'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: DeviceCategory
    ) -> None:
        """Method generated by attrs for class DeviceCategory.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: DeviceCategory


class ClientType(Computed, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by their application type.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Client application type.
    """

    class ClientType(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """Client application type.
        """

        BROWSER = 'BROWSER'
        TOLOKA_APP = 'TOLOKA_APP'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: ClientType
    ) -> None:
        """Method generated by attrs for class ClientType.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: ClientType


class OSFamily(Computed, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by their OS family.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: The operating system family.
    """

    class OSFamily(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """The operating system family.
        """

        WINDOWS = 'WINDOWS'
        OS_X = 'OS_X'
        MAC_OS = 'MAC_OS'
        LINUX = 'LINUX'
        BSD = 'BSD'
        ANDROID = 'ANDROID'
        IOS = 'IOS'
        BLACKBERRY = 'BLACKBERRY'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: OSFamily
    ) -> None:
        """Method generated by attrs for class OSFamily.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: OSFamily


class OSVersion(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by OS full version.

    For example: 14.4

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Full version of the operating system.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: float
    ) -> None:
        """Method generated by attrs for class OSVersion.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: float


class OSVersionMajor(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by OS major version.

    For example: 14

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Major version of the operating system.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class OSVersionMajor.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class OSVersionMinor(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by OS minor version.

    For example: 4

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Minor version of the operating system.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class OSVersionMinor.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class OSVersionBugfix(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by build number (bugfix version) of the operating system.

    For example: 1

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Build number (bugfix version) of the operating system.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: int
    ) -> None:
        """Method generated by attrs for class OSVersionBugfix.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: int


class UserAgentType(Computed, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by user agent type:

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User agent type.
    """

    class UserAgentType(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """User agent type.
        """

        BROWSER = 'BROWSER'
        MOBILE_BROWSER = 'MOBILE_BROWSER'
        OTHER = 'OTHER'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: UserAgentType
    ) -> None:
        """Method generated by attrs for class UserAgentType.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: UserAgentType


class UserAgentFamily(Computed, toloka.client.primitives.operators.IdentityConditionMixin):
    """Use to select users by user agent family.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User agent family.
    """

    class UserAgentFamily(toloka.client.util._extendable_enum.ExtendableStrEnum):
        """User agent family.
        """

        IE = 'IE'
        CHROMIUM = 'CHROMIUM'
        CHROME = 'CHROME'
        FIREFOX = 'FIREFOX'
        SAFARI = 'SAFARI'
        YANDEX_BROWSER = 'YANDEX_BROWSER'
        IE_MOBILE = 'IE_MOBILE'
        CHROME_MOBILE = 'CHROME_MOBILE'
        MOBILE_FIREFOX = 'MOBILE_FIREFOX'
        MOBILE_SAFARI = 'MOBILE_SAFARI'

    def __init__(
        self,
        operator: toloka.client.primitives.operators.IdentityOperator,
        value: UserAgentFamily
    ) -> None:
        """Method generated by attrs for class UserAgentFamily.
        """
        ...

    operator: toloka.client.primitives.operators.IdentityOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: UserAgentFamily


class UserAgentVersion(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by full browser version.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Full browser version. <Major version>.<Minor version>.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: typing.Optional[float] = None
    ) -> None:
        """Method generated by attrs for class UserAgentVersion.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: typing.Optional[float]


class UserAgentVersionMajor(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by major browser version.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Major browser version.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: typing.Optional[int] = None
    ) -> None:
        """Method generated by attrs for class UserAgentVersionMajor.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: typing.Optional[int]


class UserAgentVersionMinor(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by minor browser version.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Minor browser version.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: typing.Optional[int] = None
    ) -> None:
        """Method generated by attrs for class UserAgentVersionMinor.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: typing.Optional[int]


class UserAgentVersionBugfix(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by build number (bugfix version) of the browser.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: Build number (bugfix version) of the browser.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: typing.Optional[int] = None
    ) -> None:
        """Method generated by attrs for class UserAgentVersionBugfix.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: typing.Optional[int]


class Rating(Computed, toloka.client.primitives.operators.ComparableConditionMixin):
    """Use to select users by user rating.

    Attributes:
        operator: Comparison operator in the condition.
            For example, for a condition "The user must be 18 years old or older» used date of birth and operator
            GTE («Greater than or equal»). Possible key values operator depends on the data type in the field value
        value: User rating. Calculated based on earnings in all projects available to the user.
    """

    def __init__(
        self,
        operator: toloka.client.primitives.operators.CompareOperator,
        value: typing.Optional[float] = None
    ) -> None:
        """Method generated by attrs for class Rating.
        """
        ...

    operator: toloka.client.primitives.operators.CompareOperator
    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    value: typing.Optional[float]
