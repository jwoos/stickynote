import cerberus

from src.errors import ValidationError


def validate_data(schema, data, strict=True):
    v = cerberus.Validator(schema)
    v.allow_unknown = not strict

    if not v.validate(data):
        errors = v.errors
        _unpack_error(errors, prev=[])

def _unpack_error(errors, prev=None):
    if prev is None:
        prev = []

    k, v = list(errors.items())[0]
    prev.append(k)

    if isinstance(v[0], dict):
        _unpack_error(v[0], prev=prev)
    else:
        err = '[{}]' * len(prev)
        err = err.format(*prev)
        raise ValidationError('{} {}'.format(err, v[0]))
