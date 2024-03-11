import pytest
from main import StudentsInMLOPs

@pytest.fixture
def mlops_class():
    return StudentsInMLOPs()

def test_enroll_students(mlops_class):
    assert mlops_class.enrollStudents(1) == True
    assert mlops_class.enrollStudents(2) == True
    assert mlops_class.enrollStudents(1) == False

def test_drop_students(mlops_class):
    mlops_class.enrollStudents(1)
    mlops_class.enrollStudents(2)
    assert mlops_class.dropStudents(1) == True
    assert mlops_class.dropStudents(3) == False

def test_get_total_students(mlops_class):
    mlops_class.enrollStudents(1)
    mlops_class.enrollStudents(2)
    assert mlops_class.getTotalStudents() == 2
    mlops_class.dropStudents(1)
    assert mlops_class.getTotalStudents() == 1

def test_get_class_name(mlops_class):
    assert mlops_class.getClassName() == "MLOPS"
