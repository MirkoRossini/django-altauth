from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")
use_plugin("pypi:pybuilder_django_enhanced_plugin")


name = "django-altauth"
default_task = "publish"


@init
def set_properties(project):
    """
    :type project: pybuilder.core.Project
    """
    project.set_property("django_apps", ["altauth"])
    project.set_property("django_project", "example")
