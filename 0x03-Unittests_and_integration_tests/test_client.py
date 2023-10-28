#!/usr/bin/env python3
"""class to test clients module"""

import unittest
from unittest import mock
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """class to test github
    org client class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org):
        """test org method"""
        with patch('client.GithubOrgClient.org') as mock_:
            test = GithubOrgClient(org_name=org)
            self.assertEqual(test.org.return_value, mock_.return_value)

    def test_public_repos_url(self):
        """test public repos url method"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) \
                as mock_:
            mock_.return_value = {'repos_url': True}
            github = GithubOrgClient('org')
            self.assertEqual(github._public_repos_url, True)

    @patch('client.get_json')
    def test_public_repos(self, mocked):
        """test public repos"""
        Dict = [{'name': 'repo_0'}, {'name': 'repo_1'}]
        mocked.return_value = Dict
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_:
            mock_.return_value = 'World'
            github = GithubOrgClient('test').public_repos()
            self.assertEqual(github, ['repo_0', 'repo_1'])
            mock_.assert_called_once()
            mock_.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """test has license method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    [
        (org_payload, expected_repos),
        (repos_payload, apache2_repos)
    ],
    class_name="TestIntegrationGithubOrgClient"
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''testing GithubOrgClient.public_repos method in an integration test'''
    @classmethod
    def setUpClass(cls):
        '''Mock requests.get to return example payloads found in fixtures'''
        super().setUpClass()
        get_patcher = patch('requests.get')
        cls.mock_get = get_patcher.start()

        # Set side effects for the mock
        cls.mock_get.side_effect = [
            Mock(return_value=Mock(json=lambda: org_payload)),
            Mock(return_value=Mock(json=lambda: repos_payload))
        ]

    @classmethod
    def tearDownClass(cls):
        '''Stop the patcher'''
        super().tearDownClass()
        cls.mock_get.stop()

    def test_public_repos(self):
        '''method to test GithubOrgClient.public_repos'''
        # Act
        github_org_client = GithubOrgClient('google')
        actual_repos = github_org_client.public_repos()

        # Assert
        self.assertEqual(actual_repos, expected_repos)

    def test_public_repos_with_license(self):
        '''test the public_repos with the argument license="apache-2.0"'''
        # Act
        github_org_client = GithubOrgClient('google')
        actual_repos = github_org_client.public_repos(license='apache-2.0')

        # Assert
        self.assertEqual(actual_repos, apache2_repos)
