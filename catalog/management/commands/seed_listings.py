from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from catalog.models import Listing, ListingImage, ListingVideo

# Sibling of shop-backend/ — where shop/public/images/houses/*.jpg already live.
FRONTEND_IMAGES_DIR = Path(__file__).resolve().parents[4] / "shop" / "public" / "images" / "houses"

SAMPLE_VIDEO_URL = "https://www.w3schools.com/html/mov_bbb.mp4"

HOUSES = [
    {
        "title": "5-Bedroom Estate House, Trasacco Valley",
        "price": 2800000,
        "image": "estate-row-white-green.jpg",
        "location": "Trasacco Valley, Accra",
        "beds": 5,
        "baths": 5,
        "sqft": 3400,
        "description": "Detached house in a secure, landscaped estate with green-roofed twin gables, private parking, and 24/7 estate security.",
        "seller_name": "Nana Yaw Estates",
    },
    {
        "title": "4-Bedroom House with Boys' Quarters, Airport Residential",
        "price": 2200000,
        "image": "peach-arched-duplex.jpg",
        "location": "Airport Residential Area, Accra",
        "beds": 4,
        "baths": 4,
        "sqft": 3000,
        "description": "Two-storey house with a grand columned entrance, private balcony, and a separate boys' quarters annex. Paved compound with space for multiple cars.",
        "seller_name": "Efua Mensah Homes",
    },
    {
        "title": "5-Bedroom House with Garage, Adenta",
        "price": 1600000,
        "image": "yellow-arched-duplex.jpg",
        "location": "Adenta, Accra",
        "beds": 5,
        "baths": 4,
        "sqft": 2900,
        "description": "Striking two-storey home with an arched portico, private balcony, and an attached garage. Walled compound with block paving throughout.",
        "seller_name": "Osei Family Realty",
    },
    {
        "title": "3-Bedroom Bungalow (Off-Plan), Kasoa",
        "price": 650000,
        "image": "yellow-blue-bungalow-render.jpg",
        "location": "Kasoa, Central Region",
        "beds": 3,
        "baths": 2,
        "sqft": 1500,
        "description": "Off-plan bungalow available for early booking — image shown is an architect's render of the finished design. Arched porch, fitted kitchen, and fenced yard on completion.",
        "seller_name": "Akosua Properties Ghana",
    },
    {
        "title": "3-Bedroom Bungalow, Ashongman Estates",
        "price": 720000,
        "image": "orange-white-bungalow.jpg",
        "location": "Ashongman Estates, Accra",
        "beds": 3,
        "baths": 2,
        "sqft": 1600,
        "description": "Single-storey family home with a stone-accented facade, fitted kitchen, and a walled, gated compound with young trees and a small lawn.",
        "seller_name": "Kojo Antwi Realty",
    },
    {
        "title": "4-Bedroom Bungalow, Sakumono",
        "price": 980000,
        "image": "navy-blue-bungalow.jpg",
        "location": "Sakumono, Accra",
        "beds": 4,
        "baths": 3,
        "sqft": 2000,
        "description": "Spacious single-storey house with a covered side patio and a wide paved compound — plenty of room for parking and entertaining.",
        "seller_name": "Abena Realty Group",
    },
    {
        "title": "4-Bedroom Modern Townhouse, Cantonments",
        "price": 2500000,
        "image": "modern-bw-duplex-small.jpg",
        "location": "Cantonments, Accra",
        "beds": 4,
        "baths": 4,
        "sqft": 2800,
        "description": "Minimalist black-and-white townhouse with a private balcony and covered parking, in one of Accra's most sought-after neighbourhoods.",
        "seller_name": "Adjoa Homes",
    },
    {
        "title": "4-Bedroom Detached House, Dzorwulu",
        "price": 3200000,
        "image": "white-cottage-house.jpg",
        "location": "Dzorwulu, Accra",
        "beds": 4,
        "baths": 3,
        "sqft": 3100,
        "description": "Beautifully landscaped detached home with a stone walkway, statement gables, and a private home office — a quiet retreat close to the city centre.",
        "seller_name": "Yaw Darko Properties",
    },
    {
        "title": "3-Bedroom Townhouse (Off-Plan), Spintex",
        "price": 950000,
        "image": "modern-bw-duplex.jpg",
        "location": "Spintex Road, Accra",
        "beds": 3,
        "baths": 3,
        "sqft": 1900,
        "description": "Off-plan minimalist townhouse available for early booking — image shown is an architect's render. Clean lines, large windows, and a private carport on completion.",
        "seller_name": "Comfort Properties Ghana",
    },
    {
        "title": "5-Bedroom House, East Legon Hills",
        "price": 2000000,
        "image": "cream-red-roof-house.jpg",
        "location": "East Legon Hills, Accra",
        "beds": 5,
        "baths": 5,
        "sqft": 3200,
        "description": "Warm, cream-toned two-storey house with a red roof and private balcony, on a gated street with mature landscaping.",
        "seller_name": "Ama Serwaa Properties",
    },
    {
        "title": "4-Bedroom Contemporary House, Airport Hills",
        "price": 3500000,
        "image": "contemporary-grey-house.jpg",
        "location": "Airport Hills, Accra",
        "beds": 4,
        "baths": 4,
        "sqft": 3400,
        "description": "Striking contemporary build with floor-to-ceiling windows, an attached garage, and a wide paved driveway — one of Accra's newest premium developments.",
        "seller_name": "Kwame Boateng Realty",
    },
]

