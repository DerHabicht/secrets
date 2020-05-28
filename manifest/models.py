from yaml import SafeLoader, YAMLObject


class Bank(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Bank'

    def __init__(self, name, rtn, account):
        self.name = name
        self.rtn = rtn
        self.account = account


class Credential(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Credential'

    def __init__(self, service, username, type, secret):
        self.service = service
        self.username = username
        self.type = type
        self.secret = secret


class Device(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Device'

    def __init__(self, name, type, role):
        self.name = name
        self.type = type
        self.role = role


class OTP(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!OTP'

    def __init__(self, service, username, secret, devices):
        self.service = service
        self.username = username
        self.secret = secret
        self.devices = devices


class Passphrase(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Passphrase'

    def __init__(self, passphrase, start, end=None):
        self.passphrase = passphrase
        self.start = start
        self.end = end


class PassphraseHistory(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Passphrase'

    def __init__(self, service, current, notes, deprecated):
        self.service = service
        self.current = current
        self.notes = notes
        self.deprecated = deprecated


class Record(YAMLObject):
    yaml_loader = SafeLoader
    yaml_tag = u'!Record'


