import sqlite3
from flask_restful import Resource, reqparse, request
from flask_jwt import jwt_required
from models.Item import ItemModal


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This filed cannot be left blank!"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item need store id"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModal.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModal.find_by_name(name):
            return {"message": "item with item name already exist"}, 400

        data = Item.parser.parse_args()
        item = ItemModal(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "an error occure while inserting item"}, 500

        return item.json()

    def delete(self, name):
        item = ItemModal.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModal.find_by_name(name)

        if item is None:
            item = ItemModal(name, **data)
        else:
            item.price = data["price"]
        ItemModal.save_to_db(item)
        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModal.query.all()]}
