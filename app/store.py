# Calculate averages for entire menu for each restaurant

from lib.mongo import get_menu, get_all, insert_one
import pandas as pd
from sklearn.linear_model import LinearRegression
import json

if __name__ == '__main__':
  restaurants = get_all("rest_name")
  for restaurant in restaurants:
    menu = get_menu(restaurant['webname'])
    M = []
    for category in menu:
      for item in menu[category]:
        M.append([
          item["calories"],
          item["total_fat"],
          item["total_carb"],
          item["protein"],
          item["sodium"]
        ])

    df = pd.DataFrame(M)
    desc = dict(df.describe())

    doc = {
      "name": restaurant['name'],
      "webname": restaurant['webname'],
      "calories": round(desc[0]['mean'], 2),
      "total_fat": round(desc[1]['mean'],2),
      "total_carb": round(desc[2]['mean'],2),
      "protein": round(desc[3]['mean'],2),
      "sodium": round(desc[4]['mean'],2),
    }

    learn_uri = "mongodb://test:test@ds135690.mlab.com:35690/hfflearn"
    insert_one("restaurants", doc, learn_uri)
