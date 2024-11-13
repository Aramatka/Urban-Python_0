def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    

test_function()
inner_function() # т.к. область видимости находится внутри функции test_function, то выдается ошибка: "is not defined"