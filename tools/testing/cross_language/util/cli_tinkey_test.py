# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tink.tools.testing.cross_language.util.tinkey_cli."""

from absl.testing import absltest
from absl.testing import parameterized
from tools.testing.cross_language.util import cli_aead
from tools.testing.cross_language.util import cli_tinkey


class TinkeyCliWrapperTest(parameterized.TestCase):

  @parameterized.parameters(*cli_tinkey.KEY_TEMPLATES)
  def test_generate_encrypt_decrypt(self, key_template):
    keyset_handle = cli_tinkey.generate_keyset_handle(key_template)
    primitive = cli_aead.CliAead('java', keyset_handle)
    plaintext = b'plaintext'
    associated_data = b'associated_data'
    ciphertext = primitive.encrypt(plaintext, associated_data)
    output = primitive.decrypt(ciphertext, associated_data)
    self.assertEqual(output, plaintext)

if __name__ == '__main__':
  absltest.main()