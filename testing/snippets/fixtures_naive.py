try:
    setup()
    test_something_1()
finally:
    teardown()

try:
    setup()
    test_something_2()
finally:
    teardown()

try:
    setup()
    test_something_3()
finally:
    teardown()
