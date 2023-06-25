# Prompt Inputs
PROMPT_EXAMPLES = [
    {
        "question": """ 
                Infer demographic and psychographic qualities about the user and their spending habits based on the following transactions. 
                You are a financial advisor. Given the following transactions and their corresponding details, 
                provide personalized financial advice based on the user's financial goals, spending patterns, and current financial situation. 
                You should analyze the transactions, categorize them, identify any potential issues such as excessive spending or missed savings opportunities, and suggest actionable recommendations to improve the user's financial health. 
                Additionally, the advice should consider factors such as budgeting, saving, investing, debt management, and long-term financial planning. 
                Please provide comprehensive and user-friendly advice, considering both short-term and long-term financial goals. 
                Highlight which purchases were good financial decisions and which purchases were bad financial decisions.

                Example Transaction:
                amount: 2307.21. authorized_date: 2017-01-27. authorized_datetime: 2017-01-27T10:34:50Z. category: ['Shops', 'Computers and Electronics']. date: 2017-01-29. datetime: 2017-01-27T11:00:00Z. location: 300 Post St, San Francisco, US, 94108. merchant_name: Apple. name: Apple Store. payment_channel: in store. personal_finance_category: GENERAL_MERCHANDISE_ELECTRONICS.
                """,
        "answer": """
                Example Inference: 
                Psychographic Inferences: 
                - The buyer prioritizes quality and has enough money to afford an expensive laptop
                - The buyer is loyal to Apple since they bought from Apple
                - It is a computer or electronic from the Apple Store in San Francisco. Perhaps, it is a MacBook Pro with the M2 chip.

                Spending Habit Inferences: 
                - A laptop is a need for a student, the buyer doesn’t hesitate spending on needs. 
                - The amount is USD $2307.21. A MacBook Pro’s average life as per the internet is 7 years, so the amortized cost per month is USD$ 27.47. 

                Cost-effectiveness (out of 10)
                8
                Utility (out of 10)
                10
                Long-term benefits (out of 10)
                9
                Comparison with alternatives (out of 10)
                4
                Affordable (out of 10)
                3

                Advice:

                1. Evaluate Your Technology Needs: While investing in high-quality electronics can be beneficial, it's essential to evaluate your actual needs and consider more cost-effective alternatives. Determine whether the specific features and capabilities of expensive devices align with your usage requirements or if a more affordable option would suffice.

                2. Consider Refurbished or Older Models: Apple offers refurbished products that are tested, certified, and come with a warranty. These devices can provide a similar experience to new products at a lower cost. Additionally, exploring older models can often offer significant savings without sacrificing essential functionality.

                3. Explore Alternative Brands: While you may have a preference for Apple products, it's worth exploring alternative brands that offer similar features and quality at a lower price point. Compare different brands and read reviews to identify options that meet your requirements while being more affordable.

                4. Plan for Upgrades: When purchasing expensive electronics, consider their long-term lifespan and factor in the frequency of upgrades. By planning ahead and budgeting for future upgrades, you can better manage the financial impact of replacing devices in the future.

                5. Protect Your Investment: To ensure the longevity of your electronics, consider investing in protective cases, screen protectors, and warranties. This can help prevent accidental damage and extend the lifespan of your devices, reducing the need for frequent replacements.
                """,
    },
    {
        "question": """ 
                Infer demographic and psychographic qualities about the user and their spending habits based on the following transactions. 
                You are a financial advisor. Given the following transactions and their corresponding details, 
                provide personalized financial advice based on the user's financial goals, spending patterns, and current financial situation. 
                You should analyze the transactions, categorize them, identify any potential issues such as excessive spending or missed savings opportunities, and suggest actionable recommendations to improve the user's financial health. 
                Additionally, the advice should consider factors such as budgeting, saving, investing, debt management, and long-term financial planning. 
                Please provide comprehensive and user-friendly advice, considering both short-term and long-term financial goals. 
                Highlight which purchases were good financial decisions and which purchases were bad financial decisions.

                Example Transaction:
                amount: 2.97. authorized_date: 2023-06-17. authorized_datetime: 2023-06-17T19:30:00Z. category: ['Food and Drink', 'Fast-Food']. date: 2023-06-17. datetime: 2023-06-17T19:30:00Z. location: 1530 3rd Ave, Seattle, US, 98101. merchant_name: McDonald's. name: McDonald's. payment_channel: in store. personal_finance_category: FAST-FOOD.
                """,
        "answer": """
                Psychographic Inferences:

                The buyer prefers fast-food options and is likely to prioritize convenience and speed when it comes to meals.
                They may have a busy lifestyle or enjoy the convenience of fast-food chains like McDonald's.
                The buyer may not prioritize healthy eating or may indulge in fast food occasionally.
                Spending Habit Inferences:

                The purchase amount is $2.97, indicating that the buyer tends to make small and affordable purchases for meals.
                The transaction took place at a McDonald's in Seattle, suggesting that the buyer enjoys fast food from this particular chain.
                Cost-effectiveness (out of 10)
                5

                Utility (out of 10)
                7

                Long-term benefits (out of 10)
                2

                Comparison with alternatives (out of 10)
                6

                Affordable (out of 10)
                9

                Advice:

                1. Consider Healthy Alternatives: While indulging in fast food occasionally is acceptable, it's essential to prioritize a balanced and healthy diet. Look for healthier fast-food options or explore alternatives such as meal prepping or cooking at home to save money and make healthier choices.

                2. Create a Food Budget: To ensure your spending aligns with your financial goals, consider setting a budget specifically for dining out and fast food. By allocating a specific amount each month, you can manage your expenses and avoid overspending on fast food.

                3. Cook Meals at Home: Cooking meals at home can be a more cost-effective and healthier option compared to frequent visits to fast-food chains. Explore simple and quick recipes that suit your taste and lifestyle. It can also be a fun and rewarding way to improve your culinary skills.

                4. Plan Ahead: If you find yourself relying on fast food due to time constraints or convenience, consider planning your meals in advance. Prepare meals or snacks that are easy to grab on the go, such as pre-made salads, sandwiches, or fruit cups. This way, you can still enjoy the convenience without compromising on your health or budget.

                5. Explore Local Options: Instead of always opting for large fast-food chains, consider supporting local businesses that offer healthier alternatives. Look for cafes or restaurants that prioritize fresh ingredients, nutritious options, and sustainable practices. It can be a great way to discover new flavors while making better choices for your health and the community.
                """,
    },
]
PROMPT_PREFIX = "Infer demographic and psychographic qualities about the user and their spending habits based on the following transactions."
PROMPT_SUFFIX = """
Desired Format: 
Psychographic Inferences: -||-
Spending Habit Inferences: -||-
(High/Medium/Low) Cost-effectiveness 
(High/Medium/Low) Utility 
(High/Medium/Low) Long-term benefits
(High/Medium/Low) Comparison with alternatives 
(High/Medium/Low) Affordable
"""

