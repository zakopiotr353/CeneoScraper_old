import requests
from bs4 import BeautifulSoup

def get_cos(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.get_text().strip for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute].strip()
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

selectors = {
                "opinion_id": ( None, "data-entry-id"),
                "author": ("span.user-post_author-name"),
                "recommendation": ("span.user-post_author-recomendation > em"),
                "stars": ("span.user-post_score-count"),
                "purchased": ("div.review-pz"),
                "opinion_date": ("span.user-post_published > time:nth-child(1)","datetime"),
                "purchase_date": ("button.vote-yes", "data-total-vote"),
                "usefull_count": ("button.vote-yes","data-total-vote"),
                "unusefull_count": ("button.vote-no","data-total-vote"),
                "content": ("div.user-post_text"),
                "pros": ("div.review-feature_title--positivies ~ div.review-feature_item", None, True),
                "cons": ("div.review-feature_title--neagtives ~ div.review-feature_item", None, True)
            }

# product_code = input("Podaj kod produktu: ")
# product_code = "39562616"
#url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    print(type(opinions))
    if len(opinions) > 0:
        opinions_all = []
        for opinion in opinions:
            
            opinions_all = []
            for opinion in opinions:
                single_opinion = [key] = get_cos(opinion, *value)

            opinions_all.append(single_opinion)
            print(opinions_all)
    
