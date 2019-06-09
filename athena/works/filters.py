import django_filters

from athena.works.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ('name', 'student_group', "subject")
