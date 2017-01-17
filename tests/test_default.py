import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_jre_version(Command):
    assert Command.exists('java')
    c = Command('java -version')
    assert c.stderr.startswith('openjdk version "1.8.0')


def test_jdk_version(Command, TestinfraBackend):
    host = TestinfraBackend.get_hostname()
    if host == 'java-jdk':
        assert Command.exists('javac')
        c = Command('javac -version')
        assert c.stderr.startswith('javac 1.8.0')
    else:
        assert not Command.exists('javac')
