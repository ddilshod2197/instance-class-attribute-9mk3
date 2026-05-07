class TestClass:
    class_attribute = "Bu klass atributi"

    def __init__(self):
        self.instance_attribute = "Bu instanca atributi"

obj = TestClass()

print(TestClass.class_attribute)
print(obj.instance_attribute)
```

Kodni ishlatib ko'ring: 

- `TestClass.class_attribute` klass atributi bo'lib, har bir klassga tegishli bo'ladi.
- `obj.instance_attribute` esa instanca atributi bo'lib, har bir klassning instancasiga tegishli bo'ladi.
