from typing import List, Optional, TYPE_CHECKING
from pydantic.dataclasses import dataclass
from pydantic import validate_arguments
from pydantic import Field, BaseModel


if TYPE_CHECKING:
    from dataclasses import dataclass as _basemodel_decorator
else:
    def _basemodel_decorator(x): return x

@_basemodel_decorator
class Location(BaseModel):
    latitude:  Optional[float]
    longitude:  Optional[float]

    def __post_init__(self):
        if self.latitude > -90 and self.latitude < 90:
            raise ValueError("The range of latitude must be between (-90,90)")
        if self.longitude > -180 and self.longitude < 180:
            raise ValueError("The range of longitude must be between (-90,90)")

@_basemodel_decorator
class Address(Location):
    COUNTRY_CODES = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "KH", "CM", "CA", "CV", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI", "HR", "CU", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "AN", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "SH", "KN", "LC", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "CS", "SC", "SL", "SG", "SK", "SI", "SB", "SO", "ZA", "GS", "ES", "LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW", "af", "ax", "al", "dz", "as", "ad", "ao", "ai", "aq", "ag", "ar", "am", "aw", "au", "at", "az", "bs", "bh", "bd", "bb", "by", "be", "bz", "bj", "bm", "bt", "bo", "ba", "bw", "bv", "br", "io", "bn", "bg", "bf", "bi", "kh", "cm", "ca", "cv", "ky", "cf", "td", "cl", "cn", "cx", "cc", "co", "km", "cg", "cd", "ck", "cr", "ci", "hr", "cu", "cy", "cz", "dk", "dj", "dm", "do", "ec", "eg", "sv", "gq", "er", "ee", "et", "fk", "fo", "fj", "fi", "fr", "gf", "pf", "tf", "ga", "gm", "ge", "de", "gh", "gi", "gr", "gl", "gd", "gp", "gu", "gt", "gg", "gn", "gw", "gy", "ht", "hm", "va", "hn", "hk", "hu", "is", "in", "id", "ir", "iq", "ie", "im", "il", "it", "jm", "jp", "je", "jo", "kz", "ke", "ki", "kp", "kr", "kw", "kg", "la", "lv", "lb", "ls", "lr", "ly", "li", "lt", "lu", "mo", "mk", "mg", "mw", "my", "mv", "ml", "mt", "mh", "mq", "mr", "mu", "yt", "mx", "fm", "md", "mc", "mn", "ms", "ma", "mz", "mm", "na", "nr", "np", "nl", "an", "nc", "nz", "ni", "ne", "ng", "nu", "nf", "mp", "no", "om", "pk", "pw", "ps", "pa", "pg", "py", "pe", "ph", "pn", "pl", "pt", "pr", "qa", "re", "ro", "ru", "rw", "sh", "kn", "lc", "pm", "vc", "ws", "sm", "st", "sa", "sn", "cs", "sc", "sl", "sg", "sk", "si", "sb", "so", "za", "gs", "es", "lk", "sd", "sr", "sj", "sz", "se", "ch", "sy", "tw", "tj", "tz", "th", "tl", "tg", "tk", "to", "tt", "tn", "tr", "tm", "tc", "tv", "ug", "ua", "ae", "gb", "us", "um", "uy", "uz", "vu", "ve", "vn", "vg", "vi", "wf", "eh", "ye", "zm", "zw"]
    name:  Optional[str]
    local_name:  Optional[str]
    country_code:  Optional[str]
    address:  Optional[str]
    street_address:  Optional[str]
    postal_code:  Optional[str]
    city:  Optional[str]
    area:  Optional[str]
    address_local:  Optional[str]
    location_detail:  Optional[str]
    transportation_direction:  Optional[str]

    def __post_init__(self):
        if self. country_code and self.country_code not in self.COUNTRY_CODES:
            raise ValueError("Invalid Country")

@_basemodel_decorator
class Order(Location):
    distance: Optional[int]
    delivery_fee: Optional[str]
    delivery_time:  Optional[str]

@_basemodel_decorator
class RestaurantAdditional(BaseModel):
    contact_person_name:  Optional[str]
    commission_per_order:  Optional[str]
    total_order:  Optional[int]
    promotion:  Optional[str]
    phone_number_secondary:  Optional[str]
    vendor_type:  Optional[str]
    halal:  Optional[bool]
    no_of_seats:  Optional[int]
    price_per_pax:  Optional[float]
    price_per_pax_symbol:  Optional[int]
    custom_score:  Optional[str]
    payment_method:  Optional[str]
    shop_holidays:  Optional[str]
    private_dining_rooms:  Optional[str]
    private_use:  Optional[str]
    facilities:  Optional[List[str]] = []
    dining_type:  Optional[str]
    unmapped: Optional[str]

@_basemodel_decorator
class Restaurant(Address, RestaurantAdditional):
    timestamp: Optional[str]
    restaurant_id:  Optional[str]
    source: Optional[str]
    url:  Optional[str]   # The url of the rival
    website:  Optional[str]   # website of the restaurant
    # url link to the restaurant's page on rival
    restaurant_url:  Optional[str]
    name_with_branch:  Optional[str]
    restaurant_description:  Optional[str]
    chain:  Optional[str]
    opening_hours:  Optional[List[str]] = []
    cuisine_type: Optional[List[str]] = []
    phone_number:  Optional[str]
    rating:  Optional[str]
    number_of_reviews:  Optional[str]
    order_location:  Optional[List[Order]] = []
    newly_added:  Optional[bool]
    allergy_notes:  Optional[str]
    currency:  Optional[str]
    fulfillment_methods:  Optional[List[str]] = []
    menu_url:  Optional[str]
    open:  Optional[bool]
    live_at:  Optional[str]
    restaurant_email:  Optional[str]
    rank:  Optional[str]
    is_free_delivery:  Optional[bool]
    minimum_order_price:  Optional[float]
    image_url:  Optional[str]
    pickup_enabled:  Optional[bool]
    menu_info:  Optional[str]
    
    def dict(self):
        return super().dict(exclude={'COUNTRY_CODES'})
        