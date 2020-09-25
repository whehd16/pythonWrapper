import weka.core.jvm as jvm

import weka.core.packages as packages

jvm.start()


# packages.refresh_cache()

packages.install_package("CLOPE")
print(packages.installed_packages())


jvm.stop()
