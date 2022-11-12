import os
import sys
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        here = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(0, here)

        from echo_kernel.install import install_my_kernel_spec

        prefix = os.path.join(here, 'data_kernelspec')
        install_my_kernel_spec(False, prefix)

