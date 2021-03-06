To start the web server you will need uvicorn.
The command to start the server is: uvicorn api.main:app --reload

The --reload argument is for hotreloads in development but also can be used in production(?)