class ReplaceType(object):
  types = {
    "str": 'models.CharField(max_length=100, blank=True, null=True, unique=False)',
    "int": 'models.IntegerField(blank=True)',
    "bool": 'models.BooleanField(default=False)',
    "float": 'models.FloatField(default=0)',
    }

  @classmethod
  def getDjangoType(cls, field, type):
    return f'    {field} = {cls.types[type]}'

print(ReplaceType.getDjangoType('name','str'))
print(ReplaceType.getDjangoType('email','str'))
print(ReplaceType.getDjangoType('age','int'))
print(ReplaceType.getDjangoType('money','float'))