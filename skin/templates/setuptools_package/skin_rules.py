import getpass
package = prompt('Package name', rand_name())
version = prompt('Package version', '0.1')
author = prompt("Author", getpass.getuser())
author_email = prompt('Package author email')
description = prompt('Description', '')
url = prompt('Url')
