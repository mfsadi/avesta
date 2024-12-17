import requests


class TorobAPI:
    def __init__(self, cookies=None, headers=None):
        self.base_url = "https://api.torob.com"
        self.cookies = cookies or {
            'search_session': 'nkgfgycbzttafpcfwdjwsuurtsccuenl',
            '_ga': 'GA1.1.209432467.1730288294',
            'new_question_visibility': 'false',
            'deliver_city': '798',
            '_ga_RXJQRSCLTR': 'GS1.1.1732706297.6.1.1732706547.60.0.0',
            'display_mode': '',
            'is_torob_user_logged_in': 'False',
            '_ga_CF4KGKM3PG': 'GS1.1.1734440325.1.1.1734441570.0.0.0',
        }
        self.headers = headers or {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'origin': 'https://torob.com',
            'priority': 'u=1, i',
            'referer': 'https://torob.com/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

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