GADGETS = [
    {
        "title": "Smart LED Bulb (4-Pack)",
        "price": 320,
        "images": [
            "https://images.pexels.com/photos/22610370/pexels-photo-22610370.jpeg?auto=compress&cs=tinysrgb&w=1200",
            "https://images.pexels.com/photos/577514/pexels-photo-577514.jpeg?auto=compress&cs=tinysrgb&w=1200",
        ],
        "brand": "BrightHome",
        "rating": 4.6,
        "review_count": 214,
        "in_stock": True,
        "description": "Wi-Fi enabled colour-changing LED bulbs that work with voice assistants — no hub required. Runs fine on Ghana's 220–240V mains supply.",
        "seller_name": "BrightHome Ghana",
    },
    {
        "title": "Smart Plug with Energy Monitor",
        "price": 180,
        "images": [
            "https://images.pexels.com/photos/4148576/pexels-photo-4148576.jpeg?auto=compress&cs=tinysrgb&w=1200",
            "https://images.pexels.com/photos/28117696/pexels-photo-28117696.jpeg?auto=compress&cs=tinysrgb&w=1200",
        ],
        "brand": "VoltEdge",
        "rating": 4.3,
        "review_count": 98,
        "in_stock": True,
        "description": "Control any appliance remotely and track power usage in real time — handy for keeping an eye on your ECG bill.",
        "seller_name": "VoltEdge Electricals",
    },
    {
        "title": "Portable Power Bank 20,000mAh",
        "price": 420,
        "images": [
            "https://images.pexels.com/photos/10104318/pexels-photo-10104318.jpeg?auto=compress&cs=tinysrgb&w=1200",
        ],
        "brand": "ChargeUp",
        "rating": 4.8,
        "review_count": 341,
        "in_stock": False,
        "description": "Fast-charging power bank with dual USB-C ports — a reliable backup for dumsor days, with enough capacity for multiple full phone charges.",
        "seller_name": "ChargeUp Ghana",
    },
]


class Command(BaseCommand):
    help = "Seed the database with the original placeholder houses and gadgets."

    def handle(self, *args, **options):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Listings already exist — skipping seed."))
            return

        for house in HOUSES:
            listing = Listing.objects.create(
                category=Listing.Category.HOUSE,
                title=house["title"],
                price=house["price"],
                description=house["description"],
                seller_name=house["seller_name"],
                location=house["location"],
                beds=house["beds"],
                baths=house["baths"],
                sqft=house["sqft"],
            )

            image_path = FRONTEND_IMAGES_DIR / house["image"]
            if image_path.exists():
                with open(image_path, "rb") as f:
                    ListingImage.objects.create(
                        listing=listing,
                        image=File(f, name=house["image"]),
                        order=0,
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Image not found, skipping: {image_path}")
                )

            ListingVideo.objects.create(listing=listing, video_url=SAMPLE_VIDEO_URL, order=0)

        for gadget in GADGETS:
            listing = Listing.objects.create(
                category=Listing.Category.GADGET,
                title=gadget["title"],
                price=gadget["price"],
                description=gadget["description"],
                seller_name=gadget["seller_name"],
                brand=gadget["brand"],
                rating=gadget["rating"],
                review_count=gadget["review_count"],
                in_stock=gadget["in_stock"],
            )
            for index, url in enumerate(gadget["images"]):
                ListingImage.objects.create(listing=listing, url=url, order=index)

        self.stdout.write(
            self.style.SUCCESS(f"Seeded {len(HOUSES)} houses and {len(GADGETS)} gadgets.")
        )
