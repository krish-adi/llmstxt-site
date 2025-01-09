from tqdm import tqdm
import os
import json
from create_product_json import create_product_json
from create_product_redirects import create_product_redirects

# ./scripts
SCRIPTS_PATH = os.path.dirname(os.path.abspath(__file__))
# ./scripts/llmstxt-files
LLMSTXT_FILES_PATH = os.path.join(SCRIPTS_PATH, "llmstxt-files")
if not os.path.exists(LLMSTXT_FILES_PATH):
    os.makedirs(LLMSTXT_FILES_PATH)
# ./scripts/run-assets
RUN_ASSETS_PATH = os.path.join(SCRIPTS_PATH, "run-assets")
if not os.path.exists(RUN_ASSETS_PATH):
    os.makedirs(RUN_ASSETS_PATH)
# ./data.json
DATA_RAW_PATH = os.path.join(os.path.dirname(SCRIPTS_PATH), "data.json")

data_raw = json.load(open(DATA_RAW_PATH))

existing_products = [
    d
    for d in os.listdir(LLMSTXT_FILES_PATH)
    if os.path.isdir(os.path.join(LLMSTXT_FILES_PATH, d))
]

# Loop through each company
for product in tqdm(data_raw):
    product_name = product["product"]
    product_dir = os.path.join(LLMSTXT_FILES_PATH, product_name)

    if product_name not in existing_products:
        print(f"Preparing data for: {product_name}")

        # Create product directory if it doesn't exist
        if not os.path.exists(product_dir):
            os.makedirs(product_dir)

        product_json = create_product_json(product, product_dir)
        product_redirects = create_product_redirects(product)

        print(product_json)
        print(product_redirects)

        # Append to products.jsonl
        products_jsonl_path = os.path.join(RUN_ASSETS_PATH, "products.jsonl")
        with open(products_jsonl_path, "a", encoding="utf-8") as f:
            json.dump(product_json, f)
            f.write("\n")

        # Append to redirects.jsonl
        redirects_jsonl_path = os.path.join(RUN_ASSETS_PATH, "redirects.jsonl")
        with open(redirects_jsonl_path, "a", encoding="utf-8") as f:
            for redirect in product_redirects:
                json.dump(redirect, f)
                f.write("\n")

        # Update status.json
        status_path = os.path.join(RUN_ASSETS_PATH, "status.jsonl")
        status = {"product": product_name, "status": "done"}

        with open(status_path, "a", encoding="utf-8") as f:
            json.dump(status, f)
            f.write("\n")


# Path to products.jsonl and redirects.jsonl in run-assets folder
PRODUCTS_JSONL_PATH = os.path.join(RUN_ASSETS_PATH, "products.jsonl")
REDIRECTS_JSONL_PATH = os.path.join(RUN_ASSETS_PATH, "redirects.jsonl")

# Path to lib folder (one level up from scripts)
LIB_PATH = os.path.join(os.path.dirname(SCRIPTS_PATH), "lib")
ROOT_PATH = os.path.dirname(SCRIPTS_PATH)

# Read products.jsonl line by line
products_data = []
with open(PRODUCTS_JSONL_PATH, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():  # Skip empty lines
            _product = json.loads(line)
            products_data.append(_product)

# Write to product_data.json in lib folder
product_data_path = os.path.join(LIB_PATH, "products_data.json")
with open(product_data_path, "w", encoding="utf-8") as f:
    json.dump(products_data, f)

print(f"Created {product_data_path} with {len(products_data)} products")

# Read redirects.jsonl line by line
redirects_data = []
with open(REDIRECTS_JSONL_PATH, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():  # Skip empty lines
            _redirect = json.loads(line)
            redirects_data.append(_redirect)

# Write to redirects.json in root folder
redirects_path = os.path.join(ROOT_PATH, "redirects.json")
with open(redirects_path, "w", encoding="utf-8") as f:
    json.dump(redirects_data, f)

print(f"Created {redirects_path} with {len(redirects_data)} redirects")
