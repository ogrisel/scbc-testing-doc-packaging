from mypackage.mymodule import compute_square  


def test_compute_square():
    assert compute_square(0) == 0

    assert compute_square(1) == 1
    assert compute_square(-1) == 1

    assert compute_square(2) == 4
    assert compute_square(-2) == 4