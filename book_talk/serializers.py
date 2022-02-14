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
        fields = ('id', 'time_stamp', 'owner', 'body', 'book_id', 'owner', 'book')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    book_owner = serializers.ReadOnlyField(source='book_owner.username')

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'image', 'category', 'description', 'book_owner', 'comments')
