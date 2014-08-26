import json
import flask


def rpc_method(rule, **options):
    mime = 'application/json'

    def decorator(f):
        def decorated(*args, **kwargs):
            retval = f(*args)
            json_raw = __build_json(retval)

            return __build_response(json_raw)

        def __build_json(retval):
            return json.dumps(retval)

        def __build_response(json_raw):
            return flask.Response(json_raw, mimetype=mime)

        return __set_rule_to_func(f, decorated)

    def __set_rule_to_func(origin, decorated):
        name = origin.__name__

        if not hasattr(origin, '_rule_cache') or decorated._rule_cache is None:
            decorated._rule_cache = {name: [(rule, options)]}
        elif not origin.__name__ in origin._rule_cache:
            decorated._rule_cache[name] = [(rule, options)]
        else:
            decorated._rule_cache[name].append((rule, options))

        return decorated

    def __clean_decorator_kwargs():
        del options['schema']

    __clean_decorator_kwargs()
    return decorator
