from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataManagerAudienceRead")


@attr.s(auto_attribs=True)
class DataManagerAudienceRead:
    """
    Attributes:
        name (Optional[str]): Firstname and lastname or Company name
        identification_number (Optional[str]): Identification number ID / VAT ID
        phone (Union[Unset, None, str]): Phone number
        website (Union[Unset, None, str]): Website url
        email (Optional[str]): Email
        address (Optional[str]): Address
        postal_code (Optional[str]): Postal code
        city (Optional[str]): City
        province (Optional[str]): Province
        country (Optional[str]): Country
    """

    name: Optional[str]
    identification_number: Optional[str]
    email: Optional[str]
    address: Optional[str]
    postal_code: Optional[str]
    city: Optional[str]
    province: Optional[str]
    country: Optional[str]
    phone: Union[Unset, None, str] = UNSET
    website: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        identification_number = self.identification_number
        phone = self.phone
        website = self.website
        email = self.email
        address = self.address
        postal_code = self.postal_code
        city = self.city
        province = self.province
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "identification_number": identification_number,
                "email": email,
                "address": address,
                "postal_code": postal_code,
                "city": city,
                "province": province,
                "country": country,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        identification_number = d.pop("identification_number")

        phone = d.pop("phone", UNSET)

        website = d.pop("website", UNSET)

        email = d.pop("email")

        address = d.pop("address")

        postal_code = d.pop("postal_code")

        city = d.pop("city")

        province = d.pop("province")

        country = d.pop("country")

        data_manager_audience_read = cls(
            name=name,
            identification_number=identification_number,
            phone=phone,
            website=website,
            email=email,
            address=address,
            postal_code=postal_code,
            city=city,
            province=province,
            country=country,
        )

        data_manager_audience_read.additional_properties = d
        return data_manager_audience_read

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
