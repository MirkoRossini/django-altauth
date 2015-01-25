import os
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
# use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")
use_plugin("copy_resources")
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
version = "0.4"


@init
def set_properties(project):
    """
    :type project: pybuilder.core.Project
    """
    project.set_property("django_apps", ["altauth"])
    project.set_property("django_project", "example")
    project.set_property("flake8_break_build", "True")
    project.depends_on_requirements("requirements.txt")
    print(project.basedir)
    project.set_property("source_dist_ignore_patterns",
                         ["*.pyc", ".hg*", ".svn", ".CVS", "example/*",
                          "example/", "example/*.py", "*example*", "example/__init__.py", "example",
                          "src/main/python/example", "src"])
    project.set_property("distutils_classifiers", classifiers)
    project.set_property("copy_resources_target", "$dir_dist")
    project.set_property("copy_resources_glob", ["README.rst", "LICENSE", "MANIFEST.in"])

    # Hack to remove the example dir from the project
    def list_packages():
        source_path = project.expand_path("$dir_source_main_python")
        for root, dirnames, _ in os.walk(source_path):
            for directory in dirnames:
                full_path = os.path.join(root, directory)
                if os.path.exists(os.path.join(full_path, "__init__.py")):
                    package = full_path.replace(source_path, "")
                    if package.startswith(os.sep):
                        package = package[1:]
                    package = package.replace(os.sep, ".")
                    if package != "example":
                        yield package

    project.list_packages = list_packages
    project.include_file("altauth", "templates/altauth/*")
    project.include_file("altauth", "templates/base.html")

