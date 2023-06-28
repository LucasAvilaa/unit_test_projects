from .main import Costumer, System

class TestCustomer:

    def test_customer_registered_with_success(self):
        costumer = Costumer("Lucas", 30, "lucas@gmail.com")
        system = System()
        rec = system.create_costumer(costumer)
        assert rec == "Registered successfully"

    def test_underage_customer(self):
        costumer = Costumer("Lucas", 17, "lucas@gmail.com")
        system = System()
        rec = system.create_costumer(costumer)
        assert rec == "Minor, not registered"    

    def test_invalid_email_client(self):
        costumer = Costumer("Lucas", 30, "lucasgmail.com")
        system = System()
        rec = system.create_costumer(costumer)
        assert rec == "Invalid email, not registered"

    def test_customer_name_invalid(self,):
        costumer = Costumer("Lu", 30, "lucas@gmail.com")
        system = System()
        rec = system.create_costumer(costumer)
        assert rec == "Invalid name, not registered"

