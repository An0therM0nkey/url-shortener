import datetime

from flask import Blueprint, render_template, redirect

from .services import get_all_links_pairs, get_links_pair_by_short_url
from .serializers import links_pair_frontend_serializer

home = Blueprint('home', __name__)


@home.route('/')
def index():
    pairs = get_all_links_pairs()
    serialized_pairs = [links_pair_frontend_serializer(lp) for lp in pairs]
    return render_template('index.html', pairs=serialized_pairs)


@home.route('/<short_url>')
def redirect_to_original_url(short_url):
    pair = get_links_pair_by_short_url(short_url)

    serialized_pair = links_pair_frontend_serializer(pair)

    if serialized_pair['expires_on'] < datetime.datetime.now():
        return render_template('link_expired.html', links_pair=serialized_pair)

    return redirect(serialized_pair['redirect_url'])


@home.route('/api/')
def api_swagger():
    return render_template('swagger.html')
