from rest_framework import serializers
from .models import Book, Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.all(),
        source = 'book'
    )

    owner = serializers.ReadOnlyField(source = 'owner.username')
    book = serializers.HyperlinkedRelatedField(view_name='book_detail', read_only=True)

    class Meta:
        model = Comment
        fields = ('id',  'book', 'body', 'time_stamp', 'owner', 'book_id')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'image', 'category', 'description', 'owner', 'comments')
