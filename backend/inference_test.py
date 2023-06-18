import inference

examples = [
            {
                "question": 
                """ 
                Infer demographic and psychographic qualities about the user and their spending habits based on the following transactions. 
                You are a financial advisor. Given the following transactions and their corresponding details, 
                provide personalized financial advice based on the user's financial goals, spending patterns, and current financial situation. 
                You should analyze the transactions, categorize them, identify any potential issues such as excessive spending or missed savings opportunities, and suggest actionable recommendations to improve the user's financial health. 
                Additionally, the advice should consider factors such as budgeting, saving, investing, debt management, and long-term financial planning. 
                Please provide comprehensive and user-friendly advice, considering both short-term and long-term financial goals. 
                Highlight which purchases were good financial decisions and which purchases were bad financial decisions.

                Example Transaction:
                {"transactions": [
                {
                "amount": 2307.21,
                "iso_currency_code": "USD",
                "category": [
                "Shops",
                "Computers and Electronics"
                ],
                "category_id": "19013000",
                "date": "2017-01-29",
                "datetime": "2017-01-27T11:00:00Z",
                "authorized_date": "2017-01-27",
                "authorized_datetime": "2017-01-27T10:34:50Z",
                "location": {
                "address": "300 Post St",
                "city": "San Francisco",
                "region": "CA",
                "postal_code": "94108",
                "country": "US",
                "lat": 40.740352,
                "lon": -74.001761,
                "store_number": "1235"
                },
                "name": "Apple Store",
                "merchant_name": "Apple",
                "payment_channel": "in store",
                "personal_finance_category": {
                "primary": "GENERAL_MERCHANDISE",
                "detailed": "GENERAL_MERCHANDISE_ELECTRONICS"
                },
                }
                ]
                """, 

                "answer": 
                """
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
                """
            }, 

            {
                "question": 
                """ 
                Infer demographic and psychographic qualities about the user and their spending habits based on the following transactions. 
                You are a financial advisor. Given the following transactions and their corresponding details, 
                provide personalized financial advice based on the user's financial goals, spending patterns, and current financial situation. 
                You should analyze the transactions, categorize them, identify any potential issues such as excessive spending or missed savings opportunities, and suggest actionable recommendations to improve the user's financial health. 
                Additionally, the advice should consider factors such as budgeting, saving, investing, debt management, and long-term financial planning. 
                Please provide comprehensive and user-friendly advice, considering both short-term and long-term financial goals. 
                Highlight which purchases were good financial decisions and which purchases were bad financial decisions.

                Example Transaction:
                {
                "transactions": [
                    {
                    "amount”: 2.97,
                    "iso_currency_code": "USD",
                    "category": [
                        "Food and Drink",
                        “Fast-Food”
                    ],
                    "category_id": "13005000",
                    "date": "2023-06-17",
                    "datetime": "2023-06-17T19:30:00Z",
                    "authorized_date": "2023-06-17",
                    "authorized_datetime": "2023-06-17T19:30:00Z",
                    "location": {
                        "address": “1530 3rd Ave",
                        "city": “Seattle”,
                        "region": “WA”,
                        "postal_code": “98101”,
                        "country": "US",
                        "lat": 47.610693,
                        "lon": -122.338224,
                    },
                    "name": “McDonald's”,
                    "merchant_name": “McDonald's”,
                    "payment_channel": "in store",
                    "personal_finance_category": {
                        "primary": “FAST-FOOD”,
                        "detailed": “FAST-FOOD“
                    }
                    }
                ]
                }
                """, 

                "answer": 
                """
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
                """
            }
        ]

input_test = """
Infer demographic and psychographic qualities about the user and their spending habits based on the following transactions. 

{
   "amount": 19.95,
   "iso_currency_code": "USD",
   "category": [
      "Shopping",
      "Clothing"
   ],
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
      "store_number": "654"
   },
   "name": "Fashion Emporium",
   "merchant_name": "Fashion Emporium",
   "payment_channel": "in store",
   "personal_finance_category": {
      "primary": "APPAREL_AND_SERVICES",
      "detailed": "APPAREL_AND_ACCESSORIES"
   }
}
"""

infer = inference.InferenceModel(prompt_examples=examples)

result = infer.fetch_gpt_response(input_test)

print(result)