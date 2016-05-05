from flask import Flask, jsonify, request
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from IPython import embed

auth = Oauth1Authenticator(
  consumer_key='amk-HOw5ZaDGr4jAtkT4qw',
  consumer_secret='2ytvmct-MThvy7h1oPUDEajQquc',
  token='-2S6th2E32xvG6wK3l7qHEIRIBFoFn86',
  token_secret='yDvlbaYQJtuX99qZfjXc6BRSP6Q'
)

client = Client(auth)

app = Flask(__name__)

@app.route('/hello')
def hello_world():
  formatted_data = []
  params = request.args
  response = client.search(params['name'])
  for business in response.businesses:

    bus_data = {
      'name': business.name,
      'rating': business.rating,
      'rating_img_url': business.rating_img_url,
      'rating_img_url_large': business.rating_img_url_large,
      'rating_img_url_small': business.rating_img_url_small,
      'review_count': business.review_count,
      'reviews': business.reviews,
        'location': {
          'address': business.location.address,
          'city': business.location.city
        },
      'snippet_image_url': business.snippet_image_url,
      'snippet_text': business.snippet_text,
      'url': business.url,
      'image_url': business.image_url,
      'categories': business.categories
    }

    formatted_data.append(bus_data)

  return jsonify({'data':formatted_data})

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
