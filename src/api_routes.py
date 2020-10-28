from flask import request, jsonify
from flask_restful import Api, Resource

from .services import (create_links_pair, get_all_links_pairs,
                       get_links_pair, update_links_pair, delete_links_pair)
from .serializers import links_pair_api_serializer

api = Api(prefix='/api')


class LinksPairs(Resource):
    def get(self, pair_id=None):
        if pair_id:
            pair = get_links_pair(pair_id)
            return links_pair_api_serializer(pair)
        pairs = get_all_links_pairs()
        return [links_pair_api_serializer(lp) for lp in pairs]

    def post(self):
        req = request.get_json(force=True)
        original_url = req.get('original_url')
        if not original_url:
            return {'message': "Request body must include 'original_url' field"}, 400

        new_pair = create_links_pair(original_url, req.get('days_limit') or None)

        return links_pair_api_serializer(new_pair), 201

    def put(self):
        pass

    def delete(self, pair_id):
        pair = delete_links_pair(pair_id)

        return links_pair_api_serializer(pair), 200


api.add_resource(LinksPairs, '/links_pairs', '/links_pairs/', '/links_pairs/<int:pair_id>')
