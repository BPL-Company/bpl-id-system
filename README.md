# bpl_id_system
 
Api сервер для идентификации юзеров BPL.

## Auth token

`/some_method?auth_token=<auth_token>`

## Методы

`/get_user_by_id/<user_id>`

Returns User object.

user_id - Integer.


`/get_user_by_nickname/<nickname>`

Returns User object.

nickname - String.


`/create_user?nickname=<nickname>&auth_method=<auth_method>&auth_string=<auth_string>`

Returns User object.

nickname - String.

auth_method - String. (auth from auth list)

auth_string - String. (tg id, minecraft nickname, etc.)


`/set_money?user_id=<user_id>&count=<count>`

Returns Ok object.

user_id - Integer.

count - Integer.



`/inc_money?user_id=<user_id>&count=<count>`

Returns Ok object.

user_id - Integer.

count - Integer.



`/dec_money?user_id=<user_id>&count=<count>`

Returns Ok object.

user_id - Integer.

count - Integer.

## Обьекты

#User

```json
{"_id":1,
  "auth":{"email":[],"minecraft":["Vezono3"],"phone_number":[],"telegram_id":[]},
  "connected_to":[],
  "money":0,
  "nickname":"Vezono3",
  "nicknames":[],
  "role":"member"}
```

#Ok
```json
{"ok": true,
"result": {}}
```

