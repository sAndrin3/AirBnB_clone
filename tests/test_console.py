from car import Car  # Assuming your class is in a file named "car.py"

def test_car_class():
    my_car = Car("Toyota", "Camry", 2023)

    # Test get_info() method
    assert my_car.get_info() == "2023 Toyota Camry"

    # Test start_engine() method
    # You may want to use mocking or capturing stdout for this test
    # For simplicity, I'll just call the method
    my_car.start_engine()

    # Test stop_engine() method
    # You may want to use mocking or capturing stdout for this test
    # For simplicity, I'll just call the method
    my_car.stop_engine()

if __name__ == "__main__":
    test_car_class()
    print("All tests passed!")
