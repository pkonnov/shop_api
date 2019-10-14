# /api/v1/orders
GET /api/v1/orders - получить список заказов

POST /api/v1/orders - создать новый заказ:
```json
{
	"order": {
            "mailing_addr_user": "адрес доставки",
            "count": "количество товара",
            "comment_to_order": "комментарий к заказу",
            "place_of_order": "дата и время создания заказа в формате (2019-10-13T12:09:39.970364Z)",
            "order_status": "статус заказа true(активный) false(отмененый)",
            "total_cost": "цена (0000.00)",
            "user": "id пользователя",
            "product": "id товара"
        }
}
```
PUT /api/v1/orders - отменить заказ
```json
{
  "order_status": "False"
}
```
GET /api/v1/orders/filter-email - получить список заказов по требуемому email
```json
{
	"email": "email пользователя"
}
```
