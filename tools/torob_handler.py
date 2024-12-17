import requests


class TorobAPI:
    def __init__(self, cookies=None, headers=None):
        self.base_url = "https://api.torob.com"
        self.cookies = cookies
        self.headers = headers

    def get_spellcheck(self, query):
        """Fetch spellcheck suggestions for a query."""
        params = {
            'page': '0',
            'sort': 'popularity',
            'size': '24',
            'query': query,
            'q': query,
            'source': 'next_desktop',
        }
        response = requests.get(f"{self.base_url}/v4/base-product/search/",
                                params=params, cookies=self.cookies, headers=self.headers)
        if response.status_code == 200:
            result = response.json()
            return result.get("spellcheck", None)
        else:
            raise Exception(f"Failed to fetch spellcheck: {response.status_code}, {response.text}")

    def get_category_suggestions(self, query):
        """Fetch category suggestions for a query."""
        params = {
            'q': query,
            'source': 'next_desktop',
        }
        response = requests.get(f"{self.base_url}/suggestion2/",
                                params=params, cookies=self.cookies, headers=self.headers)
        if response.status_code == 200:
            result = response.json()
            categories = [row["category"]["title"] for row in result if "category" in row.keys()]
            return categories
        else:
            raise Exception(f"Failed to fetch category suggestions: {response.status_code}, {response.text}")


# Example Usage
if __name__ == "__main__":
    torob_api = TorobAPI()
    query = "لبلس زنانه"

    try:
        # Fetch spellcheck
        spellcheck = torob_api.get_spellcheck(query)
        print("Spellcheck:", spellcheck)

        # Fetch category suggestions
        suggestions = torob_api.get_category_suggestions(query)
        print("Category Suggestions:", suggestions)
    except Exception as e:
        print("Error:", e)
