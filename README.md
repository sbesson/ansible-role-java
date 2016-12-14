Java
====

Install Java JREs and optionally JDKs.

Role Variables
--------------

Optional variables:

- `javajreversions`: A list of JRE versions to install, default `[1.8.0]`
- `javajdkversions`: A list of JDK versions to install, default None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: java }


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk

License
-------

BSD