# Transactions
EXAMPLE_USER_ID = "G4N4PJzLPRFlljnkg6NvTp6er4PJyPiGKK8om"
EXAMPLE_TRANSACTIONS = [
    {
        "transaction_id": "0",
        "amount": 24.99,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Restaurants"],
        "category_id": "13005000",
        "date": "2023-06-17",
        "datetime": "2023-06-17T12:15:00Z",
        "authorized_date": "2023-06-17",
        "authorized_datetime": "2023-06-17T12:15:00Z",
        "location": {
            "address": "456 Elm St",
            "city": "Anytown",
            "region": "CA",
            "postal_code": "12345",
            "country": "US",
            "lat": 37.123456,
            "lon": -122.123456,
            "store_number": "987",
        },
        "name": "Tasty Burgers",
        "merchant_name": "Tasty Burgers",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "RESTAURANTS",
            "detailed": "RESTAURANTS",
        },
    },
    {
        "transaction_id": "1",
        "amount": 19.95,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Clothing"],
        "category_id": "19012000",
        "date": "2023-06-16",
        "datetime": "2023-06-16T17:30:00Z",
        "authorized_date": "2023-06-16",
        "authorized_datetime": "2023-06-16T17:30:00Z",
        "location": {
            "address": "789 Oak St",
            "city": "Somewhere",
            "region": "NY",
            "postal_code": "54321",
            "country": "US",
            "lat": 40.987654,
            "lon": -74.987654,
            "store_number": "654",
        },
        "name": "Fashion Emporium",
        "merchant_name": "Fashion Emporium",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "APPAREL_AND_SERVICES",
            "detailed": "APPAREL_AND_ACCESSORIES",
        },
    },
    {
        "transaction_id": "1",
        "amount": 45.75,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Groceries"],
        "category_id": "13005032",
        "date": "2023-06-15",
        "datetime": "2023-06-15T09:45:00Z",
        "authorized_date": "2023-06-15",
        "authorized_datetime": "2023-06-15T09:45:00Z",
        "location": {
            "address": "123 Market St",
            "city": "Cityville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.765432,
            "lon": -121.765432,
            "store_number": "321",
        },
        "name": "Fresh Mart",
        "merchant_name": "Fresh Mart",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "GROCERIES",
            "detailed": "GROCERIES",
        },
    },
    {
        "transaction_id": "2",
        "amount": 34.99,
        "iso_currency_code": "USD",
        "category": ["Shops", "Books"],
        "category_id": "19009000",
        "date": "2023-06-14",
        "datetime": "2023-06-14T14:20:00Z",
        "authorized_date": "2023-06-14",
        "authorized_datetime": "2023-06-14T14:20:00Z",
        "location": {
            "address": "567 Main St",
            "city": "Booktown",
            "region": "TX",
            "postal_code": "67890",
            "country": "US",
            "lat": 36.543210,
            "lon": -98.543210,
            "store_number": "890",
        },
        "name": "Bookworm's Paradise",
        "merchant_name": "Bookworm's Paradise",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "GENERAL_MERCHANDISE",
            "detailed": "GENERAL_MERCHANDISE_OTHER",
        },
    },
    {
        "transaction_id": "3",
        "amount": 55.00,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Coffee Shop"],
        "category_id": "13005043",
        "date": "2023-06-13",
        "datetime": "2023-06-13T08:00:00Z",
        "authorized_date": "2023-06-13",
        "authorized_datetime": "2023-06-13T08:00:00Z",
        "location": {
            "address": "987 Elm St",
            "city": "Coffeetown",
            "region": "WA",
            "postal_code": "54321",
            "country": "US",
            "lat": 39.876543,
            "lon": -123.876543,
            "store_number": "345",
        },
        "name": "Mornings & More",
        "merchant_name": "Mornings & More",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "RESTAURANTS",
            "detailed": "COFFEE_SHOP",
        },
    },
    {
        "transaction_id": "4",
        "amount": 12.50,
        "iso_currency_code": "USD",
        "category": ["Transportation", "Ride Sharing"],
        "category_id": "18020007",
        "date": "2023-06-12",
        "datetime": "2023-06-12T15:30:00Z",
        "authorized_date": "2023-06-12",
        "authorized_datetime": "2023-06-12T15:30:00Z",
        "location": {
            "address": "789 Maple Ave",
            "city": "Riderville",
            "region": "IL",
            "postal_code": "54321",
            "country": "US",
            "lat": 38.765432,
            "lon": -89.765432,
            "store_number": "432",
        },
        "name": "QuickRide",
        "merchant_name": "QuickRide",
        "payment_channel": "mobile app",
        "personal_finance_category": {
            "primary": "TRAVEL",
            "detailed": "RIDE_SHARING",
        },
    },
    {
        "transaction_id": "5",
        "amount": 59.99,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Electronics"],
        "category_id": "19012002",
        "date": "2023-06-11",
        "datetime": "2023-06-11T11:45:00Z",
        "authorized_date": "2023-06-11",
        "authorized_datetime": "2023-06-11T11:45:00Z",
        "location": {
            "address": "456 Oak St",
            "city": "Gadgetville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 37.654321,
            "lon": -122.654321,
            "store_number": "321",
        },
        "name": "Tech Universe",
        "merchant_name": "Tech Universe",
        "payment_channel": "online",
        "personal_finance_category": {
            "primary": "GENERAL_MERCHANDISE",
            "detailed": "GENERAL_MERCHANDISE_ELECTRONICS",
        },
    },
    {
        "transaction_id": "6",
        "amount": 20.00,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Café"],
        "category_id": "13005042",
        "date": "2023-06-10",
        "datetime": "2023-06-10T09:00:00Z",
        "authorized_date": "2023-06-10",
        "authorized_datetime": "2023-06-10T09:00:00Z",
        "location": {
            "address": "123 Walnut St",
            "city": "Coffeeville",
            "region": "WA",
            "postal_code": "54321",
            "country": "US",
            "lat": 39.543210,
            "lon": -123.543210,
            "store_number": "543",
        },
        "name": "Caffeine Fix",
        "merchant_name": "Caffeine Fix",
        "payment_channel": "in store",
        "personal_finance_category": {"primary": "RESTAURANTS", "detailed": "CAFÉ"},
    },
    {
        "transaction_id": "7",
        "amount": 8.99,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Groceries"],
        "category_id": "13005032",
        "date": "2023-06-09",
        "datetime": "2023-06-09T13:30:00Z",
        "authorized_date": "2023-06-09",
        "authorized_datetime": "2023-06-09T13:30:00Z",
        "location": {
            "address": "456 Market St",
            "city": "Cityville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.876543,
            "lon": -121.876543,
            "store_number": "234",
        },
        "name": "Fresh Grocers",
        "merchant_name": "Fresh Grocers",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "GROCERIES",
            "detailed": "GROCERIES",
        },
    },
    {
        "transaction_id": "8",
        "amount": 39.95,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Home"],
        "category_id": "19012003",
        "date": "2023-06-08",
        "datetime": "2023-06-08T16:45:00Z",
        "authorized_date": "2023-06-08",
        "authorized_datetime": "2023-06-08T16:45:00Z",
        "location": {
            "address": "789 Pine St",
            "city": "Homeware City",
            "region": "NY",
            "postal_code": "54321",
            "country": "US",
            "lat": 40.654321,
            "lon": -74.654321,
            "store_number": "678",
        },
        "name": "Home Essentials",
        "merchant_name": "Home Essentials",
        "payment_channel": "in store",
        "personal_finance_category": {"primary": "HOME", "detailed": "HOME"},
    },
    {
        "transaction_id": "9",
        "amount": 5.50,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Fast Food"],
        "category_id": "13005032",
        "date": "2023-06-07",
        "datetime": "2023-06-07T12:00:00Z",
        "authorized_date": "2023-06-07",
        "authorized_datetime": "2023-06-07T12:00:00Z",
        "location": {
            "address": "123 Main St",
            "city": "BurgerTown",
            "region": "TX",
            "postal_code": "54321",
            "country": "US",
            "lat": 37.543210,
            "lon": -98.543210,
            "store_number": "456",
        },
        "name": "Quick Bites",
        "merchant_name": "Quick Bites",
        "payment_channel": "drive-thru",
        "personal_finance_category": {
            "primary": "RESTAURANTS",
            "detailed": "FAST_FOOD",
        },
    },
    {
        "transaction_id": "10",
        "amount": 29.99,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Sports"],
        "category_id": "19012008",
        "date": "2023-06-06",
        "datetime": "2023-06-06T09:15:00Z",
        "authorized_date": "2023-06-06",
        "authorized_datetime": "2023-06-06T09:15:00Z",
        "location": {
            "address": "456 Park Ave",
            "city": "Sportsville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.765432,
            "lon": -121.765432,
            "store_number": "789",
        },
        "name": "SportZone",
        "merchant_name": "SportZone",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "SPORTING_GOODS",
            "detailed": "SPORTING_GOODS",
        },
    },
    {
        "transaction_id": "11",
        "amount": 15.00,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Café"],
        "category_id": "13005042",
        "date": "2023-06-05",
        "datetime": "2023-06-05T08:30:00Z",
        "authorized_date": "2023-06-05",
        "authorized_datetime": "2023-06-05T08:30:00Z",
        "location": {
            "address": "789 Coffee St",
            "city": "Coffeetown",
            "region": "WA",
            "postal_code": "54321",
            "country": "US",
            "lat": 39.876543,
            "lon": -123.876543,
            "store_number": "987",
        },
        "name": "Morning Brew",
        "merchant_name": "Morning Brew",
        "payment_channel": "in store",
        "personal_finance_category": {"primary": "RESTAURANTS", "detailed": "CAFÉ"},
    },
    {
        "transaction_id": "12",
        "amount": 750.25,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Electronics"],
        "category_id": "19012002",
        "date": "2023-06-04",
        "datetime": "2023-06-04T10:30:00Z",
        "authorized_date": "2023-06-04",
        "authorized_datetime": "2023-06-04T10:30:00Z",
        "location": {
            "address": "123 Tech St",
            "city": "Gadgetville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 37.654321,
            "lon": -122.654321,
            "store_number": "123",
        },
        "name": "Gadget Emporium",
        "merchant_name": "Gadget Emporium",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "GENERAL_MERCHANDISE",
            "detailed": "GENERAL_MERCHANDISE_ELECTRONICS",
        },
    },
    {
        "transaction_id": "13",
        "amount": 950.80,
        "iso_currency_code": "USD",
        "category": ["Travel", "Airfare"],
        "category_id": "18001001",
        "date": "2023-06-03",
        "datetime": "2023-06-03T14:00:00Z",
        "authorized_date": "2023-06-03",
        "authorized_datetime": "2023-06-03T14:00:00Z",
        "location": {
            "address": "456 Aviation Blvd",
            "city": "Flight City",
            "region": "NY",
            "postal_code": "54321",
            "country": "US",
            "lat": 40.543210,
            "lon": -74.543210,
            "store_number": "456",
        },
        "name": "Fly High Airlines",
        "merchant_name": "Fly High Airlines",
        "payment_channel": "online",
        "personal_finance_category": {"primary": "TRAVEL", "detailed": "AIRFARE"},
    },
    {
        "transaction_id": "14",
        "amount": 670.99,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Fashion"],
        "category_id": "19012004",
        "date": "2023-06-02",
        "datetime": "2023-06-02T16:45:00Z",
        "authorized_date": "2023-06-02",
        "authorized_datetime": "2023-06-02T16:45:00Z",
        "location": {
            "address": "789 Fashion Ave",
            "city": "Styleville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.765432,
            "lon": -121.765432,
            "store_number": "789",
        },
        "name": "Fashion Boutique",
        "merchant_name": "Fashion Boutique",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "APPAREL_AND_ACCESSORIES",
            "detailed": "APPAREL_AND_ACCESSORIES",
        },
    },
    {
        "transaction_id": "16",
        "amount": 520.75,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Restaurants"],
        "category_id": "13005000",
        "date": "2023-06-01",
        "datetime": "2023-06-01T19:30:00Z",
        "authorized_date": "2023-06-01",
        "authorized_datetime": "2023-06-01T19:30:00Z",
        "location": {
            "address": "123 Gourmet St",
            "city": "Foodieville",
            "region": "TX",
            "postal_code": "54321",
            "country": "US",
            "lat": 37.876543,
            "lon": -98.876543,
            "store_number": "123",
        },
        "name": "Fine Dining Experience",
        "merchant_name": "Fine Dining Experience",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "RESTAURANTS",
            "detailed": "RESTAURANTS",
        },
    },
    {
        "transaction_id": "17",
        "amount": 22.50,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Restaurants"],
        "category_id": "13005000",
        "date": "2023-05-31",
        "datetime": "2023-05-31T12:15:00Z",
        "authorized_date": "2023-05-31",
        "authorized_datetime": "2023-05-31T12:15:00Z",
        "location": {
            "address": "456 Foodie St",
            "city": "Food Town",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.654321,
            "lon": -121.654321,
            "store_number": "456",
        },
        "name": "Casual Eats",
        "merchant_name": "Casual Eats",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "RESTAURANTS",
            "detailed": "RESTAURANTS",
        },
    },
    {
        "transaction_id": "18",
        "amount": 550.00,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Home"],
        "category_id": "19012003",
        "date": "2023-05-30",
        "datetime": "2023-05-30T16:30:00Z",
        "authorized_date": "2023-05-30",
        "authorized_datetime": "2023-05-30T16:30:00Z",
        "location": {
            "address": "789 Furniture Ave",
            "city": "Home City",
            "region": "NY",
            "postal_code": "54321",
            "country": "US",
            "lat": 40.876543,
            "lon": -74.876543,
            "store_number": "789",
        },
        "name": "Furniture World",
        "merchant_name": "Furniture World",
        "payment_channel": "in store",
        "personal_finance_category": {"primary": "HOME", "detailed": "HOME"},
    },
    {
        "transaction_id": "19",
        "amount": 9.99,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Books"],
        "category_id": "19012001",
        "date": "2023-05-29",
        "datetime": "2023-05-29T14:45:00Z",
        "authorized_date": "2023-05-29",
        "authorized_datetime": "2023-05-29T14:45:00Z",
        "location": {
            "address": "123 Bookworm St",
            "city": "Bookville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 37.543210,
            "lon": -122.543210,
            "store_number": "123",
        },
        "name": "Novel Nook",
        "merchant_name": "Novel Nook",
        "payment_channel": "online",
        "personal_finance_category": {"primary": "MEDIA", "detailed": "BOOKS"},
    },
    {
        "transaction_id": "20",
        "amount": 750.00,
        "iso_currency_code": "USD",
        "category": ["Travel", "Hotels"],
        "category_id": "18001002",
        "date": "2023-05-28",
        "datetime": "2023-05-28T09:00:00Z",
        "authorized_date": "2023-05-28",
        "authorized_datetime": "2023-05-28T09:00:00Z",
        "location": {
            "address": "456 Hospitality Dr",
            "city": "Travelville",
            "region": "FL",
            "postal_code": "54321",
            "country": "US",
            "lat": 27.876543,
            "lon": -81.876543,
            "store_number": "456",
        },
        "name": "Luxury Hotel",
        "merchant_name": "Luxury Hotel",
        "payment_channel": "online",
        "personal_finance_category": {"primary": "TRAVEL", "detailed": "HOTELS"},
    },
    {
        "transaction_id": "21",
        "amount": 120.50,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Clothing"],
        "category_id": "19012005",
        "date": "2023-05-27",
        "datetime": "2023-05-27T15:30:00Z",
        "authorized_date": "2023-05-27",
        "authorized_datetime": "2023-05-27T15:30:00Z",
        "location": {
            "address": "789 Fashion St",
            "city": "Fashion City",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.654321,
            "lon": -121.654321,
            "store_number": "789",
        },
        "name": "Fashion Haven",
        "merchant_name": "Fashion Haven",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "APPAREL_AND_ACCESSORIES",
            "detailed": "CLOTHING",
        },
    },
    {
        "transaction_id": "23",
        "amount": 80.00,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Groceries"],
        "category_id": "13005001",
        "date": "2023-05-26",
        "datetime": "2023-05-26T11:45:00Z",
        "authorized_date": "2023-05-26",
        "authorized_datetime": "2023-05-26T11:45:00Z",
        "location": {
            "address": "123 Market St",
            "city": "Groceryville",
            "region": "NY",
            "postal_code": "54321",
            "country": "US",
            "lat": 40.543210,
            "lon": -74.543210,
            "store_number": "123",
        },
        "name": "Fresh Mart",
        "merchant_name": "Fresh Mart",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "GROCERIES",
            "detailed": "GROCERIES",
        },
    },
    {
        "transaction_id": "25",
        "amount": 250.00,
        "iso_currency_code": "USD",
        "category": ["Entertainment", "Concerts"],
        "category_id": "19013001",
        "date": "2023-05-25",
        "datetime": "2023-05-25T20:00:00Z",
        "authorized_date": "2023-05-25",
        "authorized_datetime": "2023-05-25T20:00:00Z",
        "location": {
            "address": "456 Music Ave",
            "city": "Concert City",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 37.876543,
            "lon": -122.876543,
            "store_number": "456",
        },
        "name": "Rock Concert",
        "merchant_name": "Rock Concert",
        "payment_channel": "online",
        "personal_finance_category": {
            "primary": "ENTERTAINMENT",
            "detailed": "CONCERTS",
        },
    },
    {
        "transaction_id": "26",
        "amount": 40.00,
        "iso_currency_code": "USD",
        "category": ["Travel", "Transportation"],
        "category_id": "18001001",
        "date": "2023-05-24",
        "datetime": "2023-05-24T09:30:00Z",
        "authorized_date": "2023-05-24",
        "authorized_datetime": "2023-05-24T09:30:00Z",
        "location": {
            "address": "123 Transport Rd",
            "city": "Transit City",
            "region": "FL",
            "postal_code": "54321",
            "country": "US",
            "lat": 27.543210,
            "lon": -81.543210,
            "store_number": "123",
        },
        "name": "Train Ticket",
        "merchant_name": "Train Ticket",
        "payment_channel": "online",
        "personal_finance_category": {
            "primary": "TRAVEL",
            "detailed": "TRANSPORTATION",
        },
    },
]

