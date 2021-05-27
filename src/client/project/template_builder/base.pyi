from enum import Enum
from toloka.client.primitives.base import BaseTolokaObject
from typing import (
    Dict,
    Optional,
    Type,
    Any
)


class ComponentType(Enum):
    """An enumeration.
    """

    ACTION_BULK = 'action.bulk'
    ACTION_NOTIFY = 'action.notify'
    ACTION_OPEN_CLOSE = 'action.open-close'
    ACTION_OPEN_LINK = 'action.open-link'
    ACTION_PLAY_PAUSE = 'action.play-pause'
    ACTION_ROTATE = 'action.rotate'
    ACTION_SET = 'action.set'
    ACTION_TOGGLE = 'action.toggle'
    CONDITION_ALL = 'condition.all'
    CONDITION_ANY = 'condition.any'
    CONDITION_EMPTY = 'condition.empty'
    CONDITION_EQUALS = 'condition.equals'
    CONDITION_LINK_OPENED = 'condition.link-opened'
    CONDITION_NOT = 'condition.not'
    CONDITION_PLAYED = 'condition.played'
    CONDITION_PLAYED_FULLY = 'condition.played-fully'
    CONDITION_REQUIRED = 'condition.required'
    CONDITION_SCHEMA = 'condition.schema'
    CONDITION_SUB_ARRAY = 'condition.sub-array'
    CONDITION_YANDEX_DISTANCE = '@yandex-toloka/condition.distance'
    DATA_INPUT = 'data.input'
    DATA_INTERNAL = 'data.internal'
    DATA_LOCAL = 'data.local'
    DATA_LOCATION = '@yandex-toloka/data.location'
    DATA_OUTPUT = 'data.output'
    DATA_RELATIVE = 'data.relative'
    FIELD_BUTTON_RADIO = 'field.button-radio'
    FIELD_BUTTON_RADIO_GROUP = 'field.button-radio-group'
    FIELD_CHECKBOX = 'field.checkbox'
    FIELD_CHECKBOX_GROUP = 'field.checkbox-group'
    FIELD_DATE = 'field.date'
    FIELD_EMAIL = 'field.email'
    FIELD_FILE = 'field.file'
    FIELD_IMAGE_ANNOTATION = 'field.image-annotation'
    FIELD_LIST = 'field.list'
    FIELD_MEDIA_FILE = 'field.media-file'
    FIELD_NUMBER = 'field.number'
    FIELD_PHONE_NUMBER = 'field.phone-number'
    FIELD_RADIO_GROUP = 'field.radio-group'
    FIELD_SELECT = 'field.select'
    FIELD_TEXT = 'field.text'
    FIELD_TEXTAREA = 'field.textarea'
    HELPER_CONCAT_ARRAYS = 'helper.concat-arrays'
    HELPER_ENTRIES2OBJECT = 'helper.entries2object'
    HELPER_IF = 'helper.if'
    HELPER_JOIN = 'helper.join'
    HELPER_OBJECT2ENTRIES = 'helper.object2entries'
    HELPER_REPLACE = 'helper.replace'
    HELPER_SEARCH_QUERY = 'helper.search-query'
    HELPER_SWITCH = 'helper.switch'
    HELPER_TEXT_TRANSFORM = 'helper.text-transform'
    HELPER_TRANSFORM = 'helper.transform'
    HELPER_YANDEX_DISK_PROXY = '@yandex-toloka/helper.proxy'
    LAYOUT_BARS = 'layout.bars'
    LAYOUT_COLUMNS = 'layout.columns'
    LAYOUT_SIDE_BY_SIDE = 'layout.side-by-side'
    LAYOUT_SIDEBAR = 'layout.sidebar'
    PLUGIN_HOTKEYS = 'plugin.hotkeys'
    PLUGIN_TRIGGER = 'plugin.trigger'
    PLUGIN_TOLOKA = 'plugin.toloka'
    VIEW_ACTION_BUTTON = 'view.action-button'
    VIEW_ALERT = 'view.alert'
    VIEW_AUDIO = 'view.audio'
    VIEW_COLLAPSE = 'view.collapse'
    VIEW_DEVICE_FRAME = 'view.device-frame'
    VIEW_DIVIDER = 'view.divider'
    VIEW_GROUP = 'view.group'
    VIEW_IFRAME = 'view.iframe'
    VIEW_IMAGE = 'view.image'
    VIEW_LABELED_LIST = 'view.labeled-list'
    VIEW_LINK = 'view.link'
    VIEW_LINK_GROUP = 'view.link-group'
    VIEW_LIST = 'view.list'
    VIEW_MARKDOWN = 'view.markdown'
    VIEW_TEXT = 'view.text'
    VIEW_VIDEO = 'view.video'

class BaseTemplate(BaseTolokaObject):
    def __init__(self) -> None:
        """Method generated by attrs for class BaseTemplate.
        """
        ...

    @classmethod
    def structure(cls, data: dict): ...

    _unexpected: Optional[Dict[str, Any]]

class BaseComponent(BaseTemplate):
    def __init__(self) -> None:
        """Method generated by attrs for class BaseComponent.
        """
        ...

    @classmethod
    def structure(cls, data: dict): ...

    _unexpected: Optional[Dict[str, Any]]

class BaseComponentOr(BaseTolokaObject):
    def __init__(self) -> None:
        """Method generated by attrs for class BaseComponentOr.
        """
        ...

    @classmethod
    def structure(cls, data): ...

    _unexpected: Optional[Dict[str, Any]]

def base_component_or(type_: Type, class_name_suffix: Optional[str] = None): ...

class VersionedBaseComponent(BaseComponent):
    def __init__(self, *, version: Optional[str] = '1.0.0') -> None:
        """Method generated by attrs for class VersionedBaseComponent.
        """
        ...

    def _validate_v1(self, attribute, value: str) -> str: ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]

class UnknownComponent(BaseTemplate):
    def __init__(self) -> None:
        """Method generated by attrs for class UnknownComponent.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]

class RefComponent(BaseTemplate):
    """If you need to insert the same or similar code snippets many times, reuse them.

    This helps make your configuration shorter and makes it easier for you to edit duplicate chunks of code.

    You can insert a code snippet from another part of the configuration anywhere inside the configuration. To do this,
    use the structure RefComponent(ref="path.to.element").

    This is useful when you need to insert the same snippet at multiple places in your code. For example, if you need
    to run the same action using multiple buttons, put this action in a variable and call it using RefComponent.
    """

    def __init__(self, *, ref: Optional[str] = None) -> None:
        """Method generated by attrs for class RefComponent.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    ref: Optional[str]

class ListDirection(Enum):
    """An enumeration.
    """

    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'

class ListSize(Enum):
    """An enumeration.
    """

    M = 'm'
    S = 's'

