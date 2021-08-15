import os


class ReplaceType(object):
  types = {
    "str": 'models.CharField(max_length=100, blank=True, null=True, unique=False)',
    "int": 'models.IntegerField(blank=True)',
    "bool": 'models.BooleanField(default=False)',
    "float": 'models.FloatField(default=0)',
    "datetime": 'models.DateTimeField(blank=True, null=True)',
    }

  @classmethod
  def GetDjangoType(cls, field, type):
    return f'\t{field} = {cls.types[type]}'

  @classmethod
  def CreateModel(cls, modelName):
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # MODELS_DIR = os.path.join(BASE_DIR, 'models')
    MODELS_DIR = os.path.abspath('models')

    if not os.path.exists(MODELS_DIR):
      os.makedirs(MODELS_DIR)

    usedpath = os.path.join(MODELS_DIR, '__init__.py')
    if not os.path.exists(usedpath):
      with open(usedpath, 'w'): pass

    # 'from django.db import models'
    list_import = list()
    list_class = ['class Meta:\n', f"db_table = '{modelName}'"]
    
    with open(os.path.join(MODELS_DIR, f'{modelName}.py'),'w') as fw:
      fw.write('from django.db import models\n\n')
      fw.write(f'class {modelName}(models.Model):\n')
      # here i have to make a for loop get every fields in the table
      fw.write(cls.GetDjangoType('name', 'str'))
      fw.write(cls.GetDjangoType('email', 'str'))
      fw.write(cls.GetDjangoType('age', 'str'))

      # Create Meta
      fw.write('class Meta:\n')
      fw.write(f"\tdb_table = '{modelName}'")


ReplaceType.CreateModel('Users')