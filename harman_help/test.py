class Empty:
    pass

test = Empty()
test.val1 = 'hello'
string = 'key'

setattr(test, string, 'value')

print(test.val1)
print(test.__dict__)