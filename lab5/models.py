from peewee import *

conn = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше


class Department(BaseModel):
    id = PrimaryKeyField(null=False)
    name = TextField(null=False)
    description = TextField(null=True)

    class Meta:
        table_name = 'department'


class Employee(BaseModel):
    id = PrimaryKeyField(null=False)
    name = TextField(null=False)
    sex = BooleanField(null=False)  # man = True woman = False
    position = TextField(null=False)
    birthday = DateField(null=False)
    date_of_hiring = DateField(null=False)
    department = ForeignKeyField(Department, to_field='id', on_delete='cascade',
                                 on_update='cascade')

    class Meta:
        table_name = 'employee'


def add_department(name, description=None):
    row = Department(
        name=name.lower().strip(),
        description=description,
    )
    row.save()


def add_employee(name, sex, position, birthday, date_of_hiring, department: int):
    row = Employee(
        name=name,
        sex=sex,
        position=position,
        birthday=birthday,
        date_of_hiring=date_of_hiring,
        department=department,

    )
    row.save()


def get_all_employee():
    employees = Employee.select()
    needed_fields = []
    for emp in employees:
        needed_fields.append([emp.id, emp.name, emp.sex, emp.position])
    return needed_fields


def get_all_employee_id():
    employees = Employee.select()
    needed_fields = []
    for emp in employees:
        needed_fields.append(emp.id)
    return needed_fields


def get_all_department():
    departments = Department.select()
    needed_fields = []
    for dep in departments:
        needed_fields.append([dep.id, dep.name])
    return needed_fields


def remove_current_employee(input_id: int):
    employee = Employee.get(Employee.id == input_id)
    employee.delete_instance()


def get_current_employee(id: int):
    employee = Employee.get(Employee.id == id)
    return [employee.name,
            employee.sex,
            employee.position,
            employee.birthday,
            employee.date_of_hiring,
            employee.department]


if __name__ == '__main__':
    print(get_current_employee(5))
