# bpl_id_system
 
Api сервер для идентификации юзеров BPL.

## Auth token

`/some_method?auth_token=<auth_token>`

## Методы


`/delete_user?user_id=<user_id>`

Returns User object in Ok.result

user_id - Integer.


`/get_user_by_id/<user_id>`

Returns User object in Ok.result

user_id - Integer.


`/get_user_by_nickname/<nickname>`

Returns User object in Ok.result

nickname - String.

`/get_user_by_tg_id/<tg_id>`

Returns User object in Ok.result

tg_id - Integer.


`/create_minecraft_user?nickname=<nickname>`

Returns User object in Ok.result

nickname - String.

`/create_minecraft_user?first_id=<first_id>&second_id=<second_id>`

Returns merged User object in Ok.result 

first_id - Integer.

second_id - Integer.

`/create_minecraft_user?nickname=<nickname>`

Returns User object in Ok.result

nickname - String.

`/create_user?nickname=<nickname>&auth_method=<auth_method>&auth_string=<auth_string>`

Returns User object in Ok.result

nickname - String.

auth_method - String. (auth from auth list)

auth_string - String. (tg id, minecraft nickname, etc.)


`/set_money?user_id=<user_id>&count=<count>`
or
`/set_money?minecraft=<minecraft_nickname>&count=<count>`

Returns Ok object. Creates and returns new user if not exist.

user_id - Integer.

count - Integer.

minecraft_nickname - String.



`/inc_money?user_id=<user_id>&count=<count>`
or
`/inc_money?minecraft=<minecraft_nickname>&count=<count>`

Returns Ok object. Creates and returns new user if not exist.

user_id - Integer.

count - Integer.

minecraft_nickname - String.



`/dec_money?user_id=<user_id>&count=<count>`
or
`/dec_money?minecraft=<minecraft_nickname>&count=<count>`

Returns Ok object. Creates and returns new user if not exist.

user_id - Integer.

count - Integer.

minecraft_nickname - String.




## Обьекты

# User

```json
{"_id":1,
  "money":0,
  "nickname":"Vezono2",
  "role":"member"}
```

# Ok
```json
{"ok": true,
"result": {}}
```

