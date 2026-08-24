from setuptools import find_packages, setup

package_name = 'week07_08_my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kristo Mägi',
    maintainer_email='kristo.magi@tktk.ee',
    description='ROS 2 Python package for week 7-8.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = week07_08_my_package.my_node:main',
        ],
    },
)
