from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupGroupCreate")


@attr.s(auto_attribs=True)
class GroupGroupCreate:
    """
    Attributes:
        title (Optional[str]): Group title Example: My newsletter group.
        description (Union[Unset, None, str]): Group description Example: Newsletter suscribers.
        color (Union[Unset, None, str]): Group color Example: #263238.
        public (Union[Unset, None, bool]): Is public? Example: True.
        audience (Optional[str]): Audience Example: /audiences/0df14405-90ff-4287-b3e4-ef088901ee6f.
    """

    title: Optional[str]
    audience: Optional[str]
    description: Union[Unset, None, str] = UNSET
    color: Union[Unset, None, str] = UNSET
    public: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        color = self.color
        public = self.public
        audience = self.audience

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "audience": audience,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        public = d.pop("public", UNSET)

        audience = d.pop("audience")

        group_group_create = cls(
            title=title,
            description=description,
            color=color,
            public=public,
            audience=audience,
        )

        group_group_create.additional_properties = d
        return group_group_create

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
