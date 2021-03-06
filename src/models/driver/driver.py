# Copyright 2016 Presslabs SRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod


class Driver(metaclass=ABCMeta):
    @abstractmethod
    def create(self, requirements):
        pass

    @abstractmethod
    def resize(self, id, quota):
        pass

    @abstractmethod
    def clone(self, id, parent_id):
        pass

    @abstractmethod
    def remove(self, id):
        pass

    @abstractmethod
    def expose(self, id, host, permissions):
        pass

    @abstractmethod
    def get_all(self):
        pass
