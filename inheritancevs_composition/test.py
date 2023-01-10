from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""

@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost

def main() -> None:
    """Main function."""

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

if __name__ == "__main__":
    main()