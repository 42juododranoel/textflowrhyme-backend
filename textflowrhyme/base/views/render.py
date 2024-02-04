def render_one(instance, serializer):
    return serializer(**instance.__dict__)


def render_many(instances, serializer):
    return {
        "collection": [serializer(**instance.__dict__) for instance in instances],
        "count": len(instances),
    }
