def coroutine(f):
    def wrapper_func():
        g = f()
        next(g)
        return g
    return wrapper_func


@coroutine
def storage():
    values = set()
    while True:
        val = yield
        values.add(val)
        print(f"{len(values)}")


st = storage()
st.send(42)
