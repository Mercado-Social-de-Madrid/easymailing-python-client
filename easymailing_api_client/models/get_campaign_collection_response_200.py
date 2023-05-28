from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_jsonld_campaign_read import CampaignJsonldCampaignRead
    from ..models.get_campaign_collection_response_200_hydrasearch import GetCampaignCollectionResponse200Hydrasearch
    from ..models.get_campaign_collection_response_200_hydraview import GetCampaignCollectionResponse200Hydraview


T = TypeVar("T", bound="GetCampaignCollectionResponse200")


@attr.s(auto_attribs=True)
class GetCampaignCollectionResponse200:
    """
    Attributes:
        hydramember (List['CampaignJsonldCampaignRead']):
        hydratotal_items (Union[Unset, int]):
        hydraview (Union[Unset, GetCampaignCollectionResponse200Hydraview]):
        hydrasearch (Union[Unset, GetCampaignCollectionResponse200Hydrasearch]):
    """

    hydramember: List["CampaignJsonldCampaignRead"]
    hydratotal_items: Union[Unset, int] = UNSET
    hydraview: Union[Unset, "GetCampaignCollectionResponse200Hydraview"] = UNSET
    hydrasearch: Union[Unset, "GetCampaignCollectionResponse200Hydrasearch"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hydramember = []
        for hydramember_item_data in self.hydramember:
            hydramember_item = hydramember_item_data.to_dict()

            hydramember.append(hydramember_item)

        hydratotal_items = self.hydratotal_items
        hydraview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hydraview, Unset):
            hydraview = self.hydraview.to_dict()

        hydrasearch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hydrasearch, Unset):
            hydrasearch = self.hydrasearch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hydra:member": hydramember,
            }
        )
        if hydratotal_items is not UNSET:
            field_dict["hydra:totalItems"] = hydratotal_items
        if hydraview is not UNSET:
            field_dict["hydra:view"] = hydraview
        if hydrasearch is not UNSET:
            field_dict["hydra:search"] = hydrasearch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.campaign_jsonld_campaign_read import CampaignJsonldCampaignRead
        from ..models.get_campaign_collection_response_200_hydrasearch import (
            GetCampaignCollectionResponse200Hydrasearch,
        )
        from ..models.get_campaign_collection_response_200_hydraview import GetCampaignCollectionResponse200Hydraview

        d = src_dict.copy()
        hydramember = []
        _hydramember = d.pop("hydra:member")
        for hydramember_item_data in _hydramember:
            hydramember_item = CampaignJsonldCampaignRead.from_dict(hydramember_item_data)

            hydramember.append(hydramember_item)

        hydratotal_items = d.pop("hydra:totalItems", UNSET)

        _hydraview = d.pop("hydra:view", UNSET)
        hydraview: Union[Unset, GetCampaignCollectionResponse200Hydraview]
        if isinstance(_hydraview, Unset):
            hydraview = UNSET
        else:
            hydraview = GetCampaignCollectionResponse200Hydraview.from_dict(_hydraview)

        _hydrasearch = d.pop("hydra:search", UNSET)
        hydrasearch: Union[Unset, GetCampaignCollectionResponse200Hydrasearch]
        if isinstance(_hydrasearch, Unset):
            hydrasearch = UNSET
        else:
            hydrasearch = GetCampaignCollectionResponse200Hydrasearch.from_dict(_hydrasearch)

        get_campaign_collection_response_200 = cls(
            hydramember=hydramember,
            hydratotal_items=hydratotal_items,
            hydraview=hydraview,
            hydrasearch=hydrasearch,
        )

        get_campaign_collection_response_200.additional_properties = d
        return get_campaign_collection_response_200

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
