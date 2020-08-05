import sys
sys.path.append('../')
from python_terragrunt import python_terragrunt

class TestTerragrunt(object):
    def test_apply(self):
        tf = python_terragrunt.Terragrunt()
        assert tf.apply()

    def test_destroy(self):
        tf = python_terragrunt.Terragrunt()
        assert tf.destroy()
