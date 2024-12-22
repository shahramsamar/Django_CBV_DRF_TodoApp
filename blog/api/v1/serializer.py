from rest_framework import serializers
from ...models import Post



# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
    
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id','snippet','title','content','status','relative_url','created_date','updated_date']
        # read_only_fields = ['content', 'created_date']
