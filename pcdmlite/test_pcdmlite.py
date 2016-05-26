"""
(c) University of Technology Sydney 2016

This file is part of pcdmlite.

    pcdmlite is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pcdmlite is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Netta.  If not, see <http://www.gnu.org/licenses/>.

"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

import unittest
import pcdmlite

class TestLoading(unittest.TestCase):
        
  def test_init(self):
      item = pcdmlite.Item()
      self.assertEqual(item.files, [])
      
    
if __name__ == '__main__':
    unittest.main()