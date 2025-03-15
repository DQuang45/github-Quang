class Animals:
    def __init__(self):
         pass

class dog(Animals):
        def makesound(self):
            print("woof woof woof")
class cat(Animals):
        def makesound(self):
            print("meow moew moew")
class InvalidCastException(Exception):
    """Ngoại lệ được ném khi ép kiểu không hợp lệ"""
    pass

def treatMeAsDog(animal):
    try:
        # Kiểm tra nếu animal không phải là instance của Dog
        if not isinstance(animal, dog):
            raise InvalidCastException("Cannot cast to Dog")
        return animal  # Nếu đúng, trả về object Dog
    except InvalidCastException:
        print("Impossible")
        return None

# Ví dụ sử dụng
if __name__ == '__main__':
    my_dog = dog()
    my_cat = cat()

    my_cat.makesound()
    # Thử ép một Dog
    dog_obj = treatMeAsDog(my_dog)
    if dog_obj is not None:
        dog_obj.makesound()  # In ra: "woof"

    # Thử ép một Cat
    cat_obj = treatMeAsDog(my_cat)  # In ra: "Impossible"
    if cat_obj is None:
        print("Returned None")
     