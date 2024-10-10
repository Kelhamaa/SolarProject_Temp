
from tortoise import fields
from tortoise.models import Model


class structureindb(Model):
    id = fields.IntField(pk=True)
    formula = fields.CharField(max_length=64, unique=True)
    mean_atomic_numbers=fields.FloatField(description="Mean atomic")
    max_atomic_numbers=fields.FloatField(description="Max atomic")
    min_atomic_numbers=fields.FloatField(description="Min")
    std_atomic_numbers=fields.FloatField(description="std")
    a_parameters=fields.FloatField(description="a_parameters")
    b_parameters=fields.FloatField(description="b_parameters")
    c_parameters=fields.FloatField(description="c_parameters")
    alpha_parameters=fields.FloatField(description="alpha")
    beta_parameters=fields.FloatField(description="beta")
    gamma_parameters=fields.FloatField(description="gamma")
    max_distance=fields.FloatField(description="Max distance")
    min_distance=fields.FloatField(description="Min distance")
    std_distance=fields.FloatField(description="std distance")

class pymatgenobjectindb(Model):
    id = fields.IntField(pk=True)
    element1=fields.CharField(description="element 1", max_length=2)
    element2 = fields.CharField(description="element 2", max_length=2)
    element3 = fields.CharField(description="element 3", max_length=2)
    abc=fields.CharField(description="abc", max_length=100)
    angles=fields.CharField(description="angles", max_length=100)
    volume=fields.CharField(description="volume", max_length=100)
    matrix=fields.CharField(description="matrix", max_length=100)
    pbc=fields.CharField(description="pbc", max_length=100)
    frac_coords_1=fields.CharField(description="frac_coords_1", max_length=100)
    frac_coords_2=fields.CharField(description="frac_coords_2", max_length=100)
    frac_coords_3=fields.CharField(description="frac_coords_3", max_length=100)
    frac_coords_4=fields.CharField(description="frac_coords_4", max_length=100)
    frac_coords_5=fields.CharField(description="frac_coords_5", max_length=100)
    stability=fields.CharField(description="stability", max_length=10)
    bandgap=fields.FloatField(description="bandgap", max_length=20)


class testtable(Model):
    id = fields.IntField(pk=True)
    name=fields.CharField(max_length=64, unique=True)
    mass=fields.FloatField(description="Mass")














