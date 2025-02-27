from rest_framework import serializers
from ...models import Post


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            "id",
            "snippet",
            "title",
            "content",
            "status",
            "relative_url",
            "absolute_url",
            "created_date",
            "updated_date",
        ]
        # read_only_fields = ['content', 'created_date']

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        """
        Customize the data representation based on whether it's a single post or a list view.
        """
        request = self.context.get("request")
        # print(request.__dict__)
        rep = super().to_representation(instance)

        # rep['state'] = 'list'
        # if request.parser_context.get("kwargs").get('pk'):
        #     rep['state'] = 'single'
        if request.parser_context.get("kwargs").get("pk"):
            # Single post view
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            # List view
            rep.pop("content", None)

        return rep

    def create(self, validated_data):
        validated_data["user"] = self.context[
            "request"
        ].user  # Set the user to the current logged-in user
        return super().create(validated_data)
