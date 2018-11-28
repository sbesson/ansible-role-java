import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('java-jre11')


def test_jre_version(host):
    assert host.exists('java')
    c = host.run('java -version')
    assert c.rc == 0
    # TODO: On Ubuntu openjdk-11-jre will install Java 10 until the
    # Java 11 Package is released
    assert c.stderr.startswith('openjdk version "10.0.')


def test_jdk_version(host):
    assert not host.exists('javac')
