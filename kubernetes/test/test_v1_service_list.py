# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_service_list import V1ServiceList


class TestV1ServiceList(unittest.TestCase):
    """ V1ServiceList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ServiceList(self):
        """
        Test V1ServiceList
        """
        model = kubernetes.client.models.v1_service_list.V1ServiceList()


if __name__ == '__main__':
    unittest.main()
