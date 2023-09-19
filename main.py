import argparse
from PBCrawler import Crawler
import json
from pprint import pprint


with open('info.json', "r") as json_file:
        data = json.load(json_file)

mens_categories = data['mens']
womens_categories = data['womens']
stores = data['stores']
languages = data['languages']


def main():
    parser = argparse.ArgumentParser(description="Crawl a category or specific products.")

    # Add arguments for store and language
    parser.add_argument(
        "--store",
        required=True,
        help="Specify the store you want to crawl."
    )
    parser.add_argument(
        "--language",
        required=True,
        help="Specify the language to use for crawling. Only native language and English are supported."
    )

    # Add an argument to choose between category and product
    parser.add_argument(
        "--choice",
        choices=["category", "product"],
        required=True,
        help="Choose 'category' to crawl a category or 'product' for a specific product."
    )

    args = parser.parse_args()

    if args.choice == "category":
        while True:
            # If the user chose to crawl a category, display product categories and accept a string
            inp = input("Please enter mens or womens for the category you want to crawl: ")
            if inp == "mens":
                print("Please select one out of the mens categories:")
                pprint(list(mens_categories.keys()))
            elif inp == "womens":
                print("{Please select one out of the womens categories:")
                pprint(list(womens_categories.keys()))
            else:
                print("Invalid category. Please choose mens or womens.")
                return
            
            category = input("Enter the product category: ")
            
            dic = mens_categories if inp == "mens" else womens_categories

            if category not in dic:
                print("Invalid category. Please choose a valid category.")
                return
            else:
                print(f"Crawling category: {category}")
                category_id = dic[category]
                crawler = Crawler(args.store, args.language)
                crawler.get_all_products_from_category(category_id, category)

            if input("Do you want to crawl another category? (y/n): ") == "n":
                break

    elif args.choice == "product":
        # If the user chose to crawl a specific product, accept a list of integers
        products = input("Enter a list of product IDs separated by spaces: ")
        product_ids = [int(id) for id in products.split()]
        print(f"Crawling specific products: {product_ids}")
    else:
        print("Invalid choice. Please choose 'category' or 'product'.")

if __name__ == "__main__":
    main()
