from fastapi import FastAPI

app = FastAPI() # инициализация приложения (фреймворка)


@app.get('/') # если мы получим ответ такого типа то
async def welcome() -> dict:
    return {'message': 'Главная страница'} # верни нам сообщение такого типа


@app.get('/user/admin')
async def welcome() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def welcome(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def welcome(username: str = 'Сергей', age: int = 46) -> dict:
    return {'User': username, 'Age': age}