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
    image_url = CharField(null=True)
    price = DoubleField()
    is_on_sale = BooleanField(default=False)
    sale_price = DoubleField(null=True)
    type_of_makeup = CharField(null=True)
    brand = CharField(null=True)

    @classmethod
    def prepopulate(cls):  # pragma: nocover
        products = [
            DatabaseProducts(
                id=1,
                name="Christian Louboutin 2 Brushes Face Set",
                description="Rounded and angled premium face brushes",
                price=82.99,
                is_on_sale=False,
                type_of_makeup="brushes",
                brand="Christian Louboutin",
                sale_price=80.99,
                image_url="https://us.christianlouboutin.com/media/catalog/product/cache/e1b9885bd1bf6beec4564faa4f1294da/8/4/8435415060196-8435415060196-main_image-ecommerce-christianlouboutin-facebrushes-8220014_m024_1_1200x1200.jpg"

            ),
            DatabaseProducts(
                id=2,
                name="Tom Ford Eye Color Quad",
                description="Quartet of multi-finish eyeshadows",
                price=99.99,
                is_on_sale=True,
                type_of_makeup="eyeshadow",
                brand="Tom Ford",
                sale_price=92.99,
                image_url="https://sdcdn.io/tf/tf_sku_T1EL04_2000x2000_0.png?height=700px&options=BackgroundColor%3DF2F2F2&width=700px"
            ),
            DatabaseProducts(
                id=3,
                name="E.L.F Cosmetics SRSLY Satin Lipstick - Pepper",
                description="Moisturizing lipstick that delivers smooth, buildable color and a satin finish",
                price=12.99,
                type_of_makeup="lipstick",
                brand="ELF Cosmetics",
                is_on_sale=False,
                sale_price=8.99,
                image_url="https://www.elfcosmetics.com/dw/image/v2/BBXC_PRD/on/demandware.static/-/Sites-elf-master/default/dw9fac88e9/2020/LPSTK_29696_OpenA_R.jpg?sfrm=png&sw=780&q=90"
            ),
            DatabaseProducts(
                id=4,
                name="E.L.F Cosmetics SRSLY Satin Lipstick - Sugarplum",
                description="Moisturizing lipstick that delivers smooth, buildable color and a satin finish",
                price=12.99,
                type_of_makeup="lipstick",
                brand="ELF Cosmetics",
                is_on_sale=False,
                sale_price=8.99,
                image_url="https://www.elfcosmetics.com/dw/image/v2/BBXC_PRD/on/demandware.static/-/Sites-elf-master/default/dw3eff8991/2020/LPSTK_29691_OpenA_R.jpg?sfrm=png&sw=780&q=90"
            ),
            DatabaseProducts(
                id=5,
                name="E.L.F Cosmetics Precise Blending Brush",
                description="Small, tapered makeup brush designed for precise and targeted eyeshadow application and blending",
                price=4.99,
                type_of_makeup="brushes",
                brand="ELF Cosmetics",
                is_on_sale=False,
                sale_price=3.99,
                image_url="https://www.elfcosmetics.com/dw/image/v2/BBXC_PRD/on/demandware.static/-/Sites-elf-master/default/dwcc567c59/2023/PreciseBlendingBrush/81284_OPENA_R.jpg?sfrm=png&sw=780&q=90"
            ),
            DatabaseProducts(
                id=6,
                name="Rare Beauty Soft Pinch Liquid Blush - Nude Mauve",
                description="Weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush",
                price=26.99,
                type_of_makeup="blush",
                brand="Rare Beauty",
                is_on_sale=True,
                sale_price=23.99,
                image_url="https://www.rarebeauty.com/cdn/shop/products/pdp-sku-Liquid-Blush-Dewy-Hope.jpg?v=1645133400"
            ),
            DatabaseProducts(
                id=7,
                name="Rare Beauty Soft Pinch Liquid Blush - True Red",
                description="Weightless, long-lasting liquid blush that blends and builds beautifully for a soft, healthy flush",
                price=26.99,
                type_of_makeup="blush",
                brand="Rare Beauty",
                is_on_sale=False,
                sale_price=23.99,
                image_url="https://cdn.shopify.com/s/files/1/0314/1143/7703/products/Liquid-Blush-Dewy-GRATEFUL-SKU.jpg?v=1645133400"
            ),
            DatabaseProducts(
                id=8,
                name="Rare Beauty Perfect Strokes Longwear Gel Eyeliner",
                description="Easy-glide, waterproof gel pencil that stays put all day",
                price=20.99,
                type_of_makeup="blush",
                brand="Rare Beauty",
                is_on_sale=False,
                sale_price=18.99,
                image_url="https://www.rarebeauty.com/cdn/shop/files/perfect-strokes-gel-liner-true-black-1440x1952.jpg?v=1687367688"
            ),
            DatabaseProducts(
                id=9,
                name="Rare Beauty Soft Pinch Luminous Powder Blush - Light Warm Pink",
                description="Radiant blush that lights up all skin tones with airy, seamless, and silky color",
                price=26.99,
                type_of_makeup="blush",
                brand="Rare Beauty",
                is_on_sale=False,
                sale_price=23.99,
                image_url="https://www.rarebeauty.com/cdn/shop/files/ECOMM-SOFT-PINCH-LUMINOUS-POWDER-BLUSH-CHEER.jpg?v=1710549028"
            ),
            DatabaseProducts(
                id=10,
                name="Estee Lauder Double Wear Zero-Smudge Lengthening Mascara",
                description="15-hour staying power with long lashes that last and zero smudge",
                price=39.99,
                type_of_makeup="mascara",
                brand="Estee Lauder",
                is_on_sale=False,
                sale_price=34.99,
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_9LL701_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=11,
                name="Estee Lauder Sumptuous Extreme Waterproof Lash Multiplying Volume Mascara",
                description="Outrageous volume, now in waterproof",
                price=39.99,
                type_of_makeup="mascara",
                brand="Estee Lauder",
                is_on_sale=True,
                sale_price=34.99,
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_Y9L201_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=12,
                name="Estee Lauder Pure Color Dewy Lip Color",
                description="Medium coverage in just one swipe",
                price=37.99,
                type_of_makeup="lipstick",
                brand="Estee Lauder",
                is_on_sale=False,
                sale_price=34.99,
                image_url="https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_G4DJ01_640x640_0.jpg"
            ),
            DatabaseProducts(
                id=13,
                name="Too Faced Natural Eyes Eye Shadow Palette",
                description="9 creamy comfortable matte, pearl sparkle shadows",
                price=54.99,
                type_of_makeup="eyeshadow",
                brand="Too Faced",
                is_on_sale=True,
                sale_price=51.99,
                image_url="https://www.toofaced.com/media/export/cms/products/1000x1000/2f_sku_94047_1000x1000_0.jpg"
            ),
            DatabaseProducts(
                id=14,
                name="Too Faced Natural Eyes Eye Shadow Palette",
                description="9 creamy comfortable matte, pearl sparkle shadows",
                price=54.99,
                type_of_makeup="eyeshadow",
                brand="Too Faced",
                is_on_sale=True,
                sale_price=51.99,
                image_url="https://www.toofaced.com/media/export/cms/products/1000x1000/2f_sku_94047_1000x1000_0.jpg"
            ),
            DatabaseProducts(
                id=15,
                name="NYX Epic Ink Waterproof Liquid Eyeliner",
                description="Featuring a slender and supple brush tip, this intensely pigmented, waterproof liquid eyeliner pen is perfect for drawing on precise, seamless lines",
                price=12.99,
                type_of_makeup="eyeliner",
                brand="NYX",
                is_on_sale=True,
                sale_price=10.99,
                image_url="https://www.nyxcosmetics.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-cpd-nyxusa-master-catalog/default/dwac79ee6e/ProductImages/2023/EYES/NYX_409/NYX-DTC-Makeup-Eye-Eyeliner-EPIC-INK-LINER-ALLURE_PACKSHOTS-BLACK-1505.jpg?sw=860&sh=860&sm=cut&sfrm=jpg&q=70"
            ),
            DatabaseProducts(
                id=16,
                name="NYX Epic Wear Waterproof Eyeliner Stick",
                description="High-impact, waterproof eyeliner pencil",
                price=12.99,
                type_of_makeup="eyeliner",
                brand="NYX",
                is_on_sale=False,
                sale_price=10.99,
                image_url="https://www.nyxcosmetics.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-cpd-nyxusa-master-catalog/default/dwab133b5f/ProductImages/2020/Eyes/Epic_Wear_Liner_Sticks/NYX-PMU-Makeup-Eye-EPIC-WEAR-LINER-STICKS-Eyeliner-Turquoise-Storm-EWLS11-000-0800897207533-SoldierSwatch.jpg?sw=680&sh=680&sm=cut&sfrm=jpg&q=70"
            ),
            DatabaseProducts(
                id=17,
                name="Dior Rouge Dior Lipstick",
                description="Couture color lipstick with velvet and satin lipstick finishes",
                price=64.99,
                type_of_makeup="lipstick",
                brand="Dior",
                is_on_sale=True,
                sale_price=59.99,
                image_url="https://www.dior.com/dw/image/v2/BGXS_PRD/on/demandware.static/-/Sites-master_dior/default/dw39214b65/Y0356009/Y0356009_C035500386_E01_GHC.jpg?sw=800"
            ),
            DatabaseProducts(
                id=18,
                name="Dior Rouge Dior Lipstick",
                description="Couture color lipstick with velvet and satin lipstick finishes",
                price=64.99,
                type_of_makeup="lipstick",
                brand="Dior",
                is_on_sale=True,
                sale_price=59.99,
                image_url="https://www.dior.com/dw/image/v2/BGXS_PRD/on/demandware.static/-/Sites-master_dior/default/dw39214b65/Y0356009/Y0356009_C035500386_E01_GHC.jpg?sw=800"
            ),
            DatabaseProducts(
                id=19,
                name="Dior Addict Dior Lipstick",
                description="Hydrating shine lipstick with 90% natural-origin ingredients",
                price=50.99,
                type_of_makeup="lipstick",
                brand="Dior",
                is_on_sale=False,
                sale_price=49.99,
                image_url="https://www.dior.com/dw/image/v2/BGXS_PRD/on/demandware.static/-/Sites-master_dior/default/dwa130b0a8/Y0291000/Y0291000_C029100362_E01_GHC.jpg?sw=800"
            ),
            DatabaseProducts(
                id=20,
                name="Bare Minerals Epic Wear Waterproof Eyeliner Stick",
                description="Lightweight, creamy primer prevents aging and provides mineral-based SPF protection.",
                price=32.99,
                type_of_makeup="primer",
                brand="bare minerals",
                is_on_sale=False,
                sale_price=31.99,
                image_url="https://www.bareminerals.com/cdn/shop/files/BM_SP23_Site_CLP_Primer_compare2_cc7d956b-727a-410f-9fae-a0fbe402d6da.png?v=1682016513&width=1426"
            ),
            DatabaseProducts(
                id=21,
                name="Clinique Cheek Pop Powder Blush",
                description="A burst of color, buildable and bright powder blush",
                price=32.99,
                type_of_makeup="blush",
                brand="Clinique",
                is_on_sale=False,
                sale_price=30.99,
                image_url="https://www.clinique.com/media/export/cms/products/1200x1500/cl_sku_V17517_1200x1500_0.png"
            ),
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
elif os.environ.get("API_CLEAR_DB", True) in [
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
