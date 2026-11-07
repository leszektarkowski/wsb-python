def divide(a, b):
    """Divides a/b, returns result"""
    # if a is not float or b is not float:
    #     return None
    try:
        res = a/b
    except TypeError:
        print("TypeError -> unsupported type")
        return None
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return None
    finally:
        print("Always")
    return res

if __name__ == "__main__":
    res = divide(3.2, "2.2")
    res = divide(3.2, 0)
    res = divide(5, 2)
    print(res)
    print("This is last message")