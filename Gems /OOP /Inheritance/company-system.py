from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

class Employee(ABC):
    def __init__(self, name: str, id: int, salary: float):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def display_info(self):
        pass

    def get_salary(self) -> float:
        return self.salary

    def set_salary(self, new_salary: float):
        self.salary = new_salary

class Manager(Employee):
    def __init__(self, name: str, id: int, salary: float, teams: List[str]):
        super().__init__(name, id, salary)
        self.teams_managed = teams

    def add_team(self, team: str):
        self.teams_managed.append(team)

    def display_info(self):
        print(f"Manager ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Teams: {', '.join(self.teams_managed)}")

class Developer(Employee):
    def __init__(self, name: str, id: int, salary: float, skills: List[str]):
        super().__init__(name, id, salary)
        self.skills = skills

    def add_skill(self, skill: str):
        self.skills.append(skill)

    def display_info(self):
        print(f"Developer ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Skills: {', '.join(self.skills)}")

class Project:
    def __init__(self, name: str):
        self.project_name = name
        self.team_members: List[Employee] = []

    def add_team_member(self, employee: Employee):
        self.team_members.append(employee)

    def display_project_info(self):
        print(f"Project: {self.project_name}, Team Members:")
        for member in self.team_members:
            member.display_info()

T = TypeVar('T', bound=Employee)

class EmployeeManager(Generic[T]):
    def __init__(self):
        self.employees: List[T] = []

    def add_employee(self, employee: T):
        self.employees.append(employee)

    def display_all_employees(self):
        for employee in self.employees:
            employee.display_info()

# Main execution
if __name__ == "__main__":
    employee_manager = EmployeeManager()

    manager1 = Manager("Alice Johnson", 1, 90000, ["Development", "HR"])
    dev1 = Developer("Bob Smith", 2, 80000, ["Python", "JavaScript"])
    dev2 = Developer("Charlie Brown", 3, 75000, ["Java", "C++"])
    dev3 = Developer("David", 4, 15000, ["C", "C++"])

    employee_manager.add_employee(manager1)
    employee_manager.add_employee(dev1)
    employee_manager.add_employee(dev2)
    employee_manager.add_employee(dev3)

    project = Project("New Software Launch")
    project.add_team_member(manager1)
    project.add_team_member(dev1)
    project.add_team_member(dev2)

    print("Project Information:")
    project.display_project_info()

    print("\nAll Employees:")
    employee_manager.display_all_employees()
