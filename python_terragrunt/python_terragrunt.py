import subprocess
import logging

log = logging.getLogger(__name__)


class Terragrunt:
    def __init__(self, targets=None, state='terraform.tfstate', variables=None):
        self.targets = [] if targets is None else targets
        self.state = state
        self.variables = dict() if variables is None else variables
        self.state_data = None

    def apply(self, targets=None, variables=None):
        variables = self.variables if variables is None else variables
        targets = self.targets if targets is None else targets
        parameters = []
        parameters += ['-parallelism=30']
        parameters = \
            ['terragrunt', 'apply', '-state=%s' %
                self.state, '-auto-approve ']
        cmd = ' '.join(parameters)
        return self._run_cmd(cmd)

    def _run_cmd(self, cmd):
        log.info('command: ' + cmd)
        p = subprocess.Popen(
            cmd, shell=True, text=True)
        out, err = p.communicate()
        log.info(out)

        return out, err

    def destroy(self, targets=None, variables=None):
        variables = self.variables if variables is None else variables
        targets = self.targets if targets is None else targets

        parameters = []
        parameters = \
            ['terragrunt', 'destroy', '-force', '-state=%s' % self.state]
        cmd = ' '.join(parameters)
        return self._run_cmd(cmd)
