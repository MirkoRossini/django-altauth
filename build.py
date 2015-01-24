from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")
use_plugin("pypi:pybuilder_django_enhanced_plugin")

name = "django-altauth"
default_task = ["analyze", "publish"]

description = ('A Django appliaction to allow for alternative login methods, '
               'mainly focused on authentication from static scripts')
url = 'https://github.com/MirkoRossini/django-altauth'
authors = [Author("Mirko Rossini", "mirko.rossini@ymail.com")]

classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]
version = "0.2"


@init
def set_properties(project):
    """
    :type project: pybuilder.core.Project
    """
    project.set_property("django_apps", ["altauth"])
    project.set_property("django_project", "example")
    project.set_property("flake8_break_build", "True")

    project.depends_on_requirements("requirements.txt")
