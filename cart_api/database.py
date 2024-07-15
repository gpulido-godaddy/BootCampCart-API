__author__ = "Andrew Williamson <axwilliamson@godaddy.com>"

import inspect
import os
import sys
from playhouse.postgres_ext import (
    PostgresqlDatabase,
    PostgresqlExtDatabase,
    Model,
    AutoField,
    CharField,
    DoubleField,
    BooleanField,
    IntegerField,
)

database = os.environ.get("POSTGRES_DB", "bootcamp")
user = os.environ.get("POSTGRES_USER", "bootcamp")
password = os.environ.get("POSTGRES_PASSWORD", "bootcamp")
hostname = os.environ.get("POSTGRES_HOST", "localhost")


ext_db = PostgresqlExtDatabase(database, user=user, password=password, host=hostname)


class BaseModel(Model):
    class Meta:
        database = PostgresqlDatabase(
            database, user=user, password=password, host=hostname, autorollback=True
        )


class DatabaseProducts(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    description = CharField(null=True)
    price = DoubleField()
    is_on_sale = BooleanField(default=False)
    sale_price = DoubleField(null=True)
    image_url = CharField(null=True)
    makeup_type = CharField(null=True)
    

    @classmethod
    def prepopulate(cls):  # pragma: nocover
        products = [
            DatabaseProducts(
                id=1,
                name="Christian Louboutin 2 Brushes Face Set",
                description="Rounded and angled premium face brushes",
                price=82.99,
                is_on_sale=False,
                sale_price=80.99,
                makeup_type="brushes",
                image_url="https://us.christianlouboutin.com/media/catalog/product/cache/e1b9885bd1bf6beec4564faa4f1294da/8/4/8435415060196-8435415060196-main_image-ecommerce-christianlouboutin-facebrushes-8220014_m024_1_1200x1200.jpg"
            ),
            DatabaseProducts(
                id=2,
                name="Christian Louboutin Abracadabra La Palette",
                description="Refillable 6-eyeshadow palette with buildable & highly pigmented shades",
                price=80.99,
                is_on_sale=True,
                sale_price=75.99,
                makeup_type="eyeshadow",
                image_url="https://us.christianlouboutin.com/media/catalog/product/cache/c8e9b72c512eaa31cd76a11d9f425a9e/8/4/8435415040877-8435415040877-main_image-ecommerce-christianlouboutin-rosepigallepalette-8500128_x102_1_1200x1200.jpg"
            ),
            DatabaseProducts(
                id=3,
                name="Christian Louboutin Rouge Satin Lipstick",
                description="More than satin, an ultra-silky creamy texture that offers intense colour & luminosity with the perfect glide",
                price=110.99,
                is_on_sale=False,
                sale_price=103.99,
                makeup_type="lipstick",
                image_url="https://us.christianlouboutin.com/media/catalog/product/cache/c8e9b72c512eaa31cd76a11d9f425a9e/8/4/8435415069038-8435415069038-main_image-ecommerce-christianlouboutin-boboblush-8500008_k116_1_1200x1200.jpg"
            ),
            DatabaseProducts(
                id=4,
                name="Tom Ford Eye Color Quad",
                description="Quartet of multi-finish eyeshadows",
                price=99.99,
                is_on_sale=True,
                sale_price=92.99,
                makeup_type="eyeshadow",
                image_url="https://sdcdn.io/tf/tf_sku_T1EL04_2000x2000_0.png?height=700px&options=BackgroundColor%3DF2F2F2&width=700px"
            ),
            DatabaseProducts(
                id=5,
                name="Tom Ford Shade And Illuminate Blush",
                description="A two-in-one powder cheek color with semi-matte and radiant hues",
                price=102.99,
                is_on_sale=False,
                sale_price=99.99,
                makeup_type="blush",
                image_url="https://sdcdn.io/tf/tf_sku_T9FX05_2000x2000_0.png?height=700px&options=BackgroundColor%3DF2F2F2&width=700px"
            ),
            DatabaseProducts(
                id=6,
                name="Tom Ford Shade And Illuminate Soft Radiance Primer SPF 25",
                description="A hydrating skincare-infused primer to enhance face architecture",
                price=120.99,
                is_on_sale=True,
                sale_price=118.99,
                makeup_type="primer",
                image_url="https://sdcdn.io/tf/tfb_sku_TA6101_2000x2000_0.png?height=700px&options=BackgroundColor%3DF2F2F2&width=700px"
            ),
            DatabaseProducts(
                id=7,
                name="Tom Ford Bronzer Brush 05",
                description="An all-over blending brush creates a seamless makeup look",
                price=127.99,
                is_on_sale=True,
                sale_price=124.99,
                makeup_type="brush",
                image_url="https://sdcdn.io/tf/tf_sku_T6C701_2000x2000_0.png?height=700px&options=BackgroundColor%3DF2F2F2&width=700px"
            ),
            DatabaseProducts(
                id=8,
                name="E.L.F Cosmetics SRSLY Satin Lipstick - Pepper",
                description="Moisturizing lipstick that delivers smooth, buildable color and a satin finish",
                price=12.99,
                is_on_sale=False,
                sale_price=8.99,
                makeup_type="lipstick",
                image_url="https://www.elfcosmetics.com/dw/image/v2/BBXC_PRD/on/demandware.static/-/Sites-elf-master/default/dw9fac88e9/2020/LPSTK_29696_OpenA_R.jpg?sfrm=png&sw=780&q=90"
            ),
            DatabaseProducts(
                id=9,
                name="E.L.F Cosmetics SRSLY Satin Lipstick - Sugarplum",
                description="Moisturizing lipstick that delivers smooth, buildable color and a satin finish",
                price=12.99,
                is_on_sale=False,
                sale_price=8.99,
                makeup_type="lipstick",
                image_url="https://www.elfcosmetics.com/dw/image/v2/BBXC_PRD/on/demandware.static/-/Sites-elf-master/default/dw3eff8991/2020/LPSTK_29691_OpenA_R.jpg?sfrm=png&sw=780&q=90"
            ),
            DatabaseProducts(
                id=10,
                name="E.L.F Cosmetics Precise Blending Brush",
                description="Small, tapered makeup brush designed for precise and targeted eyeshadow application and blending",
                price=4.99,
                is_on_sale=False,
                sale_price=3.99,
                makeup_type="brush",
                image_url="https://www.elfcosmetics.com/dw/image/v2/BBXC_PRD/on/demandware.static/-/Sites-elf-master/default/dwcc567c59/2023/PreciseBlendingBrush/81284_OPENA_R.jpg?sfrm=png&sw=780&q=90"
            ),
            DatabaseProducts(
                id=11,
                name="Rare Beauty Liquid Blush - Nude Mauve",
                description="Weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush",
                price=26.99,
                is_on_sale=True,
                sale_price=23.99,
                makeup_type="blush",
                image_url="https://www.rarebeauty.com/cdn/shop/products/pdp-sku-Liquid-Blush-Dewy-Hope.jpg?v=1645133400"
            ),
            DatabaseProducts(
                id=12,
                name="Rare Beauty Liquid Blush - True Red",
                description="Weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush",
                price=26.99,
                is_on_sale=False,
                sale_price=23.99,
                makeup_type="blush",
                image_url="https://cdn.shopify.com/s/files/1/0314/1143/7703/products/Liquid-Blush-Dewy-GRATEFUL-SKU.jpg?v=1645133400"
            ),
            DatabaseProducts(
                id=13,
                name="Rare Beauty Liquid Blush - Hot Pink",
                description="Weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush",
                price=26.99,
                is_on_sale=False,
                sale_price=23.99,
                makeup_type="blush",
                image_url="https://cdn.shopify.com/s/files/1/0314/1143/7703/products/Liquid-Blush-Dewy-LUCKY-SKU.jpg?v=1645133400"
            ),
            DatabaseProducts(
                id=14,
                name="Rare Beauty Liquid Blush - Muted Peach",
                description="Weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush",
                price=26.99,
                is_on_sale=True,
                sale_price=23.99,
                makeup_type="blush",
                image_url="https://cdn.shopify.com/s/files/1/0314/1143/7703/products/Liquid-Blush-Dewy-JOY-SKU.jpg?v=1645133400"
            ),
            DatabaseProducts(
                id=15,
                name="Rare Beauty Soft Pinch Luminous Powder Blush - Light Warm Pink",
                description="Radiant blush that lights up all skin tones with airy, seamless, and silky color",
                price=26.99,
                is_on_sale=False,
                sale_price=23.99,
                makeup_type="blush",
                image_url="https://www.rarebeauty.com/cdn/shop/files/ECOMM-SOFT-PINCH-LUMINOUS-POWDER-BLUSH-CHEER.jpg?v=1710549028"
            ),
            DatabaseProducts(
                id=16,
                name="Rare Beauty Perfect Strokes Longwear Gel Eyeliner",
                description="Easy-glide, waterproof gel pencil that stays put all day",
                price=20.99,
                is_on_sale=False,
                sale_price=18.99,
                makeup_type="eyeliner",
                image_url="https://www.rarebeauty.com/cdn/shop/files/perfect-strokes-gel-liner-true-black-1440x1952.jpg?v=1687367688"
            ),
            DatabaseProducts(
                id=17,
                name="Rare Beauty Stay Vulnerable Liquid Eyeshadow",
                description="Quick-and-easy eyeshadow that goes from liquid to powder in seconds",
                price=22.99,
                is_on_sale=False,
                sale_price=20.99,
                makeup_type="eyeshadow",
                image_url="https://www.rarebeauty.com/cdn/shop/products/Liquid-Eyeshadow-NearlyNeutral-SKU.jpg?v=1609891052"
            ),
            DatabaseProducts(
                id=18,
                name="Estee Lauder Pure Color Eyeshadow Quad",
                description="Luxe looks, vibrant color, and rich finishes",
                price=70.99,
                is_on_sale=True,
                sale_price=64.99,
                makeup_type="eyeshadow",
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PHHT05_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=19,
                name="Estee Lauder Double Wear Zero-Smudge Mascara",
                description="15-hour staying power with long lashes that last and zero smudge",
                price=39.99,
                is_on_sale=False,
                sale_price=34.99,
                makeup_type="mascara",
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_9LL701_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=20,
                name="Estee Lauder Waterproof Lash Multiplying Mascara",
                description="Outrageous volume, now in waterproof",
                price=39.99,
                is_on_sale=True,
                sale_price=34.99,
                makeup_type="mascara",
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_Y9L201_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=21,
                name="Estee Lauder Pure Color Dewy Lip Color",
                description="Medium coverage in just one swipe",
                price=37.99,
                is_on_sale=False,
                sale_price=34.99,
                makeup_type="lipstick",
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_G4DJ01_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=22,
                name="Too Faced Natural Eyes Eyeshadow Palette",
                description="9 creamy comfortable matte, pearl sparkle shadows",
                price=54.99,
                is_on_sale=True,
                sale_price=51.99,
                makeup_type="eyeshadow",
                image_url="https://www.toofaced.com/media/export/cms/products/1000x1000/2f_sku_94047_1000x1000_0.jpg"
            ),
            DatabaseProducts(
                id=23,
                name="Too Faced Plump & Prime Face Plumping Primer Serum",
                description="Unique serum texture for easy application under makeup",
                price=51.99,
                is_on_sale=True,
                sale_price=49.99,
                makeup_type="primer",
                image_url="https://www.toofaced.com/media/export/cms/products/1000x1000/2f_sku_118027_1000x1000_0.jpg"
            ),
            DatabaseProducts(
                id=24,
                name="Too Faced Killer Liner 36 Hour Waterproof Gel Eyeliner Pencil",
                description="Total control and 36 hour waterproof features",
                price=27.99,
                is_on_sale=False,
                sale_price=25.99,
                makeup_type="eyeliner",
                image_url="https://www.toofaced.com/media/export/cms/products/1000x1000/2f_sku_181446_1000x1000_0.jpg"
            ),
            DatabaseProducts(
                id=25,
                name="Too Faced Lady Bold Lipstick",
                description="Bold, smooth coverage and dramatic color",
                price=31.99,
                is_on_sale=True,
                sale_price=30.99,
                makeup_type="lipstick",
                image_url="https://www.toofaced.com/media/export/cms/products/1000x1000/2f_sku_181454_1000x1000_0.jpg"
            )  
        
        ]
        DatabaseProducts.bulk_create(products)


# Excercise 1:
# Define an ORM class called DatabaseCartItem which inherits from BaseModel
# and has the properties and types defined by your swagger spec.
# if neccesary, update EXAMPLE_CART_ITEM in cart_api_tests/test_exercises.py to match

class DatabaseCartItem(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    price = DoubleField()
    quantity = IntegerField()
    image_url = CharField(null=True) # getting cartItem.map function not valid

# BOOTCAMPERS: Don't modify anything below
ALL_MODELS = [
    c_type
    for c_name, c_type in inspect.getmembers(sys.modules[__name__], inspect.isclass)
    if issubclass(c_type, BaseModel) and c_type not in [BaseModel, Model]
]


def init_tables(table_models=None):  # pragma: nocover
    table_models = table_models or ALL_MODELS

    if isinstance(table_models, Model):
        table_models = [table_models]

    with ext_db.connection_context():
        print(
            f"✅ Creating tables: {', '.join(table.__name__ for table in table_models)}"
        )
        ext_db.drop_tables(table_models, cascade=True)
        ext_db.create_tables(table_models)

        if DatabaseProducts in table_models:
            print(f"✅ Populating table: {DatabaseProducts.__name__}")
            DatabaseProducts.prepopulate()


# Create any tables that don't exist
missing_tables = [table for table in ALL_MODELS if not table.table_exists()]
if missing_tables:  # pragma: nocover
    print(
        f"⚠️ Missing DB Tables: {', '.join(table.__name__ for table in missing_tables)} ⚠️"
    )
    init_tables(missing_tables)

# Else if we explicitly want the tables cleared, recreate them
elif os.environ.get("API_CLEAR_DB", False) in [
    "1",
    1,
    True,
    "true",
    "yes",
]:  # pragma: nocover
    print(
        "⛔⚠️⛔⚠️⛔⚠️⛔ API_CLEAR_DB is set to 1, we are recreating all database tables ⛔⚠️⛔⚠️⛔⚠️⛔"
    )
    init_tables()

else:
    print("The tables already exist! Let's rock and roll 🤘")