EXAMPLE_LESS_USER_ID = "less-user-id"
EXAMPLE_LESS_TRANSACTIONS = [
    {
        "transaction_id": "0",
        "amount": 24.99,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Restaurants"],
        "category_id": "13005000",
        "date": "2023-06-17",
        "datetime": "2023-06-17T12:15:00Z",
        "authorized_date": "2023-06-17",
        "authorized_datetime": "2023-06-17T12:15:00Z",
        "location": {
            "address": "456 Elm St",
            "city": "Anytown",
            "region": "CA",
            "postal_code": "12345",
            "country": "US",
            "lat": 37.123456,
            "lon": -122.123456,
            "store_number": "987",
        },
        "name": "Tasty Burgers",
        "merchant_name": "Tasty Burgers",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "RESTAURANTS",
            "detailed": "RESTAURANTS",
        },
    },
    {
        "transaction_id": "1",
        "amount": 19.95,
        "iso_currency_code": "USD",
        "category": ["Shopping", "Clothing"],
        "category_id": "19012000",
        "date": "2023-06-16",
        "datetime": "2023-06-16T17:30:00Z",
        "authorized_date": "2023-06-16",
        "authorized_datetime": "2023-06-16T17:30:00Z",
        "location": {
            "address": "789 Oak St",
            "city": "Somewhere",
            "region": "NY",
            "postal_code": "54321",
            "country": "US",
            "lat": 40.987654,
            "lon": -74.987654,
            "store_number": "654",
        },
        "name": "Fashion Emporium",
        "merchant_name": "Fashion Emporium",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "APPAREL_AND_SERVICES",
            "detailed": "APPAREL_AND_ACCESSORIES",
        },
    },
    {
        "transaction_id": "1",
        "amount": 45.75,
        "iso_currency_code": "USD",
        "category": ["Food and Drink", "Groceries"],
        "category_id": "13005032",
        "date": "2023-06-15",
        "datetime": "2023-06-15T09:45:00Z",
        "authorized_date": "2023-06-15",
        "authorized_datetime": "2023-06-15T09:45:00Z",
        "location": {
            "address": "123 Market St",
            "city": "Cityville",
            "region": "CA",
            "postal_code": "98765",
            "country": "US",
            "lat": 38.765432,
            "lon": -121.765432,
            "store_number": "321",
        },
        "name": "Fresh Mart",
        "merchant_name": "Fresh Mart",
        "payment_channel": "in store",
        "personal_finance_category": {
            "primary": "GROCERIES",
            "detailed": "GROCERIES",
        },
    },
]
