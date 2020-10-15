from ff6 import counts, offsets, sizes

from ff6.data import *
from ff6.struct import *

Shops = (
    ArrayField(
        name='shops',
        offset=offsets.ShopData,
        count=counts.Shops,
        element_size=sizes.ShopData,
        element_field=StructField(
            name='shop',
            offset=0,
            fields=(
                Enum4HighField('properties', ShopProperties, 0),
                Enum4LowField('type', ShopType, 0),
                U8Field('item1', 1),
                U8Field('item2', 2),
                U8Field('item3', 3),
                U8Field('item4', 4),
                U8Field('item5', 5),
                U8Field('item6', 6),
                U8Field('item7', 7),
                U8Field('item8', 8),
            )
        )
    ),
)
