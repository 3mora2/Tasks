def g(ob):
    print(ob)
    print('hello')
    return ob
@g
def k(o):
    print('hi')

g('o')