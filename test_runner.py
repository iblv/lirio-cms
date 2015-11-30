#!/usr/bin/python
# Copyright 2015 Google Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# [START runner]
import optparse
import os
import sys
import unittest


USAGE = """%prog SDK_PATH TEST_PATH
Run unit tests for App Engine apps.

SDK_PATH    Path to Google Cloud or Google App Engine SDK installation, usually
            ~/google_cloud_sdk
TEST_PATH   Path to package containing test modules"""


def main(sdk_path, test_path):
    # If the sdk path points to a google cloud sdk installation
    # then we should alter it to point to the GAE platform location.
    if os.path.exists(os.path.join(sdk_path, 'platform/google_appengine')):
        sys.path.insert(0, os.path.join(sdk_path, 'platform/google_appengine'))
    else:
        sys.path.insert(0, sdk_path)

    # Ensure that the google.appengine.* packages are available
    # in tests as well as all bundled third-party packages.
    import dev_appserver
    dev_appserver.fix_sys_path()

    # Loading appengine_config from the current project ensures that any
    # changes to configuration there are available to all tests (e.g.
    # sys.path modifications, namespaces, etc.)
    try:
        import appengine_config
        (appengine_config)
    except ImportError:
        print "Note: unable to import appengine_config."

    from google.appengine.ext import testbed

    testbed = testbed.Testbed()
    testbed.activate()
    testbed.init_all_stubs()

    # Discover and run tests.
    suite = unittest.loader.TestLoader().discover(test_path)

    for root, dirs, files in os.walk(test_path):
        for name in dirs:
            # print(os.path.join(root,name))
            suite.addTests(unittest.loader.TestLoader().discover(os.path.join(root,name)))

    unittest.TextTestRunner(verbosity=2).run(suite)



if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 2:
        SDK_PATH = os.environ['HOME']+'/google-cloud-sdk'
        TEST_PATH = './test'
    else:
        SDK_PATH =  args[0]
        TEST_PATH = args[1]

    main(SDK_PATH, TEST_PATH)

# [END runner]
