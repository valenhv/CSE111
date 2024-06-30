# Student: Valentina Hernandez Vera
# EXCEEDING REQUIREMENTS: The test code for kpa_to_psi is at the end of the program.
from water_flow import (
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    pressure_loss_from_fittings,
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    kpa_to_psi
)
from pytest import approx
import pytest
def test_pressure_loss_from_fittings ():
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)
def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_water_column_height():
    assert water_column_height(10, 5) == approx(12.5, abs=0.1)
    assert water_column_height(0, 5) == approx(2.5, abs=0.1)
    assert water_column_height(10, 0) == approx(10, abs=0.1)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(10) == approx(97.92, abs=0.1)
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.1)
    assert pressure_gain_from_water_height(5) == approx(48.96, abs=0.1)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.28687, 6.0, 0.013, 1.65) == approx(-1.29, abs=0.01)
    assert pressure_loss_from_pipe(0.048692, 6.0, 0.018, 1.75) == approx(-69.63, abs=0.01)
    assert pressure_loss_from_pipe(0.28687, 0, 0.013, 1.65) == approx(0, abs=0.01)

def test_kpa_to_psi():
    assert kpa_to_psi(8) == approx(1.1603, abs=0.01)
    assert kpa_to_psi(-8) == approx(-1.1603, abs=0.01)
    assert kpa_to_psi(0) == approx(0, abs=0.01)
    assert kpa_to_psi(1) == approx(0.145038, abs=0.01)

pytest.main(["-v", "--tb=line", "-rN", __file__])