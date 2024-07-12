import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem

# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItems:
    #List out all the cart item rows
    def on_get(self,req,resp):
        resp.media = [model_to_dict(item) for item in DatabaseCartItem.select()]
        resp.status = falcon.HTTP_200

    #Add a new cart item row
    def on_post(self,req,resp):
        obj = req.get_media()
        cartitem = DatabaseCartItem(
            name = obj['name'],
            price = obj['price'],
            quantity = obj['quantity'],
            image_url = obj['image_url']
        )
        cartitem.save()
        resp.media = model_to_dict(cartitem)
        resp.status = falcon.HTTP_201


class CartItem:
    #Fetch a cart item based on the given item_id
    def on_get(self, req, resp, cartitem_id):
        cartitem = DatabaseCartItem.get(id=cartitem_id)
        resp.media = model_to_dict(cartitem)
        resp.status = falcon.HTTP_200

    #Delete a cart item row based on the given item_id
    def on_delete(self, req, resp, cartitem_id):
        DatabaseCartItem.delete_by_id(cartitem_id)
        resp.status = falcon.HTTP_204
    
    #Update a cart item row based on the given item_id
    def on_patch(self, req, resp, cartitem_id):
        cartitem = DatabaseCartItem.get(id=cartitem_id)
        changes = req.media
        if "quantity" in changes:
            cartitem.quantity = changes["quantity"]
            cartitem.save()
        resp.status = falcon.HTTP_204
