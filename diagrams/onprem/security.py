# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Security(_OnPrem):
    _type = "security"
    _icon_dir = "resources/onprem/security"


class Bitwarden(_Security):
    _icon = "bitwarden.png"


class Fail2Ban(_Security):
    _icon = "fail2ban.png"


class Boundary(_Security):
    _icon = "boundary.png"


class Trivy(_Security):
    _icon = "trivy.png"


class Vault(_Security):
    _icon = "vault.png"


# Aliases

fail2ban = Fail2Ban
