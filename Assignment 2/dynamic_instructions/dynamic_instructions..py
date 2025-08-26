from agents import RunContextWrapper


HOTELS_DATA = {
    "Pearl Continental Karachi": {
        "location": "Karachi, Sindh, Pakistan",
        "rooms": "Luxury, Deluxe, and Executive suites available",
        "contact": "+92-21-111-505-505",
        "amenities": "Free WiFi, Pool, Gym, Spa, Business Center, Airport Shuttle",
        "check_in": "2:00 PM",
        "check_out": "12:00 PM",
        "dining": "Continental Buffet, Pakistani Cuisine, Rooftop BBQ",
        "price_range": "PKR 18,000 - PKR 45,000 per night"
    },
    "Serena Hotel Islamabad": {
        "location": "Islamabad, Pakistan",
        "rooms": "Standard, Executive, and Presidential suites available",
        "contact": "+92-51-111-133-133",
        "amenities": "Free WiFi, Pool, Gym, Spa, Conference Halls, Airport Shuttle",
        "check_in": "3:00 PM",
        "check_out": "12:00 PM",
        "dining": "Pakistani Cuisine, Continental Buffet, Italian Restaurant",
        "price_range": "PKR 20,000 - PKR 60,000 per night"
    },
    "Mövenpick Hotel Karachi": {
        "location": "Karachi, Sindh, Pakistan",
        "rooms": "Deluxe, Superior, and Royal suites available",
        "contact": "+92-21-3563-3333",
        "amenities": "Free WiFi, Pool, Gym, Spa, Banquet Halls, Airport Shuttle",
        "check_in": "2:00 PM",
        "check_out": "12:00 PM",
        "dining": "Pakistani Cuisine, Continental Buffet, Seafood Specialties",
        "price_range": "PKR 17,000 - PKR 50,000 per night"
    },
    "Avari Lahore": {
        "location": "Lahore, Punjab, Pakistan",
        "rooms": "Standard, Executive, and Luxury suites available",
        "contact": "+92-42-3636-6366",
        "amenities": "Free WiFi, Pool, Gym, Spa, Tennis Court, Airport Shuttle",
        "check_in": "2:00 PM",
        "check_out": "12:00 PM",
        "dining": "Continental Buffet, Pakistani Cuisine, Chinese Restaurant",
        "price_range": "PKR 15,000 - PKR 40,000 per night"
    },
    "Ramada Plaza Karachi": {
        "location": "Karachi, Sindh, Pakistan",
        "rooms": "Deluxe, Superior, and Executive suites available",
        "contact": "+92-21-9924-6666",
        "amenities": "Free WiFi, Pool, Gym, Spa, Airport Shuttle, Business Center",
        "check_in": "3:00 PM",
        "check_out": "12:00 PM",
        "dining": "Pakistani Cuisine, Continental Buffet, BBQ Terrace",
        "price_range": "PKR 14,000 - PKR 30,000 per night"
    },
    "Hotel One Murree": {
        "location": "Murree, Punjab, Pakistan",
        "rooms": "Standard and Family rooms available",
        "contact": "+92-51-677-400",
        "amenities": "Free WiFi, Parking, Room Service",
        "check_in": "1:00 PM",
        "check_out": "12:00 PM",
        "dining": "Pakistani Cuisine, Continental Breakfast",
        "price_range": "PKR 7,000 - PKR 19,000 per night"
    },
    "Shangrila Resort Skardu": {
        "location": "Skardu, Gilgit-Baltistan, Pakistan",
        "rooms": "Lake-view Cottages, Deluxe Rooms",
        "contact": "+92-5678-678-345",
        "amenities": "Free WiFi, Lake View, Gardens, Room Service",
        "check_in": "2:00 PM",
        "check_out": "11:00 AM",
        "dining": "Pakistani Cuisine, Continental Buffet, BBQ by the Lake",
        "price_range": "PKR 10,000 - PKR 23,000 per night"
    },
    "Beach Luxury Hotel Karachi": {
        "location": "Karachi, Sindh, Pakistan",
        "rooms": "Standard, Deluxe, and Suite rooms available",
        "contact": "+92-21-566-2788",
        "amenities": "Free WiFi, Sea View, Pool, Garden Dining",
        "check_in": "1:00 PM",
        "check_out": "11:00 PM",
        "dining": "Seafood Specialties, Pakistani Cuisine, Continental Buffet",
        "price_range": "PKR 8,000 - PKR 20,000 per night"
    }
}

def hotel_dynamic_instructions(context:RunContextWrapper, agent) -> str:
    """Generate dynamic instructions for the agent based on the hotel name in context."""
    hotel_name = context.context.get("hotel_name")
    
    if not hotel_name or hotel_name not in HOTELS_DATA:
        return "Ask the user for the hotel name before providing details."

    hotel_info = HOTELS_DATA[hotel_name]

    details = "\n".join([
        f"Location: {hotel_info['location']}",
        f"Rooms: {hotel_info['rooms']}",
        f"Contact: {hotel_info['contact']}",
        f"Amenities: {hotel_info['amenities']}",
        f"Check-in Time: {hotel_info['check_in']}",
        f"Check-out Time: {hotel_info['check_out']}",
        f"Dining: {hotel_info['dining']}",
        f"Price Range: {hotel_info['price_range']}"
    ])

    return (
        f"You are a hotel customer care assistant for {hotel_name}.\n"
        f"Here is the hotel information:\n{details}\n"
        "Always provide accurate and friendly responses to customer questions."
    )